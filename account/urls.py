from django.urls import path
from account.api.views import ListAccounts

urlpatterns = [
    path('', ListAccounts.as_view(), name='list_accounts'),
]