import os
import certifi
from google import genai
from dotenv import load_dotenv

load_dotenv()
os.environ['SSL_CERT_FILE'] = certifi.where()
 
 
client = genai.Client()
response = client.models.generate_content(model="gemini-2.5-flash",contents="python")
 
print(response.text)