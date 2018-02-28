import base64
import wave

f = open('mess.txt' , 'r')
data = f.read()
f.close()

f = open('test1.wav' , 'wb')
f.write(base64.decodestring(data))
f.close()

v = wave.open('test1.wav' , 'r')
frame = v.readframes(v.getnframes())

new = ""
even = ""
odd = ""

for i in range(0 , len(frame)):
    if i % 2 == 0:
        even = str(frame[i])
    elif i % 2 == 1:
        odd = str(frame[i])
        new += odd
        new += even


new_v = wave.open('test2.wav' , 'w')
new_v.setnchannels(1)
new_v.setframerate(v.getframerate())
new_v.setnframes(v.getnframes())
new_v.setsampwidth(v.getsampwidth())
new_v.writeframes(new)
new_v.close()