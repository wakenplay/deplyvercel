from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class ToDoList(models.Model):
    PENDING = "Pending"
    INPROCESS = "In Process"
    COMPLETED= "Completed"
    WORK_STATUS = [
        (PENDING, "Pending"),
        (INPROCESS, "In Process"),
        (COMPLETED, "Completed"),
    ]
    work_status = models.CharField(
        max_length=100,
        choices=WORK_STATUS,
        default=PENDING,
        null=True
    )
    sn=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    
