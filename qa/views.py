from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from paperqa import Docs

from .forms import QuestionForm

from django.conf import settings

import os
import pickle
import sys
os.environ["OPENAI_API_KEY"] = "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"


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_question(request):
    response_text=''

    models_folder = settings.BASE_DIR /'qa'
    print(models_folder)
    file_path = os.path.join(models_folder, os.path.basename("my_docs.pkl"))

    with open(file_path, "rb") as f:
        docs = pickle.load(f)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
       
        if form.is_valid():
            clean_form = form.cleaned_data
            q = clean_form['question']
        
            print(q)
            answer = docs.query(q, k = 5, max_sources = 4)
            print(answer.formatted_answer)
        
            response_text=answer.formatted_answer

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'question.html', {'response_text': response_text})