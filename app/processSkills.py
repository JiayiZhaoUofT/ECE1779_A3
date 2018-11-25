from flask import render_template, request
from app import webapp

@webapp.route('/skill_match',methods=['POST'])
def check():
    file = request.files['resume']
    filepath = os.path.join('static', file.filename)
    print(filepath)
    file.save(filepath)
    msg = s3_upload(filepath, bucketName,file.filename)
    print(msg)
    return render_template("/skillCheck.html")
