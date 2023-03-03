FROM tensorflow/tensorflow

RUN apt-get update
RUN apt-get install -y git 
RUN cd home && git clone https://github.com/vanshksharma/Signopedia-Deployment.git
RUN pip install djangorestframework
RUN pip install pillow
RUN pip install django-cors-headers
RUN cd /home/Signopedia-Deployment
CMD ["python", "/home/Signopedia-Deployment/manage.py", "runserver", "0.0.0.0:8000"]
# CMD [ "cd home" ,"git clone https://github.com/vanshksharma/Signopedia-Deployment.git","ls","cd Signopedia-Deployment","pip install -r requirements.txt" ] 
# RUN apk update
# RUN apk add git
# RUN cd home
# # RUN cd home/Signopedia-Deployment && pip install -r requirements.txt
# CMD [  "cd home/Signopedia-Deployment && python manage.py runserver 0.0.0.0:8000"]
# CMD ["cd", "home/Signopedia-Deployment"]
# CMD ["cd", "home/Signopedia-Deployment","python", "manage.py", "runserver", "0.0.0.0:8000"]


# RUN cd Signopedia-Deployment && pip install -r requirements.txt
# RUN ls
# RUN cd Signopedia-Deployment
# RUN ls
# RUN pip install -r requirements.txt
# RUN python manage.py runserver


# you will need to install docker and run it as system service
# create a file named Dockerfile with nano 
# sudo docker build -t signopedia .
# sudo docker run --rm -it -p 80:8000 signopedia 