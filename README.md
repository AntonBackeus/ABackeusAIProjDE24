# AInspector RAGget

This is a project about creating a RAG bot that uses a lancedb database to generate responses about the content of the database. In this version it uses transcripts from youtube videos as content.

## Setup

To setup the project you should first sync your virtual environment to the pyproject.toml (uv sync) to make sure you have all the required packages.

After making sure the packages are synced you need to have "Azure Functions" installed in VS code. We will use that to deploy the project to Azure. To do this we first need to initiate the resource. We do this by rightclicking "Function App" in the Azure tab on the left in VS code and choosing "Create function app in azure..." and following the steps at the top.

After generating the resource you need to go to the azure portal and then go to "Settings" -> "Environment Variables" and add "GOOGLE_API_KEY" and copy in your own google api key. And while you are on the platform you can also go to "FUNCTIONS" -> "App keys" and copy the default key. Paste that key into a .env file you create in the project and name the variable "AZURE_FUNCTION_KEY".

Now you need to populate the database with the files in the datafolder or whichever files you decide to replace them with. You can do this by running the ingestion.py file.

With that done you open the Azure page on the left again and hover/click open the WORKSPACE tab. There you will se the Function App lightningbolt. Click it then click "Deploy to Azure...". Accept the popup and your function will deploy and be active. Now you just need to run frontend/app.py with streamlit and use the RAG bot.

## Structure

The project itself is made up of the following parts:

- The RAG agent
- The streamlit app
- The API
- The lancedb database
- Azure function setup
- Helper functions (models/constants/ingestion)

The ingestion script need to be manually ran once to fetch the data files, or again if new data is downloaded. If you followed the setup you will have a streamlit app open. When using the streamlit app, every time you click send you send a request to the API with the text in the box. This text is sent by the API to the rag agent. The rag agent then uses google gemini and the lancedb to create a response to the text. That response is then returned to the API that returns it to streamlit that shows it to you.