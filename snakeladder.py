import random

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
    71: 91
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
        print("--------------")
        print(" ＼(＾O＾)／ ")
        print("{} WON the game".format(player))
        print(" ※ \(^o^)/ ※ ")
        print("--------------")
        exit(1)


def main_game(player, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value
    print("{} : Moving from {} ".format(player, old_value))
    if current_value > MAX_VAL:
        print("{} need {} to win. CANT MOVE.".format(player, (MAX_VAL - old_value)))
        return old_value

    if current_value in snakes_val:
        final_value = snakes_val.get(current_value)
        snake_bite(current_value, final_value, player)

    elif current_value in ladder_val:
        final_value = ladder_val.get(current_value)
        ladder_up(current_value, final_value, player)

    else:
        final_value = current_value

    print("{} : Moved to {}".format(player, final_value))
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
        input("{} press enter to play".format(player1))
        dice_value = dice_role()
        player1_current_pos = main_game(player1, player1_current_pos, dice_value)
        is_won(player1, player1_current_pos)

        input("{} press enter to play".format(player2))
        dice_value = dice_role()
        player2_current_pos = main_game(player2, player2_current_pos, dice_value)
        is_won(player2, player2_current_pos)

        print("------------------")
        print("{} at position {}".format(player1, player1_current_pos))
        print("{} at position {}".format(player2, player2_current_pos))
        print("------------------")


if __name__ == '__main__':
    main_start()
