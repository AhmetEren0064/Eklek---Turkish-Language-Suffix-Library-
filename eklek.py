unluler = ["a","e","ı","i","o","ö","u","ü"]
unlulerBuyukVeKucuk = ["a","e","ı","i","o","ö","u","ü","A","E","I","İ","O","Ö","U","Ü"]
kalinUnluler = ["a","ı","o","u"]
inceUnluler = ["e","i","ö","ü"]
unsuzler = ["b","c","ç","d","f","g","ğ","h","j","k","l","m","n","p","r","s","ş","t","v","y","z"]
sertUnsuzler = ["f","s","t","k","ç","ş","h","p"]

#    Plural

def plural(word):
    
    if word[-1] in "aıou" or word[-2] in "aıou":
        if word[-1] in "eiöü":
            word += "ler"
        else:
            word += "lar"
        
    elif  word[-1] in "eiöü" or word[-2] in "eiöü":
        word += "ler"
    else:
        if word[-3] in "aıou":
            word += "lar"
        else:
            word += "ler"
    
    return word



#    Question

def question(word):
    if word[-1] in "aı" or  word[-2] in "aı":
        word += " mı"
    elif word[-1] in "ou" or  word[-2] in "ou":
        word += " mu"
    elif word[-1] in "ei" or  word[-2] in "ei":
        word += " mi"
    elif word[-1] in "öü" or  word[-2] in "öü":
        word += " mü"
    else:
        if word[-3] in "aı":
            word += " mı"
        elif word[-3] in "ou":
            word += " mu"
        elif word[-3] in "ei":
            word += " mi"
        elif word[-3] in "öü":
            word += " mü"
    return word

#?-----------------------------------------------------------------------

#    Me

meYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

meDogru = [
    "ağzım",
    "alnım",
    "bağrım",
    "benzim",
    "beynim",
    "boynum",
    "böğrüm",
    "burnum",
    "genzim",
    "göğsüm",
    "gönlüm",
    "karnım",
    "oğlum",
]

def me(word):
    
    isDogru_word_sahis1 = False
    
    for i in range(len(meYanlis)):
        if word.lower() == meYanlis[i]:
            word = meDogru[i]
            isDogru_word_sahis1 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_sahis1:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
    
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
        
        if word[-1] in "aıou":
            if word[-1] in "aı":
                word += "yım"
            elif word[-1] in "ou":
                word += "yum"
        elif word[-1] in "eiöü":
            if word[-1] in "ei":
                word += "yim"
            elif word[-1] in "öü":
                word += "yüm"
        elif word[-2] in "aıou":
            if word[-2] in "aı":
                word += "ım"
            elif word[-2] in "ou":
                word += "um"
        elif word[-2] in "eiöü":
            if word[-2] in "ei":
                 word += "im"
            elif word[-2] in "öü":
                word += "üm"
        else:
            if word[-3] in "aı":
                word += "ım"
            elif word[-3] in "ie":
                word += "im"
            elif word[-3] in "ou":
                word += "um"
            elif word[-3] in "öü":
                word += "üm"
        
    return word

#?-----------------------------------------------------------------------

#    speMe

spemeYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

spemeDogru = [
    "ağzım",
    "alnım",
    "bağrım",
    "benzim",
    "beynim",
    "boynum",
    "böğrüm",
    "burnum",
    "genzim",
    "göğsüm",
    "gönlüm",
    "karnım",
    "oğlum",
]

def speme(word):
    
    isDogru_word_sahis3 = False
    
    for i in range(len(spemeYanlis)):
        if word.lower() == spemeYanlis[i]:
            word = spemeDogru[i]
            isDogru_word_sahis3 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
        
    word = word.capitalize()
    
    if not isDogru_word_sahis3:
        
        word += "'"
        
        if word[-2] in "aıou":
            if word[-2] in "aı":
                word += "yım"
            elif word[-2] in "ou":
                word += "yum"
        elif word[-2] in "eiöü":
            if word[-2] in "ei":
                word += "yim"
            elif word[-2] in "öü":
                word += "yüm"
        elif word[-3] in "aıou":
            if word[-3] in "aı":
                word += "ım"
            elif word[-3] in "ou":
                word += "um"
        elif word[-3] in "eiöü":
            if word[-3] in "ei":
                 word += "im"
            elif word[-3] in "öü":
                word += "üm"
        else:
            if word[-4] in "aı":
                word += "ım"
            elif word[-4] in "ie":
                word += "im"
            elif word[-4] in "ou":
                word += "um"
            elif word[-4] in "öü":
                word += "üm"
        
    return word

#?-----------------------------------------------------------------------

#    You

def you(word):

    if word[-1] in "aıou":
        if word[-1] in "aı":
            word += "sın"
        elif word[-1] in "ou":
            word += "sun"
    elif word[-1] in "eiöü":
        if word[-1] in "ei":
            word += "sin"
        elif word[-1] in "öü":
            word += "sün"
    elif word[-2] in "aıou":
        if word[-2] in "aı":
            word += "sın"
        elif word[-2] in "ou":
            word += "sun"
    elif word[-2] in "eiöü":
        if word[-2] in "ei":
            word += "sin"
        elif word[-2] in "öü":
            word += "sün"
    else:
        if word[-3] in "aı":
            word += "sın"
        elif word[-3] in "ie":
            word += "sin"
        elif word[-3] in "ou":
            word += "sun"
        elif word[-3] in "öü":
            word += "sün"
        
    return word
