from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video
 
# create a ModelForm
class VideoForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(VideoForm, self).__init__(*args, **kwargs)
    self.fields['url'].label = ""

  # https://www.flaviabastos.ca/add-style-to-django-forms-with-tailwindcss/
  # https://stackoverflow.com/questions/25839043/how-do-i-remove-label-text-in-django-generated-form

  # specify the name of model to use
  class Meta:
    model = Video
    # fields = "__all__"
    exclude = ['title']
    widgets= {
      "url": forms.TextInput(
          attrs={
              "class": "input input-bordered input-primary w-full max-w-xs",
              "placeholder": "Paste youtube link...",
          }
      ),
    }

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class TranscriptForm(forms.Form):
   source_lang_code = forms.CharField()
   dest_lang_code = forms.CharField()