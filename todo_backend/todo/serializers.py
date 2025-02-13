# Import the necessary module from the Django REST framework
from rest_framework import serializers

# Import the Todo model from the current app's models module
from .models import Todo

# Define a serializer class for the Todo model
class TodoSerializer(serializers.ModelSerializer):
    # Meta class to specify the model and fields for the serializer
    class Meta:
        model = Todo  # Specify the model that this serializer is for
        fields = '__all__'  # Include all fields from the model

# The '__all__' value for the fields attribute is a magical method (also known as a dunder method)
# This tells Django to include all fields from the Todo model in the serializer
