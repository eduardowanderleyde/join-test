from rest_framework import serializers
from ...models import Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'
        extra_kwargs = {'id': { 'read_only': True } }
