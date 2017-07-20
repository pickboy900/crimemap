import pymysql, dbconfig


class DBHelper:

	def connect(self, database="crimemap"):
		return pymysql.connect(host="localhost",
							   user=dbconfig.db_user,
							   password=dbconfig.db_password)


	def get_all_inputs(self):
		connection = self.connect()
		try:
			query = "SELECT description FROM crimes;"
			with connection.cusor() as cursor:
				cursor.execute(query)
			return cursor.fetchall()
		finally:
			connection.close()


	def add_input(self, data):
		connection = self.connect
		try:
			#this section introduce a delberate flaw fo sequrity
			sql = "INSERT INTO crimes (description) VALUES ('{}')".format()