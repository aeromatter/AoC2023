def part1():
	bounds = {'red': 12, 'green': 13, 'blue': 14}
	possible_games = [x for x in range(101)]
	impossible_games = []
	with open("input.txt", "r") as f:
		for line in f:
			ID = int(line.split(": ")[0].split(" ")[1])
			games = line.split(": ")[1].split("; ")
			for game in games:
				counts = game.split(",")
				for count in counts:
					count = count.split()
					if int(count[0]) > bounds[count[1]]:
						impossible_games.append(ID)

	possible_games = [x for x in possible_games if not x in impossible_games]
	print(sum(possible_games))

def part2():
	powers = []
	with open("part2.txt", "r") as f:
		for line in f:
			min_totals = {'red': 0, 'green': 0, 'blue': 0}
			games = line.split(": ")[1].split("; ")
			for game in games:
				counts = game.split(",")
				for count in counts:
					count = count.split()
					if int(count[0]) > min_totals[count[1]]:
						min_totals[count[1]] = int(count[0])
			powers.append(min_totals['red'] * min_totals['green'] * min_totals['blue'])
	print(sum(powers))

part1()
