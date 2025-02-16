from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.base.services.mistral import prompt_mistral

class MadlibsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        prompt = ("Generate a madlibs story template with the following structure:\n\n"
                  "Once upon a time in a ________(adjective)______ kingdom, there lived a ________(adjective)______ ________(noun)______ named ________(name)_______. "
                  "______(name)_______ loved to _________(verb)______ ________(adverb)_______. One day, while _________(verb)______ through the ________(adjective)______ forest, "
                  "______(name)_______ found a ________(adjective)______ ________(noun)_______.\n\n"
                  "The ________(noun)_______ was ________(adjective)_______ and ________(adjective)_______. It had ________(number)_______ ________(plural noun)_______ and a ________(adjective)______ ________(noun)_______. "
                  "______(name)_______ decided to take it home and _________(verb)______ it.\n\n"
                  "Back at the ________(adjective)______ castle, ________(name)_______ ________(adverb)______ _________(past tense verb)______ the ________(noun)_______. Suddenly, the ________(noun)_______ came to life and began to _________(verb)______ ________(adverb)_______. "
                  "It _________(past tense verb)______ ________(name)_______ to _________(verb)______ it to the ________(adjective)______ ________(noun)_______ in the ________(adjective)______ mountains.\n\n"
                  "______(name)_______ and the ________(noun)_______ set off on their ________(adjective)______ journey. Along the way, they _________(past tense verb)______ ________(number)_______ ________(plural noun)_______, _________(past tense verb)______ through ________(number)_______ ________(plural noun)_______, "
                  "and even _________(past tense verb)______ a ________(adjective)______ ________(noun)_______.\n\n"
                  "Finally, they reached the ________(adjective)______ ________(noun)_______ at the top of the ________(adjective)______ mountain. The ________(noun)_______ thanked ________(name)_______ and _________(past tense verb)______ a ________(adjective)______ ________(noun)_______ before disappearing.\n\n"
                  "______(name)_______ returned home, feeling ________(adjective)______ and ________(adjective)_______. From that day forward, ________(name)_______ knew that ________(adverb)______ _________(verb)______ could lead to the most ________(adjective)______ adventures.\n\n"
                  "---\n\n"
                  "Fill in the blanks with your chosen words to create a unique and exciting story!")

        story = prompt_mistral(prompt)
        return Response({'story': story}, status=status.HTTP_200_OK)