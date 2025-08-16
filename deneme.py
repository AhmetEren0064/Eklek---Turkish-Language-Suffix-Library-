from ek import *

#! ÖRNEK:
#todo Not oluşturma programı yazdınız. Ve notun varsayılan isminin kullanıcının adıyla olmasını istediniz.
#* Ahmet'in Projesi.
#* Mahmut'un Projesi.
#* Tolga'nın Projesi.
#? Bu kütüphaneyle artık "Tolga adlı kişinin projesi" gibi isimler takmanıza gerek kalmayacak.

name = "tolga"

#* Normalde;
print(name + "'ın projesi")
print(name + " kişisinin projesi")

#* Bununla;
print(specomplement(name) + " projesi") #* Çıktı --> Tolga'nın projesi

"""
#? Fonksiyonlar ve Beklenen Sonuçlar;

#* Şahıs Ekleri
me() kitabım
speme() Kitap'ım
you() kitapsın
speyou() Kitap'sın
youplural() kitapsınız
speyouplural() Kitap'sınız
we() kitabız
spewe() Kitap'ız

#* İyelik Ekleri
my() kitabım
spemy() Kitap'ım
your() kitabın
speyour() Kitap'ın
its() kitabı
speits() Kitap'ı
our() kitabımız
speour() Kitap'ımız
yours() kitabınız
speyours() Kitap'ınız
their() kitapları
spetheir() Kitap'ları

#* Hal Ekleri
accusative() kitabı
speaccusative() Kitap'ı
dative() kitaba
spedative() Kitap'a
locative() kitapta
spelocative() Kitap'ta
ablative() kitaptan
speablative() Kitap'tan

#* Diğer Ekler
plural() kitaplar
question() kitap mı
complement() kitabın
specomplement() Kitap'ın
relative() Kitaptaki (buradaki kelime kitap değil "kitapta" ki bitişik yazılsın diye. Ki'nin ayrı yazıldığı durumlarda kullanmayınız.)
equality() kitapça

Not: Ek eğer özel bir isme(Ahmet, Mehmet, İstanbul, Bursa gibi) gelecekse başında "spe..." bulunan fonksiyonları tercih ediniz.;
locative() --> kitapta
spelocative() --> Kitap'ta, bunun gibi."""