#?-----------------------------------------------------------------------

#    speYou

def speyou(word):
    
    word = word.capitalize()
    word += "'"

    if word[-2] in "aıou":
        if word[-2] in "aı":
            word += "sın"
        elif word[-2] in "ou":
            word += "sun"
    elif word[-2] in "eiöü":
        if word[-2] in "ei":
            word += "sin"
        elif word[-2] in "öü":
            word += "sün"
    elif word[-3] in "aıou":
        if word[-3] in "aı":
            word += "sın"
        elif word[-3] in "ou":
            word += "sun"
    elif word[-3] in "eiöü":
        if word[-3] in "ei":
            word += "sin"
        elif word[-3] in "öü":
            word += "sün"
    else:
        if word[-4] in "aı":
            word += "sın"
        elif word[-4] in "ie":
            word += "sin"
        elif word[-4] in "ou":
            word += "sun"
        elif word[-4] in "öü":
            word += "sün"
        
    return word

#?-----------------------------------------------------------------------

#    YouPlural

def youplural(word):

    if word[-1] in "aıou":
        if word[-1] in "aı":
            word += "sınız"
        elif word[-1] in "ou":
            word += "sunuz"
    elif word[-1] in "eiöü":
        if word[-1] in "ei":
            word += "siniz"
        elif word[-1] in "öü":
            word += "sünüz"
    elif word[-2] in "aıou":
        if word[-2] in "aı":
            word += "sınız"
        elif word[-2] in "ou":
            word += "sunuz"
    elif word[-2] in "eiöü":
        if word[-2] in "ei":
            word += "siniz"
        elif word[-2] in "öü":
            word += "sünüz"
    else:
        if word[-3] in "aı":
            word += "sınız"
        elif word[-3] in "ie":
            word += "siniz"
        elif word[-3] in "ou":
            word += "sunuz"
        elif word[-3] in "öü":
            word += "sünüz"
        
    return word

#?-----------------------------------------------------------------------

#    speYouPlural

def speyouplural(word):
    
    word = word.capitalize()
    word += "'"

    if word[-2] in "aıou":
        if word[-2] in "aı":
            word += "sınız"
        elif word[-2] in "ou":
            word += "sunuz"
    elif word[-2] in "eiöü":
        if word[-2] in "ei":
            word += "siniz"
        elif word[-2] in "öü":
            word += "sünüz"
    elif word[-3] in "aıou":
        if word[-3] in "aı":
            word += "sınız"
        elif word[-3] in "ou":
            word += "sunuz"
    elif word[-3] in "eiöü":
        if word[-3] in "ei":
            word += "siniz"
        elif word[-3] in "öü":
            word += "sünüz"
    else:
        if word[-4] in "aı":
            word += "sınız"
        elif word[-4] in "ie":
            word += "siniz"
        elif word[-4] in "ou":
            word += "sunuz"
        elif word[-4] in "öü":
            word += "sünüz"
        
    return word
#?-----------------------------------------------------------------------

#    We

weYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

weDogru = [
    "ağzız",
    "alnız",
    "bağrız",
    "benziz",
    "beyniz",
    "boynuz",
    "böğrüz",
    "burnuz",
    "genziz",
    "göğsüz",
    "gönlüz",
    "karnız",
    "oğluz",
]

def we(word):
    
    isDogru_word_sahis2 = False
    
    for i in range(len(weYanlis)):
        if word.lower() == weYanlis[i]:
            word = weDogru[i]
            isDogru_word_sahis2 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_sahis2:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
    
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
        
        if word[-1] in "aıou":
            if word[-1] in "aı":
                word += "yız"
            elif word[-1] in "ou":
                word += "yuz"
        elif word[-1] in "eiöü":
            if word[-1] in "ei":
                word += "yiz"
            elif word[-1] in "öü":
                word += "yüz"
        elif word[-2] in "aıou":
            if word[-2] in "aı":
                word += "ız"
            elif word[-2] in "ou":
                word += "uz"
        elif word[-2] in "eiöü":
            if word[-2] in "ei":
                 word += "iz"
            elif word[-2] in "öü":
                word += "üz"
        else:
            if word[-3] in "aı":
                word += "ız"
            elif word[-3] in "ie":
                word += "iz"
            elif word[-3] in "ou":
                word += "uz"
            elif word[-3] in "öü":
                word += "üz"
        
    return word

#?-----------------------------------------------------------------------

#    speWe

speweYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

speweDogru = [
    "ağzız",
    "alnız",
    "bağrız",
    "benziz",
    "beyniz",
    "boynuz",
    "böğrüz",
    "burnuz",
    "genziz",
    "göğsüz",
    "gönlüz",
    "karnız",
    "oğluz",
]

