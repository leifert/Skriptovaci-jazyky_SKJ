from django.http import Http404
from django.shortcuts import render, redirect
from volejbal.models import Klub, Tabulka, Trener, Hala, Hrac, Zapas, Adresa
from volejbal.forms import KlubForm, KlubFormAdd, HracForm, HalaForm, AdresaForm, TrenerForm, ZapasForm, KoloSearchForm


def main(request):
    try:
        t = Tabulka.objects.all().order_by('-body')
    except Tabulka.DoesNotExist:
        raise Http404("Tabulka does not exist")
    return render(request, 'main.html', {'tab': t})


def klub_info(request, klub_id):
    try:
        k = Klub.objects.get(id = klub_id)
    except Klub.DoesNotExist:
        raise Http404("Klub does not exist")
    return render(request, 'klub_info.html', {'klub': k})


def trener_info(request, trener_id):
    try:
        t = Trener.objects.get(id = trener_id)
    except Trener.DoesNotExist:
        raise Http404("Trener does not exist")
    return render(request, 'trener_info.html', {'trener': t})


def klub_hraci(request, klub_id):
    try:
        h = Hrac.objects.all().filter(klub_id=klub_id)
    except Hrac.DoesNotExist:
        raise Http404("Hrac does not exist")
    return render(request, 'klub_hraci.html', {'Hraci': h})


def seznam_hracu(request):
    try:
        h = Hrac.objects.all()
    except Hrac.DoesNotExist:
        raise Http404("Hrac does not exist")
    return render(request, 'seznam_hracu.html', {'Hraci': h})


def hrac_info(request, hrac_id):
    try:
        h = Hrac.objects.get(id = hrac_id)
    except Hrac.DoesNotExist:
        raise Http404("Hrac does not exist")
    return render(request, 'hrac_info.html', {'hrac': h})


def zapasy(request):
    if request.method == 'POST':
        form = KoloSearchForm(request.POST)
        if form.is_valid():
            kolo = form.cleaned_data['kolo']
            z = Zapas.objects.filter(kolo=kolo)
        else:
            z = Zapas.objects.all()
    else:
        form = KoloSearchForm({'kolo':0})
        z = Zapas.objects.all()
    return render(request, 'seznam_zapasu.html', {'zapasy': z, 'form': form})


def zapas_info(request, zapas_id):
    try:
        z = Zapas.objects.get(id = zapas_id)
    except Zapas.DoesNotExist:
        raise Http404("Zapas does not exist")
    return render(request, 'zapas_info.html', {'zapas': z})


def kluby(request):
    try:
        k = Klub.objects.all()
    except Klub.DoesNotExist:
        raise Http404("Klub does not exist")
    return render(request, 'seznam_klubu.html', {'kluby': k})


def klub_info2(request, klub_id):
    try:
        k = Klub.objects.get(id = klub_id)
    except Klub.DoesNotExist:
        raise Http404("Klub does not exist")
    return render(request, 'klub_info2.html', {'klub': k})




def klub_add(request):
    if request.method=='POST':
        form=KlubFormAdd(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('seznam_klubu')
    else:
        form=KlubFormAdd()
    return render(request,'klub_add.html',{'form':form})


def klub_delete(request, klub_id):
    try:
        k = Klub.objects.get(id = klub_id)
    except Klub.DoesNotExist:
        raise Http404("Klub does not exist")
    if request.method == 'POST':
        k.delete()
        return redirect('seznam_klubu')
    return render(request, 'klub_info2.html', {'klub': k})

def klub_edit(request, klub_id):
    try:
        k = Klub.objects.get(id = klub_id)
    except Klub.DoesNotExist:
        raise Http404("Klub does not exist")
    if request.method == 'POST':
        form = KlubForm(request.POST, instance=k)
        if form.is_valid():
            form.save()
            return render(request, 'klub_info2.html', {'klub': k})
    else:
        form = KlubForm(instance = k)
    return render(request, 'klub_edit.html', {'form': form})


def hrac_edit(request, hrac_id):
    try:
        h = Hrac.objects.get(id=hrac_id)
    except Hrac.DoesNotExist:
        raise Http404("Hrac does not exist")
    if request.method == 'POST':
        form = HracForm(request.POST, instance=h)
        if form.is_valid():
            form.save()
            return render(request, 'hrac_info.html', {'hrac': h})
    else:
        form = HracForm(instance=h)
    return render(request, 'hrac_edit.html', {'form': form})


def hrac_add(request):
    if request.method=='POST':
        form=HracForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('seznam_hracu')
    else:
        form=HracForm()
    return render(request,'hrac_add.html',{'form':form})


def hrac_delete(request, hrac_id):
    try:
        h = Hrac.objects.get(id = hrac_id)
    except Hrac.DoesNotExist:
        raise Http404("Hrac does not exist")
    if request.method == 'POST':
        h.delete()
        return redirect('seznam_hracu')
    return render(request, 'hrac_info.html', {'hrac': h})


def zapas_edit(request, zapas_id):
    try:
        z = Zapas.objects.get(id=zapas_id)
    except Zapas.DoesNotExist:
        raise Http404("Zapas does not exist")
    if request.method == 'POST':
        form = ZapasForm(request.POST, instance=z)
        if form.is_valid():
            form.save()
            return render(request, 'zapas_info.html', {'zapas': z})
    else:
        form = ZapasForm(instance=z)
    return render(request, 'zapas_edit.html', {'form': form})


def zapas_add(request):
    if request.method=='POST':
        form=ZapasForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('seznam_zapasu')
    else:
        form=ZapasForm()
    return render(request,'zapas_add.html',{'form':form})


def zapas_delete(request, zapas_id):
    try:
        z = Zapas.objects.get(id = zapas_id)
    except Zapas.DoesNotExist:
        raise Http404("Zapas does not exist")
    if request.method == 'POST':
        z.delete()
        return redirect('seznam_zapasu')
    return render(request, 'zapas_info.html', {'zapas': z})


def seznam_hal(request):
    try:
        h = Hala.objects.all()
    except Hala.DoesNotExist:
        raise Http404("Hala does not exist")
    return render(request, 'seznam_hal.html', {'haly': h})


def hala_info(request, hala_id):
    try:
        h = Hala.objects.get(id = hala_id)
    except Hala.DoesNotExist:
        raise Http404("Hala does not exist")
    return render(request, 'hala_info.html', {'hala': h})


def hala_edit(request, hala_id):
    try:
        h = Hala.objects.get(id=hala_id)
    except Hala.DoesNotExist:
        raise Http404("Hala does not exist")
    if request.method == 'POST':
        form = HalaForm(request.POST, instance=h)
        if form.is_valid():
            form.save()
            return render(request, 'hala_info.html', {'hala': h})
    else:
        form = HalaForm(instance=h)
    return render(request, 'hala_edit.html', {'form': form})


def hala_add(request):
    if request.method=='POST':
        form=HalaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('seznam_hal')
    else:
        form=HalaForm()
    return render(request,'hala_add.html',{'form':form})


def hala_delete(request, hala_id):
    try:
        h = Hala.objects.get(id = hala_id)
    except Hala.DoesNotExist:
        raise Http404("Hala does not exist")
    if request.method == 'POST':
        h.delete()
        return redirect('seznam_hal')
    return render(request, 'hala_info.html', {'hala': h})


def seznam_adres(request):
    try:
        a = Adresa.objects.all()
    except Adresa.DoesNotExist:
        raise Http404("Adresa does not exist")
    return render(request, 'seznam_adres.html', {'adresy': a})


def adresa_info(request, adresa_id):
    try:
        a = Adresa.objects.get(id = adresa_id)
    except Adresa.DoesNotExist:
        raise Http404("Adresa does not exist")
    return render(request, 'adresa_info.html', {'adresa': a})


def adresa_edit(request, adresa_id):
    try:
        h = Adresa.objects.get(id=adresa_id)
    except Adresa.DoesNotExist:
        raise Http404("Adresa does not exist")
    if request.method == 'POST':
        form = AdresaForm(request.POST, instance=h)
        if form.is_valid():
            form.save()
            return render(request, 'adresa_info.html', {'adresa': h})
    else:
        form = AdresaForm(instance=h)
    return render(request, 'adresa_edit.html', {'form': form})


def adresa_add(request):
    if request.method=='POST':
        form=AdresaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('seznam_adres')
    else:
        form=AdresaForm()
    return render(request,'adresa_add.html',{'form':form})


def adresa_delete(request, adresa_id):
    try:
        h = Adresa.objects.get(id = adresa_id)
    except Adresa.DoesNotExist:
        raise Http404("Adresa does not exist")
    if request.method == 'POST':
        h.delete()
        return redirect('seznam_adres')
    return render(request, 'adresa_info.html', {'adresa': h})


def seznam_treneru(request):
    try:
        a = Trener.objects.all()
    except Trener.DoesNotExist:
        raise Http404("Trener does not exist")
    return render(request, 'seznam_treneru.html', {'treneri': a})


def trener_info2(request, trener_id):
    try:
        a = Trener.objects.get(id = trener_id)
    except Trener.DoesNotExist:
        raise Http404("Trener does not exist")
    return render(request, 'trener_info2.html', {'trener': a})


def trener_edit(request, trener_id):
    try:
        h = Trener.objects.get(id=trener_id)
    except Trener.DoesNotExist:
        raise Http404("Trener does not exist")
    if request.method == 'POST':
        form = TrenerForm(request.POST, instance=h)
        if form.is_valid():
            form.save()
            return render(request, 'trener_info2.html', {'trener': h})
    else:
        form = TrenerForm(instance=h)
    return render(request, 'trener_edit.html', {'form': form})


def trener_add(request):
    if request.method=='POST':
        form=TrenerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('seznam_treneru')
    else:
        form=TrenerForm()
    return render(request,'trener_add.html',{'form':form})


def trener_delete(request, trener_id):
    try:
        h = Trener.objects.get(id = trener_id)
    except Trener.DoesNotExist:
        raise Http404("Trener does not exist")
    if request.method == 'POST':
        h.delete()
        return redirect('seznam_treneru')
    return render(request, 'trener_info2.html', {'trener': h})
