from autocorrect import Speller

spell = Speller(lang='en')

msg = "autocorrect can hepl you corretc the wrong wodr!"

if msg != spell(msg):
    for a, b in zip(msg.split(), spell(msg).split()):
        if a != b:
            print(a, b)
