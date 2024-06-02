import random
import itertools

class SnakesAndLadders:

    snakes = [[32, 10], [36, 6], [48, 26], [63, 18], [88, 24], [95, 56], [97, 78]]
    ladders = [[4, 14], [8, 30], [21, 42], [28, 76], [50, 67], [71, 92], [80, 99]]

    def __init__(self, *args):
        self.players_spaces = {}
        for key in args:
            self.players_spaces[key] = 0
        self.player_order = self.create_player_order(self.players_spaces)

    def reset(self):
        for key in self.players_spaces:
            self.players_spaces[key] = 0

    def print_player_order(self):
        print('Player order: {}'.format(', '.join(self.player_order)))


    def create_player_order(self, players):
        self.list_of_players = []

        for player in players:
            x = (player, random.randint(1, 100))
            self.list_of_players.append(x)

        self.list_of_players = sorted(self.list_of_players, key=lambda x: x[1], reverse=True)
        self.list_of_players = list(map(lambda y: y[0], self.list_of_players))
        return self.list_of_players


    def roll_a_dice(self, player):
        spaces_moved = None
        while spaces_moved not in [1, 2, 3, 4, 5, 6]:
            spaces_moved = int(input('Roll a dice: '))

        print('------------------------------')
        self.players_spaces[player] += spaces_moved
        x = '{} has just moved {} space(s), and is now on square {}!'

        print(x.format(player, spaces_moved, self.players_spaces[player]))
        self.check_snakes_or_ladders(player)


    def check_snakes_or_ladders(self, player):
        for snake, destination in self.snakes:
            if self.players_spaces[player] == snake:
                msg = 'Oh no, you landed on a snake. The snake sends you back to square {}.'

                self.players_spaces[player] = destination
                print(msg.format(destination))

        for ladder, destination in self.ladders:
            if self.players_spaces[player] == ladder:
                msg = 'Nice job, you landed on a ladder. The ladder sends you to square {}.'

                self.players_spaces[player] = destination
                print(msg.format(destination))


    def check_for_end(self, player):
        if self.players_spaces[player] == 100:
            print('Congratulations, {}! You have just won the game!'.format(player))
            return True
        elif self.players_spaces[player] > 100:
            msg = 'Whoops, {} went too far and has to move {} space(s) back to square {}.'

            excess_spaces = self.players_spaces[player] - 100
            self.players_spaces[player] = 100 - excess_spaces
            print(msg.format(player, excess_spaces, self.players_spaces[player]))
            return False
        else:
            pass


    def play_again(self):
        print('------------------------------')
        if answer := input('Would you like to play again? (yes/no) ').lower() != 'yes':
            return True


    def new_game(self):
        self.reset()
        self.print_player_order()
        for current_player in itertools.cycle(self.player_order):
            print('------------------------------')
            print("{}'s turn:".format(current_player))

            self.roll_a_dice(current_player)
            if self.check_for_end(current_player):
                break




