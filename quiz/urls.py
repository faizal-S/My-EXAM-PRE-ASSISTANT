from django.urls import path
from .views import upload_quiz

app_name = 'quiz'

urlpatterns = [
    path('upload/', upload_quiz, name='upload_quiz'),
]