from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader


def index(request):
    #return HttpResponse('Hello, world! You\'re at the polls index')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    contex = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(contex))


def testX(request):
    return HttpResponse('Check how work url/views')



def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))



def results(request, question_id):
    response = "You're looking at the results of question {}".format(
        question_id)
    return HttpResponse(response)



def vote(request, question_id):
    return HttpResponse("You're voting on question{}".format(question_id))

