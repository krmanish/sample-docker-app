FROM python:3.7.4

COPY . /flaskapp

WORKDIR  /flaskapp

RUN pip3 install -r requirement.txt
RUN pytest test_apps.py

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["apps.py"]

