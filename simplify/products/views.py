from django.http import Http404
from django.http import HttpResponse, HttpRequest

from .models import Question
from django.template import loader

from django.shortcuts import render
from django.shortcuts import get_object_or_404

def product_view(request:HttpRequest):
    return HttpResponse("This is a test endpoint")

def question_view(request:HttpRequest):
    """
        Returns all the questions present inside Question Model
    """
    questions = Question.objects.all()
    template = loader.get_template("products/index.html")
    context = {
        "question_list": questions
    }
    print(questions)
    # return HttpResponse(template.render(context, request))

    return render(request, "products/index.html", context)

def question_details(request, question_id):
    """
    Returns the details of a particular question
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, "products/detail.html", {"question": question})

    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "products/detail.html", {"question": question})