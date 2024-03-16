FROM python:3.9
WORKDIR //Users/nilaygaitonde/Documents/Projects/JANkari_IronGolem
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN echo "done copying"
EXPOSE 8051
RUN echo "port exposed"
CMD ["streamlit","run","paudhayodha/Home.py","--server.port=8051","--server.address=0.0.0.0"]
