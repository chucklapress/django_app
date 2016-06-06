from django.db import models
class Item(models.Model):
    full_name = models.CharField(max_length=50)
    team_name = models.CharField(max_length=10)
    attempt = models.FloatField()
    completion = models.FloatField()
    att_pct = models.FloatField()



    def __str__(self):
        return self.full_name

