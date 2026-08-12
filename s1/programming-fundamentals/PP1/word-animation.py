from time import sleep
from string import ascii_lowercase, ascii_uppercase


target_phrase = input()


current = ""
letters = " "+ascii_lowercase+ascii_uppercase

last_animating_position = 0
while current != target_phrase:
    if len(current) <= last_animating_position:
        current = current + letters[0]
        continue
    if current[last_animating_position] == target_phrase[last_animating_position]:
        last_animating_position += 1
        continue
    current = target_phrase[0:last_animating_position] + \
        letters[letters.index(current[last_animating_position]) + 1]
    sleep(0.05)
    print(current)
