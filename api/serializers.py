from dataclasses import fields
from rest_framework import serializers
from api.models import Article


# in serializers.Serializer you have to specfy all fields
"""class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()
    
    
    def create(self, validated_data):
        return Article.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
"""
# Now , we are using ModelSerializer which is concise version
# of above serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ["id", "title", "author", "email"]
        #  or can be used for all fields
        fields = "__all__"
