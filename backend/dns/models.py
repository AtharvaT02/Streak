from django.db import models

# Create your models here.

class DNSRecord(models.Model):
    domain_name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