def spewe(word):
    
    isDogru_word_sahis4 = False
    
    for i in range(len(speweYanlis)):
        if word.lower() == speweYanlis[i]:
            word = speweDogru[i]
            isDogru_word_sahis4 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
    
    word = word.capitalize()
            
    if not isDogru_word_sahis4:
        
        word += "'"
        
        if word[-2] in "aıou":
            if word[-2] in "aı":
                word += "yız"
            elif word[-2] in "ou":
                word += "yuz"
        elif word[-2] in "eiöü":
            if word[-2] in "ei":
                word += "yiz"
            elif word[-2] in "öü":
                word += "yüz"
        elif word[-3] in "aıou":
            if word[-3] in "aı":
                word += "ız"
            elif word[-3] in "ou":
                word += "uz"
        elif word[-3] in "eiöü":
            if word[-3] in "ei":
                 word += "iz"
            elif word[-3] in "öü":
                word += "üz"
        else:
            if word[-4] in "aı":
                word += "ız"
            elif word[-4] in "ie":
                word += "iz"
            elif word[-4] in "ou":
                word += "uz"
            elif word[-4] in "öü":
                word += "üz"
        
    return word

#?-----------------------------------------------------------------------

#    My

myYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

myDogru = [
    "ağzım",
    "alnım",
    "bağrım",
    "benzim",
    "beynim",
    "boynum",
    "böğrüm",
    "burnum",
    "genzim",
    "göğsüm",
    "gönlüm",
    "karnım",
    "oğlum",
]

def my(word):
    
    isDogru_word_iyelik1 = False
    
    for i in range(len(myYanlis)):
        if word.lower() == myYanlis[i]:
            word = myDogru[i]
            isDogru_word_iyelik1 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_iyelik1:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
    
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
        
        if word[-1] in unluler:
            if unluSayisi > 1:
                word += "m"
            else:
                if word[-1] in unluler or word[-2] in unluler:
                    if word[-2] in "aı":
                        word += "yım"
                    elif word[-2] in "ou":
                        word += "yum"
                    elif word[-2] in "ei":
                        word += "yim"
                    elif word[-2] in "öü":
                        word += "yüm"
        elif word[-2] in unluler:
            if word[-2] in "aı":
                word += "ım"
            elif word[-2] in "ou":
                word += "um"
            elif word[-2] in "ei":
                word += "im"
            elif word[-2] in "öü":
                word += "üm"
        else:
            if word[-3] in "aı":
                word += "ım"
            elif word[-3] in "ou":
                word += "um"
            elif word[-3] in "ei":
                word += "im"
            elif word[-3] in "öü":
                word += "üm"
        return word
    
#?-----------------------------------------------------------------------

#    speMy

spemyYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

spemyDogru = [
    "ağzım",
    "alnım",
    "bağrım",
    "benzim",
    "beynim",
    "boynum",
    "böğrüm",
    "burnum",
    "genzim",
    "göğsüm",
    "gönlüm",
    "karnım",
    "oğlum",
]

def spemy(word):
    
    isDogru_word_iyelikk1 = False
    
    for i in range(len(spemyYanlis)):
        if word.lower() == spemyYanlis[i]:
            word = spemyDogru[i]
            isDogru_word_iyelikk1 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
    
    word = word.capitalize()
            
    if not isDogru_word_iyelikk1:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
    
        word += "'"
        
        if word[-2] in unluler:
            if unluSayisi > 1:
                word += "m"
            else:
                if word[-2] in unluler or word[-2] in unluler:
                    if word[-3] in "aı":
                        word += "yım"
                    elif word[-3] in "ou":
                        word += "yum"
                    elif word[-3] in "ei":
                        word += "yim"
                    elif word[-3] in "öü":
                        word += "yüm"
        elif word[-3] in unluler:
            if word[-3] in "aı":
                word += "ım"
            elif word[-3] in "ou":
                word += "um"
            elif word[-3] in "ei":
                word += "im"
            elif word[-3] in "öü":
                word += "üm"
        else:
            if word[-4] in "aı":
                word += "ım"
            elif word[-4] in "ou":
                word += "um"
            elif word[-4] in "ei":
                word += "im"
            elif word[-4] in "öü":
                word += "üm"
        return word

#?-----------------------------------------------------------------------

#    Your

yourYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

yourDogru = [
    "ağzın",
    "alnın",
    "bağrın",
    "benzin",
    "beynin",
    "boynun",
    "böğrün",
    "burnun",
    "genzin",
    "göğsün",
    "gönlün",
    "karnın",
    "oğlun",
]

def your(word):
    
    isDogru_word_iyelik2 = False
    
    for i in range(len(yourYanlis)):
        if word.lower() == yourYanlis[i]:
            word = yourDogru[i]
            isDogru_word_iyelik2 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_iyelik2:
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
        
        if word[-1] in unluler:
            if unluSayisi > 1:
                word += "n"
            else:
                if word[-1] in unluler or word[-2] in unluler:
                    if word[-2] in "aı":
                        word += "yın"
                    elif word[-2] in "ou":
                        word += "yun"
                    elif word[-2] in "ei":
                        word += "yin"
                    elif word[-2] in "öü":
                        word += "yün"
        elif word[-2] in unluler:
            if word[-2] in "aı":
                word += "ın"
            elif word[-2] in "ou":
                word += "un"
            elif word[-2] in "ei":
                word += "in"
            elif word[-2] in "öü":
                word += "ün"
        else:
            if word[-3] in "aı":
                word += "ın"
            elif word[-3] in "ou":
                word += "un"
            elif word[-3] in "ei":
                word += "in"
            elif word[-3] in "öü":
                word += "ün"
        return word
    
#?-----------------------------------------------------------------------

#    speYour

speyourYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

