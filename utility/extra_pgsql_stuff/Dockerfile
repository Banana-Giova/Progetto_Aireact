FROM python:3.11-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY rest.py .
ENV FLASK_APP=rest.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 4160
CMD ["python", "rest.py"]
#nome app => rest_aireact

#docker build -t rest_aireact .
#run => docker run -p 4160:4160 rest_aireact