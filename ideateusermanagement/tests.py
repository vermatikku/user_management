from django.test import TestCase

# Create your tests here.

# from datetime import datetime
from rest_framework import serializers
from .serializers import UserBasicDetailsSerializer
from .models import UserBasicDetails

class Comment:
    # def __init__(self, email, content, created=None,user_basic):
    def __init__(self, content,user_basic):
        # self.email = email
        self.content = content
        self.user_basic = user_basic
        # print(content)
        # self.created = created or datetime.now()
# comment = Comment(email='leila@example.com', content='foo bar')
# serializer = CommentSerializer(data={'user': {'email': 'foobar', 'username': 'doe'}, 'content': 'baz'})
class Dummy:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class CommentSerializer(serializers.Serializer):
    # email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()
    user_basic = UserBasicDetailsSerializer()
    def create(self, validated_data):
        user_basic_data = validated_data.get('user_basic')
        user_basic_details = UserBasicDetails.objects.create(**user_basic_data)
        # user_basic_details.save()
        return Comment(**validated_data)

def test1():
    # from ideateusermanagement.tests import Comment,CommentSerializer
    cs = CommentSerializer(data={'content':'c0','user_basic':{'middle_name':'mn0','user_name':'un0','mobile_number':'00'}})
    cs.is_valid()
    cs.data
    # cs.save()