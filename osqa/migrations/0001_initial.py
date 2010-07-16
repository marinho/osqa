# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'User'
        db.create_table('osqa_user', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('email_isvalid', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('email_key', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('reputation', self.gf('osqa.models.base.DenormalizedField')(default=1)),
            ('gold', self.gf('osqa.models.base.DenormalizedField')(default=0)),
            ('silver', self.gf('osqa.models.base.DenormalizedField')(default=0)),
            ('bronze', self.gf('osqa.models.base.DenormalizedField')(default=0)),
            ('questions_per_page', self.gf('django.db.models.fields.SmallIntegerField')(default=10)),
            ('hide_ignored_questions', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('real_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('osqa', ['User'])

        # Adding model 'Activity'
        db.create_table('osqa_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['osqa.User'])),
            ('activity_type', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('active_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_auditted', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('osqa', ['Activity'])

        # Adding model 'SubscriptionSettings'
        db.create_table('osqa_subscriptionsettings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='subscription_settings', unique=True, to=orm['osqa.User'])),
            ('enable_notifications', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('member_joins', self.gf('django.db.models.fields.CharField')(default='n', max_length=1)),
            ('new_question', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('new_question_watched_tags', self.gf('django.db.models.fields.CharField')(default='i', max_length=1)),
            ('subscribed_questions', self.gf('django.db.models.fields.CharField')(default='i', max_length=1)),
            ('all_questions', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('all_questions_watched_tags', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('questions_asked', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('questions_answered', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('questions_commented', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('questions_viewed', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('notify_answers', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('notify_reply_to_comments', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('notify_comments_own_post', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('notify_comments', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('notify_accepted', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('osqa', ['SubscriptionSettings'])

        # Adding model 'ValidationHash'
        db.create_table('osqa_validationhash', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hash_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('seed', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('expiration', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 7, 17, 18, 42, 36, 96448))),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['osqa.User'])),
        ))
        db.send_create_signal('osqa', ['ValidationHash'])

        # Adding unique constraint on 'ValidationHash', fields ['user', 'type']
        db.create_unique('osqa_validationhash', ['user_id', 'type'])

        # Adding model 'AuthKeyUserAssociation'
        db.create_table('osqa_authkeyuserassociation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('provider', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='auth_keys', to=orm['osqa.User'])),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('osqa', ['AuthKeyUserAssociation'])

        # Adding model 'Tag'
        db.create_table('osqa_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deleted_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='deleted_tags', null=True, to=orm['osqa.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_tags', to=orm['osqa.User'])),
            ('used_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('osqa', ['Tag'])

        # Adding model 'MarkedTag'
        db.create_table('osqa_markedtag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_selections', to=orm['osqa.Tag'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tag_selections', to=orm['osqa.User'])),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('osqa', ['MarkedTag'])

        # Adding model 'Node'
        db.create_table('osqa_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deleted_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='deleted_nodes', null=True, to=orm['osqa.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('tagnames', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='nodes', to=orm['osqa.User'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('node_type', self.gf('django.db.models.fields.CharField')(default='node', max_length=16)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', null=True, to=orm['osqa.Node'])),
            ('abs_parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='all_children', null=True, to=orm['osqa.Node'])),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('score', self.gf('osqa.models.base.DenormalizedField')(default=0)),
            ('vote_up_count', self.gf('osqa.models.base.DenormalizedField')(default=0)),
            ('vote_down_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment_count', self.gf('osqa.models.base.DenormalizedField')(default=0)),
            ('offensive_flag_count', self.gf('osqa.models.base.DenormalizedField')(default=0)),
            ('last_edited_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_edited_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='last_edited_nodes', null=True, to=orm['osqa.User'])),
            ('active_revision', self.gf('django.db.models.fields.related.OneToOneField')(related_name='active', unique=True, null=True, to=orm['osqa.NodeRevision'])),
        ))
        db.send_create_signal('osqa', ['Node'])

        # Adding M2M table for field tags on 'Node'
        db.create_table('osqa_node_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('node', models.ForeignKey(orm['osqa.node'], null=False)),
            ('tag', models.ForeignKey(orm['osqa.tag'], null=False))
        ))
        db.create_unique('osqa_node_tags', ['node_id', 'tag_id'])

        # Adding model 'NodeRevision'
        db.create_table('osqa_noderevision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('tagnames', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='noderevisions', to=orm['osqa.User'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='revisions', to=orm['osqa.Node'])),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('revision', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('revised_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('osqa', ['NodeRevision'])

        # Adding unique constraint on 'NodeRevision', fields ['node', 'revision']
        db.create_unique('osqa_noderevision', ['node_id', 'revision'])

        # Adding model 'AnonymousNode'
        db.create_table('osqa_anonymousnode', (
            ('node_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['osqa.Node'], unique=True, primary_key=True)),
            ('validation_hash', self.gf('django.db.models.fields.related.ForeignKey')(related_name='anonymous_content', to=orm['osqa.Node'])),
            ('convertible_to', self.gf('django.db.models.fields.CharField')(default='node', max_length=16)),
        ))
        db.send_create_signal('osqa', ['AnonymousNode'])

        # Adding model 'Question'
        db.create_table('osqa_question', (
            ('node_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['osqa.Node'], unique=True)),
            ('wiki', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('wikified_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('accepted_answer', self.gf('django.db.models.fields.related.OneToOneField')(related_name='question_accepting', unique=True, null=True, to=orm['osqa.Answer'])),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('closed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='closed_questions', null=True, to=orm['osqa.User'])),
            ('closed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('close_reason', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('answer_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('view_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('favourite_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_activity_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('last_activity_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='last_active_in_questions', null=True, to=orm['osqa.User'])),
        ))
        db.send_create_signal('osqa', ['Question'])

        # Adding model 'FavoriteQuestion'
        db.create_table('osqa_favorite_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['osqa.Question'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_favorite_questions', to=orm['osqa.User'])),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('osqa', ['FavoriteQuestion'])

        # Adding unique constraint on 'FavoriteQuestion', fields ['question', 'user']
        db.create_unique('osqa_favorite_question', ['question_id', 'user_id'])

        # Adding model 'QuestionSubscription'
        db.create_table('osqa_questionsubscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['osqa.User'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['osqa.Question'])),
            ('auto_subscription', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('last_view', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 7, 16, 18, 42, 35, 817815))),
        ))
        db.send_create_signal('osqa', ['QuestionSubscription'])

        # Adding model 'Answer'
        db.create_table('osqa_answer', (
            ('node_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['osqa.Node'], unique=True, primary_key=True)),
            ('wiki', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('wikified_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('accepted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('accepted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['osqa.User'], null=True)),
        ))
        db.send_create_signal('osqa', ['Answer'])

        # Adding model 'Vote'
        db.create_table('osqa_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votes', null=True, to=orm['osqa.Node'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votes', to=orm['osqa.User'])),
            ('canceled', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('vote', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('voted_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('osqa', ['Vote'])

        # Adding model 'FlaggedItem'
        db.create_table('osqa_flagged_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flaggeditems', null=True, to=orm['osqa.Node'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flaggeditems', to=orm['osqa.User'])),
            ('flagged_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=300, null=True)),
            ('canceled', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('osqa', ['FlaggedItem'])

        # Adding model 'Badge'
        db.create_table('osqa_badge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('multiple', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('awarded_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('osqa', ['Badge'])

        # Adding unique constraint on 'Badge', fields ['name', 'type']
        db.create_unique('osqa_badge', ['name', 'type'])

        # Adding model 'Award'
        db.create_table('osqa_award', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='awards', to=orm['osqa.User'])),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='award_badge', to=orm['osqa.Badge'])),
            ('awarded_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('notified', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('osqa', ['Award'])

        # Adding model 'Repute'
        db.create_table('osqa_repute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reputes', null=True, to=orm['osqa.Node'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reputes', to=orm['osqa.User'])),
            ('canceled', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('value', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['osqa.Question'])),
            ('reputed_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('reputation_type', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('user_previous_rep', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('osqa', ['Repute'])

        # Adding model 'KeyValue'
        db.create_table('osqa_keyvalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('value', self.gf('osqa.models.utils.PickledObjectField')()),
        ))
        db.send_create_signal('osqa', ['KeyValue'])


    def backwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table('osqa_user')

        # Deleting model 'Activity'
        db.delete_table('osqa_activity')

        # Deleting model 'SubscriptionSettings'
        db.delete_table('osqa_subscriptionsettings')

        # Deleting model 'ValidationHash'
        db.delete_table('osqa_validationhash')

        # Removing unique constraint on 'ValidationHash', fields ['user', 'type']
        db.delete_unique('osqa_validationhash', ['user_id', 'type'])

        # Deleting model 'AuthKeyUserAssociation'
        db.delete_table('osqa_authkeyuserassociation')

        # Deleting model 'Tag'
        db.delete_table('osqa_tag')

        # Deleting model 'MarkedTag'
        db.delete_table('osqa_markedtag')

        # Deleting model 'Node'
        db.delete_table('osqa_node')

        # Removing M2M table for field tags on 'Node'
        db.delete_table('osqa_node_tags')

        # Deleting model 'NodeRevision'
        db.delete_table('osqa_noderevision')

        # Removing unique constraint on 'NodeRevision', fields ['node', 'revision']
        db.delete_unique('osqa_noderevision', ['node_id', 'revision'])

        # Deleting model 'AnonymousNode'
        db.delete_table('osqa_anonymousnode')

        # Deleting model 'Question'
        db.delete_table('osqa_question')

        # Deleting model 'FavoriteQuestion'
        db.delete_table('osqa_favorite_question')

        # Removing unique constraint on 'FavoriteQuestion', fields ['question', 'user']
        db.delete_unique('osqa_favorite_question', ['question_id', 'user_id'])

        # Deleting model 'QuestionSubscription'
        db.delete_table('osqa_questionsubscription')

        # Deleting model 'Answer'
        db.delete_table('osqa_answer')

        # Deleting model 'Vote'
        db.delete_table('osqa_vote')

        # Deleting model 'FlaggedItem'
        db.delete_table('osqa_flagged_item')

        # Deleting model 'Badge'
        db.delete_table('osqa_badge')

        # Removing unique constraint on 'Badge', fields ['name', 'type']
        db.delete_unique('osqa_badge', ['name', 'type'])

        # Deleting model 'Award'
        db.delete_table('osqa_award')

        # Deleting model 'Repute'
        db.delete_table('osqa_repute')

        # Deleting model 'KeyValue'
        db.delete_table('osqa_keyvalue')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'osqa.activity': {
            'Meta': {'object_name': 'Activity'},
            'active_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'activity_type': ('django.db.models.fields.SmallIntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_auditted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['osqa.User']"})
        },
        'osqa.anonymousnode': {
            'Meta': {'object_name': 'AnonymousNode', '_ormbases': ['osqa.Node']},
            'convertible_to': ('django.db.models.fields.CharField', [], {'default': "'node'", 'max_length': '16'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['osqa.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'validation_hash': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anonymous_content'", 'to': "orm['osqa.Node']"})
        },
        'osqa.answer': {
            'Meta': {'object_name': 'Answer'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'accepted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'accepted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['osqa.User']", 'null': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['osqa.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'wiki': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'wikified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'osqa.authkeyuserassociation': {
            'Meta': {'object_name': 'AuthKeyUserAssociation'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auth_keys'", 'to': "orm['osqa.User']"})
        },
        'osqa.award': {
            'Meta': {'object_name': 'Award'},
            'awarded_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'award_badge'", 'to': "orm['osqa.Badge']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notified': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'awards'", 'to': "orm['osqa.User']"})
        },
        'osqa.badge': {
            'Meta': {'unique_together': "(('name', 'type'),)", 'object_name': 'Badge'},
            'awarded_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'awarded_to': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'badges'", 'symmetrical': 'False', 'through': "orm['osqa.Award']", 'to': "orm['osqa.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'osqa.favoritequestion': {
            'Meta': {'unique_together': "(('question', 'user'),)", 'object_name': 'FavoriteQuestion', 'db_table': "'osqa_favorite_question'"},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['osqa.Question']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_favorite_questions'", 'to': "orm['osqa.User']"})
        },
        'osqa.flaggeditem': {
            'Meta': {'object_name': 'FlaggedItem', 'db_table': "'osqa_flagged_item'"},
            'canceled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'flagged_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flaggeditems'", 'null': 'True', 'to': "orm['osqa.Node']"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flaggeditems'", 'to': "orm['osqa.User']"})
        },
        'osqa.keyvalue': {
            'Meta': {'object_name': 'KeyValue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'value': ('osqa.models.utils.PickledObjectField', [], {})
        },
        'osqa.markedtag': {
            'Meta': {'object_name': 'MarkedTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_selections'", 'to': "orm['osqa.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tag_selections'", 'to': "orm['osqa.User']"})
        },
        'osqa.node': {
            'Meta': {'object_name': 'Node'},
            'abs_parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'all_children'", 'null': 'True', 'to': "orm['osqa.Node']"}),
            'active_revision': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'active'", 'unique': 'True', 'null': 'True', 'to': "orm['osqa.NodeRevision']"}),
            'added_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nodes'", 'to': "orm['osqa.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'comment_count': ('osqa.models.base.DenormalizedField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'deleted_nodes'", 'null': 'True', 'to': "orm['osqa.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_edited_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'last_edited_nodes'", 'null': 'True', 'to': "orm['osqa.User']"}),
            'node_type': ('django.db.models.fields.CharField', [], {'default': "'node'", 'max_length': '16'}),
            'offensive_flag_count': ('osqa.models.base.DenormalizedField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': "orm['osqa.Node']"}),
            'score': ('osqa.models.base.DenormalizedField', [], {'default': '0'}),
            'tagnames': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'nodes'", 'symmetrical': 'False', 'to': "orm['osqa.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'vote_down_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_up_count': ('osqa.models.base.DenormalizedField', [], {'default': '0'})
        },
        'osqa.noderevision': {
            'Meta': {'unique_together': "(('node', 'revision'),)", 'object_name': 'NodeRevision'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'noderevisions'", 'to': "orm['osqa.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': "orm['osqa.Node']"}),
            'revised_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'revision': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'tagnames': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'osqa.question': {
            'Meta': {'object_name': 'Question'},
            'accepted_answer': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'question_accepting'", 'unique': 'True', 'null': 'True', 'to': "orm['osqa.Answer']"}),
            'answer_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'close_reason': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'closed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'closed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'closed_questions'", 'null': 'True', 'to': "orm['osqa.User']"}),
            'favorited_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favorite_questions'", 'symmetrical': 'False', 'through': "orm['osqa.FavoriteQuestion']", 'to': "orm['osqa.User']"}),
            'favourite_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_activity_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_activity_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'last_active_in_questions'", 'null': 'True', 'to': "orm['osqa.User']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['osqa.Node']", 'unique': 'True'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subscriptions'", 'symmetrical': 'False', 'through': "orm['osqa.QuestionSubscription']", 'to': "orm['osqa.User']"}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wiki': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'wikified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'osqa.questionsubscription': {
            'Meta': {'object_name': 'QuestionSubscription'},
            'auto_subscription': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_view': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 16, 18, 42, 35, 817815)'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['osqa.Question']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['osqa.User']"})
        },
        'osqa.repute': {
            'Meta': {'object_name': 'Repute'},
            'canceled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reputes'", 'null': 'True', 'to': "orm['osqa.Node']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['osqa.Question']"}),
            'reputation_type': ('django.db.models.fields.SmallIntegerField', [], {}),
            'reputed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reputes'", 'to': "orm['osqa.User']"}),
            'user_previous_rep': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'osqa.subscriptionsettings': {
            'Meta': {'object_name': 'SubscriptionSettings'},
            'all_questions': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'all_questions_watched_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'enable_notifications': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_joins': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '1'}),
            'new_question': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'new_question_watched_tags': ('django.db.models.fields.CharField', [], {'default': "'i'", 'max_length': '1'}),
            'notify_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'notify_answers': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'notify_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'notify_comments_own_post': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'notify_reply_to_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'questions_answered': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'questions_asked': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'questions_commented': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'questions_viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'subscribed_questions': ('django.db.models.fields.CharField', [], {'default': "'i'", 'max_length': '1'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'subscription_settings'", 'unique': 'True', 'to': "orm['osqa.User']"})
        },
        'osqa.tag': {
            'Meta': {'object_name': 'Tag'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_tags'", 'to': "orm['osqa.User']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'deleted_tags'", 'null': 'True', 'to': "orm['osqa.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marked_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'marked_tags'", 'symmetrical': 'False', 'through': "orm['osqa.MarkedTag']", 'to': "orm['osqa.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'used_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'osqa.user': {
            'Meta': {'object_name': 'User', '_ormbases': ['auth.User']},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bronze': ('osqa.models.base.DenormalizedField', [], {'default': '0'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email_isvalid': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'email_key': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'gold': ('osqa.models.base.DenormalizedField', [], {'default': '0'}),
            'hide_ignored_questions': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'questions_per_page': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'}),
            'real_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'reputation': ('osqa.models.base.DenormalizedField', [], {'default': '1'}),
            'silver': ('osqa.models.base.DenormalizedField', [], {'default': '0'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'osqa.validationhash': {
            'Meta': {'unique_together': "(('user', 'type'),)", 'object_name': 'ValidationHash'},
            'expiration': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 17, 18, 42, 36, 145415)'}),
            'hash_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['osqa.User']"})
        },
        'osqa.vote': {
            'Meta': {'object_name': 'Vote'},
            'canceled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'null': 'True', 'to': "orm['osqa.Node']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': "orm['osqa.User']"}),
            'vote': ('django.db.models.fields.SmallIntegerField', [], {}),
            'voted_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['osqa']
