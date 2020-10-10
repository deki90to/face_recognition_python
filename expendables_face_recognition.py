import face_recognition
import cv2


video = cv2.VideoCapture('video/expendables/expendables.mp4')

banderas_image = face_recognition.load_image_file('slike/expendables/Antionio Banderas.png')
banderas_image_encoding = face_recognition.face_encodings(banderas_image)[0]

arnold_image = face_recognition.load_image_file('slike/expendables/Arnold Schwarzenegger.png')
arnold_image_encoding = face_recognition.face_encodings(arnold_image)[0]

willis_image = face_recognition.load_image_file('slike/expendables/Bruce Willis.png')
willis_image_encoding = face_recognition.face_encodings(willis_image)[0]

dolph_image = face_recognition.load_image_file('slike/expendables/Dolph Lundgren.png')
dolph_image_encoding = face_recognition.face_encodings(dolph_image)[0]

jason_image = face_recognition.load_image_file('slike/expendables/Jason Statham.png')
jason_image_encoding = face_recognition.face_encodings(jason_image)[0]

jet_image = face_recognition.load_image_file('slike/expendables/Jet Li.png')
jet_image_encoding = face_recognition.face_encodings(jet_image)[0]

gibson_image = face_recognition.load_image_file('slike/expendables/Mel Gibson.png')
gibson_image_encoding = face_recognition.face_encodings(gibson_image)[0]

randy_image = face_recognition.load_image_file('slike/expendables/Randy Couture.png')
randy_image_encoding = face_recognition.face_encodings(randy_image)[0]

stallone_image = face_recognition.load_image_file('slike/expendables/Sylvester Stallone.png')
stallone_image_encoding = face_recognition.face_encodings(stallone_image)[0]

terry_image = face_recognition.load_image_file('slike/expendables/Terry Crews.png')
terry_image_encoding = face_recognition.face_encodings(terry_image)[0]

wesley_image = face_recognition.load_image_file('slike/expendables/Wesley Snipes.png')
wesley_image_encoding = face_recognition.face_encodings(wesley_image)[0]


known_face_encodings = [
	banderas_image_encoding,
	arnold_image_encoding,
	willis_image_encoding,
	dolph_image_encoding,
	jason_image_encoding,
	jet_image_encoding,
	gibson_image_encoding,
	randy_image_encoding,
	stallone_image_encoding,
	terry_image_encoding,
	wesley_image_encoding,
]

known_face_names = [
	'Antionio Banderas',
	'Arnold Schwarzenegger',
	'Bruce Willis',
	'Dolph Lundgren',
	'Jason Statham',
	'Jet Li',
	'Mel Gibson',
	'Randy Couture',
	'Sylvester Stallone',
	'Terry Crews',
	'Wesley Snipes',
]

while True:

	_, frame = video.read()
	rgb_frame = frame[:, :, ::-1]

	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


	for (top, right, bottom, left), face_encoding in zip (face_locations, face_encodings):
		matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

		if True in matches:
			first_match_index = matches.index(True)
			name = known_face_names[first_match_index]
		else:
			name = 'Unknown'


		# name = 'Unknown'
		# face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
  		#best_match_index = np.argmin(face_distances)
  		#if matches[best_match_index]:
			#name = known_face_names[best_match_index]


		cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 1)
		# cv2.rectangle(frame, (left, bottom + 15), (right, bottom), (255, 0, 0), cv2.FILLED)

		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, name, (left, bottom + 12), font, 0.5, (255, 255, 255), 1)


	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


video.release()
cv2.destroyAllWindows()