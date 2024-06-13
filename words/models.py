from django.db import models
from django.core.validators import RegexValidator

import re

from bs4 import BeautifulSoup 
import requests 
 
class Video(models.Model):
  YOUTUBE_REGEX = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'

  url = models.URLField(primary_key=True, validators=[
        RegexValidator(
            regex=YOUTUBE_REGEX,
            message="Enter a valid youtube URL.",
            code="invalid_registration",
        ),
      ],)
  title = models.CharField(max_length=200, blank=True)

  # FIXME list of words to timestamps

  def getVideoId(self):
      return (*re.findall(Video.YOUTUBE_REGEX, self.url), self.url)[0]
  
  def setTitlefromUrl(self):
    # getting the request from url 
    r = requests.get(self.url) 
      
    # converting the text 
    s = BeautifulSoup(r.text, "html.parser") 
    link = s.find_all(name="title")[0]
    self.title = link.text[:-len(" - YouTube")]
      

  def __str__(self):
      return self.title

# Create your models here.
class Word(models.Model):
    original_text = models.CharField(max_length=200, primary_key=True)
    romanized = models.CharField(max_length=200, blank=True)
    translation = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    level = models.IntegerField()
    # example = models.CharField(max_length=200)
    # example_translation = models.CharField(max_length=200)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    start_time = models.IntegerField()
    duration = models.IntegerField()
    end_time = models.IntegerField()


    def __str__(self):
        return self.word
    
class WordList(models.Model):
    name = models.CharField(max_length=200)
    words = models.ManyToManyField(Word)

    def __str__(self):
        return self.name