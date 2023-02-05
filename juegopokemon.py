import random


print("A continuacion debera elegir un pokemon , su rival sera el computador")


pk1="Torchic"
pk2="Mudkip"
pk3="Treeko"


print("1.Torhic")
print("2.Mudkip")
print("3.Treeko")

#Ataques de pokemon tipo fuego-> Torchic
at1="Picotazo"
at2="Ascuas"
at3="Arañazo"
at4="Grito"
#Ataques de pokemon tipo agua -> Mudkip
bt1="Burbujas"
bt2="Placaje"
bt3="Pistola Agua"
bt4="Grito"
#Ataques de pokemon tipo tierra -> Treeko
ct1="Destructor"
ct2="Malicioso"
ct3="Hoja afilada"
ct4="Agilidad"

pokemon=(int(input("Que pokemon desea elegir?--> ")))
if pokemon==1:
    print(f"Elegiste {pk1} asi que tu rival sera {pk2} ")
    print(f"Tus ataques seran {at1},{at2},{at3} y {at4}")  
    def eleccion_ataques():
        ataques_usuario=(f"{at1}", f"{at2}",f"{at3}",f"{at4}")
        ataques_usuario=input(f"Elige el ataque de {pk1},{at1},{at2},{at3},{at4}--> ")
        ataques_usuario=ataques_usuario.lower()
        ataque_rival=(f"{bt1}",f"{bt2}",f"{bt3}",f"{bt4}")
        ataques_computador=random.choice(ataque_rival)
        print(f'{pk1} uso',ataques_usuario)
        print(f"{pk2} uso", ataques_computador)
        return ataques_computador, ataques_usuario
    def juego(ataques_usuario, ataques_computador, pokemonusuario_gano, pokemonrival_gano ):
        if ataques_usuario ==ataques_computador:
            print("No se hicieron daño")
        elif ataques_usuario==f"{at1}":
            if ataques_computador==f"{bt4}":
                print(f"{pk1} ha hecho daño a {pk2}")
                print(f"Mientras que {pk2} solo pudo bajarle las denfensas")
                pokemonusuario_gano+=1
            else:
                print(f"{pk1} no pudo completar su ataque")
                print(f"{pk2} y manda un feroz ataque de {bt1} a {pk1}")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{at2}":
            if ataques_computador==f"{bt1}":
                print(f"{pk1} ataco con {at2} y deja a su rival herido")
                print(f"{pk2} va a tratar de devolverle con un ataque {bt1} pero queda confundido y se ataca asi mismo")
                pokemonusuario_gano+=1
            else:
                print(f"El ataque de {pk1} no pudo ser concretado por que el {bt3} de {pk2} estuvo fuerte")
                print(f"{pk2} en este momento tiene la ventaja")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{at3}":
            if ataques_computador==f"{bt2}":
                print(f"{pk1} ataco con {at3} fue un ataque eficaz")
                print(f"{pk2} no pudo mandar{bt2} por que el ataque de {pk1} fue rapido")
                pokemonusuario_gano+=1
            else:
                print(f"El ataque de {pk1} no pudo ser concretado por que el {bt2} de {pk2} estuvo fuerte")
                print(f"{pk2} en este momento tiene la ventaja")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{at4}":
            if ataques_computador==f"{bt3}":
                print(f"{pk1} dio un {at4} fue un ataque eficaz")
                print(f"{pk2} no pudo mandar{bt3} por que el ataque de {pk1} fue rapido")
            else:
                print(f"El ataque de {pk1} no pudo ser concretado por que el {bt3} de {pk2} estuvo fuerte")
                print(f"{pk2} en este momento tiene la ventaja")
        return ataques_usuario, ataques_computador 
    def empezar_pelea():
            pokemonusuario_gano=0
            pokemonrival_gano=0
            rounds = 1
            while True:
                print('*'*10)
                print("Ronda", rounds)
                print("*" * 10)
        
                print(f"{pk1} uso", pokemonusuario_gano)
                print(f"{pk2} uso", pokemonrival_gano)
                rounds+=1
        
                ataques_usuario, ataques_computador = eleccion_ataques()
                pokemonusuario_gano, pokemonrival_gano=juego(ataques_usuario, ataques_computador, pokemonusuario_gano, pokemonrival_gano )
        
                if pokemonrival_gano ==5:
                    print(f"El ganador es{pk2}")
                    break
                               
                if pokemonusuario_gano==5:
                    print(f"El ganador es {pk1}")
                    break
    empezar_pelea()    
       
