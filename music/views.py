from django.http import HttpResponse
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    html = "<h4>This is the music app homepage</h4>"
    for album in all_albums:
        url = '/music/'+ str(album.id)+'/'
        html+=  '<a href="'+url+'">'+album.album_title+'</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    html = "<h2>Details for Album id: "+str(album_id)+ "</h2>"
    return HttpResponse(html)