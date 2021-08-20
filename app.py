from flask import Flask,request
import string
import random
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1> Home <br> Please Go to /url route </home>"
@app.route("/url", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        backup_url = request.form.get('url_name')
        if backup_url.startswith("http://"):
            url_link = backup_url.replace("http://","")
        elif backup_url.startswith("https://"):
            url_link = backup_url.replace("https://","")
        else:
            url_link=backup_url
        all_chars = url_link+string.ascii_letters + string.digits
        
        short_url="del.dog/"+''.join(random.choices(all_chars, k=5))
        return '''
                  <h1>The Shortend url value is: {}</h1>'''.format(short_url)

    # otherwise handle the GET request
    return '''
    <br>
    <div style="text-align:center">
             <h1> URL SHORTNER </h1>
           <br>
           <form method="POST">
               <br>
               <div><label>URL : <input type="url" name="url_name"></label></div>
               <br>
               <input type="submit" value="Submit">
           </form>
           </div>
           '''




    

if __name__ == '__main__':
   app.run(debug=True,port=3000)
