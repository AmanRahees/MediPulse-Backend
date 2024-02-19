from rest_framework import serializers
from accounts.models import Accounts
from base.models import Wallet, Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"

class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    class Meta:
        model = Wallet
        fields = "__all__"