from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .forms import *


side_bar = {'side_bar': {'Добавить дискуссию': 'discussion_create'}}


def discussions_home(request):
    request_dict = {'request': request}
    context = dict(list(side_bar.items()) + list(request_dict.items()))
    return render(request, template_name='discussions/discussions_index.html',context=context)


def discussion_create(request):
    pass


@login_required
def contact_message_create(request):

    if request.method == "GET":
        form = ContactForm()

    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            date_created = form.cleaned_data['date_created']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['djavarov@gmail.com']

            if cc_myself:
                recipients.append(message)

            # else:
            #     date_created_today = datetime.date.today()
            #     form = ContactForm(initial={'date_created': date_created_today})

                try:
                    send_mail(sender, subject, message, recipients, date_created)

                except:
                    return HttpResponse('Неверное заполнение')

                form = ContactForm()
                messages.success(request, 'Сообщение отправлено')
            # else:
            #     messages.error(request, 'Error')
    #
#
    return render(request, "discussions/contact_form.html", {'form': form})

