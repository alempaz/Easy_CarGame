comenzar = 'Auto encendido... hora de partir!'
parar = 'Auto detenido.'
ayuda = ('''Comenzar - Para encender y acelerar el auto
Parar - Para parar el auto
Salir - Para salir del juego''')
respuesta = ''
comenzado = False

print('-'*15, 'Bienvenidos a Rapido y Furioso Bootleg ','-'*15)
print('Si deseas mas informacion, escribe "Ayuda".')

while True:
    respuesta = (input('> ')).lower()
    if respuesta == 'comenzar':
        if comenzado:
            print('El auto ya esta encendido!')
        else:
            comenzado = True
            print(comenzar)
    elif respuesta == 'parar':
        if not comenzado:
            print('El auto ya esta parado!')
        else:
            comenzado = False
            print(parar)
    elif respuesta == 'ayuda':
        print(ayuda)
    elif respuesta == 'salir':
        break
    else:
        print("No entiendo lo que me has dicho...")
exit()

# 1 hour 41 min