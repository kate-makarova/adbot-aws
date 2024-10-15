FROM python:3.12

RUN apt-get -y update
RUN apt-get install -yqq unzip xvfb libxi6 libgconf-2-4 jq libjq1 libonig5 libxkbcommon0 libxss1 libglib2.0-0 libnss3 \
  libfontconfig1 libatk-bridge2.0-0 libatspi2.0-0 libgtk-3-0 libpango-1.0-0 libgdk-pixbuf2.0-0 libxcomposite1 \
  libxcursor1 libxdamage1 libxtst6 libappindicator3-1 libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libxfixes3 \
  libdbus-1-3 libexpat1 libgcc1 libnspr4 libgbm1 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxext6 \
  libxrandr2 libxrender1 gconf-service ca-certificates fonts-liberation libappindicator1 lsb-release xdg-utils
# install google chrome
RUN wget -O /tmp/chrome.zip https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.89/linux64/chrome-linux64.zip
RUN unzip /tmp/chrome.zip -d /usr/local/bin/


# install chromedriver
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.89/linux64/chromedriver-linux64.zip
#RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/`curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE`/linux64/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# set display port to avoid crash
#ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install asgiref
RUN pip install tensorflow
RUN pip install boto3

WORKDIR /home/root
ADD src src

CMD ["python", "src/run.py"]
#CMD ["ls","/usr/local/bin/chrome-linux64"]
#CMD ["/usr/local//bin/chrome-linux64/chrome","--headless=new","--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"]
