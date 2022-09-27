# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:57:46 2022

@author: aniqa
"""

#Vertical Analysis of Southwest Airlines for 10-Q for March 31, 2021
#We get csv for 10-Q for southwest airlines from EDGAR filings
#CSV is transformed by removing the top two columns
#csv can be found on the following onedrive URL: https://cometmail-my.sharepoint.com/:x:/g/personal/axa210345_utdallas_edu/Ebqs_t7jph1PpliyBGpjNewBMpvmhTP0tEFbirSvyWuLIQ?e=BaOW5q
    
#import necessary libraries
import pandas as pd
import dataframe_image as dfi

#read income statement into pandas
income_statement = pd.read_csv("C:/Users/aniqa/OneDrive - The University of Texas at Dallas/Documents/Courses/Semester_1/Python_Programming/Vertical Analysis/SOUTHWEST_10Q_CLEANED.csv")

#cast as pandas dataframe
income_statement = pd.DataFrame(income_statement)

#drop all null columns
income_statement = income_statement.dropna()

#reset column index after dropping nulls
income_statement = income_statement.reset_index(drop=True)


#create dictionary of column names to be converted to float for mathematical operations
    
convert_dict = {"Mar. 31, 2021":float,
                "Mar. 31, 2020":float}

#convert numerical columns into float
income_statement = income_statement.astype(convert_dict)


#divide all rows in income statement by the topline (operating revenue)
vertical_analysis = income_statement.div(income_statement.iloc[0, 1:])*100

#since performing the divide operation removes all string values from the first column, we replace the first column
#of vertical analysis with the first column of the original income statement
vertical_analysis.loc[:,['Line Item']] = income_statement['Line Item']

#test vertical analysis output
#print(vertical_analysis)

#export vertical analysis into png
dfi.export(vertical_analysis,'Vertical_Analysis_final.png')

#print analysis based on observations
print("Vertical analysis shows that net income as a percentage of revenue has increased year over year for the first quarter.\nIn 2020 Southwest actually incurred a loss, whereas in the current year they have turned a profit, albeit with a low operating margin compared to pre-pandemic levels as shown by the horizontal analysis.\n\n")
print("The overall output looks positive for the company if we look at basic measures of revenue, but more comprehensive analysis is needed")