from django.shortcuts import render
from pandas.io import json
from .models.performer import Performer
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse, request
from rest_framework.views import APIView

class call_model(APIView):
    def get(self, request):
        predictor = Performer()
        
        if request.method == 'GET':
            course:str = request.GET.get('course', 'por')
            if 'mat' in course:
                predictor = Performer(course='mat')
            
            if not predictor.is_trained:
                predictor.train()
            to_predict = pd.DataFrame.from_dict(json.loads(request.body))
            evaluation= predictor.evaluate_student(to_predict)
            
            return JsonResponse({'predict':  'passed' if evaluation[0]==1 else 'failed'})
