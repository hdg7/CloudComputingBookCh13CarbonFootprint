FROM python:3.10-slim
RUN apt-get update && apt-get install -y curl
WORKDIR /app
RUN mkdir outputs
COPY . .
RUN pip install -r requirements.txt
CMD ["fastapi", "run", "main.py", "--host=0.0.0.0", "--port=8010"]

