from sqlobject import *

from settings import DB_URI

def connect():
	sqlhub.processConnection = connectionForURI(DB_URI)

class User(SQLObject):
	name = UnicodeCol(length=64)
	domain = UnicodeCol(length=64)

class Mail(SQLObject):
	user = ForeignKey('User')
	ts = DateTimeCol()
	envelopeHeloHost = UnicodeCol(length=128)
	envelopeHeloAddress = UnicodeCol(length=20)
	envelopeFrom = UnicodeCol(length=129)
	envelopeTo = UnicodeCol()
	headerFrom = UnicodeCol(length=255)
	headerSubject = UnicodeCol(length=255)
	headers = UnicodeCol()
	body = UnicodeCol()

	class sqlmeta:
		defaultOrder = ["-ts",]

if __name__ == "__main__":
	connect()
	print "Creating tables..."
	User.createTable()
	Mail.createTable()
	print "Done."

"""
In [20]: list(Domain.select(Domain.q.name=="tm.zakx.de"))
Out[20]: [<Domain 1 name='tm.zakx.de'>]

In [21]: list(Domain.select(Domain.q.name=="tm.zakx.dess"))
Out[21]: []
"""
