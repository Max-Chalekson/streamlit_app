This streamlit application performs a simple EDA

## Structure of Application

- Project Title: Max's Streamlit Application
- Project Description: This streamlit application allows the user to upload a .csv file of their choice on the left side of the page. From there, the user can select the data type of the column they wish to run data analysis on. (1) If they choose to run analyis of Numerical data, they then can select two columns of choice. (2) If they choose analysis of Categorical data, they get to select one column of data.

(1) Numerical Data Analysis:
In the center of the website, after selecting the columns, there is a checkbox where the user can view the data frame of the .csv file that they uploaded as well as basic statistics of the dataframe, thus givign info on number of rows, columns, and the number of columns that are of the following object types: categorical, numerical, boolean, date/time. 

Below that, there is a boxplot customizer, that allows the user to pick a color of their choice, and set the title of their choice. The data that is used for the boxplot is the what the user set as their first and second column of choice. The colums that the user sets as their first and second column will be displayed on the x and y axes respectively. There is also a download button that will download a .png file of the boxplot with the name of the file being that of the boxplot title that is set by the user.

(2) Categorical Data Analysis:
In the center of the website, after selecting the column, there is a checkbox where the user can view the data frame of the .csv file 
that they uploaded as well as basic statistics of the dataframe, thus givign info on number of rows, columns, and the number of columns that are of the following object types: categorical, numerical, boolean, date/time. The viewer in this setting, can also view the object proportions of the dataset (ex: proportion of columns that are numerical, categorical, boolean, etc.). Below, the user is also able to customize a barplot with color of choice, that utilizes their column of choice, which is named on the x-axis. The user has the customization of the title of the barplot, and are also able to download a .png file of the boxplot with the name of the file being that of the boxplot title that is set by the user.