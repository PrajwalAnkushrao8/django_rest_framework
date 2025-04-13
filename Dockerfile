FROM Python:3.10-slim

WORKDIR /app

COPY requirments.txt .

RUN pip -r install requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
