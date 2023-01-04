from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=25)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task

class OwnerTask(models.Model):
    name = models.CharField(max_length=20)
    fk_task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name