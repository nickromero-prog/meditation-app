from django.db import models
from django.contrib.auth import get_user_model

# Session Model (main resource)
class Session(models.Model):
  # time_length = models.(max_length=3)
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'time_length': self.time_length
    }

  def __str__(self):
    return self.time_length
