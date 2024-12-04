from django.urls import path
from . import views

urlpatterns = [
  path('energy/positive/', views.EnergyView.as_view(positive=True)),
  path('energy/negative/', views.EnergyView.as_view(positive=False)),
  path('minor/', views.MinorView.as_view()),
  path('set_webhook/', views.SetWebhookView.as_view()),
  path('check_subscription/', views.CheckSubscriptionView.as_view()),
  path('send_invoice/', views.SendInvoiceView.as_view()),
  path('', views.MainView.as_view()),
  path('worker/', views.WorkerView.as_view()),
]
