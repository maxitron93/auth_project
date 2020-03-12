from django.urls import path
from account.api.views import Register, ListAccounts

urlpatterns = [
    path('', ListAccounts.as_view(), name='list_accounts'),
    path('register', Register.as_view()),  # Creates account and sends back token
]
