import openface
import cv2
import dlib
import os
import sys
from imutils import face_utils
import numpy as np
np.set_printoptions(precision=2,formatter={'float': '{: 0.3f}'.format})


def VideoStream(width,height,source):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    print(fileDir)
    #align = openface.align_dlib(os.path.join(fileDir,"shape_predictor_68_face_landmarks.dat"))
    #net = openface.TorchNeuralNet(os.path.join(fileDir,'nn4.small2.v1.t7'), 96)
    video = cv2.VideoCapture(source)
    print("[INFO] VIDEO STREAM START ..... ")
    cv2.namedWindow("Stream started ...",cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("Stream started ...",500,100)
    cv2.startWindowThread
    try:
        while True:
            ret,frame = video.read()
            if ret:
                resize = cv2.resize(frame,(1280,720))
                videoColor = cv2.cvtColor(resize,cv2.COLOR_BGR2RGB)
                gray = videoColor.copy()
                gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
                detector = dlib.get_frontal_face_detector()
                # faces = detector(gray,0)
                # for rect in faces:
                #     (_x,_y,_w,_h) = face_utils.rect_to_bb(rect)
                #     x = int(_x)
                #     y = int(_y)
                #     w = int(_w)
                #     h = int(_h)
                #     #print("[INFO] Have the points")
                #     roi = gray[y-100:y+(h+50),x-100:x+(w+50)]
                #     # we put a rectangle and text on faces we detect for recognition
                #     cv2.rectangle(videoColor, (x, y),(x + w , y + h),(0,0,255) ,2)
                #     cv2.putText(videoColor, "Analisi Volto",(int(x + w/2), int(y-10)),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2)
            videoShow = cv2.resize(videoColor,(width,height))
            videoShow = cv2.cvtColor(videoShow,cv2.COLOR_BGR2RGB)
            cv2.imshow("Face-dec Video",videoShow)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        cv2.destroyAllWindows()
        video.release()
        time.sleep(4)
    except:
        pass
    return 0    

if __name__ == "__main__":
    print("[INFO] Stream from video "+sys.argv[1])
    OUTPUT_SIZE_WIDTH = 680
    OUTPUT_SIZE_HEIGHT = 400
    VideoStream(OUTPUT_SIZE_WIDTH,OUTPUT_SIZE_HEIGHT,sys.argv[1])
    print("Bye Bye")