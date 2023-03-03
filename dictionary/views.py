from django.shortcuts import render
from PyDictionary import PyDictionary

def index(request):
    return render(request,'index.html')

def word(request):
    search=request.GET.get('search')
    dictionary=PyDictionary()
    meaning=dictionary.meaning(search)
    synonyms=dictionary.synonym(search)
    antonyms=dictionary.antonym(search)
    context={

        'meaning':meaning['Noun'][0],
        'synonyms':synonyms,
        'antonyms':antonyms
    }
    print(context['meaning'])
    print(context['synonyms'])
    print(context['antonyms'])
    return render(request,'home.html',context)
