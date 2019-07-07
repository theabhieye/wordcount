from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
	return render(request,'home.html')

def count(request):
	data=request.GET["fulltextarea"]
	
	word_list = data.split()
	list_len=(len(word_list))
	word_dic = {}
	for word in word_list:
		if word in word_dic:
			word_dic[word]+=1
		else:
			word_dic[word]=1
	sort_list = sorted(word_dic.items(),key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{"fulltext":data,"count":list_len,"word_dic":sort_list})


def about(request):
	return render(request,'about.html')
