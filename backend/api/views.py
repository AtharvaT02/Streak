
from rest_framework import viewsets
from dns.models import DNSRecord
from dns.serializers import DNSRecordSerializer
from rest_framework.response import Response
from rest_framework import status
import socket



class DNSRecordViewSet(viewsets.ModelViewSet):
    queryset = DNSRecord.objects.all()
    serializer_class = DNSRecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        try:
            domain_name = kwargs.get('domain')
            dns_record = DNSRecord.objects.get(domain_name=domain_name)
            serializer = DNSRecordSerializer(dns_record)
            return Response(serializer.data)
        except DNSRecord.DoesNotExist:
            try:
                ip_address = socket.gethostbyname(domain_name)
                dns_record = DNSRecord.objects.create(domain_name=domain_name, ip_address=ip_address)
                serializer = DNSRecordSerializer(dns_record)
                return Response(serializer.data)
            except socket.gaierror:
                return Response({"Error": "Invalid domain name or unable to resolve IP address"})
