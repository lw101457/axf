from django.db import models

# Create your models here.
class Bases(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    trackid = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Wheel(Bases):
    class Meta:
        db_table = 'axf_wheel'