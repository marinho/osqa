import re

from osqa.badges.base import AbstractBadge
from osqa.modules import get_modules_script_classes

ALL_BADGES = [
            cls() for name, cls
            in get_modules_script_classes('badges', AbstractBadge).items()
            if not re.search('AbstractBadge$', name)
        ]
