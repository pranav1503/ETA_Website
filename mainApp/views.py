from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from mainApp import models
from django.utils import timezone
from mainApp.forms import AddEventForm
from mainApp.models import Events, SubscribeModel
from django.contrib import messages
import re
import smtplib
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

class Home(ListView):
    template_name = 'mainApp/home.html'
    model = models.Events
    context_object_name = 'lists'

    def get_queryset(self):
        query = models.Events.objects.filter(last_date__gte=timezone.now()).order_by('-published')
        delquery = models.Events.objects.filter(last_date__lt=timezone.now()).order_by('-published')
        delquery.delete()
        return query

class AddEvent(CreateView):
    form_class = AddEventForm
    template_name = 'mainApp/addevent.html'
    def form_valid(self, AddEventForm):
        print("done")
        getModel = SubscribeModel.objects.all()
        print(getModel)
        recipiants = []
        for i in getModel:
            recipiants.append(i.email)
        try:
            from_email = settings.EMAIL_HOST_USER
            to_email = recipiants
            print(recipiants)
            subject = "ETA Club Event"
            body = "Thank your joining ETA."
            msg = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to= to_email)
            html_template = get_template('event_subs.html').render()
            msg.attach_alternative(html_template,"text/html")
            msg.send()
        except:
            print("No internet or someother error.")
        print(recipiants)
        return super(AddEvent,self).form_valid(AddEventForm)


class DetailEvent(DetailView):
    template_name = 'mainApp/detailevent.html'
    model = Events
    context_object_name = 'details'

def subscription(request):
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        if re.match(r"[^@]+@[cmrit]+\.[ac]+\.[in]+",email):
            user = SubscribeModel.objects.filter(email=email)
            if(user.exists()):
                messages.warning(request,'Your Email Already exists.',"alert alert-warning alert-dismissable")
            else:
                print("Entered")
                try:
                    from_email = settings.EMAIL_HOST_USER
                    to_email = [email]
                    subject = "ETA Club"
                    body = "Thank your joining ETA."
                    msg = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to= to_email)
                    html_template = get_template('subs.html').render()
                    msg.attach_alternative(html_template,"text/html")
                    msg.send()
                except:
                    print("No internet or someother error.")
                e = SubscribeModel(email=email)
                e.save()
                return HttpResponseRedirect(reverse('mainApp:events'))
        else:
            messages.error(request, 'Please Enter CMRIT email.')
    return render(request, 'mainApp/subscribe.html')

class Aboutus(TemplateView):
    template_name = "contact.html"
