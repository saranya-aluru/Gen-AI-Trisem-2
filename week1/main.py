import os
from dotenv import load_dotenv
from google import genai

print("Program Started!")

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

print("Gemini API Key Loaded Successfully!")

# Initialize Gemini
client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")

# Make first LLM API call
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="single word about clustering in AI"
)

# Display response
print("\n========== LLM RESPONSE ==========")
print(response.text)
print("==================================")