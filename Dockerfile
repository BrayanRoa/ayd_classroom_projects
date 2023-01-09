FROM alpine:3.10
RUN apk add python3-dev && pip3 install --upgrade pip
WORKDIR /home
COPY . /home
EXPOSE 5000
RUN pip install -r requirements.txt

RUN export FLASK_APP=entrypoint \
export FLASK_DEBUG=1 && flask shell && from app.db import db && db.create_all()

CMD ["flask","run"]