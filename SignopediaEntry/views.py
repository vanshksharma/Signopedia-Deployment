from django.shortcuts import render
from .apps import SignopediaentryConfig

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
from keras.utils.image_utils import img_to_array
import numpy as np
import tensorflow as tf
import os
from django.conf import settings

from django.http import JsonResponse
from .serialize import PostSerializer
# Create your views here.


class call_model(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.model_name="model.h5"
        self.loaded_model=tf.keras.models.load_model(os.path.join(settings.MODEL_ROOT,self.model_name))
        
    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        print(request.data["image"])
        
        if posts_serializer.is_valid():
            posts_serializer.save()
        
            # return JsonResponse({"class":str(np.argmax(response)+1)})
            # return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        img=posts_serializer.data["image"].split("/")[-1]
        print("img---->",img)
        # return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        
        try:
            im=Image.open(os.path.join(settings.MEDIA_ROOT,"post_images",img))
            im=im.resize((30,30))
            im=img_to_array(im)
            im=np.expand_dims(im,axis=0)
            print("Hitted On the URL------------------------------->>>")
            response = self.loaded_model.predict(im)
            # print(os.path.join(settings.MEDIA_ROOT,"post_images",im))
            os.remove(os.path.join(settings.MEDIA_ROOT,"post_images",img))
            return JsonResponse({"class":str(np.argmax(response)+1)})
        except Exception as e:
            print("error----->",e)
            
        
        
