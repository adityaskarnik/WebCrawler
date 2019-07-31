FROM python:3
COPY ./ /webcrawler/
WORKDIR /webcrawler
RUN pip install -r requirements.txt
# RUN python3 manage.py runserver 0.0.0.0:8000