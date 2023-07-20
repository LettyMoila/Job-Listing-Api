from flask import Flask, redirect, url_for, request
# from flask_cors import CORS
from datetime import datetime
import json

import config

from db_connect import db_connect

app = Flask(__name__)
# CORS(app)

@app.route('/')
def main():
    return "Job Listing API"

'''Client Routes and connections'''
@app.route('/client_profile/<id>', methods=['GET', 'POST'])
def client_profile_route(id=0):
    client_profile = []
    
    table_instance = db_connect('client_profile')
   
    
    if request.method == "GET":
        rows = table_instance.select()
        id = table_instance.select(condition=f"WHERE first_name='{id}'")
        for row in rows:
            cp_table = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'number': row[4],
                'address': row[5],
                'current_salary': row[6]
            }
            
            client_profile.append(cp_table)
            
            cp_dictionary = {
                'client_profile': client_profile
            }
            
            return cp_dictionary
        else:
            return 'No clients at the moment'
    elif request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        number = request.form['number']
        address = request.form['address']
        current_salary = request.form['current_salary']
        table_instance.insert("first_name, last_name, email, number,address,current_salary", 
                        f"'{first_name}','{last_name}','{email}', '{number}','{address}','{current_salary}'")
        
        return redirect('http://localhost:3000/apply/client_education')
    else:
        return 'Enter correct data'



@app.route('/client_profile/<id>/experience', methods=['GET', 'POST'])
def client_experience_route(id=0):
    client_exp = []
    
    table_instance = db_connect('client_experience')
    client = db_connect('client_profile')
    
    if request.method == "GET":
        client_id = client.select(condition=f"WHERE id='{id}'")
        rows = table_instance.select()
        for row in rows:
            exp_table = {
                'id': row[client_id],
                'current_job': row[1],
                'start_date': row[2],
                'end_date': row[3],
                'company_name': row[4],
                'job_location_city': row[5],
                'job_location_state': row[6],
                'job_location_country': row[7],
                'description': row[8]
            }
            
            client_exp.append(exp_table)
            
            exp_dictionary = {
                'client_experience': client_exp
            }
            
            return exp_dictionary
        else:
            return 'No information about client experience at the moment'
    elif request.method == "POST":
        current_job = request.form['current_job']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        company_name = request.form['company_name']
        job_location_city = request.form['job_location_city']
        job_location_state = request.form['job_location_state']
        job_location_country = request.form['job_location_country']
        description = request.form['description']
        table_instance.insert("current_job, start_date, end_date, company_name, job_location_city, job_location_state, job_location_country, description", 
                        f"'{current_job}','{start_date}','{end_date}', '{company_name}','{job_location_city}','{job_location_state}','{job_location_country}','{description}'")
        
        return redirect('http://localhost:3000/jobs')
    else:
        return 'No client experience at the moment'



@app.route('/client_profile/<id>/education', methods=['GET', 'POST'])
def client_education_route(id=0):
    client_edu = []
    
    table_instance = db_connect('client_education')
    client = db_connect('client_profile')
    
    if request.method == "GET":
        client_id = client.select(condition=f"WHERE id='{id}'")
        rows = table_instance.select()
        for row in rows:
            edu_table = {
                'id': row[client_id],
                'certificate_name': row[1],
                'major': row[2],
                'institute_name': row[3],
                'start_date': row[4],
                'end_date': row[5],
            }
            
            client_edu.append(edu_table)
            
            edu_dictionary = {
                'client_education': client_edu
            }
            
            return edu_dictionary
        else:
            return 'No information about client education at the moment'
    elif request.method == "POST":
        certificate_name = request.form['certificate_name']
        major = request.form['major']
        institute_name = request.form['institute_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        table_instance.insert("certificate_name, major, institute_name, start_date, end_date", 
                        f"'{certificate_name}','{major}','{institute_name}', '{start_date}','{end_date}'")
        
        return redirect('http://localhost:3000/apply/client_skills')
    else:
        return 'No client experience at the moment'



