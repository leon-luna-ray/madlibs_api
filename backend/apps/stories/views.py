from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class StoriesAPIView(APIView):
    def get(self, request):
        logger.info("StoriesAPIView GET method called")
        try:
            return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in StoriesAPIView: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)