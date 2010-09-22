from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from osqa.forms import FeedbackForm
from django.core.urlresolvers import reverse
from django.core.mail import mail_admins
from django.utils.translation import ugettext as _
from osqa.utils.forms import get_next_url
from osqa.models import Badge, Award, User
from osqa.badges import ALL_BADGES
from osqa import settings
from osqa.utils.mail import send_email
from osqa.settings.settingsmarkdown import *
from osqa_modules.default_badges.settings import BADGES_PAGE_TEXT

import re

def favicon(request):
    return HttpResponseRedirect(str(settings.APP_FAVICON))

def about(request):
    return render_to_response('osqa/about.html', {'text': settings.ABOUT_PAGE_TEXT.value }, context_instance=RequestContext(request))

def faq(request):
    #md = markdown.Markdown([SettingsExtension({})])
    #text = md.convert(settings.FAQ_PAGE_TEXT.value)

    return render_to_response('osqa/faq.html', {'text' : settings.FAQ_PAGE_TEXT.value}, context_instance=RequestContext(request))

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            context = {'user': request.user}

            if not request.user.is_authenticated:
                context['email'] = form.cleaned_data.get('email',None)
            
            context['message'] = form.cleaned_data['message']
            context['name'] = form.cleaned_data.get('name',None)

            recipients = [(adm.username, adm.email) for adm in User.objects.filter(is_superuser=True)]

            send_email(settings.EMAIL_SUBJECT_PREFIX + _("Feedback message from %(site_name)s") % {'site_name': settings.APP_SHORT_NAME},
                       recipients, "osqa/notifications/feedback.html", context)
            
            msg = _('Thanks for the feedback!')
            request.user.message_set.create(message=msg)
            return HttpResponseRedirect(get_next_url(request))
    else:
        form = FeedbackForm(initial={'next':get_next_url(request)})

    return render_to_response('osqa/feedback.html', {'form': form}, context_instance=RequestContext(request))
feedback.CANCEL_MESSAGE=_('We look forward to hearing your feedback! Please, give it next time :)')

def privacy(request):
    return render_to_response('osqa/privacy.html', context_instance=RequestContext(request))

def logout(request):
    return render_to_response('osqa/logout.html', {
        'next' : get_next_url(request),
    }, context_instance=RequestContext(request))

def badges(request):#user status/reputation system
    badges = Badge.objects.all().order_by('name')

    badges_dict = dict([(badge.badge, badge.description) for badge in ALL_BADGES])

    for badge in badges:
        if badge.description != badges_dict.get(badge.slug, badge.description):
            badge.description = badges_dict[badge.slug]
            badge.save()
    
    my_badges = []
    if request.user.is_authenticated():
        my_badges = Award.objects.filter(user=request.user).values('badge_id')
        #my_badges.query.group_by = ['badge_id']

    return render_to_response('osqa/badges.html', {
        'badges' : badges,
        'mybadges' : my_badges,
        'feedback_faq_url' : reverse('feedback'),
        'text': BADGES_PAGE_TEXT.value,
    }, context_instance=RequestContext(request))

def badge(request, id):
    badge = get_object_or_404(Badge, id=id)
    awards = Award.objects.extra(
        select={'id': 'auth_user.id', 
                'name': 'auth_user.username', 
                'rep':'osqa_userosqaprofile.reputation',
                'gold': 'osqa_userosqaprofile.gold',
                'silver': 'osqa_userosqaprofile.silver',
                'bronze': 'osqa_userosqaprofile.bronze'},
        tables=['osqa_award', 'auth_user', 'osqa_userosqaprofile'],
        where=['badge_id=%s AND osqa_award.user_id=auth_user.id AND osqa_userosqaprofile.user_id = auth_user.id'],
        params=[id]
    ).distinct('id')

    return render_to_response('osqa/badge.html', {
        'awards' : awards,
        'badge' : badge,
    }, context_instance=RequestContext(request))

