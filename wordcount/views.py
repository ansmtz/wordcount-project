from django.http import HttpResponse
from django.shortcuts import render
import collections
import operator
def home(request):
    return render(request, 'home.html')
def count(request):
    # получаем информацию из формы
    fulltext = request.GET['fulltext']
    count_pairs = collections.Counter(fulltext.split()).items()
    data = {
        'fulltext': fulltext,
        'length': len(fulltext.split()),     
        'count_pairs': count_pairs,
        'count_pairs_sorted': sorted(count_pairs, key = operator.itemgetter(1), reverse=True)
    }
    return render(request, 'count.html', data)  
def about(request):
    return render(request, 'about.html')    