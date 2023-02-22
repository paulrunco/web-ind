from django.urls import path
from quoting.views import QuoteListView, QuoteDetailView

urlpatterns = [
    path('quotes/', QuoteListView.as_view(), name='quotes-list'),
    path('quotes/<int:pk>', QuoteDetailView.as_view(), name='quote-detail')
]