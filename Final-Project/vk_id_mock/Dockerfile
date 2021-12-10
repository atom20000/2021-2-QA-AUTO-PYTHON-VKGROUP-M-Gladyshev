FROM python:3.8.10

ADD requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt && rm -f /requirements.txt

ADD mock.py /mock.py

CMD ["python3", "/mock.py"]