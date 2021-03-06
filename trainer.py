import cv2
import os
faceCascade=cv2.CascadeClassifier('"haarcascade_frontalface_alt.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainingData.yml")
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR,"images")
current_id=0 
label_ids={}
y_label=[]
x_train=[]
for root,dirs, files in os.walk(image_dir):
        for file in files:
                    if files.endswith("png") or file.endswith("jpg"):
                                        path=os.path.join(root, file)
                    label=os.path.basename(root).replace(" ", "-").lower()
                    print(label, path)
if not label in label_ids:
        label_ids[label] = current_id
        current_id += 1
        id_ = label_ids[label]
        pil_image = Image.open(path) .convert("L")
        size = (550, 550)
        final_image = pil_image.resize(size, Image.ANTILIAS)
        image_array = np.array(final_image, "uint8")
        faces = faceCascade.detectMultiScale(image_array,scaleFactor=1.3,minNeighbors=5)
for(x,y,w,h) in faces:
                                roi = image_array[y:y+h, x:x+w]
                                x_train.append(roi)
                                y_label.append(id_)
with open ("pickles/faces-labels.pickle", 'wb') as f:
        pickle.dump(label_ids, f)
        recognizer.train(x_train, np.array(y_label))
        recognizee.save("ecognizer/trainingData.yml")
