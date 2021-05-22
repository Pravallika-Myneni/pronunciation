from collections import Counter
from math import sqrt
import eng_to_ipa as ipa
import speech_recognition as sr

def word2vec(word):
    cw = Counter(word)
    sw = set(cw)
    lw = sqrt(sum(c*c for c in cw.values()))
    return cw, sw, lw

def cosdis(v1, v2):
    common = v1[1].intersection(v2[1])
    return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]

def speech_text(file_name):
    r = sr.Recognizer()
    with sr.AudioFile(file_name) as source:
        audio = r.listen(source)
    try:
        # print("Google Cloud Speech thinks you said " + r.recognize_google(audio))
        result = r.recognize_google(audio)
        return result
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
def pronunciation_analyzer(file_name = "Example.wav", word= "Example"):
    Word_in_Audio = speech_text(file_name)
    res = cosdis(word2vec(Word_in_Audio),word2vec(word))
    #print(res)
    return res
file_name = "Example.wav"
word ="welcome"
print(pronunciation_analyzer(file_name, word))
