from django.shortcuts import render
from .forms import QuizForm

def upload_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            # Process the uploaded files
            return redirect('quiz:success')
    else:
        form = QuizForm()
    return render(request, 'quiz/upload.html', {'form': form})