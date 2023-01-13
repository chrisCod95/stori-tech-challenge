from django.urls import path

from .views import SummaryEmail

urlpatterns = [
    path('', SummaryEmail.as_view(), name='summary_email'),
]
