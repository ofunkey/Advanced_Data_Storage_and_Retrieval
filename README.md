# Advanced_Data_Storage_and_Retrieval - Surfs Up!
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## 1 - Climate Analysis and Exploration
In this analysis, Python, SQLAlchemy and Matplotlib are used for the data exploration of your climate database. 
* Database: hawaii.sqlite file
* Create_engine to connect to your sqlite database using SQLAlchemy.
* Reflect the tables into classes and save a reference to those classes

### Precipitation Analysis
* Retrieve the last 12 months of precipitation data.
* Select only the date and prcp values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results using the DataFrame plot method.
* Use Pandas to print the summary statistics for the precipitation data

![prep ](https://github.com/ofunkey/Advanced_Data_Storage_and_Retrieval/blob/master/Surfs%20Up/Images/precipitation.png)

### Station Analysis
* Calculate the total number of stations.
* Find the most active stations.
* List the stations and observation counts in descending order.
* Which station has the highest number of observations?
    using functions such as func.min, func.max, func.avg, and func.count.
* Retrieve the last 12 months of temperature observation data (tobs) by filter by the station with the highest number of observations.
* Plot the results as a histogram with bins=12.

![histogram](https://github.com/ofunkey/Advanced_Data_Storage_and_Retrieval/blob/master/Surfs%20Up/Images/temperature_results_histogram.png)


## 2 - Climate App
Design a Flask API based on the queries.

### Routes
* /
    *   Home page.
    *   List all routes that are available.
*   /api/v1.0/precipitation
    *   Convert the query results to a Dictionary using date as the key and prcp as the value.
    *   Return the JSON representation of the dictionary.
*   /api/v1.0/stations
    *   Return a JSON list of stations from the dataset.
*   /api/v1.0/tobs
    *   query for the dates and temperature observations from a year from the last data point.
    *   Return a JSON list of Temperature Observations (tobs) for the previous year.
*   /api/v1.0/<start> and /api/v1.0/<start>/<end>
    *   Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    *   When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    *   When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    
    
##  Other Analyses
### Temperature Analysis I
Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
*   Use SQLAlchemy or pandas's read_csv().
*   Identify the average temperature in June at all stations across all available years in the dataset as well as for December temperature.
*   Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II
*   Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").
*   Plot the min, avg, and max temperature from your previous query as a bar chart.
*   Use the average temperature as the bar height.
*   Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).

![trip_avg](https://github.com/ofunkey/Advanced_Data_Storage_and_Retrieval/blob/master/Surfs%20Up/Images/trip_avg_temp.png)


##  Daily Rainfall Average
*   Calculate the rainfall per weather station using the previous year's matching dates.
*   Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
*   Create a list of dates for the trip in the format %m-%d. 
*   Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
*   Use Pandas to plot an area plot (stacked=False) for the daily normals.

![daily_rain](https://github.com/ofunkey/Advanced_Data_Storage_and_Retrieval/blob/master/Surfs%20Up/Images/daily_normals.png)


