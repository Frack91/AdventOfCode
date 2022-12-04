with open("input.txt", "rt") as stream:
	data = stream.read().split("\n")

data.pop(-1)

cont = 0
cont2 = 0

for item in range(len(data)):
	data[item] = data[item].split(",")
	data[item][0] = data[item][0].split("-")
	data[item][1] = data[item][1].split("-")
	data[item][0][0] = int(data[item][0][0])
	data[item][0][1] = int(data[item][0][1])
	data[item][1][0] = int(data[item][1][0])
	data[item][1][1] = int(data[item][1][1])

for item in range(len(data)):
	no_00 = data[item][0][0]
	no_01 = data[item][0][1]
	no_10 = data[item][1][0]
	no_11 = data[item][1][1]

	l0 = list(range(no_00, no_01 + 1))
	l1 = list(range(no_10, no_11 + 1))

	if l0[0] in l1 and l0[-1] in l1 \
	or l1[0] in l0 and l1[-1] in l0:
		cont += 1

	l0 = set(l0)
	l1 = set(l1)

	if len(l0.difference(l1)) != len(l0):
		cont2 += 1

print(cont)
print(cont2)
