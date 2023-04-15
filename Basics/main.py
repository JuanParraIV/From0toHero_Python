import random


def play_round(options):
    user_choice = get_user_choice(options)
    computer_choice = random.choice(options)
    print(f"\nTu elección: {user_choice}")
    print(f"Elección del oponente: {computer_choice}")
    return determine_winner(user_choice, computer_choice)


def get_user_choice(options):
    while True:
        user_choice = input(f"\nElige una opción ({', '.join(options)}) ").lower()
        if user_choice in options:
            return user_choice
        else:
            print("Opción no válida, por favor inténtalo de nuevo.")


def determine_winner(user_choice, computer_choice):
    results = {
        "piedra": {"tijera": "ganaste", "papel": "perdiste", "piedra": "empate"},
        "papel": {"piedra": "ganaste", "tijera": "perdiste", "papel": "empate"},
        "tijera": {"papel": "ganaste", "piedra": "perdiste", "tijera": "empate"},
    }
    outcome = results[user_choice][computer_choice]
    return outcome


def play_game():
    # Juegos por round gana el que tenga 2/3 victorias
    options = ("piedra", "papel", "tijera")
    user_wins = 0
    computer_wins = 0
    draw = 0

    while True:
        print("\n--- Nuevo round ---")
        outcome = play_round(options)
        if outcome == "ganaste":
            user_wins += 1
        elif outcome == "perdiste":
            computer_wins += 1
        else:
            draw += 1

        print(f"\nResultado del round: {outcome}")
        print(f"Puntuación actual: Usuario {user_wins} - Oponente {computer_wins}")

        if user_wins == 2 or computer_wins == 2:
            break

    print("\n--- Juego terminado ---")
    print(f"Puntuación final: Usuario {user_wins} - Oponente {computer_wins} - Empates {draw}")

    if user_wins > computer_wins:
        print("¡Felicidades, ganaste el juego!")
    elif user_wins < computer_wins:
        print("Lo siento, perdiste el juego.")
    else:
        print("El juego terminó en empate.")


if __name__ == "__main__":
    play_game()