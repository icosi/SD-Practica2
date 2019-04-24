# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Restaurant(models.Model):
    CATEGORIES = (
        ("Rice", "Rice"),
        ("Fusi", "Fusion"),
        ("BBQ", "Barbecue"),
        ("Chin", "Chinese"),
        ("Medi","Mediterranean"),
        ("Crep","Creperie"),
        ("Hind","Hindu"),
        ("Japa","Japanese"),
        ("Ital","Italian"),
        ("Mexi","Mexican"),
        ("Peru", "Peruvian"),
        ("Russ","Russian"),
        ("Turk","Turkish"),
        ("Basq","Basque"),
        ("Vegy", "Vegetarian"),
        ("Afri","African"),
        ("Egyp","Egyptian"),
        ("Grek","Greek")
    )
    _d_categories = dict(CATEGORIES)

restaurant_number = models.CharField(max_length=8, unique=True)
name = models.CharField(max_length=50)
menu_description = models.TextField()
price_average = models.DecimalField(max_digits=5, decimal_places=2)
is_promot = models.BooleanField()
rate = models.DecimalField(max_digits=3, decimal_places=1)
address = models.CharField(max_length=50)
city = models.CharField(max_length=50)
country = models.CharField(max_length=50)
featured_photo = models.ImageField()
category = models.CharField(max_length=5, choices=CATEGORIES)
capacity = models.PositiveIntegerField()

def get_human_category(self):
    return self._d_categories[self.category]

def __str__(self):
    return ('[**Promoted**]' if self.is_promot else '') + "[" + self.category + "] " \
                                                                                "[" + self.restaurant_number + "] " + self.name + " - " + self.menu_description + " (" + str(self.rate) + ")" \
                                                                                                                                                                                          ": " + str(self.price_average) + u" €"
