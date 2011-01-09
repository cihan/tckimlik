#!/usr/bin/env python
#-*- coding: utf-8 -*-

#TC Kimlik doğrulama
print "TC Kimlik numarası doğrulama oyuncağıma hoşgeldiniz. amaç girilen verinin tc kimlik algoritmasınca kontrol edilmesidir. \n"
data = raw_input("TC Kimlik Numarası?\n")
# Veriyi uzunluğunu kontrol edilecek.
if len(data) != 11:
	print "Girmiş olduğunuz numara 11 haneden oluşmak zorundadır!"
else:
# İlk hane sıfırdan farklı olmak zorunda kontrol edilecek.
	if int(data[0]) == 0:
		print "İlk hane sıfır (0) olamaz!"
	else:
#1. 3. 5. 7. 9. hanelerin toplamının 7 katından 2.4.6.8. hanelerin toplamı çıkartılıp 10'a bölündüğünde; kalan 10. haneyi vermelidir.
		if ((((int(data[0])+int(data[2])+int(data[4])+int(data[6])+int(data[8]))*7)-((int(data[1])+int(data[3])+int(data[5])+int(data[7])))) % 10) != int(data[9]):
			print "10. hane doğrulanamadı!"
		else:
#İlk 10 hanenin toplamının 10 ile bölümünden kalan 11. haneyi vermelidir.
			a = 0
			for i in data[0:10]:
				a = a + int(i)
			if (a % 10) != int(data[10]):
				print "11. hane doğrulanamadı."
			else:
				print "TC Kimlik no doğrulama başarılı."
