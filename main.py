import random

mapOptionName = {'0':'Piedra','1':'Papel','2':'Tijera'}
mapNameGamer = {'1':'Usuario','2':'Computadora'}
listValueInput = [0,1,2]
round = 1
contador_intentos = {
    1:0,
    2:0
}

getNameOption = lambda option:mapOptionName[option]

def logicWin(user,computer):
    if user==computer:
        return 0
    elif user == 0:
        if computer == 1:
            return 2
        else:
            return 1
    elif user == 1:
        if computer == 2:
            return 2
        else:
            return 1
    elif user == 2:
        if computer == 0:
            return 2
        else:
            return 1

gamerName = lambda option:mapNameGamer[option]

def detectErrorInput(input):
    if input.isdigit():
        return not(int(input) in listValueInput)
    else:
        return True

print('*'*34)
print('*','¡GANA 3 VECES Y SERÁS CAMPEÓN!','*')

while True:
    print('*'*44)
    print('*','ROUND #',round,'|| USUARIO:',contador_intentos[1],'- COMPUTADORA:',contador_intentos[2],'*')
    print('*'*44)
    user_option = input('¿0: Piedra, 1: Papel o 2: Tijera? ')
    if detectErrorInput(user_option):
        print('Dato ingresado incorrecto')
    else:
        print(f'Has escogido {user_option} =>',getNameOption(user_option))
        #computer_option = random.randint(0,2)
        computer_option = random.choice(listValueInput)
        print(f'Computador escoge {computer_option} =>',getNameOption(str(computer_option)))
        win = logicWin(int(user_option),computer_option)
        if win > 0:
            contador_intentos[win] = contador_intentos[win] + 1
            print(f'Gana {gamerName(str(win))}')
        else:
            print('Hay empate')
        if 3 in list(contador_intentos.values()):
            print('*'*40)
            print('*','EL CAMPEÓN DEL JUEGO ES',gamerName(str(list(contador_intentos.values()).index(3)+1)).upper(),'*')
            print('*'*40)
            break
    round+=1