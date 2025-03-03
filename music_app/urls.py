from django.urls import path

from music_app.views import *

urlpatterns = [
    path('api/get-pattern-string/', GetPatternStringView.as_view(), name='get-pattern-string'),
    path('api/stream/<str:filename>/', StreamAudioView.as_view(), name='stream_audio'),
]