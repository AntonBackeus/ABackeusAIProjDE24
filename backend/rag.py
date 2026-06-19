from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DATABASE_PATH
import lancedb


vector_db = lancedb.connect(uri=VECTOR_DATABASE_PATH)

rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        "You are an expert in data engineering, data science and related programming fields that makes educational content for students.",
        "Always answer based on the retrieved knowledge, but you can mix in your expertise to make the answer more coherent",
        "Don't hallucinate, rather say you can't answer it if the user prompts outside of the retrieved knowledge or otherwise unrelated to the retrieved knowledge",
        "Make sure tho keep the answer clear and concise, getting to the point directly, max 6 sentences",
        "For any educational question give an explanation if short enough to fit in the answer, if not let them now where in the video they can find the answer, and if possible give a timestamp and video name",
        "For a non-educational question, integrate a nerdy pun or joke into the answer if reasonable without forcing it, to make the answer more engaging and fun",
        "Also describe which file you have used as source",
    ),
    output_type=RagResponse,
)


@rag_agent.tool_plain
def retrieve_top_documents(query: str, k=3) -> str:
    """
    Uses vector search to find the closest k matching documents to the query
    """
    results = vector_db["articles"].search(query=query).limit(k).to_list()

    if not results:
        return """
        Filename: None,
        Filepath: None,
        Content: No relevant documents found
        """

    return f"""
    
    Filename: {results[0]["filename"]},
    
    Filepath: {results[0]["filepath"]},

    Content: {results[0]["content"]}
    
    """
