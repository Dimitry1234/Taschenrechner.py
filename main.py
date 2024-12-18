import math #Bibliothek für Mathe 

#Taschenrechner Optionen
# +
def addieren() :
     a = input("Geben Sie den ersten Zahlenwert  ein: ")
     b = input("Geben Sie den zweiten Zahlenwert ein: ")
     a = int (a) #int, dass es als Zahl eingegeben werden kann und nicht als string definiert ist-
     b = int (b) 
     c = a + b
     print("Das Ergebnis der Rechnung {}+{} lautet: {}".format(a,b,c))

#-
def subtrahieren() :
     a = input("Geben Sie  den ersten Zahlenwert ein: ")
     b = input("Geben Sie  den zweiten Zahlenwert ein: ")
     a = int (a)
     b = int (b) 
     c = a - b
     print("Das Ergebnis der Rechnung {}-{} lautet:{}".format(a,b,c))

# *
def multiplizieren() :
     a = input("Geben Sie den ersten Zahlenwert ein: ")
     b = input("Geben Sie den zweiten Zahlenwert ein: ")
     a = int (a)
     b = int (b) 
     c = a * b
     print("Das Ergebnis der Rechnung {}*{} lautet: {}".format(a,b,c))

#/
def dividieren():
     a = input("Geben Sie den ersten Zahlenwert ein: ")
     b = input("Geben Sie den zweiten Zahlenwert ein: ")
     a = int (a)
     b = int (b) 
     c = a / b
     print("Das Ergebnis der Rechnung {}/{} lautet: {}".format(a,b,c))

# Mittelwert
def mittelwert() :
    x = input("Geben Sie bitte die Anzahl an Zahlen ein, von denen der Mittelwert berechnet werden soll: ")
    x = int (x) #Eingabe der Zahlen
    zahlen = [] #Liste der Zahlen
    zaehler = 0
    mittelwert = 0
    while zaehler < x :
     y = input("Geben Sie nun die {}. Zahl ein: ".format(zaehler+1))
     y = int (y)
     zahlen.append(y) #Liste der Länger wird erhöht
     mittelwert += zahlen[zaehler]
     zaehler += 1
    mittelwert = mittelwert / x #geteilt durch die Anzahl Zahlenwerte die man gewählt hat
    anzahl = "{}"
    print("Der Mittelwert der Zahlen: {} beträgt: {}".format(zahlen, mittelwert))


# Summe einer Liste an Zahlen
def summeListe() : 
    print("Bitte geben Sie nun die Zahlen ein, von denen Sie die Summe haben wollen. Beenden Sie Ihre Eimgabe mit: \"fertig\" ein:\n ")
    zahlen = []
    zaehler = 0
    summe  = 0
    while input != "fertig" : #solange nicht "fertig", Eingabe  geht weiter
     y = input("Geben Sie nun die {}. Zahl ein: ".format(zaehler+1))
     if y == "fertig" :
      break #geht aus der while Schleife raus, da "fertig" kam
     y = int(y)
     zahlen.append(y)
     zaehler += 1
    print("Die Summe der Zahlen Ihrer Liste: {} beträgt: {} ".format(zahlen, sum(zahlen)))

#Maximum einer Liste an Zahlebn
def maximumWert() :
    print("Bitte geben Sie gleich die Zahlen der Liste ein, von denen das Maximum bestimmt werden soll. Beenden Sie die Eingabe mit\"fertig\" ein:\n ")
    zahlen = []
    zaehler = 0
    maxWert  = 0
    while input != "fertig" :
     y = input("Geben Sie nun die {}. Zahl ein: ".format(zaehler+1))
     if y == "fertig" :
      break
     y = int(y)
     zahlen.append(y)
     zaehler += 1
    print("Das Maximum Ihrer Liste: {} ist: {} ".format(zahlen, max(zahlen)))

#Minimum einer Liste an Zahlen
def minimumWert() :
    print("Bitte geben Sie gleich die Zahlen der Liste ein, von denen das Minimum bestimmt werden soll. Beenden Sie die Eingabe mit \"fertig\" ein:\n ")
    zahlen = []
    zaehler = 0
    maxWert  = 0
    while input != "fertig" :
     y = input("Geben Sie nun die {}. Zahl ein: ".format(zaehler+1))
     if y == "Fertig" :
      break
     y = int(y)
     zahlen.append(y)
     zaehler += 1
    print("Das Minimum Ihrer Liste: {} ist: {} ".format(zahlen, min(zahlen)))

#Umfang eines Kreises - bei einem gegebenen Radius
def umfangKreis() :
     r = input("Bitte geben Sie den Radius ihres Kreises in cm ein: ")
     r = int (r)
     umfang = math.pi * (r ** 2) #Potenzoperator
     print("Der Umfang ihres Kreises mit einem Radius von {}cm beträgt: {}".format(r, umfang))


#Satz des Pythagoras
def phytagoras() :
     a = input("Geben Sie bitte den Wert fuer a^2 ein: ")
     b = input("Geben Sie bitte den Wert fuer b^2 ein: ")
     a = int (a)
     b = int (b)
     z = a + b
     z = math.sqrt(z) #Wurzel
     print("Für a^2= {} und b^2= {} betraegt z= {}".format(a, b, z))


#Bedienung des Taschenrechners
def taschenrechner() :
     x = input("Welche mathemathische Operation wollen Sie ausführen?\n Geben Sie die jeweilige Nummer ein:\n1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division\n5: Mittelwertbestimmung\n6: Summe einer Liste\n7: Maximum einer Liste\n8: Minimum einer Liste\n9: Berrechnung des Umfang eines Kreises\n10:Bestimmung von C mit Satz des Phytagoras\n\n")
     x = int(x)
     if x == 1 :
      addieren()

     if x == 2 :
      subtrahieren()

     if x == 3 :
      multiplizieren()

     if x == 4 :
      dividieren()

     if x == 5 :
      mittelwert()

     if x == 6 :
      summeListe()

     if x == 7 :
      maximumWert()

     if x == 8 :
      minimumWert()

     if x == 9 :
      umfangKreis()
      1

     if x == 10 :
      phytagoras()

def main() : #Die Mainfunktion
    taschenrechner()
    x = input("\n Weiter Aufgabe mathematische Aufgabe stellen? Ja/Nein: ")
    if x == "Ja" :
        main()
    else:
        quit()

main () #die ausgeführte Funktion


