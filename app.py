from flask import Flask,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1> Home <br> Please Go to /url route </home>"
@app.route("/url", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        url_link = request.form.get('url_name')
        return '''
                  <h1>The Shortend url value is: {}</h1>'''.format(url_link)

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
