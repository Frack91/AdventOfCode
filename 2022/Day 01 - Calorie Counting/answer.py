with open("input.txt", "rt") as stream:
	data = stream.read().split("\n")

elf_id = 0
elves_calories = dict()

for line in data:

	if line == "":
		elf_id += 1
		continue

	if not elf_id in elves_calories.keys():
		elves_calories[elf_id] = 0

	elves_calories[elf_id] += int(line)

first_elf_cal = max(elves_calories.values())
print(first_elf_cal)

top_three_elves = sorted(elves_calories.values(), reverse=True)[0:3]
print(top_three_elves)

top_three_elves_cals = 0
for cal in top_three_elves:
	top_three_elves_cals += cal
print(top_three_elves_cals)