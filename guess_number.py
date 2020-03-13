import random
m = input('Please input the minimum of the range you gotta guess: ')
m = int(m)
M = input('Please input the maximum of the range you gotta guess: ')
M = int(M)
r = random.randint(m,M)
t = 0
while True:
	num = input('Please input a number from the range above and see how fast you can guess correctly: ')
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