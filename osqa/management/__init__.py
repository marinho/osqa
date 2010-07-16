from osqa.modules import get_modules_script
from django.db.models.signals import post_syncdb
import osqa.models

def setup_badges(sender, **kwargs):
    from osqa.badges import ALL_BADGES

    for badge in ALL_BADGES:
        badge.install()

post_syncdb.connect(setup_badges, sender=osqa.models)

get_modules_script('management')
