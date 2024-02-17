from django import forms
from .models import music,mark

class mymusic(forms.ModelForm):
      class Meta:
            model=music
            fields='__all__'


class mymark(forms.ModelForm):
      class Meta:
            model=mark
            fields='__all__'