elif pokemon==2:
    print(f"Elegiste {pk2} asi que tu rival sera {pk3}")
    print(f"Tus ataques seran {bt1},{bt2},{bt3} y {bt4}")  
    def eleccion_ataques():
        ataques_usuario=(f"{bt1}", f"{bt2}",f"{bt3}",f"{bt4}")
        ataques_usuario=input(f"Elige el ataque de {pk2},{bt1},{bt2},{bt3},{bt4}--> ")
        ataques_usuario=ataques_usuario.lower()
        ataque_rival=(f"{ct1}",f"{ct2}",f"{ct3}",f"{ct4}")
        ataques_computador=random.choice(ataque_rival)
        print(f'{pk2} uso',ataques_usuario)
        print(f"{pk3} uso", ataques_computador)
        return ataques_computador, ataques_usuario
    def juego(ataques_usuario, ataques_computador, pokemonusuario_gano, pokemonrival_gano ):
        if ataques_usuario ==ataques_computador:
            print("No se hicieron daño")
        elif ataques_usuario==f"{bt1}":
            if ataques_computador==f"{ct4}":
                print(f"{pk2} ha hecho daño a {pk3}")
                print(f"Mientras que {pk2} solo pudo bajarle las defensas")
                pokemonusuario_gano+=1
            else:
                print(f"{pk2} no pudo completar su ataque")
                print(f"{pk3}  manda un feroz ataque de {ct1} a {pk2}")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{bt2}":
            if ataques_computador==f"{ct1}":
                print(f"{pk2} ataco con {bt2} y deja a su rival herido")
                print(f"{pk3} va a tratar de devolverle con un ataque {ct1} pero queda confundido y se ataca asi mismo")
                pokemonusuario_gano+=1
            else:
                print(f"El ataque de {pk2} no pudo ser concretado por que el {ct3} de {pk3} estuvo fuerte")
                print(f"{pk3} en este momento tiene la ventaja")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{bt3}":
            if ataques_computador==f"{ct2}":
                print(f"{pk2} ataco con {bt3} fue un ataque eficaz")
                print(f"{pk3} no pudo mandar{ct2} por que el ataque de {pk2} fue rapido")
                pokemonusuario_gano+=1
            else:
                print(f"El ataque de {pk2} no pudo ser concretado por que el {ct2} de {pk3} estuvo fuerte")
                print(f"{pk3} en este momento tiene la ventaja")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{bt4}":
            if ataques_computador==f"{ct3}":
                print(f"{pk2} dio un {bt4} fue un ataque eficaz")
                print(f"{pk3} no pudo mandar{ct3} por que el ataque de {pk2} fue rapido")
            else:
                print(f"El ataque de {pk2} no pudo ser concretado por que el {ct3} de {pk3} estuvo fuerte")
                print(f"{pk3} en este momento tiene la ventaja")
        return ataques_usuario, ataques_computador 
    def empezar_pelea():
            pokemonusuario_gano=0
            pokemonrival_gano=0
            rounds = 1
            while True:
                print('*'*10)
                print("Ronda", rounds)
                print("*" * 10)
        
                print(f"{pk2} uso ", pokemonusuario_gano)
                print(f"{pk3} uso ", pokemonrival_gano)
                rounds+=1
        
                ataques_usuario, ataques_computador = eleccion_ataques()
                pokemonusuario_gano, pokemonrival_gano=juego(ataques_usuario, ataques_computador, pokemonusuario_gano, pokemonrival_gano )
        
                if pokemonrival_gano ==5:
                    print(f"El ganador es{pk3}")
                    break
                               
                if pokemonusuario_gano==5:
                    print(f"El ganador es {pk2}")
                    break
    empezar_pelea()    
