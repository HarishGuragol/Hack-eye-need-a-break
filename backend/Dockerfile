FROM python:3.6

RUN mkdir /project
RUN mkdir /project/backend
RUN mkdir /project/backend/static

COPY ./backend /project/backend

COPY ./fonts /project/backend/static/fonts
COPY ./js /project/backend/static/js
COPY ./css /project/backend/static/css
COPY ./index.html /project/backend/static/index.html
COPY ./webgazer.js /project/backend/static/webgazer.js


COPY ./run_server.py /project/run_server.py
WORKDIR /project/

ENV PYTHONPATH="/project"
ENV PROD=1

RUN pip3 install -r ./backend/requirements.txt
CMD ["python3", "run_server.py"]
