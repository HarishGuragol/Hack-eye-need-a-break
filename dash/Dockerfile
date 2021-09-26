FROM python:3.6

RUN mkdir /project
RUN mkdir /project/backend
RUN mkdir /project/distraction_classification
RUN mkdir /project/dash

COPY ./backend /project/backend
COPY ./distraction_classification /project/distraction_classification
COPY ./dash /project/dash
WORKDIR /project/

ENV PYTHONPATH="/project"
ENV PROD=1

RUN pip3 install -r ./dash/requirements.txt
CMD ["python3", "dash/dashboard.py"]
