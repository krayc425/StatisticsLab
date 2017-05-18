#-*- coding:utf-8 -*-
'''
print api example: print('output is: ' + str(output))
'''
import random
# from print_api import print

'''
n: the total number of games to win
n1: the number of games player1 won
n2: the number of games player2 won
'''
def Bookie1(n, n1, n2):
	for i in range(2*n-n1-n2-1):#the number of games needed to end
		D = random.randint(1,2)
		if D==1:
			n1+=1
		elif D==2:
			n2+=1
		if n1==n:#player1 wins
			return 1
		if n2==n:#player2 wins
			return 2

def Bookie2(n, n1, n2, n3, n4, n5):
	#you can write your code here
	pass

def simulate1():
	n = 10000
	win1 = 0
	win2 = 0
	for i in range(n):#simulate 10000 games
		#simulate game whose total number is 10, and player1 won 5, player2 won 2
		result = Bookie1(10,5,2)
		if result==1:
			win1+=1
		elif result==2:
			win2+=1
	print('player1 wins: ' + str(float(win1)/float(n)))
	print('player2 wins: ' + str(float(win2)/float(n)))
	# log('player1 wins: ' + str(float(win1)/float(n)))
	# log('player2 wins: ' + str(float(win2)/float(n)))

def simulate2():
	n = 10000
	win1 = 0
	win2 = 0
	win3 = 0
	win4 = 0
	win5 = 0
	for i in range(n):#simulate 10000 games
		#simulate game whose total number is 10, and player1 and player3 won 1
		result = Bookie2(10,1,0,1,0,0)
		if result==1:
			win1+=1
		elif result==2:
			win2+=1
		elif result==3:
			win3+=1
		elif result==4:
			win4+=1
		elif result==5:
			win5+=1
	print('player1 wins: ' + str(float(win1)/float(n)))
	print('player2 wins: ' + str(float(win2)/float(n)))
	print('player3 wins: ' + str(float(win3)/float(n)))
	print('player4 wins: ' + str(float(win4)/float(n)))
	print('player5 wins: ' + str(float(win5)/float(n)))

	# log('player1 wins: ' + str(float(win1)/float(n)))
	# log('player2 wins: ' + str(float(win2)/float(n)))
	# log('player3 wins: ' + str(float(win3)/float(n)))
	# log('player4 wins: ' + str(float(win4)/float(n)))
	# log('player5 wins: ' + str(float(win5)/float(n)))

if __name__ == '__main__':
	simulate1()
	#simulate2()