from rest_framework.serializers import ModelSerializer
from account.models import Account

class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'date_joined', 'last_login']
