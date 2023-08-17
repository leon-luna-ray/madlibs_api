from rest_framework import serializers

class TemplateSerializer(serializers.Serializer):
    title = serializers.CharField()
    blanks = serializers.ListField(child=serializers.CharField())
    value = serializers.ListField(child=serializers.CharField())