speyourDogru = [
    "ağzın",
    "alnın",
    "bağrın",
    "benzin",
    "beynin",
    "boynun",
    "böğrün",
    "burnun",
    "genzin",
    "göğsün",
    "gönlün",
    "karnın",
    "oğlun",
]

def speyour(word):
    
    isDogru_word_iyelikk2 = False
    
    for i in range(len(speyourYanlis)):
        if word.lower() == speyourYanlis[i]:
            word = speyourDogru[i]
            isDogru_word_iyelikk2 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
        
    word = word.capitalize()
            
    if not isDogru_word_iyelikk2:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        word += "'"
        
        if word[-2] in unluler:
            if unluSayisi > 1:
                word += "n"
            else:
                if word[-2] in unluler or word[-2] in unluler:
                    if word[-3] in "aı":
                        word += "yın"
                    elif word[-3] in "ou":
                        word += "yun"
                    elif word[-3] in "ei":
                        word += "yin"
                    elif word[-3] in "öü":
                        word += "yün"
        elif word[-3] in unluler:
            if word[-3] in "aı":
                word += "ın"
            elif word[-3] in "ou":
                word += "un"
            elif word[-3] in "ei":
                word += "in"
            elif word[-3] in "öü":
                word += "ün"
        else:
            if word[-4] in "aı":
                word += "ın"
            elif word[-4] in "ou":
                word += "un"
            elif word[-4] in "ei":
                word += "in"
            elif word[-4] in "öü":
                word += "ün"
        return word

#?-----------------------------------------------------------------------

#    Its

itsYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

itsDogru = [
    "ağzı",
    "alnı",
    "bağrı",
    "benzi",
    "beyni",
    "boynu",
    "böğrü",
    "burnu",
    "genzi",
    "göğsü",
    "gönlü",
    "karnı",
    "oğlu",
]

def its(word):
    
    isDogru_word_iyelik3 = False
    
    for i in range(len(itsYanlis)):
        if word.lower() == itsYanlis[i]:
            word = itsDogru[i]
            isDogru_word_iyelik3 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_iyelik3:
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
        
        if word[-1] in unluler:
            if unluSayisi > 1:
                if word[-1] in "aı":
                    word += "sı"
                elif word[-1] in "ou":
                    word += "su"
                elif word[-1] in "ei":
                    word += "si"
                elif word[-1] in "öü":
                    word += "sü"
            else:
                if word[-1] in unluler or word[-2] in unluler:
                    if word[-2] in "aı":
                        word += "yı"
                    elif word[-2] in "ou":
                        word += "yu"
                    elif word[-2] in "ei":
                        word += "yi"
                    elif word[-2] in "öü":
                        word += "yü"
        elif word[-2] in unluler:
            if word[-2] in "aı":
                word += "ı"
            elif word[-2] in "ou":
                word += "u"
            elif word[-2] in "ei":
                word += "i"
            elif word[-2] in "öü":
                word += "ü"
        else:
            if word[-3] in "aı":
                word += "ı"
            elif word[-3] in "ou":
                word += "u"
            elif word[-3] in "ei":
                word += "i"
            elif word[-3] in "öü":
                word += "ü"
        return word
    
#?-----------------------------------------------------------------------

#    speIts

speitsYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

speitsDogru = [
    "ağzı",
    "alnı",
    "bağrı",
    "benzi",
    "beyni",
    "boynu",
    "böğrü",
    "burnu",
    "genzi",
    "göğsü",
    "gönlü",
    "karnı",
    "oğlu",
]

def speits(word):
    
    isDogru_word_iyelikk3 = False
    
    for i in range(len(speitsYanlis)):
        if word.lower() == speitsYanlis[i]:
            word = speitsDogru[i]
            isDogru_word_iyelikk3 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
    
    word = word.capitalize()
            
    if not isDogru_word_iyelikk3:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        word += "'"
        
        if word[-2] in unluler:
            if unluSayisi > 1:
                if word[-2] in "aı":
                    word += "sı"
                elif word[-2] in "ou":
                    word += "su"
                elif word[-2] in "ei":
                    word += "si"
                elif word[-2] in "öü":
                    word += "sü"
            else:
                if word[-2] in unluler or word[-3] in unluler:
                    if word[-3] in "aı":
                        word += "yı"
                    elif word[-3] in "ou":
                        word += "yu"
                    elif word[-3] in "ei":
                        word += "yi"
                    elif word[-3] in "öü":
                        word += "yü"
        elif word[-3] in unluler:
            if word[-3] in "aı":
                word += "ı"
            elif word[-3] in "ou":
                word += "u"
            elif word[-3] in "ei":
                word += "i"
            elif word[-3] in "öü":
                word += "ü"
        else:
            if word[-4] in "aı":
                word += "ı"
            elif word[-4] in "ou":
                word += "u"
            elif word[-4] in "ei":
                word += "i"
            elif word[-4] in "öü":
                word += "ü"
        return word

#?-----------------------------------------------------------------------

#    Our

ourYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

ourDogru = [
    "ağzımız",
    "alnımız",
    "bağrımız",
    "benzimiz",
    "beynimiz",
    "boynumuz",
    "böğrümüz",
    "burnumuz",
    "genzimiz",
    "göğsümüz",
    "gönlümüz",
    "karnımız",
    "oğlumuz",
]

