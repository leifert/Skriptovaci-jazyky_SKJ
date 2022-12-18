from django import forms
from volejbal.models import Klub, Tabulka, Trener, Hala, Hrac, Zapas, Adresa

INTEGER_CHOICES = [tuple([x,x]) for x in range(1,4)]


class KoloSearchForm(forms.Form):
    kolo = forms.IntegerField(label="Kolo:", widget=forms.Select(choices=INTEGER_CHOICES,attrs={'style':'width:40px'}))


class KlubForm(forms.ModelForm):
    class Meta:
        model = Klub
        exclude = []


class KlubFormAdd(forms.ModelForm):
    class Meta:
        model = Klub
        exclude = []


class HracForm(forms.ModelForm):
    class Meta:
        model = Hrac
        exclude = []


class TrenerForm(forms.ModelForm):
    class Meta:
        model = Trener
        exclude = []


class ZapasForm(forms.ModelForm):
    class Meta:
        model = Zapas
        exclude = []


class HalaForm(forms.ModelForm):
    class Meta:
        model = Hala
        exclude = []


class AdresaForm(forms.ModelForm):
    class Meta:
        model = Adresa
        exclude = []

