from django.db import models

class db_models(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    query = models.TextField()
    class Meta:
        db_table = "customer_qus"