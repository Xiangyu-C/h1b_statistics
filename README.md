## The problem
This repo was built to answer Insight Data Engineer Fellowship challenge to output statistics of h1b visa data (top 10 occupations and top 10 states) supplied as csv file with ';' as the separator. Each file contains records of all the filed h1b visa and the information about each application. The challenge is to parse the file and calculate all the certified applications and count top 10 occupations based on the soc code and the top 10 states of the worker as txt files. 
## My approach
My approach was to read in the file header first. Then identify the columns I want (such as case_status, soc_name and work_state). I use regex to catch a pattern containing those key words since for different years, the column names are different. After finding the index of these columns, I then loop through each row to grab corresponding values of soc_name and work_state given the condition that the case has been certified by the case_status column. I then use Counter to help me find the top 10 occupations and top 10 states and write them into two separate txt files with proper headings.
## Instruction
To see the results of top occupations and top states: <br>
1.Put any of your input file in the input folder and change the name to h1b_input.csv. <br>
2.Execute the run.sh file in terminal and the two txt files will be outputed in the output folder.

This has both passed the insight testsuite in the terminal and also the website provided by Insight. I initially wrote the code to be able to process multiple csv input files and output 2 files per input but then I realized that Insight only asked for 1 input file so I modifed the code. Since it looks like the file name for input file is fixed so I took out code to search for the file first then feed the found file name to the function for parsing. To me, Insight is very implicit about this.
