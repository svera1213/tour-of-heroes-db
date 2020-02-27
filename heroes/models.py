from django.db import models

class HeroType(models.Model):
    role = models.CharField(max_length=30)
    specialty = models.CharField(max_length=30)

    def __str__(self):
        return self.role

    def lore(self):
        return "The {} type is recognised for its <{}>".format(self.role, self.specialty)

class Hero(models.Model):
    type = models.ForeignKey(HeroType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    ultiAttack = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def addVote(self):
        self.votes += 1
