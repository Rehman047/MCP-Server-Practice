import trafilatura 
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def html_remover(html_code):
    extracted=trafilatura.extract(
        html_code,
        include_comments=False,
        include_tables=False,
        favor_recall=False
    )
    return extracted

def get_response_from_llm(user_prompt,system_prompt,model):
    api_key=os.getenv("GROQ_API_KEY")

    groq_client=Groq(api_key=api_key)

    chat_completion=groq_client.chat.completions.create(
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":user_prompt}
        ],
        model=model
    )
    return chat_completion.choices[0].message.content