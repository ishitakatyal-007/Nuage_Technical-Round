from rest_framework import serializers

from .models import Friends, TransactionIOU

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('__all__')

class TransactionIOUSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionIOU
        fields = ('__all__')
