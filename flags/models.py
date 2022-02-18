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
    name = (
        ('red1', 'red1'),('red2', 'red2'),('red3', 'red3'),('red4', 'red4'),('red5', 'red5'),
        ('white1', 'white1'),('white2', 'white2'),('white3', 'white3'),('white4', 'white4'),('white5', 'white5'),
        ('blue1', 'blue1'),('blue2', 'blue2'),('blue3', 'blue3'),('blue4', 'blue4'),('blue5', 'blue5'),
    )

    Status = models.CharField(max_length=10, choices=status, default='v')
    Highlight = models.CharField(max_length=10, choices=highlight, default='n')
    color = models.CharField(max_length=10,choices=name, default='blue')
    url = models.CharField(max_length=50,null=True)
    videourl = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,default='')

    class Meta:
        unique_together = ['color']
    def __str__(self):
        return '%s' %(self.color)
class flag1(models.Model):
    name = (
        ('red', 'red'),
        ('white', 'white'),
        ('blue', 'blue'),
    )
    name = models.CharField(max_length=10,choices=name, default='red1' )
    activate =  models.CharField(max_length=10, choices=highlight, default='n')
    class Meta:
        unique_together = ['name']
    def __str__(self):
        return '%s' %(self.name)
