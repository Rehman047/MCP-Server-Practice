#Steps for AI Webscrapping
#Search the web
#Open official documentation
#Read them and write code accordingly

import http.client
import json
from dotenv import load_dotenv
import os
load_dotenv()

query="hello"
def search_web(query) -> dict | None:
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
    "q": query, "num":2
    })
    headers = {
    'X-API-KEY': os.getenv("SERPER_API_KEY"),
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

print(search_web(query))