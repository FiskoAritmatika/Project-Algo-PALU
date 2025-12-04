from django.db import models
from urllib.parse import urlparse, parse_qs


# Create your models here.
class Event(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  date = models.DateTimeField()
  location = models.CharField(max_length=200, blank=True)
  image = models.ImageField(upload_to='events/', null=True, blank=True)

  def __str__(self):
    return self.title
    
  class Meta:
    ordering = ['-date']
  
class Materi(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  youtube_url = models.URLField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  def youtube_id(self):
    if not self.youtube_url:
        return None
    url_data = urlparse(self.youtube_url)
    if 'youtube.com' in url_data.netloc:
        if url_data.path.startswith('/embed/'):
            return url_data.path.split('/')[2]
        qs = parse_qs(url_data.query)
        return qs.get('v', [None])[0]
    if 'youtu.be' in url_data.netloc:
        return url_data.path[1:]
    return None

  class Meta:
    ordering = ['-created_at']