elif pokemon==3:
    print(f"Elegiste {pk3} asi que tu rival sera {pk1}")
    print(f"Tus ataques seran {ct1},{ct2},{ct3} y {ct4}")  
    def eleccion_ataques():
        ataques_usuario=(f"{ct1}", f"{ct2}",f"{ct3}",f"{ct4} ")
        ataques_usuario=input(f"Elige el ataque de {pk3},{ct1},{ct2},{ct3},{ct4}--> ")
        ataques_usuario=ataques_usuario.lower()
        ataque_rival=(f"{at1}",f"{at2}",f"{at3}",f"{at4}")
        ataques_computador=random.choice(ataque_rival)
        print(f'{pk3} uso',ataques_usuario)
        print(f"{pk1} uso", ataques_computador)
        return ataques_computador, ataques_usuario
    def juego(ataques_usuario, ataques_computador, pokemonusuario_gano, pokemonrival_gano ):
        if ataques_usuario ==ataques_computador:
            print("No se hicieron daño")
        elif ataques_usuario==f"{ct1}":
            if ataques_computador==f"{at4}":
                print(f"{pk3} ha hecho daño a {pk1}")
                print(f"Mientras que {pk1} solo pudo bajarle las denfensas")
                pokemonusuario_gano+=1
            else:
                print(f"{pk3} no pudo completar su ataque")
                print(f"{pk1} manda un feroz ataque de {at1} a {pk3}")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{ct2}":
            if ataques_computador==f"{bt1}":
                print(f"{pk3} ataco con {ct2} y deja a su rival herido")
                print(f"{pk1} va a tratar de devolverle con un ataque {at1} pero queda confundido y se ataca asi mismo")
                pokemonusuario_gano+=1
            else:
                print(f"El ataque de {pk3} no pudo ser concretado por que el {at3} de {pk1} estuvo fuerte")
                print(f"{pk1} en este momento tiene la ventaja")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{ct3}":
            if ataques_computador==f"{at2}":
                print(f"{pk3} ataco con {ct3} fue un ataque eficaz")
                print(f"{pk1} no pudo mandar{at2} por que el ataque de {pk3} fue rapido")
                pokemonusuario_gano+=1
            else:
                print(f"El ataque de {pk3} no pudo ser concretado por que el {at2} de {pk1} estuvo fuerte")
                print(f"{pk1} en este momento tiene la ventaja")
                pokemonrival_gano+=1
        elif ataques_usuario==f"{ct4}":
            if ataques_computador==f"{at3}":
                print(f"{pk3} dio un {ct4} fue un ataque eficaz")
                print(f"{pk1} no pudo mandar{at3} por que el ataque de {pk3} fue rapido")
            else:
                print(f"El ataque de {pk3} no pudo ser concretado por que el {at3} de {pk1} estuvo fuerte")
                print(f"{pk1} en este momento tiene la ventaja")
        return ataques_usuario, ataques_computador 
    def empezar_pelea():
            pokemonusuario_gano=0
            pokemonrival_gano=0
            rounds = 1
            while True:
                print('*'*10)
                print("Ronda", rounds)
                print("*" * 10)
        
                print(f"{pk3} uso ", pokemonusuario_gano)
                print(f"{pk1} uso ", pokemonrival_gano)
                rounds+=1
        
                ataques_usuario, ataques_computador = eleccion_ataques()
                pokemonusuario_gano, pokemonrival_gano=juego(ataques_usuario, ataques_computador, pokemonusuario_gano, pokemonrival_gano )
        
                if pokemonrival_gano ==5:
                    print(f"El ganador es{pk1}")
                    break
                               
                if pokemonusuario_gano==5:
                    print(f"El ganador es {pk3}")
                    break
    empezar_pelea()    
else:
    print("No es valido su numero porfavor reinicie el programa")