from django.db import models

class FunctionDefinition(models.Model):
    name = models.CharField(max_length=100)
    code = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
