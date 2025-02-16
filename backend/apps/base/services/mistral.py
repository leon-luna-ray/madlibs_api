from mistralai import Mistral
from django.conf import settings
import os

def prompt_mistral(prompt):
    api_key = settings.MISTRAL_API_KEY
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    result = chat_response.choices[0].message.content
    return result