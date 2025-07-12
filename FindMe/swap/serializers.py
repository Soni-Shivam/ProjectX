# # swap/serializers.py

# from rest_framework import serializers
# from .models import Swap
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class SwapSerializer(serializers.ModelSerializer):
#     user_initiater = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     user_reciever = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     class Meta:
#         model = Swap
#         fields = '__all__'