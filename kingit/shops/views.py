from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import TC, Pavilion, Worker
from .form import FilterTCForm, AddTCForm, FilterPavilion, WorkerForm, FilterWorker

def managerC(request):
    tc = TC.objects.all()
    filter_tc = FilterTCForm()
    return render(request, 'shops/managerC.html', {'tc': tc, 'form': filter_tc})


class FilterTC(ListView):
    model = TC
    template_name = 'shops/managerC.html'
    context_object_name = 'tc'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filter_tc
        return context

    def get_queryset(self):
        self.filter_tc = FilterTCForm(self.request.GET)
        q_1 = self.request.GET.get('title')
        q_2 = self.request.GET.get('status')
        tc = TC.objects.filter(title__icontains=q_1, status__icontains=q_2)
        return tc


class ManagerCAdd(CreateView):
    model = TC
    form_class = AddTCForm
    template_name = 'shops/managerC_add.html'
    success_url = reverse_lazy('home')


def edit_tc(request, pk):
    tc = get_object_or_404(TC, pk=pk)
    if request.method == "POST":
        form = AddTCForm(request.POST, request.FILES, instance=tc)
        if form.is_valid():
            tc.save()
            return redirect('home')
    else:
        form = AddTCForm(instance=tc)
    return render(request, 'shops/managerC_edit.html', {'form': form, 'tc': tc})


def delete_tc(request, pk):
    try:
        tc = TC.objects.get(id=pk)
        tc.delete()
        return HttpResponseRedirect("/")
    except TC.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def managerC_pavilions(request):
    pavilions = Pavilion.objects.all()
    form = FilterPavilion
    return render(request, 'shops/managerC_pavilions.html', {'form': form, 'pavilions': pavilions})


class FilterPavilions(ListView):
    model = Pavilion
    template_name = 'shops/managerC_pavilions.html'
    context_object_name = 'pavilions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filter_pavilions
        return context

    def get_queryset(self):
        self.filter_pavilions = FilterPavilion(self.request.GET)
        q_1 = self.request.GET.get('floor')
        q_2 = self.request.GET.get('status')
        if q_2 == 'все':
            pavilions = Pavilion.objects.filter(floor=q_1)
            return pavilions
        else:
            pavilions = Pavilion.objects.filter(floor=q_1, status__icontains=q_2)
            return pavilions


############################################################################################################
# Admin

def administrator(request):
    workers = Worker.objects.all()
    form = FilterWorker()
    return render(request, 'shops/administrator.html', {'form': form, 'workers': workers})


class AdminSearch(ListView):
    model = Worker
    template_name = 'shops/administrator.html'
    context_object_name = 'workers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filter_worker
        return context

    def get_queryset(self):
        self.filter_worker = FilterWorker(self.request.GET)
        q_1 = self.request.GET.get('role')
        workers = Worker.objects.filter(role__icontains=q_1)
        return workers


class AdminADD(CreateView):
    model = Worker
    form_class = WorkerForm
    template_name = 'shops/administrator_add.html'
    context_object_name = 'workers'

def admin_edit(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        form = WorkerForm(request.POST, request.FILES, instance=worker)
        if form.is_valid():
            worker.save()
            return redirect('administrator')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'shops/administrator_edit.html', {'worker': worker, 'form': form})


def delete_worker(request, pk):
    try:
        worker = Worker.objects.get(id=pk)
        worker.delete()
        return redirect('administrator')
    except TC.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
