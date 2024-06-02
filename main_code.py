from objects import SnakesAndLadders

game = SnakesAndLadders('Steven', 'Joseph', 'Mary')
while True:
    game.new_game()
    if game.play_again():
        break

print('------------------------------')
print('Okay, thanks for playing!')
