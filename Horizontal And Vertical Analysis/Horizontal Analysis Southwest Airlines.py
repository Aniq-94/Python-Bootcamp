# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:30:50 2022

@author: aniqa
"""
#Import Necessary libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#We are using csv downloads from SEC EDGAR for 10-K filings from the periods ending 2017 - 2021
#For the purposes of easy data transformation, the structure of the csv has been changed by transposing the data
#Data transposition in excel allows much easier plotting using seaborn
#A copy of the sample file can be found at this onedrive URL:https://cometmail-my.sharepoint.com/:x:/g/personal/axa210345_utdallas_edu/EfWMMJlYurhFn3P0oFzTaL8BCGBfXeq6sbmrN7qmypVTGw?e=Pxfqei

#import csv using pandas
income_statement = pd.read_csv('C:/Users/aniqa/OneDrive - The University of Texas at Dallas/Documents/Courses/Semester_1/Python_Programming/SOUTHWEST_10K_2017-2021_Transposed.csv')

#Convert csv to datafram
income_statement = pd.DataFrame(income_statement)

#Select necessary columns and cast into new dataframe
income_statement_refined = income_statement[["Year Ended", "NET INCOME (LOSS)", "Total operating revenues","Total operating expenses, net"]]

#use melt function to condense dataframe so that we can use multiple lines on the same graph using hue parameter in seaborn
income_statement_melt = income_statement_refined.melt("Year Ended",var_name='Line Item',value_name="Amount (billions of USD)")

#set size of the figure using matplotlib
plt.figure(figsize=(10,6))
#create line plot using seaborn
plot = sns.lineplot(data = income_statement_melt, x = "Year Ended", y = "Amount (billions of USD)", hue = "Line Item")

#set title of plot using matplotlibe
plt.title("Southwest Airlines Income Trend")

#print statement containing analysis
print("As can be seen the net income, operating revenues and operating expenses follow a similar trajectory\n\nIn the pandemic era we see Southwest incurring losses due to higher drop in operating revenues with a lower corresponding decrease in operating expenses (likely due to pausing of flights during the pandemic while retaining staff).\n")
print("Post pandemic the firm has seen a return to profitability but not to pre-pandemic levels")