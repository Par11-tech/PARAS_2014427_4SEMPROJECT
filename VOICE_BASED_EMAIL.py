import smtplib
import pyttsx3
import speech_recognition as sr
from win32com.client import Dispatch
from email.message import EmailMessage   # Firstly Install all these packages

listener = sr.Recognizer()   # lis
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()



def get_info() :      #funtion for geeting voice from user and then  converting it into the text
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        try:
            info = listener.recognize_google(voice)
            print(format(info))
            return info.lower()

        except:
            talk('did not hear properly')




def send_email(rceriver,subject,message): # function that is used to send automated email with the help of server
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('ps9800589@gmail.com','Paras@123')
    email = EmailMessage()
    email['from'] ='ps9800589@gmail.com'
    email['to'] =rceriver
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)



Name_list = {                     # dictonary that contain name as key and email addresses as value
    'paras':'ps713677@gmail.com',
    'sagar':'ps468257@gmail.com',
    'vasu':'surajsharma935991@gmail.com'
}



def get_email_info():    #funtion that will get all infomation for email sending like to whom,subject of email and content of email
    talk('hi to whom you want to send email')
    name = get_info()
    rceriver= Name_list[name]
    talk('what is the subject of your email')
    subject= get_info()
    talk('what is content of your email')
    message = get_info()
    send_email(rceriver,subject,message)
    talk('hey dude your message is sent')  #after the email is sent it will ask the user for further he want to send another email or not
    talk('do you want to send more emails for this say true and if not say false')
    send_more = get_info()
    if 'True' in send_more:
        get_email_info()




import easyimap as e  #function that will login to the given account and will read the latest email in the inbox and store that details in the varibles
password="Paras@123"
username="ps9800589@gmail.com"
server= e.connect("imap.gmail.com",username,password)
server.listids()
email=server.mail(server.listids()[0])
subject=email.title
sender = email.from_addr
content=email.body


def get_inbox(): #funtion that will speak out the variable create int above funtion
    temp="content of your last email is"
    temp1="your last email is sent by"
    temp2=" the content of your email is "
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(temp)
    speak.Speak(subject)
    speak.Speak(temp1)
    speak.Speak(sender)
    speak.Speak(content)
    speak.Speak(content)


def get_option(): #function that will provide option to the user whether  he want to send email to read an email
    speak = Dispatch(("SAPI.SpVoice"))
    temp1=" invalid option   "
    temp= " speak 1 for sending email and 2 for reading your last email"
    speak.Speak(temp)
    option= get_info()
    if option=="1":
        get_email_info()
    elif option=="2":
        get_inbox()
    else:
        speak.Speak(temp1)
        get_option()


get_option() #here we called our option funtion that will do the required task
