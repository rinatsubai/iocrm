from django import forms

from .models import *

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name', 'cover_image', 'artist_link', 'landing')
        
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('song', 'artist', 'price', 'agreement', 'result', 'yandex', 'status')
        
class TransactionForm(forms.ModelForm):
    
    class Meta:
        model = Transaction
        fields = ('artist', 'song', 'type', 'q', 'receipt', 'comment',)