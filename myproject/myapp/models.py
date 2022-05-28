from django.db import models

# Create your models here.

class Feature():
    def __init__ (self, id, name, details):
        self.id = id
        self.name = name
        self.details = details
