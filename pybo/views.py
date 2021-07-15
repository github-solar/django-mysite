from django.shortcuts import render, get_object_or_404, redirect
#get_object_or_404를 임포트 하는 것은 오류발생시 화면 메시지 출력하기 위해서 추가한다.
#from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

def index(request):
    question_list = Question.objects.order_by('-create_date')
    #-내림차순으로 정렬
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)
    #return HttpResponse("pybo 환영합니다.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.create_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()

    context = {'question':question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    #답변 등록은 리턴 render가 아니고 리다렉트로 해줘야 한다.

def question_create(request):  #질문 등록 함수 생성
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else: #request.method == 'GET'
        form = QuestionForm()

    #form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


# Create your views here.
