from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from quoteline.models import SingleQuote
from django.core.cache import cache

def allquotes():
  quotes = cache.get('allquotes')
  if not quotes:
    quotes = SingleQuote.objects.all()
    cache.set('allquotes', quotes)
  return quotes

# Create your views here.
class GreetingView(View):
  greeting = "Hello. This is a test."
  
  def get(self, request):
    return render(request, "quoteline/index.html")

class ShowQuote(View):
  def get(self, request, *args, **kwargs):
    gen1 = allquotes().order_by('?')[:1]
    gen2 = allquotes().order_by('?')[:1]
    toReturn = [gen1[0].quote_text, gen2[0].quote_text]
    return render(request, "quoteline/showquote.html", {'quote' : toReturn })
    
