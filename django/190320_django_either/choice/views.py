from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions
    }
    return render(request, 'choice/index.html', context)
    
def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    answers = question.answer_set.all()
    if answers:
        first = len(question.answer_set.filter(pick=1))*100 // len(answers)
        second = 100-first
    else:
        first, second = 0, 0
    context = {
        'question' : question,
        'answers' : answers,
        'first' : first,
        'second' : second,
    }
    print('#######', question.img_1)
    return render(request, 'choice/detail.html', context)
    
def new(request):
    if request.method == "POST":
        question = Question()
        question.title = request.POST.get('title')
        question.select_1 = request.POST.get('select_1')
        question.img_1 = request.FILES.get('img_1')
        question.select_2 = request.POST.get('select_2')
        question.img_2 = request.FILES.get('img_2')
        question.save()
        return redirect('choice:index')
    else:
        return render(request, 'choice/new.html')
    
def edit(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == "POST":
        question.title = request.POST.get('title')
        question.select_1 = request.POST.get('select_1')
        question.select_2 = request.POST.get('select_2')
        question.save()
        return redirect('choice:detail', question_pk)
    else:
        context = {
            'question' : question,
        }
        return render(request, 'choice/edit.html', context)

def delete(request, question_pk):
    if request.method == "POST":
        question = Question.objects.get(pk=question_pk)
        question.delete()
        return redirect('choice:index')
    else:
        return redirect('choice:index')

def new_answer(request, question_pk):
    if request.method == "POST":
        answer = Answer(question_id=question_pk)
        answer.pick = request.POST.get('pick')
        answer.comment = request.POST.get('comment')
        answer.save()
        return redirect('choice:detail', question_pk)
        
def answer_delete(request, question_pk, answer_pk):
    if request.method == "POST":
        answer = Answer(pk=answer_pk)
        answer.delete()
    return redirect('choice:detail', question_pk)