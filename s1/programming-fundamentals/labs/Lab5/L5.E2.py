nouns = ["I", "We"]
verbs = ["play", "watch"]

# we don't split the input into list right away
# because we first check if the input is not empty
games_input = input()

# exit early if the input is empty
if games_input == "":
    exit(0)

games = games_input.split(" ")

# output is grouped by nouns first
for noun in nouns:
    # then the game
    for verb in verbs:
        for game in games:
            if game == "":
                continue
            print(f'{noun} {verb} {game}.')
