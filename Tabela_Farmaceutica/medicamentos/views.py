from django.shortcuts import render, redirect
from .models import Medicamento
from .forms import MedicamentoForm

# Create your views here.
def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()

    return render(request, 'lista.html', {'medicamentos':medicamentos})

def novo_medicamento(request):
    form = MedicamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_medicamentos')

    return render(request, 'medicamento_form.html', {'form':form})