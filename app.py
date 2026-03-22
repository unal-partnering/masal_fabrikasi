import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv() # .env dosyasındaki anahtarları yükler
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
