from rest_framework.decorators import api_view
from rest_framework.response import Response
from .predictor import Cnn
from .serializers import MusicSerializer
from .models import Music
import os

@api_view(["GET"])
def trial(request):
    return Response("REally dude")
    
@api_view(["POST"])
def add_song(request):
    print("-----------------ADD SONG-----------------------")
    data = request.data
    print('-----------------------------------------------------------')
    new_song = Music.objects.create(
        song= data['song'],
        creation_date = data["creation_date"]                   
    )
    serializer = MusicSerializer()(new_song,many=False)
    return Response(serializer.data)

@api_view(["GET"])
def predict(request):
    songs = Music.objects.order_by('-creation_date')
    song_path = songs[0].song
    
    song_path = os.path.join('musics/',str(song_path))
    cnn = Cnn()
    music = cnn.make_prediction(songs)(song_path)
    # number = cnn.re_shape(image).reshape(784)
    print("ooooooooooooooooooooo")
    # predicted = cnn.predict_number(music)

    
    return Response(f'{music}')
















         


# from django.shortcuts import render
# from .models import Music
# from .serializers import MusicSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .forms import MusicForm

# from mutagen.mp3 import MPEGInfo
# import mutagen
# import librosa
# # Create your views here.

# """
# GETTING ALL THE MUSICS FOR HISTORY PAGE
# """
# @api_view(['GET'])
# def getMusics(request):
#     musics = Music.objects.all()
#     serializer = MusicSerializer(musics, many = True)
#     return Response(serializer.data)




# def index(request):
    
#     documents = Music.objects.all()
#     if request.method == 'POST':
#         if len(request.FILES) == 0:
#             messages.error(request,'Upload a file')
#             return redirect("predictor:index")

#         form = MusicForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploadfile = request.FILES['document']
#             print(uploadfile.name)
#             print(uploadfile.size)
#             if not uploadfile.name.endswith('.wav'):
#                 messages.error(request,'Only .wav file type is allowed')
#                 return redirect("predictor:index")
#             meta = getmetadata(uploadfile)
            
#             genre = predict_gen(meta)
#             print(genre)

#             context = {'genre':genre}
#             return render(request,'music/result.html',context)

#     else:
#         form = MusicForm()

#     return render(request,'music/result.html',{'documents':documents,'form':form})
#     # form = MusicForm()
#     # if request.method == 'POST':
       
#     #     form = MusicForm(request.POST,request.FILES)
        
#     #     if form.is_valid():
#     #         song = request.FILES['song']
#     #         # print(song)
#     #         audio_file_prop = mutagen.File(song, easy=True)
#     #         audio_file = MPEGInfo(song)

#     #         title = audio_file_prop.get('title')
#     #         artist = audio_file_prop.get('artist')
#     #         genre = audio_file_prop.get('genre')
#     #         size = audio_file.length
#     #         attrs =  [title[0], artist[0], genre[0], size]
#     #         m = Music(title = attrs[0], artist = attrs[1], length = attrs[3], genre = attrs[2], song=song)
#     #         m.save()
   
#     # context = {'form' : form}
#     # return render(request, 'music_api/form.html', context)





# from django.shortcuts import render
# # from django.contrib.auth.forms import UserCreationForm
# from .forms import UserForm, LoginForm
# from .models import User
# # Create your views here.
# def registerView(request):
#     form = UserForm()
#     if request.method == 'POST':
       
#         form = UserForm(request.POST or None)
        
#         if form.is_valid():
#             form.save()
            
#     context = {'form': form}
#     return render(request, 'music_api/register.html', context)

# def loginView(request):
    
#     l_form = LoginForm()
#     if request.method == 'POST':
#         uservalue = ""
#         l_form = LoginForm(request.POST or None)
#         if l_form.is_valid():
#             f_user = l_form.save(commit = False)
        
#             uservalue= l_form.cleaned_data.get("name")
#             # print(uservalue)
#             try:
#                 user= User.objects.get(name=uservalue)
#                 context= {'l_form': l_form, 'message': "You are welcome here"}
#                 # return render(request, 'user/login.html', context)
#             except User.DoesNotExist:
#                 print("No way")
            
#     context = {'l_form': l_form}
#     return render(request, 'music_api/login.html', context)