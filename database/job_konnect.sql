CREATE TABLE "client_profile" (
  "id" SERIAL PRIMARY KEY,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "number" integer,
  "address" varchar,
  "current_salary" varchar
);



CREATE TABLE "client_experience" (
  "id" integer,
  "current_job" varchar,
  "start_date" timestamp,
  "end_date" timestamp,
  "company_name" varchar,
  "job_location_city" varchar,
  "job_location_state" varchar,
  "job_location_country" varchar,
  "description" varchar
);



CREATE TABLE "client_education" (
  "id" integer,
  "certificate_name" varchar,
  "major" varchar,
  "institute_name" varchar,
  "start_date" timestamp,
  "end_date" timestamp
);

CREATE TABLE "client_skills" (
  "id" SERIAL PRIMARY KEY,
  "skill_set" VARCHAR,
  "skill_level" integer
);

INSERT INTO client_skills (id, skill_set, skill_level)
VALUES (
  1,
    'Communication',
    7
  );


CREATE TABLE "company" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "website" varchar
);

INSERT INTO company ( name, description, website)
VALUES (
    'Lexis Nexis',
    'Solar Energy Company',
    'lexisnexis.co.za'
  );

INSERT INTO company (name, description, website)
VALUES (
    'Vodacom',
    'Global network company',
    'vodacom.co.za'
  );

INSERT INTO company (name, description, website)
VALUES (
    'Apple',
    'Digital Technology Company',
    'apple.co'
  );

INSERT INTO company (name, description, website)
VALUES (
    'ILab',
    'Gaming company',
    'i-lab_tech.co'
  );


CREATE TABLE "job_post" (
  "id" SERIAL PRIMARY KEY ,
  "company_id" integer,
  "role" varchar,
  "description" varchar,
  "skill_set" varchar,
  "location" varchar,
  "created_at" timestamp,
  "closed_at" timestamp
);



CREATE TABLE job_location (
  id SERIAL PRIMARY KEY,
  street_add TEXT NOT NULL,
  city TEXT NOT NULL,
  province TEXT NOT NULL,
  country TEXT NOT NULL,
  code INT NOT NULL,
  job_id INT NOT NULL,
  FOREIGN KEY(job_id) REFERENCES job_post(id)
);

CREATE TABLE job_type (
  id SERIAL PRIMARY KEY,
  job_type TEXT NOT NULL,
  job_id INT NOT NULL,
  FOREIGN KEY(job_id) REFERENCES job_post(id)
);

ALTER TABLE "client_experience" ADD FOREIGN KEY ("id") REFERENCES "client_profile" ("id");

ALTER TABLE "client_education" ADD FOREIGN KEY ("id") REFERENCES "client_profile" ("id");

ALTER TABLE "client_skills" ADD FOREIGN KEY ("id") REFERENCES "client_profile" ("id");

ALTER TABLE "job_post" ADD FOREIGN KEY ("company_id") REFERENCES "company" ("id");

