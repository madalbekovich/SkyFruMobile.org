# FROM python:3.8-slim-buster as builder

# WORKDIR /usr/src/app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN apt-get update \
#     && apt-get install -y gcc netcat nano libmagic1 build-essential gdal-bin libgdal-dev gettext gettext-base \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# # RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# #########
# # FINAL #
# #########

# FROM python:3.8-slim-buster

# RUN mkdir -p /home/app

# RUN apt-get update \
#     && apt-get install -y netcat nano libmagic1 \
#     && apt-get clean

# RUN apt-get update && apt-get install -y \
#     gdal-bin \
#     libgdal-dev

# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/static
# RUN mkdir $APP_HOME/media
# WORKDIR $APP_HOME

# COPY --from=builder /usr/src/app/wheels /wheels
# COPY --from=builder /usr/src/app/requirements.txt .

# RUN pip install watchdog
# RUN pip install --upgrade pip
# RUN python -m venv venv
# ENV PATH="$HOME/venv/bin:$PATH"

# RUN pip install --no-cache /wheels/*

# COPY ./src $APP_HOME
# COPY .env $APP_HOME/

# RUN chmod +x /home/app/web/manage.py
# CMD ["/home/app/web/entrypoint.sh"]


FROM python:3.8-slim-buster AS builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y gcc netcat nano libmagic1 build-essential gdal-bin libgdal-dev gettext gettext-base \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Финальный образ
FROM python:3.8-slim-buster

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME/static $APP_HOME/media
WORKDIR $APP_HOME

RUN apt-get update \
    && apt-get install -y netcat nano libmagic1 gdal-bin libgdal-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

RUN pip install --upgrade pip
RUN pip install watchdog

COPY ./src $APP_HOME
COPY .env $APP_HOME/

RUN chmod +x /home/app/web/manage.py
CMD ["/home/app/web/entrypoint.sh"]