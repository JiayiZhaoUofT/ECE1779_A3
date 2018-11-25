from flask import render_template, request
from app import webapp

@webapp.route('/skill_match',methods=['POST'])
def check():
    if request.form['desired']:
        desiredSkills = request.form['desired'].split(',')
        return render_template("/skillMatch.html", skills = desiredSkills)
