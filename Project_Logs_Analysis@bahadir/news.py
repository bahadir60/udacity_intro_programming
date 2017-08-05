#! /usr/bin/python3

import psycopg2
import datetime
import sys

'''BEFORE RUNNING NEWS.PY, PLEASE GO TO README.MD FILE
FOR USING INSTRUCTIONS AND CREATES VIEW TABLES'''


def connect():
    """Connect function connect to the PostgreSQL database.
    Returns connection and cursor."""
    try:
        db = psycopg2.connect("dbname={}".format('news'))
        c = db.cursor()
        return db, c
    except:
        print("Unable to connect to database")
        sys.exit()


def articles_pop():
    db, c = connect()
    c.execute("SELECT * FROM ArticleNameNumber LIMIT 3")
    articles = c.fetchall()
    db.close()

    print("1. What are the most popular three articles of all time?")
    for article in articles:
        print(str(article[0]) + " - " + str(article[1]) + ' views')
    return articles


def authors_pop():
    db, c = connect()
    c.execute("SELECT authors.name, NumAuthorArticleTotal.result "
              "AS totalarticle "
              "FROM authors, NumAuthorArticleTotal "
              "WHERE authors.id = NumAuthorArticleTotal.authorId "
              "ORDER BY totalarticle DESC;")
    authors = c.fetchall()
    db.close()

    print("2. Who are the most popular article authors of all time?")
    for author in authors:
        print(str(author[0]) + " - " + str(author[1]) + ' views')
    return authors


def error_percentage():
    db, c = connect()
    c.execute("SELECT logdays.logday AS bigerrordays, "
              "CAST(errordays.total*100 AS FLOAT) / "
              "CAST(logdays.total AS FLOAT) AS percentage "
              "FROM logdays, errordays "
              "WHERE logdays.logday = errordays.errorday "
              "GROUP BY logdays.logday, "
              "errordays.total, logdays.total "
              "HAVING CAST(errordays.total*100 AS FLOAT) / "
              "CAST(logdays.total AS FLOAT) >= 1 "
              "ORDER BY bigerrordays ASC;")
    bigerrordays = c.fetchall()
    db.close()

    print("3. On which days did more than 1% of requests lead to errors?")
    for bigerrorday in bigerrordays:
        day = (bigerrorday[0]).date().strftime("%B %d, %Y")
        percentage = round(bigerrorday[1], 1)
        print(str(day) + " - " + str(percentage) + '% errors\n')
    return bigerrordays


if __name__ == "__main__":
    articles_pop()
    authors_pop()
    error_percentage()
