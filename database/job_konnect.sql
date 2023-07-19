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
  "client_id" integer,
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
  "client_id" integer,
  "certificate_name" varchar,
  "major" varchar,
  "institute_name" varchar,
  "start_date" timestamp,
  "end_date" timestamp
);

CREATE TABLE "client_skills" (
  "client_id" integer,
  "skill_set_id" integer,
  "skill_level" integer
);

CREATE TABLE "skill_set" (
  "id" SERIAL,
  "skill_set_name" varchar
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
  "location" varchar,
  "created_at" timestamp,
  "closed_at" timestamp
);

INSERT INTO job_post (company_id, role, description, location
  )
VALUES (
    1,
    'Web Developer',
    'Looking for a junior developer',
    'Durban'
  );



CREATE TABLE "job_post_skill_set" (
  "skill_set_id" integer,
  "job_post_id" integer,
  "skill_level" integer
);

CREATE TABLE "job_post_activity" (
  "client_id" integer,
  "job_post_id" integer,
  "apply_date" date
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

ALTER TABLE "client_profile" ADD FOREIGN KEY ("id") REFERENCES "job_post_activity" ("client_id");

ALTER TABLE "client_experience" ADD FOREIGN KEY ("client_id") REFERENCES "client_profile" ("id");

ALTER TABLE "client_education" ADD FOREIGN KEY ("client_id") REFERENCES "client_profile" ("id");

ALTER TABLE "client_skills" ADD FOREIGN KEY ("client_id") REFERENCES "client_profile" ("id");

ALTER TABLE "client_skills" ADD FOREIGN KEY ("skill_set_id") REFERENCES "skill_set" ("id");

ALTER TABLE "job_post" ADD FOREIGN KEY ("id") REFERENCES "job_post_activity" ("job_post_id");

ALTER TABLE "job_post" ADD FOREIGN KEY ("company_id") REFERENCES "company" ("id");

ALTER TABLE "job_post_skill_set" ADD FOREIGN KEY ("job_post_id") REFERENCES "job_post" ("id");

ALTER TABLE "job_post_skill_set" ADD FOREIGN KEY ("skill_set_id") REFERENCES "skill_set" ("id");

ALTER TABLE "job_post_skill_set" ADD FOREIGN KEY ("skill_level") REFERENCES "client_skills" ("skill_level");
