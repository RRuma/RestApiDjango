from django.db import models

# Create your models here.
class Brand(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    brandName = models.CharField(max_length=140)

    def __str__(self):
        return self.brandName

    description = models.TextField()

