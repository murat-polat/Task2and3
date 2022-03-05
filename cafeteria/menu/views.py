from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# Display questins
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'menu/index.html', context)

# Get question and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'menu/detail.html', { 'question': question })

# Get question and display results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'menu/results.html', { 'question': question })

# Submit for a question and choice
def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'menu/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        ## Increase choice(menu) and save to the database
        selected_choice.votes += 1
        selected_choice.save()
       
        return HttpResponseRedirect(reverse('menu:results', args=(question.id,)))