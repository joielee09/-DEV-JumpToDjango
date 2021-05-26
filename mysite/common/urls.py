from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), #view를 참조할 때는 common의 login.html을 참조하라
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]