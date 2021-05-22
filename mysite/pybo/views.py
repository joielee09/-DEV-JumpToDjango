from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question
from django.utils import timezone

def index(request): # index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체.
  
    # pybo 목록출력
  question_list = Question.objects.order_by('-create_date')
  context  = {'question_list': question_list}

  # return HttpResponse("안녕하세요, pybo에 오신 것을 환영합니다.")
  return render(request, 'pybo/question_list.html', context) # django template

def detail(request, question_id):

  # question = Question.objects.get(id=question_id)
  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}

  # return HttpResponse("답변이 아직 작성되지 않았습니다.")
  return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)