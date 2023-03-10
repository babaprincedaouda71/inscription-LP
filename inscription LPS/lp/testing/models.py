from django.db import models


class Cars(models.Model):
    nom = models.CharField(max_length = 100)

    def __str__(self):
        return self.nom


class Models(models.Model):
    nom = models.CharField(max_length = 100)
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom



class Sell(models.Model):
    num = models.CharField(max_length = 100)
    nom = models.CharField(max_length = 100)
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    model = models.ForeignKey(Models, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom