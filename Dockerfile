FROM python:alpine3.17
WORKDIR /app
COPY MainScores.py /app
COPY Utils.py /app
COPY Scores.txt /Scores.txt
RUN pip install flask
EXPOSE 5000
CMD ["python", "MainScores.py", "--host=0.0.0.0"]
