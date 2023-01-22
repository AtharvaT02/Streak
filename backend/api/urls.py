# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

from django.urls import path
from .views import DNSRecordViewSet

urlpatterns = [
    path('dnsrecord/', DNSRecordViewSet.as_view({'post': 'create','get': 'retrieve'}), name='dnsrecord'),
    path('dnsrecord/<str:domain>/', DNSRecordViewSet.as_view({'get': 'retrieve'}), name='dnsrecord'),
]
