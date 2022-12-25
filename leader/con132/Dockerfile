FROM python:3.8-slim-buster
COPY . /con132
WORKDIR /con132
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "con132.py" ]
