import MySQLdb

# this file will be checked by a script.
# make sure you dont change variable names like ans1, or q1
# make sure your database name is amazon
# and your tables are called links and metadata

# write your UNI
uni = "uni1234"

# after you're done, write down the answers below
ans1 = "Name of the Product"
ans2 = "Name of the Product"
ans3 = 5.1234
ans4 = 20
ans5 = 100
ans6 = 15

#ans6 comes from the Spark part

# SQL code begins
# connect to MySQL server
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="amazon")        # name of the data base

# The cursor object is your handle to the DB. 
# Use it to execute queries
cur = db.cursor()

def example():
	"""
	Example query to get the ID of our cat book
	"""
	# Use all the SQL you like
	cat_book = '"The Maine Coon Cat (Learning About Cats)"'
	cur.execute("SELECT * FROM metadata WHERE title="+cat_book)

	row = cur.fetchone()
	return row[1]

def q1():
	"""
	Code for q1 goes here
	"""
	ans1 = ""
	return ans1

def q2():
	"""
	Code for q2 goes here
	"""
	ans2 = ""
	return ans2

def q3():
	"""
	Code for q3 goes here
	"""
	ans3 = ""
	return ans3

def q4():
	"""
	Code for q4 goes here
	"""
	ans4 = ""
	return ans4

def q5():
	"""
	Code for q5 goes here
	"""
	ans5 = ""
	return ans5


ans0 = example()
print ans0

ans1 = q1()
print ans1

db.close()