def our(word):
    
    isDogru_word_iyelik4 = False
    
    for i in range(len(ourYanlis)):
        if word.lower() == ourYanlis[i]:
            word = ourDogru[i]
            isDogru_word_iyelik4 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_iyelik4:
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
        
        if word[-1] in unluler:
            if unluSayisi > 1:
                if word[-1] in "aı":
                    word += "mız"
                elif word[-1] in "ou":
                    word += "muz"
                elif word[-1] in "ei":
                    word += "miz"
                elif word[-1] in "öü":
                    word += "müz"
            else:
                if word[-1] in unluler or word[-2] in unluler:
                    if word[-2] in "aı":
                        word += "yımız"
                    elif word[-2] in "ou":
                        word += "yumuz"
                    elif word[-2] in "ei":
                        word += "yimiz"
                    elif word[-2] in "öü":
                        word += "yümüz"
        elif word[-2] in unluler:
            if word[-2] in "aı":
                word += "ımız"
            elif word[-2] in "ou":
                word += "umuz"
            elif word[-2] in "ei":
                word += "imiz"
            elif word[-2] in "öü":
                word += "ümüz"
        else:
            if word[-3] in "aı":
                word += "ımız"
            elif word[-3] in "ou":
                word += "umuz"
            elif word[-3] in "ei":
                word += "imiz"
            elif word[-3] in "öü":
                word += "ümüz"
        return word
    
#?-----------------------------------------------------------------------

#    speOur

speourYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

speourDogru = [
    "ağzımız",
    "alnımız",
    "bağrımız",
    "benzimiz",
    "beynimiz",
    "boynumuz",
    "böğrümüz",
    "burnumuz",
    "genzimiz",
    "göğsümüz",
    "gönlümüz",
    "karnımız",
    "oğlumuz",
]

def speour(word):
    
    isDogru_word_iyelikk4 = False
    
    for i in range(len(speourYanlis)):
        if word.lower() == speourYanlis[i]:
            word = speourDogru[i]
            isDogru_word_iyelikk4 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
    
    word = word.capitalize()
            
    if not isDogru_word_iyelikk4:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        word += "'"
        
        if word[-2] in unluler:
            if unluSayisi > 1:
                if word[-2] in "aı":
                    word += "mız"
                elif word[-2] in "ou":
                    word += "muz"
                elif word[-2] in "ei":
                    word += "miz"
                elif word[-2] in "öü":
                    word += "müz"
            else:
                if word[-2] in unluler or word[-3] in unluler:
                    if word[-3] in "aı":
                        word += "yımız"
                    elif word[-3] in "ou":
                        word += "yumuz"
                    elif word[-3] in "ei":
                        word += "yimiz"
                    elif word[-3] in "öü":
                        word += "yümüz"
        elif word[-3] in unluler:
            if word[-3] in "aı":
                word += "ımız"
            elif word[-3] in "ou":
                word += "umuz"
            elif word[-3] in "ei":
                word += "imiz"
            elif word[-3] in "öü":
                word += "ümüz"
        else:
            if word[-4] in "aı":
                word += "ımız"
            elif word[-4] in "ou":
                word += "umuz"
            elif word[-4] in "ei":
                word += "imiz"
            elif word[-4] in "öü":
                word += "ümüz"
        return word
    
#?-----------------------------------------------------------------------

#    Yours

yoursYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

yoursDogru = [
    "ağzınız",
    "alnınız",
    "bağrınız",
    "benziniz",
    "beyniniz",
    "boynunuz",
    "böğrünüz",
    "burnunuz",
    "genziniz",
    "göğsünüz",
    "gönlünüz",
    "karnınız",
    "oğlunuz",
]

def yours(word):
    
    isDogru_word_iyelik5 = False
    
    for i in range(len(yoursYanlis)):
        if word.lower() == yoursYanlis[i]:
            word = yoursDogru[i]
            isDogru_word_iyelik5 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_iyelik5:
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
        
        if word[-1] in unluler:
            if unluSayisi > 1:
                if word[-1] in "aı":
                    word += "nız"
                elif word[-1] in "ou":
                    word += "nuz"
                elif word[-1] in "ei":
                    word += "niz"
                elif word[-1] in "öü":
                    word += "nüz"
            else:
                if word[-1] in unluler or word[-2] in unluler:
                    if word[-2] in "aı":
                        word += "yınız"
                    elif word[-2] in "ou":
                        word += "yunuz"
                    elif word[-2] in "ei":
                        word += "yiniz"
                    elif word[-2] in "öü":
                        word += "yünüz"
        elif word[-2] in unluler:
            if word[-2] in "aı":
                word += "ınız"
            elif word[-2] in "ou":
                word += "unuz"
            elif word[-2] in "ei":
                word += "iniz"
            elif word[-2] in "öü":
                word += "ünüz"
        else:
            if word[-3] in "aı":
                word += "ınız"
            elif word[-3] in "ou":
                word += "unuz"
            elif word[-3] in "ei":
                word += "iniz"
            elif word[-3] in "öü":
                word += "ünüz"
        return word
    
#?-----------------------------------------------------------------------

#    speYours

speyoursYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

speyoursDogru = [
    "ağzınız",
    "alnınız",
    "bağrınız",
    "benziniz",
    "beyniniz",
    "boynunuz",
    "böğrünüz",
    "burnunuz",
    "genziniz",
    "göğsünüz",
    "gönlünüz",
    "karnınız",
    "oğlunuz",
]

