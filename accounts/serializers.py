from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Accounts

class AccountRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ("username", "email", "role", "password")

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class AccountLoginSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role
        return token
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ("id", "username", "email", "role", "is_active", "created_at")