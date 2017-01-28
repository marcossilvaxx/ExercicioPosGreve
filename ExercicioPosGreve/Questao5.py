dia=int (input("Quantos cigarros você fuma por dia?: "))
tempo=int (input("A quantos anos você fuma?: "))
total = 10*dia*tempo*365.2425
total1= total /1440
print ("Vc perdeu %d dias da sua vida" %total1)