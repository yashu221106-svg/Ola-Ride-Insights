SET SQL_SAFE_UPDATES = 0;
UPDATE OLA_Cleaned_Data
SET
    V_TAT = NULLIF(TRIM(V_TAT), ''),
    C_TAT = NULLIF(TRIM(C_TAT), ''),
    Driver_Ratings = NULLIF(TRIM(Driver_Ratings), ''),
    Customer_Rating = NULLIF(TRIM(Customer_Rating), '');
    SELECT
    COUNT(*) AS Total_Rows,
    SUM(V_TAT IS NULL) AS Missing_V_TAT,
    SUM(C_TAT IS NULL) AS Missing_C_TAT,
    SUM(Driver_Ratings IS NULL) AS Missing_Driver_Ratings,
    SUM(Customer_Rating IS NULL) AS Missing_Customer_Rating
FROM OLA_Cleaned_Data;
ALTER TABLE OLA_Cleaned_Data
MODIFY V_TAT DECIMAL(10,2) NULL,
MODIFY C_TAT DECIMAL(10,2) NULL,
MODIFY Driver_Ratings DECIMAL(3,2) NULL,
MODIFY Customer_Rating DECIMAL(3,2) NULL;
DESCRIBE OLA_Cleaned_Data;

SELECT Date, Time
FROM OLA_Cleaned_Data
LIMIT 10;
ALTER TABLE OLA_Cleaned_Data
MODIFY COLUMN Date DATETIME NULL,
MODIFY COLUMN Time TIME NULL;
ALTER TABLE OLA_Cleaned_Data
MODIFY COLUMN Date DATETIME NULL,
MODIFY COLUMN Time TIME NULL;

DESCRIBE OLA_Cleaned_Data;

SELECT COUNT(*) AS Total_Rows
FROM OLA_Cleaned_Data;

-- Q1: Retrieve all successful bookings

SELECT *
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Success';

-- Q1: Verify total successful bookings

SELECT COUNT(*) AS Successful_Bookings
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Success';

-- Q2: Average ride distance for each vehicle type

SELECT
    Vehicle_Type,
    AVG(Ride_Distance) AS Average_Ride_Distance
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Success'
GROUP BY Vehicle_Type
ORDER BY Average_Ride_Distance DESC;

-- Q3: Total customer-cancelled rides

SELECT
    COUNT(*) AS Total_Customer_Cancellations
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Canceled by Customer';

-- Q4: Top 5 customers by number of successful rides

SELECT
    Customer_ID,
    COUNT(*) AS Total_Rides
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Success'
GROUP BY Customer_ID
ORDER BY Total_Rides DESC
LIMIT 5;

-- Q5: Driver cancellations due to personal and car-related issues

SELECT
    COUNT(*) AS Total_Driver_Cancellations
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Canceled by Driver'
AND Canceled_Rides_by_Driver = 'Personal & Car related issue';

-- Q6: Maximum and minimum driver ratings for Prime Sedan

SELECT
    MAX(Driver_Ratings) AS Maximum_Driver_Rating,
    MIN(Driver_Ratings) AS Minimum_Driver_Rating
FROM OLA_Cleaned_Data
WHERE Vehicle_Type = 'Prime Sedan'
AND Booking_Status = 'Success';

-- Q7: Retrieve all rides paid through UPI

SELECT *
FROM OLA_Cleaned_Data
WHERE Payment_Method = 'UPI';

-- Q7: Verify total UPI bookings

SELECT
    COUNT(*) AS Total_UPI_Bookings
FROM OLA_Cleaned_Data
WHERE Payment_Method = 'UPI';

-- Q8: Average customer rating per vehicle type

SELECT
    Vehicle_Type,
    AVG(Customer_Rating) AS Average_Customer_Rating
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Success'
GROUP BY Vehicle_Type
ORDER BY Average_Customer_Rating DESC;

-- Q9: Total booking value of successful rides

SELECT
    SUM(Booking_Value) AS Total_Successful_Booking_Value
FROM OLA_Cleaned_Data
WHERE Booking_Status = 'Success';

-- Q10: Incomplete rides with their reasons

SELECT
    Booking_ID,
    Booking_Status,
    Incomplete_Rides,
    Incomplete_Rides_Reason
FROM OLA_Cleaned_Data
WHERE Incomplete_Rides = 'Yes';

-- Q10: Count incomplete rides by reason

SELECT
    Incomplete_Rides_Reason,
    COUNT(*) AS Total_Incomplete_Rides
FROM OLA_Cleaned_Data
WHERE Incomplete_Rides = 'Yes'
GROUP BY Incomplete_Rides_Reason
ORDER BY Total_Incomplete_Rides DESC;