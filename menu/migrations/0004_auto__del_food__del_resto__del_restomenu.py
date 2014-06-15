# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Food'
        db.delete_table(u'menu_food')

        # Deleting model 'Resto'
        db.delete_table(u'menu_resto')

        # Deleting model 'RestoMenu'
        db.delete_table(u'menu_restomenu')


    def backwards(self, orm):
        # Adding model 'Food'
        db.create_table(u'menu_food', (
            ('cost', self.gf('django.db.models.fields.FloatField')(null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'menu', ['Food'])

        # Adding model 'Resto'
        db.create_table(u'menu_resto', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.RestoMenu'], null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gettable_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'menu', ['Resto'])

        # Adding model 'RestoMenu'
        db.create_table(u'menu_restomenu', (
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(related_name='children', null=True, to=orm['menu.RestoMenu'], blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('food', self.gf('django.db.models.fields.FloatField')()),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'menu', ['RestoMenu'])


    models = {
        u'menu.menuruurls': {
            'Meta': {'object_name': 'MenuRuURLs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['menu']