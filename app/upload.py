from flask import render_template, session, request, redirect, url_for
from app import webapp
import os

@webapp.route('/',methods=['GET'])
@webapp.route('/index',methods=['GET'])
@webapp.route('/upload',methods=['GET'])
def upload():
    return render_template("/upload.html")
@webapp.route('/skill_check',methods=['POST'])
def upload_and_skill_check():
    #todo: upload PDF to s3
    file = request.files['resume']
    filepath = os.path.join('app/static/user_images', file.filename)
    file.save(filepath)
    filename = file.filename
    # s3_upload(filepath, filename)
    return render_template("/skillCheck.html")
