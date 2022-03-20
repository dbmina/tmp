from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save  # 추가
from django.dispatch import receiver 
# Create your models here.

class Profile(models.Model):   # 추가    
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    college = models.CharField(max_length=20, blank=True)    
    major = models.CharField(max_length=20, blank=True)
    college_filtered_users = []
    major_filtered_users = []

    # for user in User.objects.filter(profile__college = college).exclude(username= username):
    #     college_filtered_users.append(user.username)
    #     if college_filtered_users == []:
    #          college_filtered_users.append("같은 학교 사람이 없습니다.")
            

    # for user in User.objects.filter(profile__major = major).exclude(username= username):
    #      major_filtered_users.append(user.username)
    #      if major_filtered_users == []:
    #         major_filtered_users.append("같은 전공 사람이 없습니다.")

    @receiver(post_save, sender=User)  
    def create_user_profile(sender, instance, created, **kwargs):        
        if created:          
            Profile.objects.create(user=instance)  
    
    @receiver(post_save, sender=User)  
    def save_user_profile(sender, instance, **kwargs):        
        instance.profile.save()