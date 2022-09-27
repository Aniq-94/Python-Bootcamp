# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:30:50 2022

@author: aniqa
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

income_statement = pd.read_csv('C:/Users/aniqa/OneDrive - The University of Texas at Dallas/Documents/Courses/Semester_1/Python_Programming/SOUTHWEST_10K_2017-2021_Transposed.csv')

income_statement = pd.DataFrame(income_statement)

income_statement_refined = income_statement[["Year Ended", "NET INCOME (LOSS)", "Total operating revenues","Total operating expenses, net"]]

print(income_statement_refined)

income_statement_melt = income_statement_refined.melt("Year Ended",var_name='Line Item',value_name="Amount (billions of USD)")



plt.figure(figsize=(10,6))
plot = sns.lineplot(data = income_statement_melt, x = "Year Ended", y = "Amount (billions of USD)", hue = "Line Item")
plt.title("Southwest Airlines Income Trend")

print("As can be seen the net income, operating revenues and operating expenses follow a similar trajectory\n\nIn the pandemic era we see Southwest incurring losses due to higher drop in operating revenues with a lower corresponding decrease in operating expenses (likely due to pausing of flights during the pandemic while retaining staff).\n")
print("Post pandemic the firm has seen a return to profitability but not to pre-pandemic levels")