from django.urls import path
from . import views

urlpatterns = [
  path('matrix/<str:date1>/', views.MatrixView.as_view()),
  path('matrix/<str:date1>/<str:date2>/', views.MatrixView.as_view()),
	path('worker/', views.WorkerView.as_view())
]
