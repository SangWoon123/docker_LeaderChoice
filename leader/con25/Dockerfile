FROM python:3.8-slim-buster
COPY . /con25
WORKDIR /con25
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "con25.py" ]
