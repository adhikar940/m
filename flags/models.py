from django.db import models
highlight = (
    ('y', 'y'),
    ('n', 'n'),
)
class flag(models.Model):
    status = (
        ('v', 'v'),
        ('p', 'p'),
    )
    Status = models.CharField(max_length=10, choices=status, default='v')
    Highlight = models.CharField(max_length=10, choices=highlight, default='n')
    color = models.CharField(max_length=10)
    url = models.CharField(max_length=50,null=True)
    videourl = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)

    class Meta:
        unique_together = ['color']
    def __str__(self):
        return '%s' %(self.color)
class flag1(models.Model):
    name = models.CharField(max_length=10,default='red' )
    activate =  models.CharField(max_length=10, choices=highlight, default='n')
    class Meta:
        unique_together = ['name']
    def __str__(self):
        return '%s' %(self.name)
