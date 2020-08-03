from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['textarea']
    word_lst = data.split()
    word_length = len(word_lst)

    worddictionary={}
     
    for word in word_lst:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    
    sorted_lst = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
            
    return render(request,'count.html',{'word':data,'word_count':word_length,'worddictionary': sorted_lst})