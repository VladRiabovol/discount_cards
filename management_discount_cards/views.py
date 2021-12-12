from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from management_discount_cards.models import Card
from management_discount_cards.forms import CardDeleteForm, ChangeStatusForm
from management_products.models import Purchase
from django.views.generic.detail import DetailView
from django.db.models import Q
from datetime import date
from management_discount_cards.serializers import CardSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class CardAPIListView(ListAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    permission_classes = [AllowAny]


def check_expired(context):
    for item in context['cards_list']:
        if item.end_of_activity < date.today():
            item.status = 'expired'
        elif item.status:
            item.status = 'enabled'
        elif not item.status:
            item.status = 'disabled'
    return context


class CardsListView(ListView):
    template_name = "list_of_cards.html"
    model = Card

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards_list'] = Card.objects.all()
        return check_expired(context)


class CardDetailView(DetailView):
    model = Purchase
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards_list'] = Purchase.objects.filter(card_id=self.object.id)
        return context


def delete_page(request):
    if request.method == 'POST':
        form = CardDeleteForm(request.POST)
        print(form)
        if form.is_valid():
            data = request.POST
            id = data.get('id')
            Card.objects.filter(id=id).delete()
            return render(request, 'delete_success.html')
    else:
        form = CardDeleteForm()

    return render(request, 'delete_page.html', {'form': form})


def search_page(request):
    return render(request, 'search_page.html')


class SearchListView(ListView):
    template_name = "search_result.html"
    model = Card

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request.GET.get('search_value')
        if request == 'enabled':
            context['cards_list'] = Card.objects.filter(status=True)
            return check_expired(context)
        elif request == 'disabled':
            context['cards_list'] = Card.objects.filter(status=False)
            return check_expired(context)
        else:
            context['cards_list'] = Card.objects.filter(Q(series__icontains=request) |
                                                        Q(number__icontains=request))
            return check_expired(context)


def change_status(request):
    if request.method == 'POST':
        form_change_status = ChangeStatusForm(request.POST)
        if form_change_status.is_valid():
            print(form_change_status.cleaned_data)
            id = request.POST.get('id')
            enabled = request.POST.get('enabled')
            disabled = request.POST.get('disabled')
            if enabled:
                change = Card.objects.filter(id=id).update(status=True)
            elif disabled:
                change = Card.objects.filter(id=id).update(status=False)
            return redirect('cards-list')
    else:
        form_change_status = ChangeStatusForm()

    return render(request, 'change_status.html', {'form_change_status': form_change_status})




