FROM python:3.8-slim-buster
COPY . /con54
WORKDIR /con54
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "con54.py" ]
