from django.db import models
from django.utils import timezone




class task (models.Model):
    title = models.CharField(max_length=50)
    asign_date = models.DateTimeField(default=timezone.now)
    Subject = models.TextField(max_length=1000)
    Target_Date = models.DateTimeField
    Done = models.BooleanField(default=False)
    Actualdate = models.DateTimeField
    Doc =models.FileField(upload_to='tasksfile/',default="")
    image =models.ImageField (upload_to='tasksImage/')


    def __str__(self):
        return self.title

    class Meta :
        ordering=('-id',)
        verbose_name='Task'
        verbose_name_plural='Tasks'



# Create your models here.
