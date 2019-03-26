import os
import shutil
for(dirname,dirs,files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.jpeg')|filename.endswith('.jpg')|filename.endswith('.png')|filename.endswith('.gif'):
			if not os.path.exists("pictures"):
				os.makedirs("pictures")
			else:
				shutil.move(filename,"pictures")
		elif filename.endswith('.mp3')|filename.endswith('.wav')|filename.endswith('.WAV'):
			if not os.path.exists("music"):
				os.makedirs("music")
			else:
				shutil.move(filename,"music")
		elif filename.endswith('.mp4'):
			if not os.path.exists("video"):
				os.makedirs("video")
			else:
				shutil.move(filename,"video")
		elif filename.endswith('.avi'):
			if not os.path.exists("movies"):
				os.makedirs("movies")
			else:
				shutil.move(filename,'movies')
		elif filename.endswith('.pdf')|filename.endswith('.doc')|filename.endswith('.docx')|filename.endswith('.mp4'):
			if not os.path.exists("documents"):
				os.makedirs("documents")
			else:
				shutil.move(filename,'documents')


