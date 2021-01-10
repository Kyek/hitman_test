from django.db import models
from django.contrib.auth.models import User


class Hitman(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)
    managed = models.ManyToManyField(to=User, related_name="hitmen_managed")


class Hit(models.Model):
    class HitStatus(models.TextChoices):
        ASSIGNED = "A"
        FAILED = "F"
        COMPLETED = "C"

    description = models.CharField(max_length=128)
    target_name = models.CharField(max_length=128)
    asignee = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name="hits")
    created_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name="hits_created")
    status = models.CharField(max_length=1, choices=HitStatus, default=HitStatus.ASSIGNED)
