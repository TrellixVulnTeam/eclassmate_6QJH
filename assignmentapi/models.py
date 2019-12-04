from django.db import models
from django.contrib.auth.models import User



class Answer(models.Model):
    anstext= models.TextField(blank=True)
    ansfile = models.FileField(upload_to='uploads/')
    pub_date = models.DateTimeField(auto_now_add=True)
    matename = models.ForeignKey(User,on_delete=models.CASCADE)
    upvote = models.IntegerField()
    downvote = models.IntegerField()




class Images(models.Model):
    answer = models.ForeignKey(Answer, default=None,on_delete=models.CASCADE)
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')





class Assignment(models.Model):
    title = models.TextField()
    subject = models.CharField(max_length=255)
    content_assignment = models.FileField(upload_to='uploads/') 
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    answer = models.ManyToManyField(Answer, blank=True)


    def __str__(self):
        return self.subject



