
#Project Domain: Voice Assistant
#Learner/Creater Name: Vyomesh Javle

#Aim
'''Create voice assistance to aid teachers to incorporate 
daily lecture record into excel file of type csv format.'''

#Importing neccessary Packages for Voice Assistant
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import time

#CSV_writer is used to write data in CSV file
from csv import writer

#Dicitionary to store key-value information recieved from User Speech
collect={}

#Creating Function listen to hear out user
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #Statement to let user know he/she needs to speak
        print("I am listening..")
        audio = r.listen(source,phrase_time_limit = 5)
    #variable to store speech by user
    data="" 
    try:
        data = r.recognize_google(audio,language='en-US')
        #print data entered from the speech
        print("Data Entered was:"+data) 
    except sr.UnknownValueError:
        print("Unable to Hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data

#Function to convert text to speech
def respond(String):
    print(String)
    tts = gTTS(text=String,lang="en")
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")

#Function to enter + append the speeched 
#Data into Excel file(CSV format)
def add_to_csv(d,e):
#d= list  in which schedule is present
#e=file in which it has to store
    with open(e, 'a', newline='') as lecture_data:
        csv_collect=writer(lecture_data)
        csv_collect.writerow(d)

def voice_assistant(data): 
    if "new" in data:        
        listening = True
        respond("Sure!")
    if "today" in data:
        listening=True
        respond("Enter the date:")
        a = listen()
        collect['Date']=a    
    if "time" in data:
        listening=True
        respond("Enter the time:")
        Hour = listen()
        collect['Time']= Hour
    if "class" in data:
        listening=True
        respond("Enter the Class:")
        Class = listen()  
        collect['Class']= Class
    if "topic" in data:
        listening=True
        respond("Enter the Topic Taught: ")
        Topic= listen()
        collect['Topic']= Topic
    if "ok" in data:
        listening=True
        #Processing of data into csv format
        print("Processing.....")
        respond("Done!")
        #Print the data in dicitionary format
        print(collect) 
        #Gets only the value for each key in dicitionary
        a_list=[collect.get('Date'),collect.get('Time'),collect.get('Class'),collect.get('Topic')] 
        #Add and appends the data to csv file
        add_to_csv(a_list,'M_Sc_Bio.csv')
        
    #When prompted stop Voice assitant will     
    if "stop" in data:
        listening = False
        print("Listening Stopped")
        respond("Sayonara, See You Next Time!")

    try:
        return listening
    except UnboundLocalError:
        print("Timed out")
        
    
time.sleep(2)
print("Voice Assistant at your service,")
respond("What can I do for you?")
listening = True
while listening == True:
    #Every time listen is activated, speech would be stored in variable 'data'
    data = listen()
    listening = voice_assistant(data)
    
   

    
    
