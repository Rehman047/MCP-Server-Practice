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
from fastmcp import FastMCP
load_dotenv()
import sys


mcp=FastMCP("any_name")

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
        response = await client.get(url, timeout=30.0)
        cleaned_response=html_remover(response.text)
        return cleaned_response




@mcp.tool()
async def get_docs(query:str):
    """
    Search the latest docs for a given query
    
    """
   
    results=await search_web(query)

    print("SERPER RESULTS:", results, file=sys.stderr)
    if len(results['organic']) == 0:
        return "Nothing"
    texts=[]
    for result in results['organic']:
        link=result.get("link","default")
        page_text=await fetch_url(link)
        if page_text:
            labelled_page_text=f"SOURCE {link} \n {page_text}"
            texts.append(labelled_page_text)
    return "\n\n".join(texts)





def main():
    mcp.run(transport="stdio")

if __name__=="__main__":
    main()