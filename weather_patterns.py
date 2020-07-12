import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def find_min_max_temps(data):
    grouped_high = data.groupby(['Month', 'Day', 'Element']).max()
    grouped_low = data.groupby(['Month', 'Day', 'Element']).min()
    high_temps = []
    low_temps = []
    for i in range(1, 13):
        x = grouped_high.xs((i, 'TMAX'), level=('Month', 'Element'))
        temps = np.array(x['Data_Value'])
        high_temps.extend(temps)

    for i in range(1, 13):
        y = grouped_low.xs((i, 'TMIN'), level=('Month', 'Element'))
        temps_l = np.array(y['Data_Value'])
        low_temps.extend(temps_l)

    # Division by 10 to convert Tenths of Celsius to Celsius
    high_temps = (np.array(high_temps, dtype='int64')) / 10
    low_temps = (np.array(low_temps, dtype='int64')) / 10
    return high_temps, low_temps, grouped_high


def c2f(x):
    return (1.8 * x) + 32


def f2c(x):
    return (x - 32) / 1.8


def plot_graph(high, low, record_h_days, record_l_days, record_ls, record_hs, x_ax, x_labls):
    fig = plt.figure()
    plt.plot(high, color='orange', alpha=0.35, label="Highest ('05 -'14)")
    plt.plot(low, color='blue', alpha=0.35, label="Lowest ('05 -'14)")
    plt.scatter(record_l_days, record_ls, color='black', marker='.', label="2015(Lower than lowest '05 -'14 value)",
                s=75)
    plt.scatter(record_h_days, record_hs, color='red', marker='.', label="2015(Higher than highest '05 -'14 value)",
                s=75)
    plt.xlim(1, 365)

    plt.xticks(x_ax, x_labls)
    fig.autofmt_xdate(ha='left', rotation=0)

    secaxy = plt.gca().secondary_yaxis('right', functions=(c2f, f2c))
    secaxy.set_ylabel('Fahrenheit (F)', fontsize='large')
    secaxy.spines['right'].set_visible(False)

    plt.gca().fill_between(range(len(high)),
                           high, low,
                           facecolor='grey',
                           alpha=0.15)
    plt.legend(loc=4, frameon=False, fontsize='medium')
    plt.box(on=False)
    plt.ylabel('Celsius ($^\circ$C)', fontsize='large')
    plt.title('Highest & Lowest Temperatures by Day of Year (2005 - 2015)\n Ann Arbor, Michigan, USA',
              fontweight='bold')
    plt.show()


# Loading and setting up the data frames
weather_data = pd.read_csv('weather_data (Coursera version).csv', index_col='Date', parse_dates=True)
weather_data.sort_index(inplace=True)
weather_data_14 = weather_data.drop(weather_data['2015-01-01':].index, axis=0)
weather_data_15 = weather_data['2015-01-01':]

# Removing the leap years
leap_years = pd.unique(weather_data_14[weather_data_14.index.is_leap_year == True].index.year)

year_1 = '%d-02-29' % leap_years[0]
year_2 = '%d-02-29' % leap_years[1]
weather_data_14 = weather_data_14[(weather_data_14.index != year_1) &
                                  (weather_data_14.index != year_2)]
weather_data_14['Month'] = weather_data_14.index.month
weather_data_14['Day'] = weather_data_14.index.day
weather_data_14 = weather_data_14.reset_index(drop=True)

# Finding the maximum and minimum temperatures ever recorded by day of the year ( 1 - 365) over 2005 - 2014 & 2005
high_temps, low_temps, grouped_high = find_min_max_temps(weather_data_14)
weather_data_15_c = weather_data_15.copy()  # To avoid set with copy warning (not necessary)
weather_data_15_c['Month'] = weather_data_15_c.index.month
weather_data_15_c['Day'] = weather_data_15_c.index.day
high_temps_15, low_temps_15, grouped_high_15 = find_min_max_temps(weather_data_15_c)

# Finding the days on which the 2015 recordings were higher than those over the 2005 - 2014 period
record_highs = np.where(high_temps_15 > high_temps, high_temps_15, 0)
record_highs_days = np.nonzero(record_highs)
record_highs_days = record_highs_days[0]  # nonzero returns indices of nonzero values as tuples. In this case
# the tuples has no second values since our array is 1-D
record_highs = record_highs[~np.equal(record_highs, 0)].astype(int)

# Finding the days on which the 2015 recordings were lower than those over the 2005 - 2014 period
record_lows = np.where(low_temps_15 < low_temps, low_temps_15, 0)
record_lows_days = np.nonzero(record_lows)
record_lows_days = record_lows_days[0]
record_lows = record_lows[~np.equal(record_lows, 0)].astype(int)

# Defining the x-axis and its labels as months in a year
# Find the starting day of each month (1 for January, 32 for February, 60 for March and so on)
x_axis = [0]
d_prev = 0
for i in range(1, 12):
    d_current = len(grouped_high.xs(i, level='Month')) // 2  # can use group_high_15 as well. This is just to get the
    # number of days in each month.
    x_axis.append(d_current + d_prev)
    d_prev = x_axis[1 + (i - 1)]
x_axis = np.array([i + 1 for i in x_axis])
x_labels = pd.to_datetime(x_axis, format='%j').strftime('%b')

plot_graph(high=high_temps, low=low_temps, record_h_days=record_highs_days, record_l_days=record_lows_days,
           x_labls=x_labels, x_ax=x_axis, record_hs=record_highs, record_ls=record_lows)
