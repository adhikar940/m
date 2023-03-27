from django.db import models
from django.core.validators import RegexValidator
from n.models import *
class description(models.Model):
    min = (
        ('0', '0'),
        ('1', '1'),
    )
    minister=models.CharField(max_length=5,choices=min, default='' )
    Session_Title = models.ForeignKey(Sessions,on_delete=models.CASCADE, null=True, blank=True)
    date = models.CharField(max_length=15,null=True)
    time = models.CharField(max_length=15,null=True)
    ministry = models.CharField(max_length=50,null=True)
    videotime = models.CharField(max_length=15,null=True)
    mpname= models.CharField(max_length=50,null=True)
    state_video= models.CharField(max_length=50,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,blank=True)
    party= models.CharField(max_length=50,null=True)
    image_data = models.TextField(null=True, blank=True, validators=[RegexValidator(
        regex=r'^data:image\/\w+;base64,',
        message='Invalid base64 encoded image format',
        code='invalid_base64_image'
    )])
    class Meta:
        abstract = True
