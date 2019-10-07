from django.shortcuts import render, redirect
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    question = Question.objects.get(id=id)
    context = {
        'question': question,
    }
    return render(request, 'detail.html', context)

def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        Question.objects.create(content=content)
        return redirect('questions:index')
    else:
        return render(request, 'form.html')