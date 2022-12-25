FROM python:3.8-slim-buster
COPY . /con99
WORKDIR /con99
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "con99.py" ]
