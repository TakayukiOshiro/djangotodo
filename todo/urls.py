from django.urls import path
from .views import TodoDetail, TodoList, DetailView

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail")
]