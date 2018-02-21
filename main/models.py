from django.db import models

# Create your models here.

class Notification(models.Model):
    email = models.EmailField(blank=True, null=True)
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=80)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name != '' or self.surname != '':
            value = self.name
            if value != '':
                value += ' '
            value += self.surname
        else:
            value = self.email
        return value
