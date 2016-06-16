from django.db import models


class Contents(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    create_dt = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'contents'