def speyours(word):
    
    isDogru_word_iyelikk5 = False
    
    for i in range(len(speyoursYanlis)):
        if word.lower() == speyoursYanlis[i]:
            word = speyoursDogru[i]
            isDogru_word_iyelikk5 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
    
    word = word.capitalize()
    
    if not isDogru_word_iyelikk5:
        
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
            
        word += "'"
        
        if word[-2] in unluler:
            if unluSayisi > 1:
                if word[-2] in "aı":
                    word += "nız"
                elif word[-2] in "ou":
                    word += "nuz"
                elif word[-2] in "ei":
                    word += "niz"
                elif word[-2] in "öü":
                    word += "nüz"
            else:
                if word[-2] in unluler or word[-3] in unluler:
                    if word[-3] in "aı":
                        word += "yınız"
                    elif word[-3] in "ou":
                        word += "yunuz"
                    elif word[-3] in "ei":
                        word += "yiniz"
                    elif word[-3] in "öü":
                        word += "yünüz"
        elif word[-3] in unluler:
            if word[-3] in "aı":
                word += "ınız"
            elif word[-3] in "ou":
                word += "unuz"
            elif word[-3] in "ei":
                word += "iniz"
            elif word[-3] in "öü":
                word += "ünüz"
        else:
            if word[-4] in "aı":
                word += "ınız"
            elif word[-4] in "ou":
                word += "unuz"
            elif word[-4] in "ei":
                word += "iniz"
            elif word[-4] in "öü":
                word += "ünüz"
        return word
    
#?-----------------------------------------------------------------------

#    Their

def their(word):
    if word[-1] in "aıou" or word[-2] in "aıou":
        if word[-1] in "eiöü":
            word += "leri"
        else:
            word += "ları"
    elif word[-1] in "eiöü" or word[-2] in "eiöü":
        word += "leri"
    else:
        if word[-3] in "aıou":
            word += "ları"
        elif word[-3] in "eiöü":
            word += "leri"
    return word
#?-----------------------------------------------------------------------

#    speTheir

def spetheir(word):
    
    word = word.capitalize()
    word += "'"
    
    if word[-2] in "aıou" or word[-3] in "aıou":
        if word[-2] in "eiöü":
            word += "leri"
        else:
            word += "ları"
    elif word[-2] in "eiöü" or word[-3] in "eiöü":
        word += "leri"
    else:
        if word[-4] in "aıou":
            word += "ları"
        elif word[-4] in "eiöü":
            word += "leri"
    return word

#?-----------------------------------------------------------------------

#    Complement
complementYanlis = [
    "su",
    "şehir",
    "fikir"
]

complementDogru = [
    "suyun",
    "şehrin",
    "fikrin"
]

    
def complement(word):
    
    isDogru_word_complement = False
    
    for i in range(len(complementYanlis)):
        if word.lower() == complementYanlis[i]:
            word = complementDogru[i]
            isDogru_word_complement = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word_complement:
    # ın, in, un, ün, nın, nin, nun, nün
    
        if word[-1] in unluler:
            if word[-1] in "aı":
                word += "nın"
            elif word[-1] in "ou":
                word += "nun"
            elif word[-1] in "ei":
                word += "nin"
            elif word[-1] in "öü":
                word += "nün"
        elif word[-2] in unluler:
            if word[-1] in "aı":
                word += "ın"
            elif word[-1] in "ou":
                word += "un"
            elif word[-1] in "ei":
                word += "in"
            elif word[-1] in "öü":
                word += "ün"
        else:
            if word[-3] in "aı":
                word += "ın"
            elif word[-3] in "ou":
                word += "un"
            elif word[-3] in "ei":
                word += "in"
            elif word[-3] in "öü":
                word += "ün"
    return word

#?-----------------------------------------------------------------------

#    SpeComplement
specomplementYanlis = [
    "su",
    "şehir",
    "fikir"
]

specomplementDogru = [
    "Su'yun",
    "Şehir'in",
    "Fikir'in"
]

    
def specomplement(word):
    
    isDogru_word_complement2 = False
    
    for i in range(len(specomplementYanlis)):
        if word.lower() == specomplementYanlis[i]:
            word = specomplementDogru[i]
            isDogru_word_complement2 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
    
    word = word.capitalize()
    
    if not isDogru_word_complement2:
    # ın, in, un, ün, nın, nin, nun, nün
    
        word += "'"
        
        if word[-2] in unluler:
            if word[-2] in "aı":
                word += "nın"
            elif word[-2] in "ou":
                word += "nun"
            elif word[-2] in "ei":
                word += "nin"
            elif word[-2] in "öü":
                word += "nün"
        elif word[-2] in unluler:
            if word[-2] in "aı":
                word += "ın"
            elif word[-2] in "ou":
                word += "un"
            elif word[-2] in "ei":
                word += "in"
            elif word[-2] in "öü":
                word += "ün"
        else:
            if word[-4] in "aı":
                word += "ın"
            elif word[-4] in "ou":
                word += "un"
            elif word[-4] in "ei":
                word += "in"
            elif word[-4] in "öü":
                word += "ün"
    return word

#?-----------------------------------------------------------------------

#    Accusative

accusativeYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

accusativeDogru = [
    "ağzı",
    "alnı",
    "bağrı",
    "benzi",
    "beyni",
    "boynu",
    "böğrü",
    "burnu",
    "genzi",
    "göğsü",
    "gönlü",
    "karnı",
    "oğlu",
]

