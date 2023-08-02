from django.http import HttpResponse

from .models import Client


def index(request):
    clients = Client.objects.all()
    res = ''
    for client in clients:
        res += f'{client.name} - {client.email} - {client.phone} - {client.age} - {client.city}<br>'
    return HttpResponse(res)
