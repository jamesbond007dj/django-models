from django.db import models

class Gibson(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField()
    field_name = models.ImageField(upload_to='static/img', height_field=None, width_field=None, max_length=10000)
   

    def __str__(self):
        return self.title 