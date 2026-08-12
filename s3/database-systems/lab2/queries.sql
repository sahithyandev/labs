-- Find the IDs of students who take a course done at "Packard" building AND a course done at "Watson" building order by their ids (Ascending)
SELECT students_packard.ID
FROM (
		SELECT DISTINCT ID
		FROM takes
		WHERE course_id IN (
				SELECT course_id
				FROM section
				WHERE building = 'Packard'
			)
	) AS students_packard
	INNER JOIN (
		SELECT DISTINCT ID
		FROM takes
		WHERE course_id IN (
				SELECT course_id
				FROM section
				WHERE building = 'Watson'
			)
	) AS students_watson USING (ID)
ORDER BY ID ASC;
-- Find the course_id, prereq_id pairs for all the course_ids.
SELECT course.course_id,
	prereq_id
FROM course
	LEFT JOIN prereq ON course.course_id = prereq.course_id;
-- Find the title of the prerequisite course for "Database System Concepts"
SELECT course.title
FROM prereq
	JOIN course ON course.course_id = prereq.prereq_id
WHERE prereq.course_id = (
		SELECT course_id
		FROM course
		WHERE course.title = 'Database System Concepts'
	);
-- Create a view named "student_grades" containing each student's id,name, course_id and respective grade.
DROP VIEW IF EXISTS student_grades;
CREATE VIEW student_grades AS
SELECT student.ID,
	student.name,
	takes.course_id,
	takes.grade
FROM student
	JOIN takes ON student.ID = takes.ID;
-- Using the "student_grades" view find the name of the student who has obtained an "A" for course "BIO-101".
SELECT name
FROM student_grades
WHERE course_id = 'BIO-101'
	AND grade = 'A';
--  Find the names of the students who have not taken any course ever.
SELECT name
FROM (
		SELECT ID
		FROM student
		EXCEPT
		SELECT DISTINCT ID
		FROM takes
	) AS idle_students
	JOIN student ON student.ID = idle_students.ID
ORDER BY name;
-- Find names of students in biology department with their corresponding advisor ids.
SELECT name,
	advisor.i_ID
FROM student
	JOIN advisor ON advisor.s_ID = student.ID
WHERE student.dept_name = 'Biology';
--  Find the names of all the instructors from the “Finance” department (sort by instructor name in ascending order).
SELECT name
FROM instructor
WHERE dept_name = 'Finance'
ORDER BY name ASC;
-- Find the names of courses in the “Biology” department which 3 or more credits (sort by course title in ascending order).
SELECT title
FROM course
WHERE dept_name = 'Biology'
	AND credits >= 3
ORDER BY title ASC;
-- Find the names of students who are from the “Computer Science” department who have taken more than 50 credits  (sort by name in the ascending order) .
SELECT name
FROM student
WHERE dept_name = 'Comp. Sci.'
	AND tot_cred > 50
ORDER BY name ASC;
-- Find the names of all instructors who have taught courses during the 2010 “Summer” semester (sort by name in the ascending order).
SELECT instructor.name
FROM instructor
	RIGHT OUTER JOIN teaches ON instructor.id = teaches.ID
WHERE teaches.semester = 'Summer'
	AND teaches.year = 2010
ORDER BY instructor.name ASC;
-- Find the total amount that needs to be paid for the instructors in the “Comp. Sci.” Department.
SELECT SUM(salary) as total_salary
FROM instructor
WHERE dept_name = 'Comp. Sci.';
-- Find the number of instructors in “Finance” department.
SELECT COUNT(*)
FROM instructor
WHERE dept_name = 'Finance';
-- Find the name of the student who has taken the highest number of total credits.
SELECT name
FROM student
ORDER BY tot_cred DESC
LIMIT 1;
-- For the student with ID “45678”, show all course_id, title, year, and semester of all courses registered for by the student  (sort by course_id).
SELECT takes.course_id,
	course.title,
	takes.year,
	takes.semester
