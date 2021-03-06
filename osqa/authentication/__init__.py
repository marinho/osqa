import re
import django.dispatch
from osqa.modules import get_modules_script_classes
from osqa.authentication.base import AuthenticationConsumer, ConsumerTemplateContext
from django.conf import settings

class ConsumerAndContext:
    def __init__(self, id, consumer, context):
        self.id = id
        self._consumer = consumer

        context.id = id
        self.context = context

    @property
    def consumer(self):
        return self._consumer()

consumers = dict([
            (re.sub('AuthConsumer$', '', name).lower(), cls) for name, cls
            in get_modules_script_classes('authentication', AuthenticationConsumer).items()
            if not re.search('AbstractAuthConsumer$', name)
        ])

contexts = dict([
            (re.sub('AuthContext$', '', name).lower(), cls) for name, cls
            in get_modules_script_classes('authentication', ConsumerTemplateContext).items()
        ])

AUTH_PROVIDERS_AVAILABLE = dict([
            (name, ConsumerAndContext(name, consumers[name], contexts[name])) for name in consumers.keys()
            if name in contexts
        ])

AUTH_PROVIDERS = dict([(k,v) for k,v in AUTH_PROVIDERS_AVAILABLE.items() if k in settings.ENABLED_AUTH_PROVIDERS])

#todo: probably this don't belong here, also this post_stored routine needs a lot of work
user_logged_in = django.dispatch.Signal(providing_args=["user", "old_session"])
user_updated = django.dispatch.Signal(providing_args=["instance", "updated_by"])

#def post_stored_anonymous_content(user,old_session,**kwargs):
#    from osqa.models import AnonymousQuestion, AnonymousAnswer
#    aq_list = AnonymousQuestion.objects.filter(session_key = old_session)
#    aa_list = AnonymousAnswer.objects.filter(session_key = old_session)
#    import settings
#    if settings.EMAIL_VALIDATION == 'on':#add user to the record
#        for aq in aq_list:
#            aq.author = user
#            aq.save()
#        for aa in aa_list:
#            aa.author = user
#            aa.save()
#        #maybe add pending posts message?
#    else: #just publish the questions
#        for aq in aq_list:
#            aq.publish(user)
#        for aa in aa_list:
#            aa.publish(user)
#
#user_logged_in.connect(post_stored_anonymous_content)
