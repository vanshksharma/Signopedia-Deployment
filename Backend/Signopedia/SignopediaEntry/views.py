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
from .serialize import CustomJSONSerializer
# Create your views here.


class call_model(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.model_name="model.h5"
        self.loaded_model=tf.keras.models.load_model(os.path.join(settings.MODEL_ROOT,self.model_name))
        
    def get(self,request):
        if request.method == 'GET':
            
            # sentence is the query we want to get the prediction for
            # params =  request.GET.get('qry')
            im=Image.open(os.path.join(settings.MEDIA_ROOT,"image.png"))
            im=im.resize((30,30))
            im=img_to_array(im)
            im=np.expand_dims(im,axis=0)
            print("Hitted On the URL------------------------------->>>")
        
            # serializer = CustomJSONSerializer()
            
            
            # predict method used to get the prediction
            response = self.loaded_model.predict(im)
            
            # return JsonResponse(serializer.serialize(["hello_world"]), safe=False)
            
            # returning JSON response
            return JsonResponse({"class":str(np.argmax(response)+1)})
        
        
