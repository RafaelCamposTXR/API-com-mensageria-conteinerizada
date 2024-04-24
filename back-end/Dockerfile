FROM python
RUN apt-get update
WORKDIR /back-end
COPY . /back-end/
RUN pip install -r requirements.txt 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]