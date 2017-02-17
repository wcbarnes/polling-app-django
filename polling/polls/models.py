from __future__ import unicode_literals

# Create your models here.

from mongoengine import *

class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)
    uid = SequenceField()
    def __str__(self):
        return self.choice_text

class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))
    uid = SequenceField()

    meta = {
        'indexes': [
            'question',
            ('pub_date', '+question')
        ]
    }
    def __str__(self):
        return self.question

