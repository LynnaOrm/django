# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..belt_exam4.models import User #import the folder and class
from .models import *
from datetime import date


def index(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'quotes': Quote.objects.exclude(favorited_by=User.objects.get(id=request.session['user_id'])),
        'fave_quotes': Quote.objects.filter(favorited_by=User.objects.get(id=request.session['user_id']))
      
    }
    return render(request, 'quotes/index.html', context)


def add(request):
    errs = Quote.objects.validate(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
        return redirect("/quotes")
    
    else:
		Quote.objects.create(
        quoted_by=request.POST['quoted_by'], 
		message=request.POST['message'],
        posted_by=User.objects.get(id=request.session['user_id']))
		return redirect('/quotes')

#def delete(request, id):
	#delete_quote = Quote.objects.get(id=id)
	#delete_quote.delete()
    #return redirect('/quotes')


def remove(request, id):
    print "deleting"
    thisquote = Quote.objects.get(id=id)
    thisuser = User.objects.get(id=request.session['user_id'])
    thisquote.favorited_by.remove(thisuser)
    print "finishing deleting"
    return redirect('/quotes')



def join(request, id):
    joinuser = User.objects.get(id=request.session['user_id'])
    joinquote = Quote.objects.get(id=id)
    joinuser.favorites.add(joinquote) #fix
    return redirect('/quotes')



def view(request, id):
    if "user_id" not in request.session:
        return redirect('/')
    context = {
        'posts': Quote.objects.filter(posted_by=User.objects.get(id=id)),
        'user': User.objects.get(id=id),
    }
    return render(request, 'quotes/posts.html', context)
