# Python program to translate
# speech to text and text to speech

from openai import OpenAI
import speech_recognition as sr
import pyttsx3
from subprocess import call
# Initialize the recognizer 
r = sr.Recognizer() 
client = OpenAI(
	api_key= "sk-proj-zJKN9xjvznwTYetwOoXiT3BlbkFJJgkflT3ZuEoLRWMEOiU0"
)
# Function to convert text to speech
def SpeakText(command, r):
	# Initialize the engine
	engine = pyttsx3.init()
	engine.setProperty("volume", 1.0)
	engine.setProperty("rate", r)
	engine.say(command) 
	engine.runAndWait()
	
#Function to convert the question into an answer
def getAnswer(question):
	answer = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[{
			"role":"user", "content":question
		}]
	)
	return answer.choices[0].message.content.strip()

# Loop infinitely for user to speak
try:
	# use the microphone as source for input.
	with sr.Microphone() as source2:
		
		# wait for a second to let the recognizer
		# adjust the energy threshold based on
		# the surrounding noise level 
		r.pause_threshold = 1
		r.dynamic_energy_threshold= True
		r.adjust_for_ambient_noise(source2, duration=1)
		SpeakText("Hey, How can I help you today?", 200)
		#listens for the user's input 
		audio2 = r.listen(source2)
		SpeakText("Processing", 200)
		# Using google to recognize audio
		MyText = r.recognize_google(audio2)
		MyText = MyText.lower()
		print("Did you say:",MyText)
		#Getting answer from chatgpt API
		answer = MyText
		answer = getAnswer(MyText)
		print("Answer: ", answer)
		SpeakText(answer, 200)

except sr.RequestError as e:
	print("Could not request results; {0}".format(e))
	
except sr.UnknownValueError as e:
	print("Did not understand")
	SpeakText("I did not understand. Please Repeat", 200)