def accusative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word1 = False
    
    for i in range(len(accusativeYanlis)):
        if word.lower() == accusativeYanlis[i]:
            word = accusativeDogru[i]
            isDogru_word1 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word1:
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
        
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
    
        if word[-1] in "aıou":
            if word[-1] in "aı":
                word += "yı"
            elif word[-1] in "ou":
                word += "yu"
        elif word[-1] in "eiöü":
            if word[-1] in "ei":
                word += "yi"
            elif word[-1] in "öü":
                word += "yü"
        elif word[-2] in "aıou":
            if word[-2] in "aı":
                word += "ı"
            elif word[-2] in "ou":
                word += "u"
        elif word[-2] in "eiöü":
            if word[-2] in "ei":
                 word += "i"
            elif word[-2] in "öü":
                word += "ü"
        else:
            if word[-3] in "aı":
                word += "ı"
            elif word[-3] in "ie":
                word += "i"
            elif word[-3] in "ou":
                word += "u"
            elif word[-3] in "öü":
                word += "ü"
            
    return word

#?-----------------------------------------------------------------------

#    Speaccusative

speaccusativeYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

speaccusativeDogru = [
    "ağzı",
    "alnı",
    "bağrı",
    "benzi",
    "beyni",
    "boynu",
    "böğrü",
    "burnu",
    "genzi",
    "göğsü",
    "gönlü",
    "karnı",
    "oğlu",
]

def speaccusative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word2 = False
    
    for i in range(len(speaccusativeYanlis)):
        if word.lower() == speaccusativeYanlis[i]:
            word = speaccusativeDogru[i]
            isDogru_word2 = True
            
    word = word.capitalize()
            
    if not isDogru_word2:
        
        word += "'"
    
        if word[-2] in "aıou":
            if word[-2] in "aı":
                word += "yı"
            elif word[-2] in "ou":
                word += "yu"
        elif word[-2] in "eiöü":
            if word[-2] in "ei":
                word += "yi"
            elif word[-2] in "öü":
                word += "yü"
        elif word[-3] in "aıou":
            if word[-3] in "aı":
                word += "ı"
            elif word[-3] in "ou":
                word += "u"
        elif word[-3] in "eiöü":
            if word[-3] in "ei":
                 word += "i"
            elif word[-3] in "öü":
                word += "ü"
        else:
            if word[-4] in "aı":
                word += "ı"
            elif word[-4] in "ie":
                word += "i"
            elif word[-4] in "ou":
                word += "u"
            elif word[-4] in "öü":
                word += "ü"
            
    return word

#?----------------------------------------------------------------------------

#    Dative

dativeYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

dativeDogru = [
    "ağza",
    "alna",
    "bağra",
    "benze",
    "beyne",
    "boyna",
    "böğre",
    "burna",
    "genze",
    "göğse",
    "gönle",
    "karna",
    "oğla",
]

def dative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word3 = False
    
    for i in range(len(dativeYanlis)):
        if word.lower() == dativeYanlis[i]:
            word = dativeDogru[i]
            isDogru_word3 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word3:
        unluSayisi = sum(1 for i in word if i in unlulerBuyukVeKucuk)
        
        if unluSayisi > 1:
            if word[-1] in "pçtk":
                if word[-1] == "p":
                    word = word[:-1] + "b"
                elif word[-1] == "ç":
                    word = word[:-1] + "c"
                elif word[-1] == "t":
                    word = word[:-1] + "d"
                elif word[-1] == "k":
                    if word[-2] in unlulerBuyukVeKucuk:
                        word = word[:-1] + "ğ"
                    else:
                        word = word[:-1] + "g"
                    
        if word[-1] in "aıou":
            word += "ya"
        elif word[-2] in "aıou":
            if word[-1] in "eiöü":
                word += "ye"
            else:
                word += "a"
        elif word[-1] in "eiöü":
            word += "ye"
        elif word[-2] in "eiöü":
            word += "e"
        
        else:
            if word[-3] in "aıou":
                word += "a"
            if word[-3] in "eiöü":
                word += "e"
                
    return word

#?----------------------------------------------------------------------------

#    Spedative

spedativeYanlis = [
    "ağız",
    "alın",
    "bağır",
    "beniz",
    "beyin",
    "boyun",
    "böğür",
    "burun",
    "geniz",
    "göğüs",
    "gönül",
    "karın",
    "oğul",
]

spedativeDogru = [
    "ağza",
    "alna",
    "bağra",
    "benze",
    "beyne",
    "boyna",
    "böğre",
    "burna",
    "genze",
    "göğse",
    "gönle",
    "karna",
    "oğla",
]

def spedative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word4 = False
    
    for i in range(len(spedativeYanlis)):
        if word.lower() == spedativeYanlis[i]:
            word = spedativeDogru[i]
            isDogru_word4 = True
            

    word = word.capitalize()
            
    if not isDogru_word4:
        
        word += "'"
        if word[-2] in "aıou":
            word += "ya"
        elif word[-3] in "aıou":
            if word[-2] in "eiöü":
                word += "ye"
            else:
                word += "a"
        elif word[-2] in "eiöü":
            word += "ye"
        elif word[-3] in "eiöü":
            word += "e"
        
        else:
            if word[-4] in "aıou":
                word += "a"
            if word[-4] in "eiöü":
                word += "e"
                
    return word

#?----------------------------------------------------------------------------

#    Locative

locativeYanlis = []
locativeDogru = []

def locative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word5 = False
    
    for i in range(len(locativeYanlis)):
        if word.lower() == locativeYanlis[i]:
            word = locativeDogru[i]
            isDogru_word5 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word5:
        if word[-1] in sertUnsuzler:
            if word[-2] in "aıou":
                word += "ta"
            elif word[-2] in "eiöü":
                word += "te"
            else:
                if word[-3] in "aıou":
                    word += "ta"
                elif word[-3] in "eiöü":
                    word += "te"
                    
        else:
            if word[-1] in "aıou" or word[-2] in "aıou":
                if word[-1] in "eiöü":
                    word += "de"
                else:
                    word += "da"
            elif word[-1] in "eiöü" or word[-2] in "eiöü":
                word += "de"
            else:
                if word[-3] in "aıou":
                    word += "da"
                elif word[-3] in "eiöü":
                    word += "de"
    return word

#?----------------------------------------------------------------------------

#    Spelocative

spelocativeYanlis = []
spelocativeDogru = []

def spelocative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word6 = False
    
    for i in range(len(spelocativeYanlis)):
        if word.lower() == spelocativeYanlis[i]:
            word = spelocativeDogru[i]
            isDogru_word6 = True
            
    word = word.capitalize()
            
    if not isDogru_word6:
        word += "'"
        if word[-2] in sertUnsuzler:
            if word[-3] in "aıou":
                word += "ta"
            elif word[-3] in "eiöü":
                word += "te"
            else:
                if word[-4] in "aıou":
                    word += "ta"
                elif word[-4] in "eiöü":
                    word += "te"
                    
        else:
            if word[-2] in "aıou" or word[-3] in "aıou":
                if word[-2] in "eiöü":
                    word += "de"
                else:
                    word += "da"
            elif word[-2] in "eiöü" or word[-3] in "eiöü":
                word += "de"
            else:
                if word[-4] in "aıou":
                    word += "da"
                elif word[-4] in "eiöü":
                    word += "de"
    return word

#?----------------------------------------------------------------------------

#    Ablative

ablativeYanlis = []
ablativeDogru = []

def ablative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word7 = False
    
    for i in range(len(ablativeYanlis)):
        if word.lower() == ablativeYanlis[i]:
            word = ablativeDogru[i]
            isDogru_word7 = True
            
    if word[0] in "ERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ":
        word = word.capitalize()
            
    if not isDogru_word7:
        if word[-1] in sertUnsuzler:
            if word[-2] in "aıou":
                word += "tan"
            elif word[-2] in "eiöü":
                word += "ten"
            else:
                if word[-3] in "aıou":
                    word += "tan"
                elif word[-3] in "eiöü":
                    word += "ten"
                    
        else:
            if word[-1] in "aıou" or word[-2] in "aıou":
                if word[-1] in "eiöü":
                    word += "den"
                else:
                    word += "dan"
            elif word[-1] in "eiöü" or word[-2] in "eiöü":
                word += "den"
            else:
                if word[-3] in "aıou":
                    word += "dan"
                elif word[-3] in "eiöü":
                    word += "den"
    return word

#?----------------------------------------------------------------------------

#    Speablative

speablativeYanlis = []
speablativeDogru = []

def speablative(word):
    global unlulerBuyukVeKucuk, unsuzler
    
    isDogru_word8 = False
    
    for i in range(len(speablativeYanlis)):
        if word.lower() == speablativeYanlis[i]:
            word = speablativeDogru[i]
            isDogru_word8 = True
            
    word = word.capitalize()
            
    if not isDogru_word8:
        word += "'"
        if word[-2] in sertUnsuzler:
            if word[-3] in "aıou":
                word += "tan"
            elif word[-3] in "eiöü":
                word += "ten"
            else:
                if word[-4] in "aıou":
                    word += "tan"
                elif word[-4] in "eiöü":
                    word += "ten"
                    
        else:
            if word[-2] in "aıou" or word[-3] in "aıou":
                if word[-2] in "eiöü":
                    word += "den"
                else:
                    word += "dan"
            elif word[-2] in "eiöü" or word[-3] in "eiöü":
                word += "den"
            else:
                if word[-4] in "aıou":
                    word += "dan"
                elif word[-4] in "eiöü":
                    word += "den"
    return word

#?----------------------------------------------------------------------------

# Relative

def relative(word):
    word += "ki"
    return word

#?-----------------------------------------------------------------------------

# Equality

def equality(word):
    global unlulerBuyukVeKucuk, unsuzler
            
    
    if word[-1] in sertUnsuzler:
        if word[-2] in "aıou":
            word += "ça"
        elif word[-2] in "eiöü":
            word += "çe"
        else:
            if word[-3] in "aıou":
                word += "ça"
            elif word[-3] in "eiöü":
                word += "çe"
                    
    else:
        if word[-1] in "aıou" or word[-2] in "aıou":
            word += "ca"
        elif word[-1] in "eiöü" or word[-2] in "eiöü":
            word += "ce"
        else:
            if word[-3] in "aıou":
                word += "ca"
            elif word[-3] in "eiöü":
                word += "ce"
    return word

#?-----------------------------------------------------------

