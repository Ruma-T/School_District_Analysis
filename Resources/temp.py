# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Dependencies and Setup
import pandas as pd

# File to Load (Remember to change the path if needed.)
school_data_to_load = "schools_complete.csv"
student_data_to_load = "students_complete.csv"

# Read the School Data and Student Data and store into a Pandas DataFrame
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)

# Cleaning Student Names and Replacing Substrings in a Python String
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

# Check names.
student_data_df.head(10)

# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np
# Step 2. Use the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.
#row_df = student_data_df.loc[(student_data_df.grade=='9th') & (student_data_df.school_name=='Thomas High School'),"reading_score"]
#student_data_df.loc[(student_data_df.grade=='9th') & (student_data_df.school_name=='Thomas High School'),"reading_score", "math_score"] = np.nan
#row_df = student_data_df.loc[(student_data_df.grade=='9th') & (student_data_df.school_name=='Thomas High School'),"reading_score", "math_score"]
per_school_counts = student_data_df.set_index(["school_name" == "Thomas High School"]),["grade" == "9th",:]
per_school_counts
