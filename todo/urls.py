from django.urls import path
from .views import TodoDetail, TodoList, TodoCreate

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
]