import random
import time

# ustalanie początkowej ceny krypta
cena = 1  #kwh
ilosc_krypto = 1000

#poczatkowa ilosc energi w sieci 
energia = 1000

produkcja_energi = 0
pobor_energi = 0


# ustalanie początkowego popytu i podaży [sztuki]
popyt = 100
podaż = 100

#  czynnik losowy wpływającego na popyt i podaż
czynnik = random.uniform(0.5, 1.5)

# symulacja zmiany czynnika wpływającego na popyt i podaż
while True:

    #Zmiana podaży i popytu w losowaniu
    czynnik = random.uniform(70, 130)
    popyt = czynnik

    czynnik = random.uniform(70, 130)
    podaż = czynnik
    
    wsp_podaży = 1 + 0.98* (popyt - podaż)/100

    # Zmiana w produkcji i poboru energi elektrycznej
    
    produkcja_energi = random.uniform(800,1200)
    pobor_energi = random.uniform(800,1200)
    #wsp_energi = 1 + 0.98* (pobor_energi - produkcja_energi)/1000

    delta_energi = pobor_energi - produkcja_energi

    wsp_energi =  (energia + delta_energi)/energia
    energia = energia + delta_energi


    # ustalenie nowej ceny krypto
    cena = cena * wsp_podaży * (1/wsp_energi)
    
    # wyświetlenie wyników

    print(f"Cena krypto: {cena:.2f} kwh, popyt: {popyt:.0f} sztuk, podaż: {podaż:.0f} sztuk, ,ilośc energi {energia:0f} kWh, ilość krypto {ilosc_krypto:.0f}" )
    
    # zatrzymanie programu na 10 sekund
    time.sleep(10)