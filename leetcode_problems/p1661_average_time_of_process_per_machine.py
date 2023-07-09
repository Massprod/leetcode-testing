
# SQL schema:
# DROP TYPE IF EXISTS activity_type_enum;
# CREATE TYPE activity_type_enum AS ENUM('start', 'end');
# DROP TABLE IF EXISTS activity;
# Create table If Not Exists Activity (machine_id int, process_id int, activity_type activity_type_enum, timestamp float);
# Truncate table Activity;
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'start', '0.712');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'end', '1.52');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'start', '3.14');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'end', '4.12');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'start', '0.55');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'end', '1.55');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'start', '0.43');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'end', '1.42');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'start', '4.1');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'end', '4.512');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'start', '2.5');
# insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'end', '5');
# -------------------
# There is a factory website that has several machines each running the same number of processes.
# Write an SQL query to find the average time each machine takes to complete a process.
# The time to complete a process is the 'end' timestamp minus the 'start' timestamp.
# The average time is calculated by the total time to complete
#   every process on the machine divided by the number of processes that were run.
# The resulting table should have the machine_id along with the average time as processing_time,
#   which should be rounded to 3 decimal places.
# Return the result table in any order.

# PostgreSQL query:
# SELECT
# e1.machine_id,
# ROUND(SUM(CASE WHEN e1.activity_type = 'start' THEN -e1.timestamp
# 		    ELSE e1.timestamp
# 		    END)::decimal
# 	    /
# 	    ((SELECT COUNT(e2.machine_id)
# 	      FROM activity AS e2
# 	      WHERE e2.machine_id = e1.machine_id)::decimal / 2
# 	    ), 3) AS processing_time
# FROM activity AS e1
# GROUP BY e1.machine_id
# ORDER BY e1.machine_id;
