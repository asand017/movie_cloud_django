from django.db import models

# Create your models here
class CloudReq(models.Model):
	# word cloud request
	film_title = models.CharField(max_length=100)
	subs_file = models.FileField('film subtitle.srt')

class CloudOut(models.Model):
	# word cloud output from input subtitle file
	film = models.ForeignKey(CloudReq, on_delete=models.CASCADE)
	cloud_img = models.ImageField()
