from django.shortcuts import render
from django.http import JsonResponse
from .inferer import get_solution

def home(request):
    return render(request, 'index.html')


def search_panne(request):
    #form = TaskForm(request.POST)
    if request.method == 'POST':
        #task = form.save()
        label=request.POST.get('panne')
        context=get_solution(label)
        data = {'label': label, 'context':context}
        print(context)
        return JsonResponse({'sol': data})
    else:
        return JsonResponse({'error': 'Invalid form data.'})