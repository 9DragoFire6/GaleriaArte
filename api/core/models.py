from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateField(auto_now_add = True,
                                 auto_now = False, blank = True,
                                 null = True)
    
    completed = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True,
                             null = True)
    
    def __str__(self):
        return self.task


# Create your models here.
