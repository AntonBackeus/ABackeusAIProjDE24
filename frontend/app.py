import streamlit as st
import requests
from pathlib import Path
import dotenv
from os import getenv

dotenv.load_dotenv()

ASSETS_PATH = Path(__file__).absolute().parents[1] / "assets"

url = f"https://aiproj-bvd8ahh9f6fpescz.swedencentral-01.azurewebsites.net/rag/query"
#?code={getenv('AZURE_FUNCTION_KEY')}
def layout():

    st.markdown("# AInspector RAGget")
    st.markdown("Ask a question about AIgineers educational content and get an answer based on the retrieved knowledge")
    text_input = st.text_input(label="Ask a questions")

    if st.button("Send") and text_input.strip() != "":
        response = requests.post(url, json={"prompt": text_input})

        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])

#    if st.button("Send") and text_input.strip():
#
#        st.write("URL:", url)
#
#        response = requests.post(
#            url,
#            json={"prompt": text_input},
#        )
#
#        st.write("Status:", response.status_code)
#        st.write("Headers:", dict(response.headers))
#        st.write("Body:", response.text)

if __name__ == "__main__":
    layout()
