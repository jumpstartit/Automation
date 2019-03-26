import os
import shutil
cwd=os.getcwd()
print(cwd)
print(os.path.isdir('.'))
print(os.listdir(cwd))
for(dirname,dirs,files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.jpeg')|filename.endswith('.jpg')|filename.endswith('.png')|filename.endswith('.gif'):
			shutil.move(filename,"Pictures")
		elif filename.endswith('.mp3')|filename.endswith('.wav')|filename.endswith('.WAV'):
			shutil.move(filename,"music")
		elif filename.endswith('.mp4'):
			shutil.move(filename,"video")
		elif filename.endswith('.avi'):
			shutil.move(filename,'movies')
		elif filename.endswith('.pdf')|filename.endswith('.doc')|filename.endswith('.docx')|filename.endswith('.mp4'):
			shutil.move(filename,'documents')


