from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts import load_prompt

_ = load_dotenv(find_dotenv())

prompt = load_prompt("./lecture/data.json")
#prompt = load_prompt("./data.yaml")

chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

print(prompt.format(country="Japan"))