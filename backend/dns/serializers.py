from rest_framework import serializers
from .models import DNSRecord

class DNSRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNSRecord
        fields = ('domain_name', 'ip_address')

    def validate(self, data):
        if 'domain_name' not in data:
            raise serializers.ValidationError("Missing domain name.")
        return data
