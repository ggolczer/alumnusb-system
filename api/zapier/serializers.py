from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Contact
  
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__' 




    
      