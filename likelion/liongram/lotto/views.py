from django.shortcuts import render,redirect

import random
# Create your views here.


def lotto(request):
    if request.method == 'GET':
        return render(request,'lotto_input.html')    
    else:
        arr = []
        number = int(request.POST.get('number'))
        for _ in range(number):
            temp =[]
            for _ in range(7):
                temp.append(random.randrange(1,50))
            arr.append(temp)
        context = {'count':number,'arr':arr}
        return render(request,'lotto.html',context)

