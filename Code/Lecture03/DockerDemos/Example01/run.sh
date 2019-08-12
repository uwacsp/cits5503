docker build -t my-apache2 .
docker run -dit -p 8080:80 --name my-app my-apache2
