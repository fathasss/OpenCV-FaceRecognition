#%%
#Library import
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt 

#%%
#Photo import
img1 = "my_db/Android-3.jpg"
img2 = "my_db/img-glass.jpg"

#OpenCV FaceCassade
faceCascade = cv2.CascadeClassifier(
    r"classifier/haarcascade_frontalface_default.xml")

#FaceRecognition Function
def function(path1,path2):
    var1_cv=cv2.imread(path1)
    var2_cv=cv2.imread(path2)

    gray1=cv2.cvtColor(var1_cv,cv2.COLOR_BGR2RGB)
    gray2=cv2.cvtColor(var2_cv,cv2.COLOR_BGR2RGB)

    faces1 = faceCascade.detectMultiScale(gray1, 1.1,4)
    faces2 = faceCascade.detectMultiScale(gray2, 1.1,4)

    for (x,y,w,h) in faces1:
        cv2.rectangle(var1_cv,(x,y),(x+w, y+h),(0,255,0),3)

    for (x,y,w,h) in faces2:
        cv2.rectangle(var2_cv,(x,y),(x+w, y+h),(0,255,0),3)

    plt.imshow(var1_cv[:,:,::-1])
    plt.show()
    plt.imshow(var2_cv[:,:,::-1])
    plt.show()
    dface = DeepFace.verify(path1,path2)

    if dface["verified"] == True:
        print("\nAynı kişiler :)")   
    if dface["verified"] == False:
        print("\nFarklı kişiler :(")

#Application Output
function(img1,img2)

# %%
