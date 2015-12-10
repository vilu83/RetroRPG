#RPG

import os *
import sys, socket
import random as rd
import multiprocessing as mp
import classes *
import combat

if sys.platform == 'linux2':
	clear = lambda: os.system('clear')
else:
	clear = lambda: os.system('cls')

print '\t\t RETRO RPG \n'
prompt1 = raw_input('Are you starting anew?(Y/N)')
if prompt1 == Y:
	pl1 = character()
	print 'Excellent, so tell me '

print "Please be welcome to Alarduin\nIt's a world full of adventure and fries"
play = raw_input('Are you new here? (Y/N)')
if play == Y:
	pl1 = character()
	datos = raw_input('ingrese el nombre de su personaje: ')
	psw = raw_input('ingrese la clave de su personaje: ')
	data_pl = open(datos+'.data', 'r')
	for

questions = {a = 'You and your party are ambushed!\nWhat do you do?\n\na) Fight back\nb)give my comrades time to flee\nc)escape leaving your party\nd)that will never happen to me',
b= 'What is your goal on this journey?\na)to be the most powerful adventurer\nb)Help restoring humanity\nc)dunno, adventure\nd)to find stange and mysterious loot',
c = 'A friend got poisoned!\nWhat do you do?\na)Search for herbs nearby\nb)carry him to him to the closest settlement\nc)Spare him some potions\nd)Cut the affected limb',
d = 'You witness a robbery and you are unarmed, you:\na)Face the robber\nb)I would never be unarmed\nc)Steal from the robber\nd)Alert the authorities',
e = 'You are at the brinck of death against a powerful foe, you:\na)In the killing blow we trust!\nb)Flee\nc)Hide, recover and strike back\nd)Pretend to be a rock', 
f = 'If you could not be an adventurer. What would you do for a living\na)A mercenary\nb)A Guardsmen\nc)a treasure hunter\nd)a ourier', 
g = 'Which tine is the best time to travel?\na)Daytime\nb)Dusk\nc)Nighttime\nd)dawn',
h = 'Which describes you better?\na)Brave\nb)Very loyal\nc)Impulsive\nd)a curious wanderer',
i = 'Which kind of weapon do you prefer?\na)Warhammer\nb)Dagger\nc)Crossbow\nd)Sword and shield',
j = 'Your foe begs for mercy, you:\na)Kill it\nb)Sapre its life\nc)robb him and let it go\nd)Imprison it'
