from django.shortcuts import render

# Create your views here.
from tchat.models import Room


def index_view(request):
    return render(request, 'tchat/index.html', {
        'rooms': Room.objects.all(),
    })


def room_view(request, room_name):
    tchat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'tchat/room.html', {
        'room': tchat_room,
    })