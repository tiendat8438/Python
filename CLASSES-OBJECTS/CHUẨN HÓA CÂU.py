txt = ''
while True:
    try:
        txt += input()
        if txt[-1] not in '.?!': txt+=' .'
        else:
            if txt[-2] != ' ': txt = f'{txt[:-1]} {txt[-1]}'
        txt += ' '
    except:
        break
words = txt.split()
i = 0 
while i<len(words):
    sen = ''
    while i<len(words) and words[i] not in '.?!':
        sen+=words[i]+' '
        i+=1
    if words[i] in '.?!': sen = sen[:-1] + words[i]
    i+=1
    print(sen[0].upper() + sen[1:].lower())