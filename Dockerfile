FROM python:3.9-alpine
LABEL maintainer="alekseevmax26@gmail.com"
WORKDIR /homework5
COPY requirements.txt .

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./app

CMD ["pytest", "--browser_name", "chrome", "--url", "https://demo.opencart.com"]

