import pyautogui   #It let's to control the mouse and keyboard to automate interactions with other applications e.g. to pause and play the music or video
import pyttsx3     #Use for text-to-speech conversion. e.g. Here we use it that Dyla can ask the user
import speech_recognition as speechRecognition   #Use to convert users voice into text e.g. User said open chrome so to we should get text
import datetime    #Use to get the current date and time
import webbrowser  #Use to display web-based documents to users e.g. open an url, openeing a youtube
import os       #Use to interact with the system e.g. creating a textfile opening a program or a file
import pywhatkit as pyWhatKit #Use to automate Emails, play Youtube videos, send Whatsapp messages with
                                # just one command.

engine = pyttsx3.init('sapi5') #Intialize the engine for text-to-speech.
voices = engine.getProperty('voices') #Get all the voice pack in a list
engine.setProperty('voice', voices[1].id) #Set the voice of the engine. 0 index in list voices for male and 1 for female.
engine.setProperty("rate",178) #Set the rate of speaking i.e. speaks slow or fast

def speak(audio):
    '''
    This function use to get an audio stream of a given string. i.e. Dyla will
    speak when a string we pass to this function.
    :param audio:  A string
    :return: Audio stream of given String
    '''
    engine.say(audio) #This function takes a text and speak that text
    engine.runAndWait() #This function will make the speech audible in the system

def wishMe():
    '''
    This function is used to wish the user. That according to the time
    Dyla will wish the user by saying good Morning, good afternoon and good evening!
    And Also Dyla will introduce herself and say how may I help you
    :return:
    '''
    hour = int(datetime.datetime.now().hour) #Extract the hours from current time
    if hour>=0 and hour<12:         #If hour between 0 and 12 then Dyla wish by saying Good morning!
        speak("Good Morning!")      #Dyla will speak good Morning
    elif hour>=12 and hour<18:      #If hour between 12 and 18 then Dyla wish by saying Good Afternoon!
        speak("Good Afternoon!")    #Dyla will speak good Afternoon
    else:                           #If hours between 19 and 24
        speak("Good Evening!")      #Dyla will speak good Evening!
    speak("I am Dyla. Please tell me how may I help you") #Dyla will interdouce herself and speak how may Dyla help you

def takeCommand():
    '''
    This function get a command from microphone and convert it into string i.e. take input as an audio
    and convert that input into a text and return that text
    :return: This function returns a text
    '''
    recognizer = speechRecognition.Recognizer()  # Recognizer is a class that will use to recognize the audio
    with speechRecognition.Microphone() as source: #Use the default microphone as the audio source
        print("Listening...")                #Print listening that Dyla in listening State
        recognizer.pause_threshold = 0.8     #Seconds of non-speaking audio before a phrase is considered complete
        audio = recognizer.listen(source)    #Listen for the first phrase and extract it into audio data

    try:
        print("Recognizing...")            #Print that Dyla try to recognize the speech
        query = recognizer.recognize_google(audio, language='en-pk') #Recognize speech using Google Speech Recognitio and the language of recognition is Pakistan
        print("User said: ", query)        #Print what user has given a command to Dyla i.e. spoke

    except Exception as e:                 #if voice does not recognize so don't terminate by printing an error
        print("Say that again please...")  #Print that say it again please in case of Dyla not able to recognize the speech
        return "None"                      #Return string none in case of not recognizing
    return query                           #Return string what user has said in voice

def weatherForecast():
    '''
    This function allow user to get the weather forecast of loction that user command
    :return: Open a page with full weather forecast of the given location
    '''
    speak("Please Sir, tell me the Location??") #Ask the location for weather forecast
    city = takeCommand() #Store Location in city
    webbrowser.open("https://www.msn.com/en-xl/weather/forecast/in-"+city) #Open the the given URl
    speak("Weather page is Successfully opend you can see Sir!") #Tell user that weather page is successfully opened

