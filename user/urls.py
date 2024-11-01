from django.urls import path
from . import views

urlpatterns = [
  path('user/', views.UserView.as_view()),
  path('refresh/', views.RefreshView.as_view()),
  path('matrix_requests/', views.MatrixRequestsView.as_view()),
  path('masters/<str:name>/', views.MastersView.as_view()),
  path('sessions/', views.SessionsView.as_view()),
	path('worker/', views.LocalWorkerView.as_view())
]