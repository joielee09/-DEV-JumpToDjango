from django.http.response import HttpResponse
from django.shortcuts import render

def index(request): # index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체.
  return HttpResponse("안녕하세요, pybo에 오신 것을 환영합니다.")