from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)  # duplicate check on this base
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True)
    source = models.CharField(max_length=50, default="website")  # website/whatsapp/instagram
    status = models.CharField(max_length=20, default="new")  # new/contacted/follow-up
    created_at = models.DateTimeField(auto_now_add=True)
    last_contacted = models.DateTimeField(blank=True, null=True)


