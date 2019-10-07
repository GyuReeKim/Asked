from django.shortcuts import render, redirect
from .models import Question

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        Question.objects.create(content=content)
        return redirect('questions:index')
    else:
        return render(request, 'form.html')