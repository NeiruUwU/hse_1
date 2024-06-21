from tortoise import fields
from tortoise.models import Model
from enum import Enum

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    questions = fields.ManyToManyField('models.Question', through='user_question_pivot', related_name="users")
    rating = fields.ReverseRelation['Rating']


class Game(Model):    
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    code = fields.CharField(max_length=50, unique=True)
    questions = fields.ReverseRelation['Question']
    options = fields.ReverseRelation['Answer']
    rating = fields.ReverseRelation['Rating']

    class Type(Enum):
        FONT  = "game_font"
        COLOR = "game_color"

class Rating(Model):
    game = fields.ForeignKeyField('models.Game', related_name='rating')
    user = fields.ForeignKeyField('models.User', related_name='rating')
    amount = fields.IntField(default=0)
    
    
class Question(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=True)
    img_path = fields.CharField(max_length=50)
    game = fields.ForeignKeyField('models.Game', related_name='questons')
    answer = fields.ForeignKeyField('models.Answer', related_name='questons')
    users = fields.ManyToManyRelation['User']
    options = fields.ReverseRelation['OptionPivot']
    
    
class OptionPivot(Model):
    question = fields.ForeignKeyField('models.Question', related_name='options')
    answer = fields.ForeignKeyField('models.Answer', related_name='options')


class Answer(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    game = fields.ForeignKeyField('models.Game', related_name='options')
    options = fields.ReverseRelation['OptionPivot']
    

    
    