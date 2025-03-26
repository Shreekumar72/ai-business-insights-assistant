import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Correct: load from environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Choose a working model from your list
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def generate_prompt(user_query):
    return f"""
    You are a Business Strategy Assistant.

    Query: {user_query}

    Tasks:
    1. Identify the domain (finance, sales, ops, etc.)
    2. Break the query into reasoning steps
    3. Give 3 strategic and actionable recommendations

    Format your answer:
    - Domain:
    - Breakdown:
    - Recommendations:
    """

def get_business_insight(user_query):
    prompt = generate_prompt(user_query)
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    query = input("Enter your business question: ")
    result = get_business_insight(query)
    print("\n--- AI Insight ---\n")
    print(result)
