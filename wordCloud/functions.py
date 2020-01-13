def handle_uploaded_file(f):
	with open('wordCloud/static/wordCloud/upload/temp.srt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
