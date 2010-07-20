from osqa.models.user import UserOSQAProfile

class ExtendedUser(object):
    def process_request(self, request):
        """Old code disabled because this middleware is a big workaround"""

        # Force saving the current user if it hasn't a OSQA profile. This calls a signal
        # that creates the profile.
        if request.user.is_authenticated() and\
           UserOSQAProfile.objects.filter(user=request.user).count() == 0:
            request.user.save()

