print("***BİLGİ YARIŞMASI OYUNUNA HOŞGELDİNİZ***")
puan=0
dogruCevap=0
yanlısCevap=0
print("1.soru:")
question="Alfabemizin ilk harfi nedir? \n"
answer=input(question)
if answer=="A" or answer=="a":
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("2.soru:")
question="Dünyamızın uydusu nedir? \n"
answer=input(question)
if answer=="AY" or answer=="ay" or answer=="Ay":
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("3.soru:")
question="8+2= \n"
answer=int(input(question))
if answer==10:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap=+1
print("4.soru:")
question="3+9= \n"
answer=int(input(question))
if answer==12:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("5.soru:")
question="3+3= \n"
answer=int(input(question))
if answer==6:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("6.soru:")
question="3+4= \n"
answer=int(input(question))
if answer==7:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("7.soru:")
question="3+6= \n"
answer=int(input(question))
if answer==9:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("8.soru:")
question="5+5= \n"
answer=int(input(question))
if answer==10:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("9.soru:")
question="2+5= \n"
answer=int(input(question))
if answer==7:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
print("10.soru:")
question="9+2= \n"
answer=int(input(question))
if answer==11:
  puan=puan+10
  dogruCevap+=1
else:
  yanlısCevap+=1
if dogruCevap<5:
  print("Başarısız")
else:
  print("Başarılı")
print("Toplam puan:",puan)
  


