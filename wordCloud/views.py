from django.shortcuts import render
from django.http import HttpResponse
from .functions import handle_uploaded_file
from .forms import UploadSrtForm


# Create your views here.

# will have just the index view for this project

def index(request):
	if request.method == 'POST':
		form = UploadSrtForm(request.POST, request.FILES)
		if form.is_valid():
			request.FILES['file']
			return HttpResponse("Successful upload")
	else:
		form = UploadSrtForm()

	return render(request, 'wordCloud/index.html', {'form': form})


#def index(request):
#	return HttpResponse("Movie Cloud init page")
