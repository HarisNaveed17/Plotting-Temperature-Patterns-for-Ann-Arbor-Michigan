# Plotting-Temperature-Patterns-for-Ann-Arbor-Michigan
Highest and Lowest Temperature Variation by Day of Year over (2005 - 2015) in Ann Arbor, Michigan

## **Background:**
I did this little exercise as part of the U of Michigan's Applied Plotting course on Coursera. Since the course's matplotlib version is severely outdated (2.0.0), I decided to write a python script and upload it here.

## **The Data:**
The datafile 'weather_data.csv' is a subset of weather data downloaded from the NCEI (National Center for Environmental Information), a subdepartment of the NOAA (National Oceanic and Atmospheric Administration). Specifically, the data is from GHCN (Global Historical Climate Network) - Daily. The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.

The following variables are present in the datafile:

* **id** : station identification code
* **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
* **element** : indicator of element type
* **TMAX** : Maximum temperature (tenths of degrees C)
* **TMIN** : Minimum temperature (tenths of degrees C)
* **value** : data value for element (tenths of degrees C)

This data comes from 24 weather stations around Ann Arbor, Michigan, United States. You can find these station IDs and download their data from the NCEI website, it's SUPER neat: https://www.ncdc.noaa.gov/cdo-web/

The data on there is formatted slightly differently though, it simply mentions the TMAX, TMIN columns and no element indicator. I suggest adding the element column to that data, rather than modifying the code to run it in its original form.

## **The Script:**
The script has the following functions:
* find_min_max_temps(data): Finds the maximum and minimum temperatures ever recorded on a day of the year (1 - 365) over the period 2005 - 2015
* f2c(x): Converts Farhenheit to Celsius
* c2f(x): Converts Celsius to Farhenheit
* plot_graph(high, low, record_h_days, record_l_days, record_ls, record_hs, x_ax, x_labls): Plots the visual.

The script follows this process:
* Determines whether there are any leap years in the data and eliminates them. This is done because leap years can hinder our objective.
* Finds the maximum/minimum temperature ever recorded on a day of the year (1 - 365) over the period 2005 - 2015.
* Determines on what days were the 2015 max/min temperature values higher/lower than the highest/lowest values over the period 2005 - 2014.
* The actual x - axis is from 1 - 365, but with some date time magic, I transform it into months.
* It then plots the graph.

## **Conclusion:**
From the graph you'll see that the autumn and early winter of 2015 was significantly warmer than the same time of the year over the past 10 years. Furthermore, the late winter season of 2015 had the coldest temperatures over the past 10 years. Thus, it can be assumed that winter in 2015 was somewhat delayed (as far as temperature only is concerned) than the past 10 years.

This is a very basic visualization though, but great if you're just starting to get into matplotlib!
