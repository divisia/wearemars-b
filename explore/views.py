from django.shortcuts import render
from .models import GenericRecord

try:
    clicks = GenericRecord.objects.get(typestr='clicks')
except GenericRecord.DoesNotExist:
    clicks = GenericRecord.objects.create(typestr='clicks', value='0')
clicks.value = int(clicks.value)

def landing(request):
    clicks.value += 1 # int(clicks.value) + 1
    clicks.save()

    for key in ['X_FORWARDED_FOR', 'REMOTE_ADDR']:
        ip = request.META.get(key, None)
        if ip:
            break
    
    return render(request, 'landing.html', {
        'ip': ip,
        'clicks': clicks.value,
    })
