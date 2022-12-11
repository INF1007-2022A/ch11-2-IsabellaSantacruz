"""
Chapitre 11.3

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import *


# TODO: Créer la classe Spell qui a les même propriétés que Weapon, mais avec un coût en MP pour l'utiliser
class Spell(Weapon):
	"""
	Un sort dans le jeu.

	:param name: Le nom du sort
	:param power: Le niveau d'attaque
	:param mp_cost: Le coût en MP d'utilisation du sort
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	# TODO: __init__
	def __init__(self, name, power, min_level, mp_cost):
		super().__init__(name, power, min_level)
		self.mp_cost = mp_cost

# TODO: Déclarer la classe Magician qui étend la classe Character
class Magician(Character):
	"""
	Un utilisateur de magie dans le jeu. Un magicien peut utiliser des sorts, mais peut aussi utiliser des armes physiques. Sa capacité à utiliser des sorts dépend 

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param max_mp: MP maximum
	:param attack: Le niveau d'attaque physique du personnage
	:param magic_attack: Le niveau d'attaque magique du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage

	:ivar using_magic: Détermine si le magicien tente d'utiliser sa magie dans un combat.
	"""
	def __init__(self, name, max_hp, attack, defense, level, max_mp, magic_attack):
		# TODO: Initialiser les attributs de Character
		# TODO: Initialiser le `magic_attack` avec le paramètre, le `max_mp` et `mp` de la même façon que `max_hp` et `hp`, `spell` à None et `using_magic` à False.
		super().__init__(name, max_hp, attack, defense, level)
		self.magic_attack = magic_attack
		self.max_mp = max_mp
		self.mp = max_mp
		self.spell = None
		self.using_magic = False


	@property
	def mp(self):
		pass

	@mp.setter
	def mp(self, val):
		pass

	# TODO: Écrire les getter/setter pour la propriété `spell`.
	#       On peut affecter None.
	#       Si le niveau minimal d'un sort est supérieur au niveau du personnage, on lève ValueError.
	@property
	def spell(self):
		return self.__spell
	
	@spell.setter
	def spell(self,val):
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.__spell = val

	# TODO: Surcharger la méthode `compute_damage` 
	def compute_damage(self, other):
		# Si le magicien va utiliser sa magie (`will_use_spell()`):
			# Soustraire à son MP le coût du sort
			# Retourner le résultat du calcul de dégâts magiques
		if self.will_use_spell():
			self.mp -= self.spell.mp_cost
			numerateur = (2*(self.level+self.magic_attack)/5 + 2)*self.spell.power
			crit = 1
			if random.randrange(8)==0:
				crit = 2
			modifier = crit*random.randrange(85,101)/100
			dmg = (numerateur/50 + 2)*modifier
			return dmg
		# Sinon
			# Retourner le résultat du calcul de dégâts physiques
		else:
			dmg, crit = super().compute_damage()
			return dmg

	def will_use_spell(self):
		if self.using_magic and self.spell is not None:
			return True
		return False

	def _compute_magical_damage(self, other):
		pass

	def _compute_physical_damage(self, other):
		# TODO: Calculer le dommage physique exactement de la même façon que dans `Character`
		pass

