# utils/config.py
import os
from dotenv import load_dotenv
from groq import Groq


BASE_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(BASE_DIR, "..", "APIKeys.env")
ENV_PATH = os.path.abspath(ENV_PATH)

print("Loading env from:", ENV_PATH)

load_dotenv(dotenv_path=ENV_PATH)

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
