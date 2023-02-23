import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response3(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.2,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )
    return response["choices"][0]["text"]

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.3,
    )
    return response["choices"][0]["text"]


def summarizing(pdf_content):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=pdf_content,
    temperature=0.5,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=1
    )
    return response["choices"][0]["text"]