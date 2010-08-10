import os.path
from base import Setting, SettingSet
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

UPLOAD_SET = SettingSet('paths', _('File upload settings'), _("File uploads related settings."), 600)

UPFILES_FOLDER = Setting('UPFILES_FOLDER', os.path.join(settings.MEDIA_ROOT, 'upfiles'), UPLOAD_SET, dict(
    label = _("Uploaded files folder"),
    help_text = _("The filesystem path where uploaded files will be stored. Please note that this folder must exist."),
    ))

UPFILES_ALIAS = Setting('UPFILES_ALIAS', settings.MEDIA_URL+'upfiles/', UPLOAD_SET, dict(
    label = _("Uploaded files alias"),
    help_text = _("The url alias for uploaded files. Notice that if you change this setting, you'll need to restart your site."),
    ))

ALLOW_MAX_FILE_SIZE = Setting('ALLOW_MAX_FILE_SIZE', 2.5, UPLOAD_SET, dict(
    label = _("Max file size"),
    help_text = _("The maximum allowed file size for uploads in mb."),
    ))
