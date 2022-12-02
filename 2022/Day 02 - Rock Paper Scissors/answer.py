# points                  adv  you
# 1 for choosing rock     (A)  (X)
# 2 for choosing paper    (B)  (Y)
# 3 for choosing scissors (C)  (Z)
# 0 if the player lost
# 3 if it was a draw
# 6 if the player won

with open("input.txt", "rt") as stream:
	strategy_guide = stream.read().split("\n")

for match in range(len(strategy_guide)):
	if strategy_guide[match] == "":
		del strategy_guide[match]
		continue
	strategy_guide[match] = strategy_guide[match].split()


def calculate(data = strategy_guide):
	points = 0
	round_points = 0
	for item in data:
		round_points = 0
		if item[1] == "X":
			round_points += 1
		elif item[1] == "Y":
			round_points += 2
		elif item[1] == "Z":
			round_points += 3
		
		if item[0] == "A" and item[1] == "X" or \
		item[0] == "B" and item[1] == "Y" or \
		item[0] == "C" and item[1] == "Z":
			round_points += 3
		elif item[0] == "A" and item[1] == "Y" or \
		item[0] == "B" and item[1] == "Z" or \
		item[0] == "C" and item[1] == "X":
			round_points += 6


		points += round_points
	return points

print(calculate())

# Part two
for match in strategy_guide:
	if match[1] == "X":
		if match[0] == "A":
			match[1] = "Z"
		elif match[0] == "B":
			match[1] = "X"
		elif match[0] == "C":
			match[1] = "Y"

	elif match[1] == "Y":
		if match[0] == "A":
			match[1] = "X"
		if match[0] == "B":
			match[1] = "Y"
		if match[0] == "C":
			match[1] = "Z"

	elif match[1] == "Z":
		if match[0] == "A":
			match[1] = "Y"
		elif match[0] == "B":
			match[1] = "Z"
		elif match[0] == "C":
			match[1] = "X"

print(calculate())