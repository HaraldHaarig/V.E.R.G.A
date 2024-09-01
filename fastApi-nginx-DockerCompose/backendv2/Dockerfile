FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

#COPY ./app /code/app
COPY simpleFastAPIv2.py /code/

CMD ["fastapi", "run", "simpleFastAPIv2.py", "--port", "8000"]