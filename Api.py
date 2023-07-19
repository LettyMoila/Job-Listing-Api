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
        id = 11
        role = request.form['tittle']
        location = request.form['location']
        description = request.form['description']
        created_at = datetime.now()
        table_instance.insert("id ,company_id, role, location, description, created_at, closed_at", f"'{id}','{company_id}','{role}','{description}', '{location}','{created_at}','{closed_at}'")
        
        return 'success'


@app.route('/job_post_activity')
def job_post_activity_route():
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
@app.route('/job_post_skill_set') #TO FIX >> add client id and skill set id
def job_post_skill_set():
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
def skill_set(id=0):
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
    