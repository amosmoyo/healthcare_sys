from django.db import models

# creating an abstract class for the time the model was created and updated
# It will not return an instance of the class

class TrackModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
    ordering = ('created_at', ) # asceding ordering