from flask import render_template, request, redirect, url_for
from app import webapp


@webapp.route('/',methods=['GET'])
@webapp.route('/index',methods=['GET'])
@webapp.route('/upload',methods=['GET'])
def upload():
    return render_template("/upload.html")

@webapp.route('/skill_check',methods=['POST'])
def upload_and_skill_check():
    #todo: upload PDF to s3
    file = request.files['file']
    filename = file.filename

    return render_template("/skillCheck.html")
