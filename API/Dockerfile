FROM python:3.9

WORKDIR /code

COPY ./API/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./API /code/app

CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]

EXPOSE 80


# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]