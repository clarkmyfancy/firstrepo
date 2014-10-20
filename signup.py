import webapp2  
import cgi
import re
form="""
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <title>Signup Page</title>
    <link rel="stylesheet" type="text/css" href="stylesheets/signup.css">
  </head>
  <body>
    <h1>Signup</h1>
    <form method="post">
      <table>
        <tr>
          <td class="label">Username</td>
          <td><input type="text" name="username" value=""></td>
          <td class="error"></td>
        </tr>

        <tr>
          <td class="label">Password</td>
          <td><input type="password" name="password" value=""></td>
          <td class="error"></td>
        </tr>

        <tr>
          <td class="label">Verify Password</td>
          <td><input type="password" name="verify" value=""></td>
          <td class="error"></td>
        </tr>

        <tr>
          <td class="label">Email (optional)</td>
          <td><input type="text" name="email" value=""></td>
          <td class="error"></td>
        </tr>
      </table>

      <input type="submit">

    </form>
  </body>
</html>
"""
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"[\w.%-]+@[\w.-]+\.[a-zA-Z]{2,4}/")

def valid_username(name):
    return USER_RE.match(name)
def valid_pass(password):
    return PASS_RE.match(password)
def valid_email(email):
    return EMAIL_RE.match(email)

class signup(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)
    def post(self):
        user_name = valid_username(self.request.get('username'))
        username = self.request.get("username")
        user_pass = valid_pass(self.request.get('password'))
        password = self.request.get("password") 
        user_email = valid_email(self.request.get('email'))
        email = self.request.get("email")
        if not (user_name and user_pass and user_email):
            self.response.write("Welcome " +username+ "!")
        else:
            self.response.write(form)
    
    '''def write_form(self, error="", username="", password="", email=""):
        self.response.write(form % {"error":error, "username":username, "password":password, "email":email})'''
        
application = webapp2.WSGIApplication([
    ('/', signup),   
], debug=True)