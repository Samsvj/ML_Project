#!/usr/bin/python3
import cv2

def findmouth(img):

	# INITIALIZE: loading the classifiers
	haarFace  = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	haarMouth = cv2.CascadeClassifier('haarcascade_mouth.xml')
	
	# running the classifiers 
	detectedFace  = haarFace.detectMultiScale(img, 1.3, 5)
	detectedMouth = haarMouth.detectMultiScale(img, 1.3, 5)

	#find the largest detected face as detected face
	maxFaceSize = 0
	maxFace = 0
	
	#storing detected face with maximum area in a variable called maxFace
	if (detectedFace).all(): 
		for x,y,h,w in detectedFace: 
			if h*w > detectedFace.all():
				maxFaceSize = (w*h)
				maxFace= img[(x,y),(x+w,y+h)]
				
		# if face not detected 
		if maxFace.any() == 0: 
			return 2

	# FILTER MOUTH
	# empty list to store mouth img in.
	filteredMouth = []
	
	#storing detected images of mouth in a list named filteredMouth
	if (detectedMouth).all():
		if True:
			k=len(detectedMouth)
			for i in range(k):
				filteredMouth.append(detectedMouth[i])
			
	maxMouthSize = 0
	# visualising filtered mouth as a 2-D array and checking and storing the image area of mouth detected by the harr file 
	for i in range(len(filteredMouth)):
		for j in range(4):
			if filteredMouth[i][2]*filteredMouth[i][3] > maxMouthSize:
	  			maxMouthSize = filteredMouth[i][2]*filteredMouth[i][3]
	  			
	try:
		return filteredMouth
	except UnboundLocalError:
		return 2