def videoAndMusicOperations(query):
    '''
    This function use to control the video by a voice i.e to mute,pause
    Also this function allow to user volume down and up
    :param query:  Take a command from user through microphone
    :return:  Apply function appropriate to the user command that reconized
    '''
    if 'pause' in query:
        pyautogui.press("space") #Automate the keyboard. Use here to press 'space' key to pause
        speak("Paused")  #Tell user that video or music is paused

    elif "play" in query:
        pyautogui.press("space") #Automate the keyboard. Use here to press 'space' key to play
        speak("Played") #Tell user that video or music is played
    elif "mute" in query:
        pyautogui.press("m") #Automate the keyboard. Use here to press 'm' key to mute
        speak("Muted")#Tell user that video or music is muted
    elif "un mute" in query:
        pyautogui.press("m") #Automate the keyboard. Use here to press 'm' key to mute
        speak("Un Muted")#Tell user that video or music is unmuted
    elif "volume up" in query:
        i = 1
        if '2' in query: #if user command to up volume by 2 or press volume up button 2 times
            while i <= 2: #Use iteration to press volume up button 2 times
                pyautogui.press("volumeup") #Automate the keyboard. Use here to press 'volume up' key to volume up
                i+=1
        elif '5' in query:#if user command to up volume by 5 or press volume up button 5 times
            while i <= 5:#Use iteration to press volume up button 2 times
                pyautogui.press("volumeup") #Automate the keyboard. Use here to press 'volume up' key to volume up
                i+=1
        speak("Turned volume up")               #Tell user that volume is up
    elif "volume down" in query:
        i = 1
        if '2' in query:                        #if user command to down volume by 2 or press volume down button 2 times
            while i <= 1:                       #Use iteration to press volume down button 2 times
                pyautogui.press("volumedown")   #Automate the keyboard. Use here to press 'volume down' key to volume down
                i+=1
        elif '5' in query:                      #if user command to down volume by 5 or press volume down button 5 times
            while i <= 5:                       #Use iteration to press volume down button 5 times
                pyautogui.press("volumedown")   #Automate the keyboard. Use here to press 'volume down' key to volume down
                i+=1
        speak("Turned volume down,sir")         #Tell user that volume is down
if __name__ == "__main__":
    '''
    This is the main function in which all functions are invoked in order to perform the functionality
    '''
    wishMe()                                    #First wish the user
    try:
        while True:
            query = takeCommand().lower()           #Take command from user through microphone
            if 'play music' in query:                         #if User want to play music
                music_dir = 'C:\\Users\\Cyber World\\Music'     #Store path of music directory
                songs = os.listdir(music_dir)                   #Store all the songs  of music directory in songs
                print(songs)                                    #Print all songs that are stored in  music directory
                os.startfile(os.path.join(music_dir, songs[0])) #startfile() method use to open,play e.g. Play the first song of music directory
            elif 'open youtube' in query:                       #if User want to open youtube
                webbrowser.open("youtube.com")                  #open the link youtube.com
                query = 'none'
                while query == 'none':
                    speak("Are  you  want  to  search  and  play  a  video  or  a  playlist  on youtube??") #Ask user to play video or playlist from youtube
                    query = takeCommand().lower()                   #Store user's command in query
                if query == 'yes':                              #if user command yes
                    speak("What you want to play???")           #Ask user the title of video/playlist name
                    query = takeCommand()                       #Store user's command
                    pyWhatKit.playonyt(query)                   #Play youtube video with most matching user's command
            elif 'play' in query or 'pause' in query or 'mute' in query or 'un mute' in query or 'volume' in query: #if user want to pause,play,mute volume up and down
                videoAndMusicOperations(query)                  #Then invoke videoAndMusicOperations(query) to apply operation
            elif 'weather' in query:                #If query contain something about weather
                weatherForecast()                   #invoke weatherForecast()  function to forecast weather of any location
            elif 'sleep' in query:
                speak("Okay Gonna sleep now")
                print("Okay gonna sleep now")
                break
    except Exception(e):
        speak("Okay Sir")
