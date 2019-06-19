from django.urls import path
from .views import home,detail,remove,add_new_todo,edit_todo

urlpatterns = [
    path('', home, name ="home"),
    path('create/', add_new_todo, name ="list-add"),
    path('<int:pk>/', detail, name ="list-detail"),
    path('<int:pk>/delete/', remove, name ="list-delete"),
    path('<int:pk>/update/', edit_todo, name ="list-update"),
    
]
