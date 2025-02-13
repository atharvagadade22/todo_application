# Import the necessary module from Django
from django.db import models

# Create your models here.

# Define a model class for Todo
class Todo(models.Model):
    # Define a string representation method for the model
    def __str__(self):
        # Return the title of the Todo item as its string representation
        return self.Title
    
    # Define the fields of the Todo model
    Title = models.CharField(max_length=50)  # Title field with a maximum length of 50 characters
    Desc = models.TextField(max_length=400)  # Description field with a maximum length of 400 characters
    status = models.BooleanField()  # Status field to indicate whether the Todo item is completed or not