FROM takes
	JOIN course ON takes.course_id = course.course_id
WHERE takes.ID = '45678'
ORDER BY course_id;
-- Find the names of students who are supervised by instructor “Einstein” (sort by student name in the ascending order). 
SELECT student.name
FROM advisor
	JOIN instructor ON advisor.i_ID = instructor.ID
	JOIN student ON advisor.s_ID = student.ID
WHERE instructor.name = 'Einstein'
ORDER BY student.name;
-- Find the name of the course that is designated as a prerequisite by most number of courses (sort by course title in the ascending order).
SELECT course.title
FROM course
WHERE course.course_id = (
		SELECT prereq_id
		FROM prereq
		GROUP BY prereq_id
		ORDER BY COUNT(*) DESC
		LIMIT 1
	);
-- Find the names of all students who have taken any Comp. Sci. course ever (there should be no duplicate names and they should be sorted by student name in the ascending order). 
SELECT DISTINCT student.name
FROM student
	JOIN takes ON student.ID = takes.ID
	JOIN course ON takes.course_id = course.course_id
WHERE course.dept_name = 'Comp. Sci.'
ORDER BY student.name;
-- Display the IDs of all instructors who have never taught a course (sort by instructor ID in ascending order).
SELECT ID
FROM instructor
EXCEPT
SELECT DISTINCT ID
FROM teaches
ORDER BY ID;
-- As in Q12, but display the names of the instructors also, not just the IDs (sort by instructor name in ascending order).
SELECT non_teaching_instructors.ID,
	name
FROM (
		SELECT ID
		FROM instructor
		EXCEPT
		SELECT DISTINCT ID
		FROM teaches
	) AS non_teaching_instructors
	JOIN instructor ON instructor.ID = non_teaching_instructors.ID
ORDER BY name;
-- How many “A” grades have been given for the course “Intro. to Computer Science”
SELECT COUNT(*)
FROM takes
WHERE grade = 'A'
	AND course_id IN (
		SELECT course_id
		FROM course
		WHERE title = 'Intro. to Computer Science'
	);
-- Find the course names, year, semester, and grades obtained by the student “Shankar” (sort by course title in the ascending order).
SELECT course.title,
	takes.year,
	takes.semester,
	takes.grade
FROM takes
	JOIN course ON takes.course_id = course.course_id
WHERE takes.ID = (
		SELECT ID
		FROM student
		WHERE name = 'Shankar'
	)
ORDER BY course.title ASC;
-- List the names of all CS hundred level courses (Course codes that starts as CS-1). Sort by course title in descending order. 
SELECT title
FROM course
WHERE course_id LIKE 'CS-1%'
ORDER BY title DESC;
-- Find the names of departments who have instructors that get annual salaries between 60,000 to 80,000 (sort by dept_name in ascending order and there should be no duplicates). 
SELECT DISTINCT dept_name
FROM instructor
WHERE salary BETWEEN 60000 AND 80000
ORDER BY dept_name ASC;
-- List the names of instructors in ascending order with their respective salaries.
SELECT name,
	salary
FROM instructor
ORDER BY name ASC;
-- Find the names and average salaries of all departments whose average salary is greater than 40,000 (sort by dept_name in the ascending order).
SELECT department.dept_name,
	AVG(instructor.salary) AS avg_salary
FROM department
	JOIN instructor ON department.dept_name = instructor.dept_name
GROUP BY department.dept_name
HAVING AVG(instructor.salary) > 40000
ORDER BY department.dept_name ASC;
-- Find names of instructors with salary greater than that of some (at least one) instructor in the “Biology” department (sort by instructor name in ascending order).
SELECT instructor.name
FROM instructor
WHERE instructor.salary > (
		SELECT MIN(instructor.salary)
		FROM instructor
		WHERE instructor.dept_name = 'Biology'
	)
ORDER BY instructor.name ASC;