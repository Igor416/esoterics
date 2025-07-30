from django.urls import path
from . import views

urlpatterns = [
  path('user/', views.UserView.as_view()),
  path('refresh/', views.RefreshView.as_view()),
  path('matrix_requests/', views.MatrixRequestsView.as_view()),
  path('matrix_requests/<str:id>/', views.MatrixRequestsView.as_view()),
	path('worker/', views.WorkerView.as_view())
]