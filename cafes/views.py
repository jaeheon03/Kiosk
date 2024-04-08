from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from cafes.models import *
from django.db.models import Avg
from django.http import HttpResponseRedirect


# Create your views here.
class MenuLV(ListView):
    model=Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Menu.objects.annotate(avg_evaluation=Avg('review__evaluation'))
        context['object_list'] = object_list
        return context

class MenuDV(DetailView):
    model = Menu
    template_name = 'cafes/menu_detail.html'

class ReviewCreateView(CreateView):
    model = Review
    fields=['evaluation','content']
    template_name = 'cafes/review_create.html'

    def form_valid(self, form):
        form.instance.menu = Menu.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
        
    def get_success_url(self):
        menu_id = self.kwargs['pk']
        return reverse('cafes:detail', args=[menu_id])

class MenuCreateView(CreateView):
    model = Menu
    fields = ['name', 'cafe', 'price']
    template_name = 'cafes/menu_form.html'
    success_url = reverse_lazy('cafes:index')  

class MenuUpdateView(UpdateView):
    model = Menu
    fields = ['name', 'cafe', 'price']
    template_name = 'cafes/menu_form.html'
    success_url = reverse_lazy('cafes:index')  
    
class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'cafes/menu_delete.html'
    success_url = reverse_lazy('cafes:index') 

def OrderCreate(request,pk):   
    menu=get_object_or_404(Menu,pk=pk)
    menu.order_set.create(size=request.POST.get('size'),temperature=request.POST.get('temperature'),option=request.POST.get('option'))
    return HttpResponseRedirect(reverse("cafes:index" ))

def ReviewDelete(request,review_id,pk):
    review=get_object_or_404(Review,id=review_id)
    review.delete()
    return HttpResponseRedirect(reverse("cafes:detail", kwargs={'pk': pk}))

class OrderLV(ListView):
    model=Order

def OrderDelete(request,pk):
    order=get_object_or_404(Order,id=pk)
    order.delete()
    return HttpResponseRedirect(reverse("cafes:order_index"))
