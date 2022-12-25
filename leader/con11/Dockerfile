FROM python:3.8-slim-buster
COPY . /con11
WORKDIR /con11
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "con11.py" ]
