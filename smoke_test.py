from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

MODEL = "gemini-3.1-flash-lite"

response = client.models.generate_content(
    model=MODEL,
    contents="Say hi"
)

print(response.text)