from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    question = Question.objects.get(id=id)
    # answers = Answer.objects.filter(question_id=id)
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

def answer_create(request, question_id):
    if request.method == "POST":
        content = request.POST.get('content')
        question = Question.objects.get(id=question_id)
        Answer.objects.create(content=content, question=question)
        return redirect('questions:detail', question_id)
    else:
        pass

def answer_delete(request, question_id, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.delete()
    return redirect('questions:detail', question_id)