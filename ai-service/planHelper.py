import os
import openai

def planHelper(idea):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Suggest a recommendation for the following idea\n\n" + idea + "\n\nrecommendation:",
        temperature=0.7,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return (response["choices"][0]["text"])

planHelper("I want to open an ice cream shop in finland")