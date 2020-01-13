def handle_uploaded_file(f):
	with open('wordCloud/static/upload/temp.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
