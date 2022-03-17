from django.db import models

# Create your models here.

# Models are classes
class List(models.Model):
    # We're using sqlite which is the default. Not suitable for anything but small volume systems.
    # two things in our list. Item itself 200 characters and a boolean for whether or not the item has been completed.
    
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    # This is important for the admin page.
    def __str__(self):
        return self.item