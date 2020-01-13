from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .functions import handle_uploaded_file
from .forms import UploadSrtForm


# Create your views here.

# will have just the index view for this project

#def handle_uploaded_file(f):
#	with open('./upload/temp.txt', 'wb+') as destination:
#		for chunk in f.chunks():
#			destination.write(chunk)


#def upload_file(request):
#	if request.method == 'POST':
#		form = UploadSrtForm(request.POST, request.FILES)
#		if form.is_valid():
#			handle_uploaded_file(request.FILES['file'])
#			return HttpResponseRedirect('/success/url/')
#	else:
#		form = UploadSrtForm()
#
#	return render(request, 'upload.html', {'form': form})


def index(request):
	return HttpResponse("Movie Cloud init page")
