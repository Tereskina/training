from bottle import route, run, view, response
from random import random
from horoscope import generate_prophecies

@route("/api/forecasts")
def api_test():
	response.headers['Access-Control-Allow-Origin'] = '*' #нужен, чтобы CORS не блокировал
	return {
		"prophecies": generate_prophecies()
	}

run(
	host="localhost",
	port=8080,
	autoreload=True
)
