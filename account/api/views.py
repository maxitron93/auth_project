from rest_framework.views import APIView
from account.models import Account
from account.api.serializers import RegistrationSerializer, AccountSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token


class Register(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {} # This is what we'll return to the view
        if serializer.is_valid():
            account = serializer.save()
            data['email'] = account.email
            token = Token.objects.get(user=account)
            data['token'] = token.key
        else:
            # If the serializer throws any errors, return the error
            data = serializer.errors
        return Response(data=data, status=status.HTTP_201_CREATED)

class ListAccounts(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
