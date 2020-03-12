from rest_framework.views import APIView
from account.models import Account
from account.api.serializers import RegistrationSerializer, AccountSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


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

# Using ObtainAuthToken from rest_framework to create custom login (returns the user's Token)
class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class ListAccounts(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