@app.route('/client_profile/<id>/skills', methods=['GET', 'POST'])
def client_skills(id=0):
    client_skill = []
    
    table_instance = db_connect('client_skills')
    client = db_connect('client_profile')
    rows = table_instance.select()
    
    if request.method == "GET":
        id = client.select(condition=f"WHERE id='{id}'")
        for row in rows:
            cs_table = {
                'id': row[id],
                'skill_set': row[1],
                'skill_level': row[2],
            }
            
            client_skill.append(cs_table)
            
            cs_dict = {
                'client_skills': client_skills
            }
            
            return cs_dict
        else:
            return 'No information about client skills at the moment'
    elif request.method == "POST":
        skill_level = request.form['skill_level']
        skill_set = request.form['skill_set']
        table_instance.insert("skill_level, skill_set",
                        f"'{skill_level}','{skill_set}'")
        
        return redirect('http://localhost:3000/apply/thank_you')
    else:
        return 'No client experience at the moment'
    
 
'''Job Routes and Connections'''
@app.route('/job_post/', methods=['GET', 'POST'])
def job_post_route():
    data = request.form
    job_post = []
    
    table_instance = db_connect('job_post')
    
    rows = table_instance.select()
    if request.method == "GET":
        for row in rows:
            jp_table = {
                'id': row[0],
                'company_id': row[1],
                'role': row[2],
                'description': row[3],
                'skill_set': row[4],
                'location': row[5],
                'created_at': row[6],
                'closed_at': row[7]
            }
            
            job_post.append(jp_table)
            
            jp_dictionary = {
                'job_post': job_post
            }
            
            return jp_dictionary
    elif request.method == "POST":
        company_id = 1
        role = request.form['tittle']
        location = request.form['location']
        description = request.form['description']
        skill_set = request.form['skill_set']
        created_at = datetime.now()
        closed_at = datetime.now()
        table_instance.insert("company_id, role, location, description,skill_set, created_at, closed_at",
                        f"'{company_id}','{role}','{description}','{skill_set}', '{location}','{created_at}','{closed_at}'")
        
        return redirect('http://localhost:3000/')



@app.route('/company/', methods=['GET', 'POST'])
def company_route():
    c_ompany = []
    
    table_instance = db_connect('company')
    
    rows = table_instance.select()
    
    if request.method == 'GET':
        for row in rows:
            company_table = {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'website': row[3]
            }
            
            c_ompany.append(company_table)
            
            company_dict = {
                'company': c_ompany
            }
            
            return company_dict
    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        website = request.form['website']
        table_instance.insert("name, description, website", f"'{name}','{description}', '{website}'")
        return redirect(url_for('company_route'))
 
    
#JOB LOCATION ROUTE 
@app.route('/job_location', methods=['GET'])
def location_route():
    temp_location = []
    
    location_instance = db_connect('job_location')
    
    rows = location_instance.select()
    jobpost_instance = db_connect('job_post')
    
    jp_id = jobpost_instance.select(condition=f"WHERE id='{id}'")
    
    if request.method == "GET":
        for row in rows:
            location = {
                'id': row[0],
                'street_add': row[1],
                'city': row[2],
                'province': row[3],
                'country': row[4],
                'code': row[5],
                'job_id': row[jp_id],
            }
            
            temp_location.append(location)
            
            location_dict = {
                'job_location': temp_location
            }
            
            return location_dict
        else:
            return 'No information about job location at the moment'

  
#JOB TYPE ROUTE 
@app.route('/job_type', methods=['GET'])
def job_type_route():
    jtype = []
    
    job_type_instance = db_connect('job_type')
    
    rows = job_type_instance.select()
    jobpost_instance = db_connect('job_post')
    
    jp_id = jobpost_instance.select(condition=f"WHERE id='{id}'")
    
    for row in rows:
        typeJob = {
            "id" : row[0],
            "job_type ": row[1],
            "job_id": row[jp_id]
        }
        
        jtype.append(typeJob)
        
        type_dict = {
            'job_type': jtype
        }
        
        return type_dict
    else:
        return 'No information about job type at the moment'
    