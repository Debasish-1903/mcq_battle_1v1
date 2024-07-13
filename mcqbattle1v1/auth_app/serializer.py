
from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
      
      first_name=serializers.CharField(
           max_length=40,
           required=True,
           error_messages={
                "required":"First Name is required",
                "blank":"First Name is required",
           }

      )
      last_name=serializers.CharField(
           max_length=40,
           required=True,
           error_messages={
                "required":"Last Name is required",
                "blank":"Last Name is required",
           }

      )
      email=serializers.EmailField(
           
           required=True,
           error_messages={
                "required":"email is required",
                "blank":"email is required",
                "invalid":"Please enter a valid email",
           }

      )
      password=serializers.CharField(
           write_only=True,
           required=True,
           error_messages={
                "required":"Password is required",
                "blank":"Password is required",
           }

      )

      



class LoginSerializer(serializers.Serializer):    
    email=serializers.EmailField(
           
           required=True,
           error_messages={
                "required":"email is required",
                "blank":"email is required",
                "invalid":"Please enter a valid email",
           }

      )
    password=serializers.CharField(
           write_only=True,
           required=True,
           error_messages={
                "required":"Password is required",
                "blank":"Password is required",
           }

      )
