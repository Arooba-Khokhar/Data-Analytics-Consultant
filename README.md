# Data-Analytics-Consultant

## Part A

This test deals with a tool based data stack starting from web based data acquisition,
transfer and storage to a data warehouse and visualization in a BI tool.
It tests your ability to quickly get into (new) tools, setting them up and finding a solution that
works. It also gives you a good impression of what kind of tasks may come up during your
work at 9 friendly white rabbits. Note, you do not need to have prior knowledge of these
tools. You will find a coarse guideline and some hints below. The test description below does
not always exactly describe what is needed in this step, so you need to abstract. You can of
course always google for help yourself as you need.

1. Create accounts on following  sites
2. Create account on Segment
3. Create Google Analytics account
4. Create Service account 
5. Create Bigquery account 
6. Configure Cloud Platform
7. google analytics
8. Installing Cloud SDK
9. Google Data Studio


There are three steps to complete the task:

### Data Acquisition

Fork segment project
created github page (https://arooba-khokhar.github.io/pagestest/)

###  Data Warehouse

Create account on Segment and Add source
copy the Segment snippet


###  Visualize

Create an account with Google Data Studio


## Part B

### SQL

 Suppose you have a table that contains records about customers
(NAME,CITY,PROFESSION,AGE). When customer data changes an ETL process uploads
new versions of the record to the table. This will however not change the existing record of
the customer but rather add a new record with the new data. The ETL process fills a
columns “LOADDATE” with the current timestamp of when the upload happened. Sketch a
query that returns a list of cities and the number of customers currently living there.



## Part C

ETL/python: Complete the following python script which extracts public COVID data and
loads it into BigQuery. The data source provides the data in pivoted form, row are countries
and columns are dates. We need the unpivoted form where rows are facts with the
dimensions country and date. The script is missing the unpivoting operation.

