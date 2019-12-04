from django.db import models

class Note(models.Model):
    semester = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add= True)
    content = models.FileField(upload_to='upload/')
    chapter = models.CharField(max_length=255)
    link = models.URLField()
    thumnail = models.ImageField(upload_to='upload/')

    def __str__(self):
        return '{}-{}({})'.format(self.semester, self.subject, self.pub_date)
