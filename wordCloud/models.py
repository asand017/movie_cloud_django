from django.db import models
#from django.forms import ModelForm

# Create your models here
class CloudReq(models.Model):
	# word cloud request
	title = models.CharField(max_length=100)
	file = models.FileField('film subtitle.srt')#, upload_to='uploads/')
	#cloud_img = models.ImageField()

	def __str__(self):
		return self.film_title

#class CloudOut(models.Model):
	# word cloud output from input subtitle file
	#film = models.ForeignKey(CloudReq, on_delete=models.CASCADE)
	#cloud_img = models.ImageField()

	#def __str__(self):
		#return self.film

#class CloudForm(ModelForm):
	#class Meta:
		#model = CloudReq
		#fields = ['title', 'file', 'cloud_img']
