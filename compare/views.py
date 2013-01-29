from django.template import Context, loader, RequestContext
from django.views.generic.simple import direct_to_template
from compare.models import Topic, TopicForm
from django.http import HttpResponse, HttpResponseRedirect

#compare module view
def index(request):
    latest_poll_list = Topic.objects.all()
    t = loader.get_template('topics/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))

def add(request):
    if request.method == 'POST':
      form = TopicForm(request.POST)
      if form.is_valid():
        new_topic = form.save()
        return HttpResponseRedirect('add/success')
    else:
      form = TopicForm()

    return direct_to_template(request,
                              'topics/add.html',
                              {'form':form})