FROM python:3.9-alpine
WORKDIR /opslyft
ENV  MESSAGE="Hello Opslyft, please hire me :)"
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
