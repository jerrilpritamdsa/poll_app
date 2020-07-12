from django.shortcuts import render, redirect
from .forms import PollForm
from .models import Poll
from django.http import HttpResponse
# Create your views here.
def home(request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render(request, 'pollapp/home.html', context)
    
def create(request):
    if request.method=='POST':
        form=PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:    
        form=PollForm()
    context={'form':form}
    return render(request, 'pollapp/create.html', context)
    
def vote(request, id):
    poll=Poll.objects.get(pk=id)
    if request.method=='POST':
        choice=request.POST['poll']
        if choice == 'option1':
            poll.count_one += 1
        elif choice == 'option2':
            poll.count_two += 1
        elif choice == 'option3':
            poll.count_three += 1
        else:
            return HttpResponse(400, "Invalid Form")
            
        poll.save()
        return redirect ('results',poll.id)
        
    context={'poll':poll}
    return render(request, 'pollapp/vote.html', context)
    
    
def results(request, id):
    poll = Poll.objects.get(pk=id)
    context = {
        'poll' : poll
    }
    return render(request, 'pollapp/results.html', context)