from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from auth.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status

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
