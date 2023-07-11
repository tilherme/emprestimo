from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('loan-request/', loan_request_view, name='loan-request'),

]