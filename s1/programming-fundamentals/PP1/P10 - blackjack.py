def remove_prefix(card: str):
    return card[1]


cards_for_dealer = map(remove_prefix, input().split(" "))
cards_for_player = map(remove_prefix, input().split(" "))


def points_for_card(card: str):
    if len(card) != 1:
        return 0
    value = card[0]
    if value.isdigit():
        return int(value)
    if value == "J" or value == "Q" or value == "K":
        return 10
    if value == "A":
        return 11
    return 0


score_for_dealer = sum(map(points_for_card, cards_for_dealer))
print(score_for_dealer)

score_for_player = sum(map(points_for_card, cards_for_player))
print(score_for_player)

if score_for_dealer > 21 and "A" in cards_for_dealer:
    score_for_dealer -= 10

if score_for_player > 21 and "A" in cards_for_player:
    score_for_player -= 10

if score_for_dealer == 21 or (score_for_dealer <= 21 and score_for_player < score_for_dealer):
    print("Lost")
    exit()
if score_for_player == 21 or (score_for_player <= 21 and score_for_player > score_for_dealer):
    print("Won")
    exit()

print("Hit")
