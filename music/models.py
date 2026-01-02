from django.db import models

# Create your models here.

class Music(models.Model):
    singer = models.ForeignKey('Singer', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='music/')
    audio = models.FileField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.singer.name
    
    class Meta:
        ordering = ['-published_date']
    

class Singer(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=350)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name