from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class PasspredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'passpredictor'

    #Load our model
    path = os.path.join(settings.Models, 'models.p')
