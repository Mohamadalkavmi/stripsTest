from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
  title =models.CharField(max_length =5000)
  content =models.CharField(max_length =5000)
  createted_at = models.DateTimeField(default = timezone.now())
  image = models.ImageField(upload_to ='post-image/')

  class Meta:
    verbose_name =("Post")
    verbose_name_plural =("Posts")

  def __str__(self):
    return self.title

  def get_absoluter_url(self):
    return revers("Post_detail" ,kwart ={"pk":self.pk} )