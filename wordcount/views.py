from django.http import HttpResponse
from django.shortcuts import render
import operator

def home_page(request):
    return render(request, 'home.html')

def count_page(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    context = {
        'fulltext': fulltext,
        'count': len(wordlist),
        'word_dict': sorted_list,
    }
    return render(request, 'count.html', context)

def about_page(request):
    return render(request, 'about.html')