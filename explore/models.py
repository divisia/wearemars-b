from django.db import models

class GenericRecord(models.Model):
    typestr = models.CharField(max_length=64)
    value = models.TextField()

    def __str__(self):
        return f'{self.typestr} : {self.value[0:min(20, len(self.value))]}'
