from django.shortcuts import render
from .models import *
# Create your views here.
from os import name
from django.shortcuts import redirect, render

from django.contrib import messages
import json
from django.http import JsonResponse
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image

def index(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        brainImage = request.FILES.get('brainImage')
        
        obj = PatientData.objects.create(
            name=name,
            age = age,
            brainImage=brainImage,
        )
        
        obj.save()
        print(obj.brainImage.name)
        model = load_model("D:/project5/ml_project/brain_tomer/BrainTomer10Epochs.h5")
        img = cv2.imread("D:/project5/ml_project/public/"+obj.brainImage.name)
        img=Image.fromarray(img,"RGB")
        img=img.resize((64,64))
        img_arr=np.array(img)
        input_img=np.expand_dims(img_arr,axis=0)
        result=model.predict(input_img)
        result = result[0][0]
        if result == 0.0:
            msg="No, Tumer is not Detected"
        else:
            msg="Yes, Tumer is Detected"

        obj.result=result
        obj.save()
        return render(request,"detection.html",{'obj':obj,'msg':msg})
        
    return render(request,"index.html")
