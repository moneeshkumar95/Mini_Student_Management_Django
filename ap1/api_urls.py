from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/student', views.liststudent, name="list"),
    path('api/student/<int:rn>', views.updatestud, name="apiupdate_student"),
    path('api/student/add-mark', views.marks, name="apiadd_mark"),
    path('api/student/add-mark/<str:pk>', views.updatemarks, name="apiupdate_mark"),

]