from flask import Flask, redirect, url_for, request
from flask_cors import CORS
from datetime import datetime
import json

import config

from db_connect import db_connect

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Job Listing API"

'''Client Routes and connections'''
@app.route('/client_profile/<id>', methods=['GET', 'POST'])
def client_profile_route(id):
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

#CLIENT EXPERIENCE
@app.route('/client_profile/<client_id>/experience', methods=['GET', 'POST'])
def client_experience_route(client_id=0):
    client_exp = []
    
    table_instance = db_connect('client_experience')
    client = db_connect('client_profile')
    
    
    if request.method == "GET":
        client_id = client.select(condition=f"WHERE id='{id}'")
        rows = table_instance.select()
        for row in rows:
          
            exp_table = {
                'client_id': row[client_id],
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
        client_id = client.select(condition=f"WHERE id='{id}'")
        current_job = request.form['current_job']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        company_name = request.form['company_name']
        job_location_city = request.form['job_location_city']
        job_location_state = request.form['job_location_state']
        job_location_country = request.form['job_location_country']
        description = request.form['description']
        table_instance.insert("client_id, current_job, start_date, end_date, company_name, job_location_city, job_location_state, job_location_country, description", 
                        f"'{client_id}','{current_job}','{start_date}','{end_date}', '{company_name}','{job_location_city}','{job_location_state}','{job_location_country}','{description}'")
        
        return 'success'
    else:
        return 'No client experience at the moment'


# CLIENT EDUCATION
@app.route('/client_profile/<id>/education')
def client_education_route(id=0):
    client_edu = []
    
    table_instance = db_connect('client_education')
    client = db_connect('client_profile')
    
    client_id = client.select(condition=f"WHERE id='{id}'")
    
    rows = table_instance.select()
    
    for row in rows:
        edu_table = {
            'client_id': row[client_id],
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
        return 'No information about Jclient education at the moment'
    
# CLIENT SKILLS
@app.route('/client_profile/<id>/skills')
def client_skills(id=0):
    client_skills = []
    
    table_instance = db_connect('client_skills')
    client = db_connect('client_profile')
    
    client_id = client.select(condition=f"WHERE id='{id}'")
    skills = db_connect('skill_set')
    skill_id = skills.select(condition=f"WHERE id='{id}'")
    
    rows = table_instance.select()
    
    for row in rows:
        cs_table = {
            'client_id': row[client_id],
            'skill_set_id': row[skill_id],
            'skill_level': row[2]
        }
        
        client_skills.append(cs_table)
        
        cs_dict = {
            'client_skills': client_skills
        }
        
        return cs_dict
    else:
        return 'No information about client skills at the moment'
 
 
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
                'location': row[4],
                'created_at': row[5],
                'closed_at': row[6]
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
        created_at = datetime.now()
        closed_at = datetime.now()
        table_instance.insert("company_id, role, location, description, created_at, closed_at", f"'{company_id}','{role}','{description}', '{location}','{created_at}','{closed_at}'")
        
        return 'success'


@app.route('/client_profile/<client_id>/job_post/<job_post_id>/activity')
def job_post_activity_route(client_id=0, job_post_id=0):
    jp_activity = []
    
    table_instance = db_connect('job_post_activity')
    
    rows = table_instance.select()
    
    for row in rows:
        jpa_table = {
            'client_id': row[0],
            'job_post_id': row[1],
            'apply_date': row[2] 
        }
        
        jp_activity.append(jpa_table)
        
        jpa_dictionary = {
            'job_post_activity': jp_activity
        }
        
        return jpa_dictionary
    else:
        return 'No information about Job Posts Activity at the moment'
        

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

#JOB POST SKILL SET
@app.route('/job_post/<job_post_id>/skill_set/<skill_set_id>')
def job_post_skill_set(skill_set_id=0, job_post_id=0):
    jp_skill_set = []
    
    table_instance = db_connect('job_post_skill_set')
    
    rows = table_instance.select()
    
    for row in rows:
        jp_skill_set_table = {
            'skill_set_id': row[0],
            'job_post_id': row[1],
            'skill_level': row[2]
        }
        
        jp_skill_set.append(jp_skill_set_table)
        
        jp_skill_set_dict = {
            'job_post_skill_set': jp_skill_set
        }

        return jp_skill_set_dict
    else:
        return 'No information about Job Post Skill Sets at the moment'
    
    
#SKILL SET ROUTE
@app.route('/skill_set/', methods=['GET', 'POST']) 
def skill_set():
    skill_set = []
    
    table_instance = db_connect('skill_set')
    
    rows = table_instance.select()
    
    for row in rows:
        skill_set_table = {
            'id': row[0],
            'skill_set_name': row[1]
        }
        
        skill_set.append(skill_set_table)
        
        skill_set_dict = {
            'skill_set': skill_set
        }    
        return skill_set_dict
    else:
        return 'No information about Skill Sets at the moment'
    
#JOB LOCATION ROUTE 
@app.route('/job_location')
def location_route():
    temp_location = []
    
    location_instance = db_connect('job_location')
    
    rows = location_instance.select()
    
    for row in rows:
        location = {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'website': row[3]
        }
        
        temp_location.append(location)
        
        location_dict = {
            'job_location': temp_location
        }
        
        return location_dict
    else:
        return 'No information about job location at the moment'
    
#JOB TYPE ROUTE 
@app.route('/job_type')
def job_type_route():
    jtype = []
    
    job_type_instance = db_connect('job_type')
    
    rows = job_type_instance.select()
    
    for row in rows:
        typeJob = {
            "id" : row[0],
            "job_type ": row[1],
            "job_id": row[2]
        }
        
        jtype.append(typeJob)
        
        type_dict = {
            'job_type': jtype
        }
        
        return type_dict
    else:
        return 'No information about job type at the moment'
    