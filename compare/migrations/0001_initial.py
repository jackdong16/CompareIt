# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table('compare_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('compare', ['Topic'])

        # Adding model 'Choice'
        db.create_table('compare_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compare.Topic'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('likes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('compare', ['Choice'])

        # Adding model 'Description'
        db.create_table('compare_description', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compare.Choice'])),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('likes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('compare', ['Description'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table('compare_topic')

        # Deleting model 'Choice'
        db.delete_table('compare_choice')

        # Deleting model 'Description'
        db.delete_table('compare_description')


    models = {
        'compare.choice': {
            'Meta': {'object_name': 'Choice'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compare.Topic']"})
        },
        'compare.description': {
            'Meta': {'object_name': 'Description'},
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compare.Choice']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {})
        },
        'compare.topic': {
            'Meta': {'object_name': 'Topic'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['compare']