from question import Question ,QuestionRevision, FavoriteQuestion, QuestionSubscription
from answer import Answer, AnswerRevision
from tag import Tag, MarkedTag
from meta import Vote, FlaggedItem
from user import User, UserOSQAProfile, Activity, ValidationHash, AuthKeyUserAssociation, SubscriptionSettings
from repute import Badge, Award, Repute
from node import Node, NodeRevision, NodeMetaClass, AnonymousNode
from comment import Comment
from utils import KeyValue

# Sets South support to customized fields (otherwise South doesn't recognize them and raise a warning)
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [r"^osqa\.models\.\w+\.\w+"])
except:
    pass

from base import *

# Signal that signs an instance as "is new" everytime it is save and there is no ID
def is_new(sender, instance, **kwargs):
    try:
        instance._is_new = not bool(instance.id)
    except:
        pass
pre_save.connect(is_new)

__all__ = [
        'Node', 'NodeRevision', 'AnonymousNode', 
        'Question', 'FavoriteQuestion', 'QuestionSubscription', 'QuestionRevision',
        'Answer', 'AnswerRevision',
        'Tag', 'Comment', 'Vote', 'FlaggedItem', 'MarkedTag', 'Badge', 'Award', 'Repute',
        'Activity', 'ValidationHash', 'AuthKeyUserAssociation', 'SubscriptionSettings', 'KeyValue', 'User',
        ]

from osqa.modules import get_modules_script_classes

for k, v in get_modules_script_classes('models', models.Model).items():
    if not k in __all__:
        __all__.append(k)
        exec "%s = v" % k

NodeMetaClass.setup_relations()
