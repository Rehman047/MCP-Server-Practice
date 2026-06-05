#Steps for AI Webscrapping
#Search the web
#Open official documentation
#Read them and write code accordingly

import http.client
import json
from dotenv import load_dotenv
import os
import httpx
import asyncio
from response_clean import html_remover
load_dotenv()


SERPER_URL="https://google.serper.dev/search"
query="hello"

async def search_web(query) -> dict | None:
    headers = {
    'X-API-KEY': os.getenv("SERPER_API_KEY"),
    'Content-Type': 'application/json'
    }
    payload = json.dumps({
    "q": query, "num":2
    })

    async with httpx.AsyncClient() as client:
        
        response=await client.post(
            SERPER_URL,headers=headers,data=payload,timeout=30.0
        )
        response.raise_for_status()
        return response.json()
    
async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, timeout=30.0)
        cleaned_response=html_remover(response)
        return cleaned_response.text

docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs",
    "uv": "docs.astral.sh/uv",
}




async def get_docs(query:str,library:str):
    if library not in docs_urls.keys():
        raise ValueError("unkown")
    new_query=f"site:{docs_urls[library]} {query}"

    results=await search_web(new_query)

    if len(results) == 0:
        return "Nothing"








res=asyncio.run(search_web(query))
print(res)