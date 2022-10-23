import random

#--------------Funciones------------------------------
def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
      print('🚨 Esa opcion No Es valida 🚨')
      #continue
      return None, None


    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('🪨 piedra gana a tijera ✂️')
            print('🙋user gano!🎖️')
            user_wins += 1
        else:
            print('📄 Papel gana a piedra 🪨')
            print('🤖computer gano!🎖️')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('📄 papel gana a piedra 🪨')
            print('🙋user gano!🎖️')
            user_wins += 1
        else:
            print('✂️ tijera gana a papel 📄')
            print('🤖computer gano!🎖️')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('✂️ tijera gana a papel 📄')
            print('🙋user gano!🎖️')
            user_wins += 1
        else:
            print('🪨 piedra gana a tijera ✂️')
            print('🤖computer gano!🎖️')
            computer_wins += 1
    return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
    
    print(f'''
    🤖 Computer wins: {computer_wins}
    🙋 User wins: {user_wins}
            ''')
    
    if user_wins == 3:
        print('🎖️El ganador es User🎖️')
        exit()
        
    if computer_wins == 3:
        print('🎖️El ganador es Computer🎖️')
        exit()

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        rounds += 1

        user_options, computer_options= choose_options()
        user_wins, computer_wins =check_rules(user_options, computer_options, user_wins, computer_wins)
        check_winner(user_wins, computer_wins) 

#------------------Ejecución del juego --------------------        
print("""
      [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
                  >>> Ingresa una opción <<<
      """)

run_game()