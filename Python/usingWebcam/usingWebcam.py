import cv2
import dropbox
import time    
import random

start_time = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    
    while (result):
        ret,frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite("newPicture1.jpg","frame")
        result = False

    return image_name
   
    print("Image is taken successfully.")            
    videoCaptureObject.release()
    cv2.destroyAllWindows()

    
def uploadFiles(image_name):
    access_token = 'sl.A4CehFS5MBTEaDGcGpjQqTpL4iYMkCM3JXAhxwrCql0I3LagxCs_kIuMqC4GwhsHY4n0Dw_YjaNBHKPhpTBb_aqh0KocZLTsCQ4j8dik0-cM5qQ07XYFlAg8NIPHzF1Vx-iB7W0'
    
    file = image_name
    file_from = file
    file_to ="/newFolder1/" + (image_name)
    
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)


    print ("File Successfully Uploaded.")

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = takeSnapshot()
            uploadFiles(name)

main()
