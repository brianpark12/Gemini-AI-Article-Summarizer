# Fast-Article-Summarizer
By Brian Park
The Article Summarizer summarizes key points from word docx, pdf file, or an website.
# Overview
Python-based utility designed to streamline the pre-production phase of educational science media. By leveraging the Google Gemini 3 Flash model, the script automates the process of distilling dense academic papers (PDFs), reports (DOCX), or online articles into concise, audience-specific summaries and key talking points.

The goal of Fast Art is to bridge the gap between complex scientific literature and engaging video content, ensuring that scripts remain accurate yet accessible to target demographics ranging from middle schoolers to industry professionals.

# Installation
1. Clone the Repository: git clone https://github.com/brianpark12/Fast-Article-Summarizer.git
                         cd fast-art
2. Install dependencies: pip install google-genai httpx
3. Generate API Google Gemini API key from Google AI Studio and insert it into the script

# Features
Multi-format support: The program is able to process .docx, .pdf, and url
Easy Website information extraction: utilizes httpx
Targeted Audience: Users can cutomize summarization based on audience

# Technology
Python: Core logic and script execution
httpx: Fetches information from websites
google-genai: Generative AI for summarization

# Review
Could be improved to allow for more types of files to be applicable such as .png
Can generate scripts for video generator by summarizing articles or news
