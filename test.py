import sqlite3


class DBConnector:



	def __init__(self):

		self.conn = sqlite3.connect("db.sqlite3")

		self.cur = self.conn.cursor()

		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS users(
			id int PRIMARY KEY,
			name text,
			phone text
			);
			""")

		self.conn.commit()

		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS polls(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			question text
			);
			""")

		self.conn.commit()


		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS pollanswers(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			pollid INTEGER,
			answer text
			);
			""")

		self.conn.commit()

		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS pollansweredusers(
			answerid INTEGER,
			userid INTEGER,
			username text
			);
			""")

		self.conn.commit()


	def add_user(self, user_id, name, phone):
		self.cur.execute("""INSERT INTO users VALUES(?, ?, ?)""", (user_id, name, phone))
		self.conn.commit()


	def get_user(self, user_id): 
		self.cur.execute("""SELECT * FROM users WHERE id=(?)""", (user_id, ))
		res = self.cur.fetchone()
		return res


	def get_all_users(self): 
		self.cur.execute("""SELECT * FROM users""")
		res = self.cur.fetchall()
		return res


	def delete_user(self, user_id):
		self.cur.execute("""DELETE FROM users WHERE id=(?)""", [user_id])
		user = self.get_user(user_id)
		return user



	def add_poll(self, question):
		self.cur.execute("""INSERT INTO polls(question) VALUES(?)""", (question, ))
		self.conn.commit()
		return self.cur.lastrowid


	def get_poll(self, poll_id): 
		self.cur.execute("""SELECT * FROM polls WHERE id=(?)""", (poll_id, ))
		res = self.cur.fetchone()
		return res


	def get_all_polls(self): 
		self.cur.execute("""SELECT * FROM polls""")
		res = self.cur.fetchall()
		return res


	def delete_poll(self, poll_id):
		self.cur.execute("""DELETE FROM polls WHERE id=(?)""", (poll_id, ))
		res = self.get_poll(poll_id)
		return res



	def add_pollanswer(self, poll_id, answer_text):
		self.cur.execute("""INSERT INTO pollanswers(pollid, answer) VALUES(?, ?)""", (poll_id, answer_text))
		self.conn.commit()
		return self.cur.lastrowid


	def get_pollanswer(self, pollanswer_id): 
		self.cur.execute("""SELECT * FROM pollanswers WHERE id=(?)""", (pollanswer_id, ))
		res = self.cur.fetchone()
		return res


	def get_all_pollanswers(self): 
		self.cur.execute("""SELECT * FROM pollanswers""")
		res = self.cur.fetchall()
		return res


	def get_all_pollanswers_of_poll(self, poll_id): 
		self.cur.execute("""SELECT * FROM pollanswers WHERE pollid=(?)""", (poll_id, ))
		res = self.cur.fetchall()
		return res


	def delete_pollanswer(self, pollanswer_id):
		self.cur.execute("""DELETE FROM pollanswers WHERE id=(?)""", (pollanswer_id, ))
		res = self.get_pollanswer(pollanswer_id)
		return res



	def add_pollanswereduser(self, answer_id, user_id, username):
		self.cur.execute("""INSERT INTO pollansweredusers(answerid, userid, username) VALUES(?, ?, ?)""", (answer_id, user_id, username))
		self.conn.commit()
		return self.cur.lastrowid


	def get_pollanswereduser(self, answer_id, user_id): 
		self.cur.execute("""SELECT * FROM pollansweredusers WHERE answerid=(?) AND userid=(?)""", (answer_id, user_id))
		res = self.cur.fetchone()
		return res


	def get_all_pollansweredusers(self): 
		self.cur.execute("""SELECT * FROM pollansweredusers""")
		res = self.cur.fetchall()
		return res


	def get_all_pollansweredusers_of_answer(self, answer_id): 
		self.cur.execute("""SELECT * FROM pollansweredusers WHERE answerid=(?)""", (answer_id, ))
		res = self.cur.fetchall()
		return res


	def delete_pollanswereduser(self, answer_id, user_id):
		self.cur.execute("""DELETE FROM pollansweredusers WHERE answerid=(?) AND userid=(?)""", (answer_id, user_id ))
		res = self.get_pollanswereduser(answer_id, user_id)
		return res




if __name__ == '__main__':
	db = DBConnector()

	pollanswereduserid = db.add_pollanswereduser(2, 1, 'aaa')
	print(pollanswereduserid)
	pollanswereduser = db.get_pollanswereduser(1, 1)
	print(pollanswereduser)
	pollansweredusers = db.get_all_pollansweredusers()
	print(pollansweredusers)
	pollansweredusersofanswerid1 = db.get_all_pollansweredusers_of_answer(1)
	print(pollansweredusersofanswerid1)
