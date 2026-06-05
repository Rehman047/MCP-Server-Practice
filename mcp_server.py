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
    
res=asyncio.run(search_web(query))
print(res)