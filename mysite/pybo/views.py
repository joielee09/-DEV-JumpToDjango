from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Question
from django.utils import timezone
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request): # index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체.
  
  page = request.GET.get('page', '1')  # 페이지
  
  # pybo 목록출력
  question_list = Question.objects.order_by('-create_date')
  context  = {'question_list': question_list}
  
  # 페이징처리
  paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
  page_obj = paginator.get_page(page)

  context = {'question_list': page_obj}
  # return HttpResponse("안녕하세요, pybo에 오신 것을 환영합니다.")
  return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):

  # question = Question.objects.get(id=question_id)
  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}

  # return HttpResponse("답변이 아직 작성되지 않았습니다.")
  return render(request, 'pybo/question_detail.html', context)

@login_required
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # 추가한 속성 author 적용
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required
def question_create(request):
    """
    pybo 질문생성
    """
    if(request.method == 'POST'):
      form = QuestionForm(request.POST) 
      if form.is_valid(): # POST 요청 받은 form이 유효한 지 검사
        question = form.save(commit=False) # commit=False: 임시저장
        question.author = request.user  # 추가한 속성 author 적용
        question.create_date = timezone.now() # question 객체를 반환 받아 create_date 값 설정 후
        question.save() # 데이터로 실제 저장
        return redirect('pybo:index')
    else:
      form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

