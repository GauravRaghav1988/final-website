from django.db import models
from django.utils import timezone
# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
# models.py




# class BlogPost(models.Model):
#     heading = models.CharField(max_length=255)
#     post_number = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=255, default="Gaurav Raghav")
#     image = models.ImageField(upload_to='post_images/', blank=True, null=True)
#     content = models.TextField()

#     def __str__(self):
#         return f'{self.post_number}: {self.heading} by {self.user_name}'


class BlogPost(models.Model):
    heading = models.CharField(max_length=255)
    post_number = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, default="Gaurav Raghav")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.post_number}: {self.heading} by {self.user_name} create at {self.created_at}'


