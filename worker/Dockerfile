FROM python:3.9.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x wait-for-it.sh

CMD [ "./wait-for-it.sh", "storage:27017", "--timeout=60", "--strict", "--", "python3", "start.py" ]
