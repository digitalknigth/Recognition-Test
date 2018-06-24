import cv2

class VideoStream:

    def __init__(self,width,height):
        self.width = width;
        self.height = height;

    def VideoStreaming(self,source):
        video = cv2.VideoCapture(source)
        cv2.namedWindow("Stream started ...",cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("Stream started ...",500,100)
        cv2.startWindowThread
        try:
            while True:
                ret, frame = video.read()
                if ret:
                    resize = cv2.resize(frame,(1280,720))
                    videoColor = cv2.cvtColor(resize,cv2.COLOR_BGR2RGB)
                    gray = videoColor.copy()
                    gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
                    videoShow = cv2.resize(videoColor,(self.width,self.height))
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
