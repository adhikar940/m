from django.db import models
highlight = (
    ('y', 'y'),
    ('n', 'n'),
)
class flag1(models.Model):
    name = (
        ('red', 'red'),
        ('white', 'white'),
        ('blue', 'blue'),
    )
    name = models.CharField(max_length=10,choices=name, default='blue' )
    activate =  models.CharField(max_length=10, choices=highlight, default='n')
    class Meta:
        unique_together = ['name']
    def __str__(self):
        return '%s' %(self.name)
class flag(models.Model):
    status = (
        ('v', 'v'),
        ('p', 'p'),
    )
    Status = models.CharField(max_length=10, choices=status, default='v')
    Highlight = models.CharField(max_length=10, choices=highlight, default='n')
    color = models.ForeignKey(flag1, on_delete=models.CASCADE,null=True, default='')
    url = models.CharField(max_length=50,null=True)
    videourl = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,default='')
    def __str__(self):
        return '%s' %(self.name)
