#!/usr/bin/python
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import String


import speech_recognition as sr
rospy.init_node('talker',anonymous=True)
global k

def recognize_speech_from_mic(recognizer, microphone):
    global k    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    print("Speak now!")
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    print("Transcribing..")
    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response
    


def main():
    global k
    # Print the SR Version and program data
    #pub = rospy.Publisher('/posision',String,queue_size=10)#speech recognition pub to text_to_text
    pub1 = rospy.Publisher('/key',String, queue_size = 10)#face detection
    print("Python Speech To Text via speech_recognition\n Speech Recognition Version:" + str(sr.__version__) )

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    #po = ['3.14 2.13++','5.846 3.647+-']

    while(True):
        k = 'hello Chetak'
        response = recognize_speech_from_mic(recognizer, microphone)
        print [ord(c) for c in ((str(response["transcription"])))]
        print('next')
        print [ord(l) for l in k]
	print(response["transcription"])
	pub1.publish(response["transcription"])
        #pub.publish(str(po[1]))

if __name__ == '__main__':
    main()

