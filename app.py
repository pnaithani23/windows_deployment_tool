import flask
from flask import Flask, request, render_template
import winrm
#before running this please run the below command on windows server
#winrm set winrm/config/service @{AllowUnencrypted="true"}
#(from cmd, not powershell)

APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@APP.route('/windows', methods =["GET", "POST"])
def red():
    if request.method == "POST":
        host_ip = request.form.get("HOST_IP")
        user_name = request.form.get("USER_TEXT")
        pass_word = request.form.get("PASSWORD_TEXT")
        s = winrm.Session(host_ip, auth=(user_name, pass_word))
        r = s.run_cmd('ipconfig', ['/all'])
        #r = s.run_cmd('host')
        #print(r.status_code)
        #print(r.std_out.splitlines(True))
        print(r.std_out)
    return render_template("windows.html")

if __name__ == '__main__':
    APP.debug=True
    APP.run()