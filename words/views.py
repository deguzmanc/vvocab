# from django import forms
# from django.http import HttpResponse, HttpResponseRedirect
# from django.forms import ValidationError
from django.shortcuts import render
from django.views.decorators.http import require_POST


from youtube_transcript_api import YouTubeTranscriptApi

# import form class from django
# from django import forms

# import Video from models.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, TranscriptForm, VideoForm


def index(request):
  context = {}
  context["form"] = VideoForm()
  return render(request, "index.html", context)


def user_signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = SignupForm()
  return render(request, 'signup.html', {'form': form})

# login page


def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user:
        login(request, user)
        return redirect('index')
  else:
    form = LoginForm()
  return render(request, 'login.html', {'form': form})

# logout page


def user_logout(request):
  logout(request)
  return redirect('login')


@require_POST
def submitlink(request):
  context = {}

  # create a form instance and populate it with data from the request:
  form = VideoForm(request.POST)
  # context['form'] = form

  # check whether it's valid:
  if form.is_valid():
    video = form.save(commit=False)
    video.setTitlefromUrl()
    context['video'] = video

    transcript_list = YouTubeTranscriptApi.list_transcripts(
        video.getVideoId())

    context['languages'] = transcript_list

    return render(request, "submit-results.html", context)

  # ValidationError
  context = {}
  context['error'] = form.errors
  return render(request, "error.html", context)


def gettranscript(request):

  transcript_form = TranscriptForm(request.POST)
  print(transcript_form)
  context = {'form': transcript_form}
  return render(request, "transcript.html", context)

# def video(request):
#    return render(request, "video-page.html")


def video(request, id=None):
  if id is None:
    return render(request, "video-page.html")
  context = {}
  context["id"] = id
  words_jp = YouTubeTranscriptApi.get_transcript(id, languages=['ja'])
  print(words_jp)

  context["words"] = words_jp
  return render(request, "video-page.html", context)
