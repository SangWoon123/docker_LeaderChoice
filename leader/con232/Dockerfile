FROM python:3.8-slim-buster
COPY . /con232
WORKDIR /con232
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "con232.py" ]
