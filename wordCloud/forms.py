from django import forms

class UploadSrtForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()
	cloud_img = forms.ImageField()
