from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, verbose_name="артист")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.FileField(upload_to='images/', null=True, blank=True)
    ordering = ["updated_at"]
    artist_link = models.CharField(max_length=200, verbose_name="ссылка", blank=True, null=True)
    landing = models.BooleanField()
    @property
    def get_cover_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return self.cover_image.url
        else:
            return "/media/images/avatar.png"
        
    def __str__(self):
        return self.name
    
PROJECT_CHOICES = (
    ('demo','DEMO'),
    ('ongoing', 'ONGO'),
    ('done','DONE'),
)
class Project(models.Model):
    song = models.CharField(max_length=200, verbose_name="песни")
    artist = models.ForeignKey(Artist, related_name="projects", verbose_name="проекты", on_delete = models.PROTECT)
    price = models.IntegerField(verbose_name="стоимость")
    agreement = models.URLField(blank=True, null=True, verbose_name="договор")
    result = models.URLField(blank=True, null=True, verbose_name="результат")
    yandex = models.URLField(blank=True, null=True, verbose_name="ссылка на прослушивание")
    status = models.CharField(max_length=16, choices=PROJECT_CHOICES, default='demo', verbose_name="статус")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.song
    
    ordering = ["-updated_at"]
    
TRANSACTION_CHOICES = (
    ('pre','PRE'),
    ('post', 'POST'),
    ('other','OTHER'),
)

class Transaction(models.Model):
    artist = models.ForeignKey(Artist, related_name="transactions", verbose_name="артист", on_delete = models.PROTECT)
    song = models.ForeignKey(Project, related_name="transactions", verbose_name="песня", on_delete = models.PROTECT)
    type = models.CharField(max_length=6, choices=TRANSACTION_CHOICES, verbose_name="тип", default='pre')
    q = models.IntegerField(verbose_name="сумма")
    receipt = models.URLField(blank=True, null=True, verbose_name="чек")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.CharField (max_length=512, verbose_name="комментарий")
    
    ordering = ["-updated_at"]
    
    def __str__(self):
        return self.q
    
class Release(models.Model):
    release_cover = models.FileField(upload_to='images/', null=True, blank=True)
    song = models.ForeignKey(Project, related_name="projects", verbose_name="проекты", on_delete = models.PROTECT)
    landing = models.BooleanField()
    release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.song.song
    
    ordering = ["updated_at"]
    
    @property
    def get_cover_url(self):
        if self.release_cover and hasattr(self.release_cover, 'url'):
            return self.release_cover.url
        else:
            return "/media/images/avatar.png"