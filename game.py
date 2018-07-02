#!/usr/bin/python3

from random import choice
from time import sleep

f_poke = {
	'name': 'Pikachu',
	'health': 120,
	'damage': 40,
	'agility': 20,
}

s_poke = {
	'name': 'Totodile',
	'health': 100,
	'damage': 49,
	'agility': 20,
}

pokes = list()

if f_poke['agility'] > s_poke['agility']:
	pokes.append(f_poke)
	pokes.append(s_poke)

elif s_poke['agility'] > f_poke['agility']:
	pokes.append(s_poke)
	pokes.append(f_poke)

else:
	_pokes = [ f_poke, s_poke, ]
	_poke_index = choice(range(2))

	pokes.append(_pokes[_poke_index])

	del _pokes[_poke_index]

	pokes.append(_pokes[0])

	del _pokes


attack_index = 0
defense_index = 1

loop = 0
max_loop = 1000

lost_health_format = '{name} lost {lost_health} health points.'.format
turn_health_show_format = '{name} health: {health} points.'.format

print(turn_health_show_format(
	name=pokes[0]['name'],
	health=pokes[0]['health'],
))

print(turn_health_show_format(
	name=pokes[1]['name'],
	health=pokes[1]['health'],
))

while (pokes[0]['health'] > 0 and pokes[1]['health'] > 0) or loop >= max_loop:
	sleep(2)
	pokes[defense_index]['health'] -= pokes[attack_index]['damage']

	print(lost_health_format(
		name=pokes[defense_index]['name'],
		lost_health=pokes[attack_index]['damage']
	))

	print(turn_health_show_format(
		name=pokes[0]['name'],
		health=pokes[0]['health'],
	))

	print(turn_health_show_format(
		name=pokes[1]['name'],
		health=pokes[1]['health'],
	))

	if attack_index:
		attack_index = 0
		defense_index = 1

	else:
		attack_index = 1
		defense_index = 0

	loop += 1

winner_format = '{name} is the winner!!!'.format

if f_poke['health'] > 0:
	print(winner_format(name=f_poke['name']))

elif s_poke['health'] > 0:
	print(winner_format(name=s_poke['name']))