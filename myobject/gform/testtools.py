#-*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired


class rollcard(Form):
	role_id = StringField('请输入角色id',validators=[DataRequired()])
	server = SelectField('请选择对应服务器',choices=[('server_1','994一服主干'),('server_2','995二服分支')])
	card_pool = SelectField('请选择对应的卡池',choices=[('1','一号卡池'),('2','二号卡池'),('3','三号卡池')])
	roll_choise = SelectField('请选择抽卡方式',choices=[('0','钻石单抽'),('1','扭蛋券单抽'),('2','十连抽')])
	count = StringField('抽卡次数',validators=[DataRequired()])

class update(Form):
	server = SelectField('请选择对应服务器',choices=[('server_1','994一服主干'),('server_2','995二服分支'),('inter_server','跨服服务器')])

class item_search(Form):
	item = StringField('请输入要查找的道具id',validators=[DataRequired()])
	