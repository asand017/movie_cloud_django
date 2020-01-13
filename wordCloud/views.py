from django.shortcuts import render
from django.http import HttpResponse
from .functions import srt_to_txt
from .forms import UploadSrtForm
import pysrt
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Create your views here.

# will have just the index view for this project

def index(request):
	if request.method == 'POST':
		form = UploadSrtForm(request.POST, request.FILES)
		if form.is_valid():
			f = request.FILES['file']
			# need to verify file 'f' is a srt file
			
			srt_to_txt(f)
			return HttpResponse("Successful upload")
	else:
		form = UploadSrtForm()

	return render(request, 'wordCloud/index.html', {'form': form})


#def index(request):
#	return HttpResponse("Movie Cloud init page")
