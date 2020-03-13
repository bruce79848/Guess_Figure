import random
r = random.randint(1,100)
t = 0
while True:
	num = input('Input a number from 1~100 to see how fast you make it to a correct guess: ')
	num = int(num)
	t = t + 1
	if num == r:
		print('Bingo!')
		print('You`ve taken', t , 'guess(es).')
		break
	elif num > r:
		print('Too big!')
	elif num < r:
		print('Too small!')
	print('You`ve taken', t , 'guess(es).')