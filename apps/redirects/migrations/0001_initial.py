# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Redirect'
        db.create_table('redirects_redirect', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('old_path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, db_index=True)),
            ('new_path', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('redirects', ['Redirect'])

    def backwards(self, orm):
        # Deleting model 'Redirect'
        db.delete_table('redirects_redirect')

    models = {
        'redirects.redirect': {
            'Meta': {'ordering': "('old_path',)", 'object_name': 'Redirect'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'old_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['redirects']