from rest_framework.views import APIView
from account.models import Account
from account.api.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ListAccounts(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
