from bottle import route, run, static_file
import eyeot

@route('/ac/togglePower')
def togglePower():
	ac.power_on()
	return {"response":"ok"}

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def main():
	return static_file('static/remote.html', root='./')


ac = eyeot.ACRemoteController()

run(host='0.0.0.0', port=80, debug=True)
