FROM python 

WORKDIR /site

COPY . .
COPY teste.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]