#!/usr/bin/env python
import MySQLdb
def conMySQL():
#connect function
errorMessage = 'cannot connect database, please check it'
try:
#gbk code-confuse,utf8?
conn = MySQLdb.connect(
host = 'localhost',
user = 'userinfo',
passwd = 'ljn7168396',
db = 'userinfo',
port = 3306,
charset = 'utf8'
)
return conn
#run sql
#cur.execute('')
except MySQLdb.Error, e:
print errorMessage
#Login
#empty value user, passwd, db
#user =
#passwd =
#db =
def createNewAccount(cutename, username, userpasswd, sex, years):
#return a connection
conn = conMySQL()	
cur = conn.cursor()
value = ['',
cutename,
username,
userpasswd,
sex,
years
]
#search user existence
cur.execute('SELECT * FROM
userinfo WHERE
username = %s', value[1])
findresult = cur.fetchall()
#exist user
if not findresult:
#php-style
#cur.execute("INSERT INTO users VALUES (NULL, " + "'" + username + "'" + ", NULL, '" + sex + "'")
cur.execute('INSERT INTO
users
VALUES(%s,%s,%s,%s,%s)' ,value
)
#IMPORTANT create new frnd table and feeling table
cur.execute('create table frnd_%s(
id int unsigned not null,
frndnum int unsigned not null auto_increment primary key,
frndid int unsigned not null
)',value[0])
cur.execute(
'create table feeling_%s(
id int unsigned not null,
feelingnum int unsigned not null auto_increment primary key,
text varchar(108) not null,
image char(100) ,
video char(100),
add_time time not null
)',value[0]
)
else:
print "You should create another user and change
another username"
#in order to insert it really,youshould
conn.commit()
#successful
cur.close()
conn.close()
#edit nickname
def editAccountCutename(cutename, username, userpasswd):
conn = conMySQL()
cur = conn.cursor()
cur.execute('SELECT * FROM userinfo WHERE
password = %s AND username = %s', username, userpasswd)
findresult = cur.fetchall()
if findresult:
cur.execute('
UPDATE userinfo SET cutename = %s WHERE
username = %s', cutename, username)
#update edit-time
cur.execute('
UPDATE userinfo SET edit_date = CURRENT_DATE
WHERE username = %s', username
)
else:
print "you input wrong username or password,
please try again"
conn.commit()
cur.close()
conn.close()
def editAccountYears(years, username, userpasswd):
conn = conMySQL()
cur = conn.cursor()
cur.execute('SELECT * FROM userinfo WHERE
password = %s AND username = %s', username, userpasswd)
findresult = cur.fetchall()
if findresult:
cur.execute('
UPDATE userinfo SET years = %i WHERE
username = %s', years, username)
#update edit-time
cur.execute('
UPDATE userinfo SET edit_date = CURRENT_DATE
WHERE username = %s', username
)
else:
print "you input wrong username or password,
please try again"
conn.commit()
cur.close()
conn.close()
def editAccountPassword(password, username, userpasswd):
conn = conMySQL()
cur = conn.cursor()
cur.execute('SELECT * FROM userinfo WHERE
password = %s AND username = %s', username, userpasswd)
findresult = cur.fetchall()
#no secure
if findresult:
cur.execute('
UPDATE userinfo SET password = %s WHERE
username = %s', password, username)
#update edit-time
cur.execute('
UPDATE userinfo SET edit_date = CURRENT_DATE
WHERE username = %s', username
)
else:
print "you input wrong username or password,
please try again"
conn.commit()
cur.close()
conn.close()
#duality relationship ,a->b and a<-b
def addFriend(userid, frndid):
conn = conMySQL()
cur = conn.cursor()
cur.execute('SELECT * FROM frnd_%s WHERE frndid = %d', userid, frndid )
findresult1 = cur.fetchall()
cur.execute('SELECT * FROM frnd_%s WHERE frndid = %d', frndid, userid)
findresult2 = cur.fetchall()
if (not findresult1) and (not findresult2):
cur.execute('
INSERT INTO frnd_%s	(id, frndnum, frndid) va	lues (%s, '', %s)
', userid, userid, frndid)
cur.execute('
INSERT INTO frnd_%s	(id, frndnum, frndid) values (%s, '', %s)
', frndid, frndid, userid)
else:
print "You are already friends"
conn.commit()
cur.close()
conn.close()
#find friend
def searchFriend():
conn = conMySQL()
cur = conn.cursor()
conn.commit()
cur.close()
conn.close()
def deleteFriend(userid, frndid):
conn = conMySQL()
cur = conn.cursor()
conn.commit()
cur.close()
conn.close()