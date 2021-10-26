from django.shortcuts import render
from .models.performer import Performer

from django.shortcuts import render
from django.http import JsonResponse, request
from rest_framework.views import APIView

class call_model(APIView):
    def get_prediction(self, request):
        predictor = Performer()
        if request.method == 'GET':
            course:str = request.Get('course')
            if 'mat' in course:
                predictor = Performer(course='mat')
            
            evaluation= predictor.evaluate_student(request.body)
            
            return JsonResponse({'predict':  'pass' if evaluation[0]==1 else 'fail'})
