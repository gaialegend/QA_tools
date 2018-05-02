#-*- coding:utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
	name = StringField('请输入内容',validators=[DataRequired()])
	submit = SubmitField("确认提交")
