from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('home/', views.TaskListView.as_view(), name='home'),
    path('details/<int:pk>/', views.TaskDetailView.as_view(), name='details'),
    path('edit/<int:pk>/', views.TaskUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view() ,name='delete'),

]
