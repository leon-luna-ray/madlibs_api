from django.http import JsonResponse
from mistralai import Mistral
from django.conf import settings
from rest_framework.decorators import api_view

@api_view(['POST'])
def generate_story(request):
    """Generate a madlibs story using Mistral AI"""
    try:
        client = Mistral(api_key=settings.MISTRAL_API_KEY)
        
        prompt = """Generate a fun and creative madlibs story. 
                   Include placeholders for nouns, verbs, adjectives, and adverbs.
                   Make the story engaging and suitable for all ages."""
        
        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{
                "role": "user",
                "content": prompt,
            }]
        )
        
        story = chat_response.choices[0].message.content
        
        return JsonResponse({
            'success': True,
            'story': story
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)