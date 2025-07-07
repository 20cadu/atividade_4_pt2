from django.test import TestCase

# Create your tests here.
'''
set search_path to public;

select * from info_app_person;

INSERT INTO info_app_person(name, age, gender, email) VALUES ('Ana','20' , 'Female', 'ana@gmail.com');
INSERT INTO info_app_person(name, age, gender, email) VALUES ('Lucas','32' , 'Male', 'lucas@gmail.com');

select * 
    FROM info_app_person
WHERE name like 'L%'

delete from info_app_person where email='ana@gmail.com'

SELECT
  SPLIT_PART(name, ' ', 1) AS first_name,
  COUNT(*) AS total
FROM
  public.info_app_person
GROUP BY
  name
ORDER BY
  total DESC

SELECT * FROM info_app_person LIMIT 5;
'''