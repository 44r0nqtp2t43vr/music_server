from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse, Http404
import os
from django.conf import settings

# Create your views here.
class GetPatternStringView(APIView):
    def get(self, request):
        return Response(
            {
                "data": "<000000000000000000000000000000>",
            }, 
            status=status.HTTP_200_OK,
        )
    
class StreamAudioView(APIView):
    """API view to stream an audio file from media/audio/"""

    def get(self, request, filename):
        file_path = os.path.join(settings.MEDIA_ROOT, "audio", filename)
        print(file_path)

        if not os.path.exists(file_path):
            return Response(
                {"error": "Audio file not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        return FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
