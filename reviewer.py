import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing. Add OPENAI_API_KEY to your .env file."
    )

client = OpenAI(api_key=api_key)


def review_code(code, language):

    prompt = (
        "You are an expert software engineer and code reviewer.\n\n"
        f"Review the following {language} code.\n\n"
        "CODE:\n"
        f"{code}\n\n"
        "Analyze the code for:\n"
        "1. Bugs and logical errors\n"
        "2. Security vulnerabilities\n"
        "3. Code quality and style problems\n"
        "4. Performance and optimization opportunities\n"
        "5. Bad programming practices\n"
        "6. Maintainability issues\n\n"
        "Provide your answer using these sections:\n\n"
        "## Summary\n"
        "Give a short overall assessment.\n\n"
        "## Bugs\n"
        "List each bug, explain why it happens, and give its severity.\n"
        "If there are no bugs, write 'None found'.\n\n"
        "## Security Issues\n"
        "List security vulnerabilities.\n"
        "If there are none, write 'None found'.\n\n"
        "## Optimization\n"
        "Suggest performance and efficiency improvements.\n"
        "If there are none, write 'None found'.\n\n"
        "## Code Quality\n"
        "Suggest improvements for readability, structure, and maintainability.\n\n"
        "## Fixed Code\n"
        "Provide the complete improved version of the code.\n\n"
        "Important:\n"
        "- Do not invent problems that are not present.\n"
        "- Explain technical issues clearly.\n"
        "- Keep suggestions practical."
    )

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text