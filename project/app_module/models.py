from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=34)

    def __str__(self):
        return self.name
