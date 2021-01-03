from django.db import models
from django.contrib.auth import get_user_model

# Session Model (main resource)
class Session(models.Model):
  time_length = models.IntegerField()
  owner = models.ForeignKey(get_user_model(), related_name='sessions', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def as_dict(self):
    """Returns dictionary version of Session models"""
    return {
        'id': self.id,
        'time_length': self.time_length,
        'created_at': self.created_at
    }

  def __int__(self):
    return self.time_length
