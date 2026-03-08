#By Brian Park
#Summarizer.py is a script that summarizes the content of a docx or pdf file or a website.
#Google Gemini is utilized to summarize the contents of an article and extract key points.
#httpx is used to fetch the contents.
#os is used to access the API key from the environment variable.

import httpx
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")
client = genai.Client(api_key = key)

if key is None:
    print("API KEy is either missing or invalid. Please check .env file and try again.")
    print("Please format it as API_KEY=your_key_here in the .env file.")
    exit()

url = input("Please enter the URL of a document or an article you want to summarize (PDF or DOCX format): ").strip()
information = None

if url.endswith(".pdf"): #checks if the URL is in PDF format.
    type = 'application/pdf'
    doc_data = httpx.get(url).content
    information = types.Part.from_bytes(data = doc_data, mime_type = type)#creates objects from the doucment data in bytes format.

elif url.endswith(".docx"): # checks if the URL is in DOCX format.
    type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    doc_data = httpx.get(url).content
    information = types.Part.from_bytes(data = doc_data, mime_type = type) 

else: #assume it as a website.
    body = httpx.get(url) #extracts the content of the website.
    information = f"The content of the website: {body.text}"

level = input("\nWhat is the target audience for this video? (e.g., middle school college students, or workers in the field): ").strip().lower()
prompt = f"This article will be for {level} level. Precisely summarize the content of the document around 3 sentences, and provide a list of around 5 key points from the document. More or less keypoints are allowed if truly necessary."

try:
    response = client.models.generate_content( #creates response based on gemini 3 flash model.
    model = "gemini-3-flash-preview",
    contents = [information, prompt]
)
except:
    print("An error occurred while generating the summary. Please try again later.")
    exit()

print("\n" + response.text) #prints output.
