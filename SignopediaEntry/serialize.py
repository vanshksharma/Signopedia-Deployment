from django.core.serializers.json import Serializer as JSONSerializer
from django.utils.encoding import force_str
from django.utils.functional import Promise

from rest_framework import serializers
from .models import Post

# class CustomJSONSerializer(JSONSerializer):
#     def default(self, obj):
#         if isinstance(obj, Promise):
#             return force_str(obj)
#         else:
#             return super().default(obj)
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'