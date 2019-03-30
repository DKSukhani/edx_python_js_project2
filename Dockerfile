FROM python
WORKDIR /home
ADD . /home
RUN alias pip=pip3
RUN alias python=python3
RUN pip3 install psycopg2
RUN pip3 install flask-bcrypt
RUN pip3 install flask-login
RUN pip3 install requests
CMD tail -f /dev/null