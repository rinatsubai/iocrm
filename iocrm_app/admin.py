from django.contrib import admin
from .models import *

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'artist_link', 'landing')
    pass

admin.site.register(Artist, ArtistAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('song', 'artist', 'price', 'status', 'agreement', 'result', 'yandex', 'created_at', 'updated_at')
    pass

admin.site.register(Project, ProjectAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('q', 'type', 'artist', 'song', 'comment', 'receipt', 'created_at', 'updated_at')
    pass

admin.site.register(Transaction, TransactionAdmin)

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('song', 'release_date', 'landing',)
    pass

admin.site.register(Release, ReleaseAdmin)