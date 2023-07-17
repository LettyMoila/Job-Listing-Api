from flask import Flask, send_file
from flask_cors import CORS

import config

from db_connect import db_connect

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Job Listing API"


# JOB POST ROUTE
@app.route('/job_post')
def job_post_route():
    job_post = []
    
    table_instance = db_connect('job_post')
    
    rows = table_instance.select()
    
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
    else:
        return 'No information about Job Posts at the moment'

# JOB POST ACTIVITY ROUTE
@app.route('/job_post_activity') #TO FIX
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
        


#COMPANY ROUTE 
@app.route('/company')
def company_route():
    c_ompany = []
    
    table_instance = db_connect('company')
    
    rows = table_instance.select()
    
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
    else:
        return 'No information about Companies at the moment'

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
@app.route('/skill_set') 
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
    