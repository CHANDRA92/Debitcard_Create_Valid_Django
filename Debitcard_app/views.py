from django.shortcuts import render, redirect
from django.http import HttpResponse
from .check_debit import checkLuhn
from django.contrib import messages
from .luhn_algo import luhn

# Create your views here.
def check(request):
    if request.method == "POST":
        checkno = request.POST['checkno']
        
        lenth=len(checkno)
        print(lenth)

        if checkLuhn(checkno) and lenth == 16:
            
            # login(request, user)
            # fname = user.first_name
            messages.success(request, "Card No is Valid!!")
            # return render(request, "home.html",{"fname":fname})
        elif checkLuhn(checkno) is False:
            messages.warning(request, "Card No is not valid!!")
        # else:
        #     messages.warning(request, "Card No is not valid!!")
    

        # print(checkno)
    return render(request, 'check.html')
    # return HttpResponse('Bad Credentials')
def Generate(request):
    card_no=luhn()
    # return HttpResponse('Bad Credentials')
    # return redirect('',{"card_no":card_no})
    return render(request, "check.html",{"card_no":card_no})
    