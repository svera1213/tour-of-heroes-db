from django.test import TestCase
from heroes.models import HeroType
from heroes.models import Hero

class HeroTypeTestCase(TestCase):
    def setUp(self):
        HeroType.objects.create(role="marksman", specialty="attack speed")
        HeroType.objects.create(role="tank", specialty="armor")

    def test_heroes_show_lore(self):
        """Animals that can speak are correctly identified"""
        marksman = HeroType.objects.get(role="marksman")
        tank = HeroType.objects.get(role="tank")
        self.assertEqual(marksman.lore(), 'The marksman type is recognised for its <attack speed>')
        self.assertEqual(tank.lore(), 'The tank type is recognised for its <armor>')

class HeroTestCase(TestCase):
    def setUp(self):
        heroType = HeroType.objects.create(role="marksman", specialty="attack speed")
        Hero.objects.create(type=heroType, name='Moskov', ultiAttack='Death Spear')

    def test_hero_get_ulti(self):
        hero = Hero.objects.get(name="Moskov")
        self.assertEqual(hero.ultiAttack, 'Death Spear')

    def test_hero_get_type(self):
        hero = Hero.objects.get(name="Moskov")
        self.assertEqual(hero.type.role, 'marksman')

    def test_hero_get_specialty(self):
        hero = Hero.objects.get(name="Moskov")
        self.assertEqual(hero.type.specialty, 'attack speed')

    def test_hero_get_votes(self):
        hero = Hero.objects.get(name="Moskov")
        self.assertEqual(hero.votes, 0)

    def test_hero_add_votes(self):
        hero = Hero.objects.get(name="Moskov")
        hero.addVote()  # +1 vote
        self.assertEqual(hero.votes, 0)
