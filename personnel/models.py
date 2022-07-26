from django.db import models

# Create your models here.

class Personnel(models.Model):
    id_perso = models.AutoField(primary_key=True)
    name_per = models.CharField(max_length=20, blank=True, null=True)
    prenoms_perso = models.CharField(max_length=20, blank=True, null=True)
    email_perso = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personnel'

    def __str__(self):
        return  self.name_per