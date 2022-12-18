from django.db import models


class Trener(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=40)
    datum_narozeni = models.DateField()

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Hala(models.Model):
    nazev = models.CharField(max_length=100)
    kapacita = models.IntegerField()
    adresa = models.ForeignKey('Adresa',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazev}, {self.adresa}'


class Adresa(models.Model):
    mesto = models.CharField(max_length=50)
    smerovaci_cislo = models.IntegerField()
    ulice = models.CharField(max_length=50)
    cislo_popisne = models.IntegerField()

    def __str__(self):
        return f'{self.ulice} {self.cislo_popisne}, {self.mesto} {self.smerovaci_cislo}'


class Klub(models.Model):
    nazev = models.CharField(max_length=100)
    trener = models.ForeignKey('Trener',on_delete=models.CASCADE)
    hala = models.ForeignKey('Hala',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazev}'


class Hrac(models.Model):
    klub = models.ForeignKey('Klub',on_delete=models.CASCADE)
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=40)
    datum_narozeni = models.DateField()
    pozice = models.CharField(max_length=50)
    vyska = models.IntegerField()

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Zapas(models.Model):
    kolo = models.IntegerField()
    domaci = models.ForeignKey('Klub',on_delete=models.CASCADE,related_name='domaci')
    hoste = models.ForeignKey('Klub',on_delete=models.CASCADE,related_name='hoste')
    domaci_sety = models.IntegerField()
    hoste_sety = models.IntegerField()
    datum_zapasu = models.DateTimeField()


class Tabulka(models.Model):
    klub = models.ForeignKey('Klub',on_delete=models.CASCADE)
    zapasy_celkem = models.IntegerField()
    vyhry = models.IntegerField()
    prohry = models.IntegerField()
    vyhrane_sety = models.IntegerField()
    prohrane_sety = models.IntegerField()
    body = models.IntegerField()

