# Eklek---Turkish-Language-Suffix-Library-
 Suffix support for Turkish language, very functional and useful.

This project provides a functional morpheme model for Turkish, designed to handle complex word formations and grammatical structures.
It includes 34 distinct functions covering pronouns, cases, possessive endings, plurals, questions, and connectors.

Features;

- Rule-based: Incorporates core Turkish rules including vowel harmony, consonant softening, and pluralization.

- Exceptions handled: Common irregularities are included. Only a very small subset of exceptions to exceptions exist and can be considered special cases.

- Composable functions: The 34 functions can be combined like puzzle pieces, allowing you to create complex morphological structures in a modular and flexible way.


This part is in Turkish to explain Turks the project's functions; 

## ÖRNEK:
Not oluşturma programı yazdınız. Ve notun varsayılan isminin kullanıcının adıyla olmasını istediniz.
- Ahmet'in Projesi.
- Mahmut'un Projesi.
- Tolga'nın Projesi.
### Bu kütüphaneyle artık "Tolga adlı kişinin projesi" gibi isimler takmanıza gerek kalmayacak.

name = "tolga"

#### Normalde;
- print(name + " kişisinin projesi")

#### Bununla;
- print(specomplement(name) + " projesi") #* Çıktı --> Tolga'nın projesi


# Fonksiyonlar ve Beklenen Sonuçlar;

### Şahıs Ekleri
- me() --> kitabım
- speme() --> Kitap'ım
- you() --> kitapsın
- speyou() --> Kitap'sın
- youplural() --> kitapsınız
- speyouplural() --> Kitap'sınız
- we() --> kitabız
- spewe() --> Kitap'ız

### İyelik Ekleri
- my() --> kitabım
- spemy() --> Kitap'ım
- your() --> kitabın
- speyour() --> Kitap'ın
- its() --> kitabı
- speits() --> Kitap'ı
- our() --> kitabımız
- speour() --> Kitap'ımız
- yours() --> kitabınız
- speyours() --> Kitap'ınız
- their() --> kitapları
- spetheir() --> Kitap'ları

### Hal Ekleri
- accusative() --> kitabı
- speaccusative() --> Kitap'ı
- dative() --> kitaba
- spedative() --> Kitap'a
- locative() --> kitapta
- spelocative() --> Kitap'ta
- ablative() --> kitaptan
- speablative() --> Kitap'tan

### Diğer Ekler
- plural() --> kitaplar
- question() --> kitap mı
- complement() --> kitabın
- specomplement() --> Kitap'ın
- relative() --> Kitaptaki (buradaki kelime kitap değil "kitapta" ki bitişik yazılsın diye. Ki'nin ayrı yazıldığı - durumlarda kullanmayınız.)
- equality() --> kitapça

## Not:  
Ek eğer özel bir isme(Ahmet, Mehmet, İstanbul, Bursa gibi) gelecekse başında "spe..." bulunan fonksiyonları tercih ediniz.;
locative() --> kitapta
spelocative() --> Kitap'ta, bunun gibi.


## License

This project is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.  
You may use it for personal and educational purposes only.  
Commercial use or modifications of the code are not permitted.  
Credit must be given to the original author.