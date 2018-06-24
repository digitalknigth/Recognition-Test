import VideoStream
import sys

if __name__=="__main__":
    print("[INFO] Stream from video "+sys.argv[1])
    OUTPUT_SIZE_WIDTH = 680
    OUTPUT_SIZE_HEIGHT = 400
    stream = VideoStream.VideoStream(OUTPUT_SIZE_WIDTH,OUTPUT_SIZE_HEIGHT)
    stream.VideoStreaming(sys.argv[1])
    print("Bye Bye")