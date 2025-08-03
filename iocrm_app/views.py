from datetime import timezone
from django.shortcuts import redirect, render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import ArtistForm, ProjectForm, TransactionForm

def home(request):
    return render(request, 'iocrm_app/home.html', {})

def tr_list(request):
    trs = Transaction.objects.order_by('-updated_at')
    return render(request, 'iocrm_app/tr_list.html', {'trs': trs})
 
def ar_list(request):
    ars = Artist.objects.order_by('-updated_at')
    return render(request, 'iocrm_app/ar_list.html', {'ars': ars})

def ar_detail(request, pk):
    ar = get_object_or_404(Artist, pk=pk)
    return render(request, 'iocrm_app/ar_detail.html', {'ar': ar})
 
def pr_list(request):
    prs = Project.objects.order_by('-updated_at')
    return render(request, 'iocrm_app/pr_list.html', {'prs': prs})

def pr_detail(request, pk):
    pr = get_object_or_404(Project, pk=pk)
    return render(request, 'iocrm_app/pr_detail.html', {'pr': pr})

def tr_detail(request, pk):
    tr = get_object_or_404(Transaction, pk=pk)
    return render(request, 'iocrm_app/tr_detail.html', {'tr': tr})

def ar_new(request):
    form = ArtistForm()
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            ar = form.save(commit=False)
            ar.save()
            return redirect('ar_detail', pk=ar.pk)
    else:
        form = ArtistForm()
    return render(request, 'iocrm_app/ar_edit.html', {'form': form})

def ar_edit(request, pk):
    ar = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES, instance=ar)
        if form.is_valid():
            ar = form.save(commit=False)
            ar.save()
            return redirect('ar_detail', pk=ar.pk)
    else:
        form = ArtistForm(instance=ar)
    return render(request, 'iocrm_app/ar_edit.html', {'form': form})

def pr_new(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            pr = form.save(commit=False)
            pr.save()
            return redirect('pr_detail', pk=pr.pk)
    else:
        form = ProjectForm()
    return render(request, 'iocrm_app/pr_edit.html', {'form': form})

def pr_edit(request, pk):
    pr = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=pr)
        if form.is_valid():
            pr = form.save(commit=False)
            pr.save()
            return redirect('pr_detail', pk=pr.pk)
    else:
        form = ProjectForm(instance=pr)
    return render(request, 'iocrm_app/pr_edit.html', {'form': form})

def tr_new(request):
    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            tr = form.save(commit=False)
            tr.save()
            return redirect('tr_detail', pk=tr.pk)
    else:
        form = TransactionForm()
    return render(request, 'iocrm_app/tr_edit.html', {'form': form})

def tr_edit(request, pk):
    tr = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=tr)
        if form.is_valid():
            tr = form.save(commit=False)
            tr.save()
            return redirect('tr_detail', pk=tr.pk)
    else:
        form = TransactionForm(instance=tr)
    return render(request, 'iocrm_app/tr_edit.html', {'form': form})