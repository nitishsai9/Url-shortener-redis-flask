# Flask-Redis-Docker-Url-Shortner

### Built With

* [Bootstrap](https://getbootstrap.com)
* [Docker](https://docs.docker.com/compose/gettingstarted/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Redis](https://redis.io/)

### Installation


1. Build and run

   ```sh
   docker-compose build
   docker-compose up
   
   
   ```
2. Remove or Stop
   ```sh
   docker-compose down
   docker-compose down -v [will remove volumes]
   ```

   ```
3. Access in Browser Home Page
   ```sh
   
   http://localhost:3000/ 
   ```


   ```
3. Access in Browser Shortener Page
   ```sh
   
   http://localhost:3000/url

   will have simple html ui which takes user input and converts the url
   to short url with del.dog as prefix.
   
   ```
   
4.  Test in cli
   ```sh
  
  curl -d "url_name=https://google.com" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:3000/url


  curl -d "url_name=https://google.com" -X POST http://localhost:3000/url


   ```