import random
r = random.randint(1,100)
while True:
	num = input('Input a number from 1~100 to see how fast you make it to a correct guess: ')
	num = int(num)
	if num == r:
		print('Bingo!')
		break
	elif num > r:
		print('It`s bigger than the answer, take another try.')
	elif num < r:
		print('It`s smaller than the answer, take another try.')