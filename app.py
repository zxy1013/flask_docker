from flask import Flask,render_template
from sql.user_sql import Session

app = Flask(__name__)

@app.route('/')
def hello_world():
	session = Session( )
	sql = "select * from user"
	cursor = session.execute(sql)
	result = cursor.fetchall( )
	session.close( )
	return render_template('user.html',user=result)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')