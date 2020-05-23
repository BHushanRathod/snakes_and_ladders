import random
import sys

MAX_VAL = 100
DICE_FACE = 6

snakes_val = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

ladder_val = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,
    71: 81
}


def dice_role():
    dice_value = random.randint(1, DICE_FACE)
    print("Dice Roled: ", dice_value)
    return dice_value


def snake_bite(current_value, old_value, player):
    stmt = "{} bitten by SNAKE. From {} position DOWN to {} position".format(player, current_value, old_value)
    print(stmt)


def ladder_up(current_value, old_value, player):
    stmt = "{} got ladder. From {} position UP to {} position".format(player, current_value, old_value)
    print(stmt)


def is_won(player, position):
    if position == MAX_VAL:
        print("{} WON the game".format(player))
        sys.exit(1)


def main_game(player, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("PASS")

    if current_value in snakes_val:
        final_value = snakes_val.get(current_value)
        snake_bite(current_value, final_value, player)

    elif current_value in ladder_val:
        final_value = ladder_val.get(current_value)
        ladder_up(current_value, final_value, player)

    else:
        final_value = current_value

    return final_value


def player_names():
    player1 = input("Enter Player one name: ")
    player2 = input("Enter Player two name: ")
    return player1, player2


def main_start():
    player1, player2 = player_names()

    player1_current_pos = 0
    player2_current_pos = 0

    while True:
        print("------------------")
        print("{} at position {}".format(player1, player1_current_pos))
        print("{} at position {}".format(player2, player2_current_pos))
        print("------------------")
        val1 = input("{} your turn, press a key".format(player1))
        print("{} Rolling Dice".format(player1))
        dice_value = dice_role()
        print("{} moving from {}".format(player1, player1_current_pos))
        player1_current_pos = main_game(player1, player1_current_pos, dice_value)
        print("{} moved to {}".format(player1, player1_current_pos))
        is_won(player1, player1_current_pos)

        print("------------------")
        val2 = input("{} you turn, press a key ".format(player2))
        print("{} Rolling Dice".format(player2))
        dice_value = dice_role()
        print("{} moving from {}".format(player2, player2_current_pos))
        player2_current_pos = main_game(player2, player2_current_pos, dice_value)
        print("{} moved to {}".format(player2, player2_current_pos))
        is_won(player2, player2_current_pos)


if __name__ == "__main__":
    main_start()
