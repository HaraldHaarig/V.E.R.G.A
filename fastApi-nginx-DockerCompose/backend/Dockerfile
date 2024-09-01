FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

#COPY ./app /code/app
COPY simpleFastAPI.py /code/

CMD ["fastapi", "run", "simpleFastAPI.py", "--port", "8000"]