# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Food'
        db.create_table(u'menu_food', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('cost', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'menu', ['Food'])

        # Adding model 'Resto'
        db.create_table(u'menu_resto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('gettable_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.RestoMenu'], null=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'menu', ['Resto'])

        # Adding model 'RestoMenu'
        db.create_table(u'menu_restomenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('food', self.gf('django.db.models.fields.FloatField')()),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['menu.RestoMenu'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'menu', ['RestoMenu'])


    def backwards(self, orm):
        # Deleting model 'Food'
        db.delete_table(u'menu_food')

        # Deleting model 'Resto'
        db.delete_table(u'menu_resto')

        # Deleting model 'RestoMenu'
        db.delete_table(u'menu_restomenu')


    models = {
        u'menu.food': {
            'Meta': {'object_name': 'Food'},
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'menu.menuruurls': {
            'Meta': {'object_name': 'MenuRuURLs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'menu.resto': {
            'Meta': {'object_name': 'Resto'},
            'gettable_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.RestoMenu']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'menu.restomenu': {
            'Meta': {'object_name': 'RestoMenu'},
            'food': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['menu.RestoMenu']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['menu']