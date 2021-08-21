FROM python:latest

RUN https://github.com/JoaoAssalim/Bill_Bot.git

COPY requirements.txt .
RUN pip install --no-cache-dir -U -r requirements.txt 

RUN python3 -u -m voxpopuli.voice_install all

COPY . .
CMD ["python3", "-u", "Bot_Bill.py"]