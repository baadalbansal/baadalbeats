
from django.core.checks import messages
from django.shortcuts import redirect, render
from baadalbeats.models import Song,Watchlater ,History , Channel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect
from django.db.models import Case, Value, When, query


def index(request):
    song = Song.objects.all()

    return render(request, 'index.html',{'song': song})

def songs(request):
    song = Song.objects.all()
    return render(request ,'baadalbeats/songs.html',{'song': song})

def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request ,'baadalbeats/songpost.html',{'song': song})

def login(request):
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username , password = password)
        from django.contrib.auth import  login
        login(request,user)
        redirect("/")

       

    return render(request ,'baadalbeats/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]


        myuser = User.objects.create_user(username,email,pass1)
        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.save()
        user = authenticate(username=username , password = pass1)
        from django.contrib.auth import  login
        login(request,user)

        channel = Channel(name =username)
        channel.save()
    
        return redirect('/')
    return render(request ,'baadalbeats/signup.html')

def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST["video_id"]
        watch = Watchlater.objects.filter(user = user  )
        for i in watch:
            if video_id == i.video_id:
                message = "your video is already added"
                break
        else: 

            watchlater = Watchlater(user = user , video_id = video_id)
            watchlater.save()
            message = " your video is successfully added"

        song=Song.objects.filter(song_id=video_id).first()  
        return render(request,f"baadalbeats/songpost.html" , {'song' : song , "message": message})

    wl = Watchlater.objects.filter(user =request.user)
    ids =[]
    for i in wl:
        ids.append(i.video_id)    

    preserved =Case(*[When(pk= pk , then= pos) for pos,pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in = ids).order_by(preserved)      
        
    
    return render(request,'baadalbeats/watchlater.html',{'song':song})    



def logout_user(request):

    logout(request)
    return redirect("/")

def history(request):
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']
        history = History(user=user, music_id=music_id)
        history.save()

        return redirect(f"/baadalbeats/songs/{music_id}")

    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in = ids).order_by(preserved) 

    return render(request, 'baadalbeats/history.html', {"history": song})


def channel(request, channel):
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(video_ids)])
    song = Song.objects.filter(song_id__in=video_ids).order_by(preserved)    

    return render(request, "baadalbeats/channel.html", {"channel": chan, "song": song})



def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        singer = request.POST['singer']
        tag = request.POST['tag']
        image = request.POST['image']
        album = request.POST['album']
        credit = request.POST['credit']
        song1 = request.FILES['file']

        song_model = Song(Name=name, singer=singer, tags=tag, image=image, album=album, credit=credit, song=song1)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))
        print(channel_find)

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()

    return render(request, "baadalbeats/upload.html")

def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs = song.filter(Name__icontains = query)
    return render(request, "baadalbeats/search.html" , {"songs": qs} , {"songs" :qs, "query" : query})


 


        

