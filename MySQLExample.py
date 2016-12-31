import MySQLdb as mdb
import sys

def dbExample1():
    try:
        con = mdb.connect('localhost', 'ken', 'branson', 'testdb')

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO Person VALUES(null, 'Cheryl', 'Branson', '1972-04-03')")

        cur.execute("SELECT * FROM PERSON")

        results = cur.fetchall()
        desc= cur.description
        print desc[0][0], desc[1][0], desc[2][0], desc[3][0]
        for row in results:
            print row["PersonID"], row["FirstName"], row["LastName"], row["DateOfBirth"]

        con.commit()

    except mdb.Error as e:
        if con:
            con.rollback()

        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:

        if con:
            con.close()

def dbExample2():
    con = mdb.connect('localhost', 'ken', 'branson', 'testdb')
    # "with" context manager automatically takes care of doing commit/rollback and try/except/finally logic
    with con:

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO Person VALUES(null, 'Cheryl', 'Branson', '1972-04-03')")

        cur.execute("SELECT * FROM PERSON")

        results = cur.fetchall()
        desc= cur.description
        print desc[0][0], desc[1][0], desc[2][0], desc[3][0]
        for row in results:
            print row["PersonID"], row["FirstName"], row["LastName"], row["DateOfBirth"]

        con.commit()

