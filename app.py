from flask import Flask,request
import string
import random
import os
import redis

host_url = os.getenv('CACHE_REDIS_URL')
redis = redis.from_url(host_url)

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
        
        # read Through cache method
        
        if redis.get(url_link):
            short_url=redis.get(url_link)
            short_url=short_url.decode()
        else:
            short_url="del.dog/"+''.join(random.choices(all_chars, k=5))
            redis.set(url_link,short_url)
            
    





        return '''
        <div style="text-align:center">

        <h1>The Shortend url value is</h1>
         <a href={actual_url} alt="Url Shortner", target="_blank"> {ShortUrl} </a>
        </div>          
                  '''.format(ShortUrl=short_url,actual_url=backup_url)

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
   app.run(debug=True, host="0.0.0.0", port=3000)
