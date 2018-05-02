#-*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired

#gmtools_url = {'server_1':'http://115.182.192.230:50180/gd?','server_2':'http://115.182.192.229:50280/gd?'}



class gmtoolform(Form):
	role_id = StringField('请输入角色id',validators=[DataRequired()])
	server = SelectField('请选择对应服务器',choices=[('server_1','994一服主干'),('server_2','995二服分支')])
	user_level = StringField('设置要调整的等级',validators=[DataRequired()])

class rollcard(Form):
	role_id = StringField('请输入角色id',validators=[DataRequired()])
	server = SelectField('请选择对应服务器',choices=[('server_1','994一服主干'),('server_2','995二服分支')])
	user_level = StringField('设置要调整的等级',validators=[DataRequired()])
	card_pool = SelectField('请选择对应的卡池',choices=[('1','一号卡池'),('2','二号卡池'),('3','三号卡池')])
	roll_choise = SelectField('请选择抽卡方式',choices=[('0','钻石单抽'),('1','扭蛋券单抽'),('2','十连抽')])
	count = StringField('抽卡次数',validators=[DataRequired()])
