from django.urls import path
from pybo import views

app_name = 'pybo'
# url 별칭 - 네임스페이스다.

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create')
]