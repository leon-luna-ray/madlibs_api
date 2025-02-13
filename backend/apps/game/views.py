import json
import random

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TemplateSerializer


class RandomTemplateView(APIView):
    def get(self, request, *args, **kwargs):
        json_file_path = (
            settings.BASE_DIR / "apps" / "game" / "game_data" / "templates.json"
        )

        with open(json_file_path, "r") as json_file:
            templates_data = json.load(json_file)

        templates = templates_data["templates"]

        random_index = random.randint(0, len(templates) - 1)
        selected_template = templates[random_index]

        serializer = TemplateSerializer(selected_template)

        return Response(serializer.data, status=status.HTTP_200_OK)
