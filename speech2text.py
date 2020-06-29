import speech_recognition as sr

r = sr.Recognizer()
count = 0
words = ['kill', 'rob', 'hands up']
print('Analyzing and processing Audio input based on NLP')
print('Listening.....')
while True:

    with sr.Microphone() as source:
       
        audio = r.listen(source)
        

    try:
        text = r.recognize_google(audio)
        #print('you said:\n' + text)
        if text.find('kill')>-1 or text.find('down')>-1 or text.find('fast')>-1 or text.find('all the money')>-1 or text.find('hands')>-1:
        	count=count+1
        	print(count)
        	if(count==2):
        		break


    except Exception as e:
        print('Not recognized')


print("There might be potential danger")
