import pysrt
import os
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

stops = []
stopwords = open("./wordCloud/static/wordCloud/stopwords.txt")
for sw in stopwords:
	stops.append(sw.replace("\n", ""))
stopwords.close()

def srt_to_txt(f):

	# call a function to convert django internal file to srt compatible file
	convert_to_srt(f)
	pth = "./wordCloud/static/wordCloud/uploads/subs.srt"

	subt = pysrt.open(pth)	
	lineCount = len(subt)
	subout = open("./wordCloud/static/wordCloud/uploads/out.txt", "w+")
	
	for i in range(0, lineCount):
		line = subt[i].text
		newLine = cleanLine(line)
		newLine = removeStop(newLine)
		subout.write(newLine)
		subout.write('\n')

	subout.close()
	generate_word_cloud()

def black_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
	return "hsl(0, 0%, 0%)"

def cleanLine(line): # remove stop words
	newline = line.replace("<i>", "")
	newline = newline.replace("</i>", "")
	newline = newline.replace("\'s", "")
	newline = newline.replace(",", "")
	newline = newline.replace(".", "")
	newline = newline.replace("-", " ")
	newline = newline.replace("?", "")
	newline = newline.replace("!", "")
	newline = newline.replace("$", "")
	newline = newline.replace(":", "")
	newline = newline.replace("\"", "")
	return newline

def removeStop(line):
	words = line.split()
	space = " "
	newline = []
	for word in words: # check against stop list
		if(word.isdigit()):
			continue;
		
		word = word.lower()
		if(word not in stops):
			newline.append(word)
			#if(word in movieWords):
			#	movieWords[word] = movieWords[word] + 1
			#else:
			#	movieWords[word] = 1

	newline = space.join(newline)
	return newline

# create wordcloud gen function
def generate_word_cloud():
	dataset = open("./wordCloud/static/wordCloud/uploads/out.txt").read()
	wordcloud = WordCloud(background_color = "white",
							max_words = 25,
							width = 1200,
							height = 1000,
							color_func = black_color_func,
							collocations=False).generate(dataset)

	#plt.imshow(wordcloud.recolor(color_func=black_color_func, random_state=3), interpolation="bilinear")
	#plt.axis('off')
	#plt.show()
	#wordcloud.to_file("./wordCloud/static/wordCloud/images/output.png")
	wordcloud.to_file("./media/wordCloud/images/output.png")

def convert_to_srt(f):
	with open("./wordCloud/static/wordCloud/uploads/subs.srt", "wb+") as output:
		for chunk in f.chunks():
			output.write(chunk)
	
