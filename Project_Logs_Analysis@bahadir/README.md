#This readme file for Logs Analysis Project
=================================
Describe-Summary:
-----------------
At first create tables after then run python file (news.py)
At first creating table for first function and second creating table for second function
Thirt and forth creating tables for thirt function
Pyhton file include 3 function to answer project necessities.
For run use 'How to run' below. 
Test results showing the picture 'program_output.png'
For clearance for Pep8, check picture 'pip8_online_check.png'
=================================

How to run:
-----------
1. copy 'news.py' to vagrant file '/newsdata' folder
2. open your command and in vagrant run $ vagrant ssh (if you did not vagrant up before first at first $vagrant up)  
3. $ cd /vagrant/newsdata
4. $ psql -d news (if newsdata.sql did not use before: $ psql -d news -f newsdata.sql)
5. Create tables one by one as given below:

'''CREATE ArticleNameNumber VIEW WITH TWO COLUMN. FIRST COLUMN IS ARTICLES TITLE AND 
SECOND IS HOWMANY THIS TITLE IN LOG'''

Copy below for create first table:
--------------------------------- 
CREATE VIEW ArticleNameNumber AS 
SELECT articles.title, count(log.path) as number 
FROM articles, log 
WHERE '/article/' || articles.slug=log.path  
GROUP BY articles.title 
ORDER BY number DESC;

'''CREATE NumAuthorArticleTotal VIEW WITH TWO COLUMN. FIRST COLUMN IS AUTHORSID AND 
SECOND IS HOWMANY ARTICLES HAVE THIS ID'''

Copy below for create second table:
--------------------------------- 
CREATE VIEW NumAuthorArticleTotal AS 
SELECT articles.author as authorId , SUM(ArticleNameNumber.number) as result 
FROM articles, ArticleNameNumber 
WHERE ArticleNameNumber.title = articles.title 
GROUP BY articles.author;

'''CREATE errordays and logdays VIEWS ARE WITH TWO COLUMN. FIRST COLUMNS OF EACH IS ERROR DAYS AND 
ALL LOG DAYS. SECOND COLUMN OF EACH IS HOWMANY CONNECTION MADE BY EVERY DAY AND IT'S ERROR ONES'''

Copy below for create thirth table:
--------------------------------- 
CREATE VIEW errordays AS 
SELECT date_trunc('day', time) as errorday, COUNT(status) as total 
FROM log 
WHERE status != '200 OK' 
GROUP BY errorday 
ORDER BY errorday ASC;

Copy below for creat forth table:
--------------------------------- 
CREATE VIEW logdays AS 
SELECT date_trunc('day', time) as logday, COUNT(status) as total 
FROM log 
GROUP BY logday 
ORDER BY logday ASC;

6. After creating tables run $ \q command for return /newsdata folder
7. use command $ python news.py
8. Results should be on screen
9. For test results and usage go to 'program_output.png'
