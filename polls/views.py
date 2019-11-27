from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    """The home page for Polls app."""
    return render(request, 'polls/index.html')

def questions(request):
    """Show all questions"""
    # Query the database for all questions
    questions = Question.objects.all()
    # Context that will send to the template
    context = {'questions': questions}
    return render(request, 'polls/questions.html', context)
