-- Table: UserActivity
-- +------------------+---------+
-- | Column Name      | Type    | 
-- +------------------+---------+
-- | user_id          | int     |
-- | activity_date    | date    |
-- | activity_type    | varchar |
-- | activity_duration| int     |
-- +------------------+---------+
-- (user_id, activity_date, activity_type) is the unique key for this table.
-- activity_type is one of ('free_trial', 'paid', 'cancelled').
-- activity_duration is the number of minutes the user spent on the platform that day.
-- Each row represents a user's activity on a specific date.
-- A subscription service wants to analyze user behavior patterns.
-- The company offers a 7-day free trial, after which users can subscribe to a paid plan or cancel. Write a solution to:

-- Find users who converted from free trial to paid subscription
-- Calculate each user's average daily activity duration during their free trial period (rounded to 2 decimal places)
-- Calculate each user's average daily activity duration during their paid subscription period (rounded to 2 decimal places)
-- Return the result table ordered by user_id in ascending order.

--  -------------------------

-- working_sol 83.89% -> 295ms
SELECT *
FROM 
(SELECT
    user_id,
    ROUND(AVG(CASE WHEN "free_trial" = activity_type
         THEN activity_duration
        --  We need to use `NULL` because AVG() will consider any value as an extra
         ELSE NULL
    END), 2) as trial_avg_duration,
    ROUND(AVG(CASE WHEN "paid" = activity_type
         THEN activity_duration
         ELSE NULL
    END), 2) as paid_avg_duration
FROM UserActivity
GROUP BY user_id
ORDER BY user_id) as t1
WHERE t1.paid_avg_duration <> 0;

