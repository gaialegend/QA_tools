#-*-coding:utf-8 -*-

from flask import Flask,render_template,redirect,url_for
from flask.ext.bootstrap import Bootstrap  
from script import severupdate
from gform import switch_time as stime
from wtforms.validators import DataRequired
import config
import sys
from script import gm_tools
from script import rollcard
from script import csv2name
from gform import gmtools
from gform import testtools
from flask import make_response,send_file,send_from_directory
import os.path
from flask import request
from werkzeug import secure_filename
import get_filelist

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
bootstrap = Bootstrap(app)
#dirpath = os.path.join(app.root_path,'script')
dirpath = app.root_path
UPLOAD_FOLDER = dirpath + '\upload_file'

ALLOWED_EXTENSIONS = set(['zip'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/restart/')
def restart():
	result = severupdate.restartserver('server_2')
	# print 'result = %s' &(str(result))
	#app.logger.debug(result.encode('utf-8'))
	return render_template('restart.html',result=result.encode(encoding='UTF-8'),fuction=0)

@app.route('/restart_230/')
def restart_230():
	result = severupdate.restartserver('server_1')
	return render_template('restart.html',result=result.encode(encoding='UTF-8'),fuction=0)

@app.route('/restart_new',methods=['GET','POST'])
def restart_new():
	form = testtools.update()
	if request.method == 'POST':
		server = form.server.data
		result = severupdate.restartserver(server)
		return '重启成功 请手动刷新页面'
	return render_template('restart_new.html',form=form)




@app.route('/time')
def time():
	result = severupdate.time('server_1')
	result2 = severupdate.time('server_2')
	return render_template('restart.html',result=result.encode(encoding='UTF-8'),result2=result2.encode(encoding='UTF-8'),fuction=1)

@app.route('/time/switch',methods=['GET','POST'])
def switch():
	# _time = severupdate.time('server_2')
	# form = stime.NameForm('server_2')
	# if form.validate_on_submit():
	# 	print form.name.data
	# 	# _time = severupdate.time('server_2')
	# 	print _time
	# 	result = severupdate.time_switch(form.name.data,'server_2')
	# 	print '---------------------------------------'
	# 	print result
	# return render_template('switch_time.html',form=form,server_time=_time,platform='229')
	_time = severupdate.time('server_2')
	form = stime.NameForm()
	if form.validate_on_submit():
		_time = severupdate.time('server_2')
		result = severupdate.time_switch(form.name.data,'server_2')
		print '-------------------------------------------'
		print result
	
	return render_template('switch_time.html',form=form,server_time=_time,platform='229')

@app.route('/gmtool')
def gmtool():
	return render_template('gm_tool.html')

@app.route('/gmtool/charater',methods=['GET','POST'])
def add_hero():
	form = stime.NameForm()
	if form.validate_on_submit():
		gm_tool = gm_tools.Gmtools()
		gm_tool.add_hero(form.name.data)
	return render_template('addhero.html',form=form)

@app.route('/update')
def server_update():
	result = severupdate.restartserver()
	return render_template('restart.html',result=result.encode(encoding='UTF-8'),fuction=1)

@app.route('/gmtool/add_all_item',methods=['GET','POST'])
def create_all_item():
	form = stime.NameForm()
	if form.validate_on_submit():
		gm_tool = gm_tools.Gmtools()
		gm_tool.create_all_item(form.name.data,'server_2')
	return render_template('create_item.html',form=form)

@app.route('/gmtool/add_all_item_230',methods=['GET','POST'])
def create_all_item_230():
	form = stime.NameForm()
	if form.validate_on_submit():
		gm_tool = gm_tools.Gmtools()
		gm_tool.create_all_item(form.name.data,'server_1')
	return render_template('create_item.html',form=form)

@app.route('/time/switch_time_230',methods=['GET','POST'])
def switch_time_230():
	_time = severupdate.time('server_1')
	form = stime.NameForm()
	if form.validate_on_submit():
		_time = severupdate.time('server_1')
		result = severupdate.time_switch(form.name.data,'server_1')
		print '-------------------------------------------'
		print result
	
	return render_template('switch_time.html',form=form,server_time=_time,platform='230')

@app.route('/<platform>/status',methods=['GET','POST'])
def get_platform_status(platform):
	res_list = []
	result = severupdate.get_serverstatus_new(platform)
	for x in result.keys():
		res_list.append(x)
	return render_template('platfrom_status.html',li=res_list,result=result)



@app.route('/<platform>/<switch_>',methods=['GET','POST'])
def platform_switch(platform,switch_):
	result = severupdate.server_switch(platform,switch_)
	return 'success'

@app.route('/gmtool/new_gmtools',methods=['GET','POST'])
def super_man():
	form = gmtools.gmtoolform()
	if form.validate_on_submit():
		gm_tool = gm_tools.Gmtools()
		gm_tool.super_man(form.role_id.data,form.server.data,form.user_level.data)
	return render_template('new_gmtools.html',form=form)

@app.route('/download/<path:filename>',methods=['GET'])
def downloader(filename):
	return send_from_directory(dirpath,filename,as_attachment=True)

@app.route('/test_tool/rollcard',methods=['GET','POST'])
def rollcard_test_1():
	form = testtools.rollcard()
	print type(form.roll_choise)
	if form.validate_on_submit():
		print '---------------------1111------------------------'
		rollcard_test_ = rollcard.rollcard()
		if form.roll_choise.data == '0' or form.roll_choise.data == '2':
			rollcard_test_.set_money(form.role_id.data,'2','999999999',form.server.data)
		else:
			rollcard_test_.order(form.role_id.data,'create_item','1012',form.server.data,form.count.data)
		filename = rollcard_test_.rollcard_post(form.role_id.data,form.count.data,form.roll_choise.data,form.card_pool.data,form.server.data)
		print filename
	if request.method == 'POST':
		print filename
		return send_from_directory(dirpath,filename,as_attachment=True)	
	return render_template('rollcard_test.html',form=form)

@app.route('/download/<filename>',methods=['GET','POST'])
def package_download(filename):
	if request.method == 'GET':
		_dir_path = dirpath + '\package\download'
		print _dir_path
		print filename
		return send_from_directory(_dir_path,filename,as_attachment=True)

@app.route('/download/getfilelist',methods=['GET','POST'])
def get_packfilelist():
	file_dic = get_filelist.get_downloadfile()
	url_pack = {}
	for x in file_dic.keys():
		url_pack[x] = '/download/' + x 
	return render_template('pack_filelist.html',pack_dic=url_pack)




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['GET','POST'])
def upload_file():
	form = testtools.update()
	if request.method == 'POST':
		server = form.server.data
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			upload_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
			file.save(os.path.join(upload_path))
			filename_ = severupdate.server_update_new(file.filename,server)
			result = severupdate.server_update(filename_,server)
			return result
	return render_template('upload.html',form=form)

@app.route('/item_search',methods=['GET','POST'])
def item_search():
	form = testtools.item_search()
	if request.method == 'POST':
		# print form.item.data
		# print type(form.item.data)
		# try:
		# 	item_name = int(form.item.data.decode('utf-8'))
		# 	item_name = csv2name.get_item_name(form.item.data)
		# 	item_type = 1
		# except ValueError:
		# 	print '------------------------------------------'
		# 	print 'hello'
		# 	print type(form.item.data)			
		# 	item_name = csv2name.get_item_id(form.item.data)
		# 	if type(item_name) == type({}):
		# 		item_type = 2
		# 	else:
		# 		item_type = 3
		# if form.item.data == None:
		# 	item_name = '搜寻内容为空'
		# return render_template('item_search.html',form=form,item_name=item_name,item_type=item_type)
		#print int(form.item.data)
		try:
			item_name =csv2name.get_item_name(form.item.data)
			item_name = [{'name':item_name[1],'type':item_name[0],'id':form.item.data}]
		except KeyError:
			item_name = csv2name.get_item_id(form.item.data)
		if form.item.data == None:
			item_name = {'name':'搜寻内容为空'}
		item_type = 0
		return render_template('item_search.html',form=form,item_name=item_name,item_type=item_type)
	item_name = ''
	return render_template('item_search.html',form=form,item_name=item_name)


if __name__ == '__main__':
	app.config.from_object('config')
	app.run(host='0.0.0.0',debug=True,threaded=True)