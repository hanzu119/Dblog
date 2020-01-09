FROM python:3.7-alpine
LABEL version="1.0"
LABEL description="D-blog image"
COPY . /code/D-Blog
WORKDIR /code
RUN apk add --update --no-cache mariadb-connector-c-dev \
	&& apk add --no-cache --virtual .build-deps \
		mariadb-dev \
		gcc \
		musl-dev \
	&& pip install mysqlclient==1.4.6 \
	&& apk del .build-deps
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
apk update && \
apk add --no-cache gcc g++ python3-dev linux-headers libffi-dev jpeg-dev openssl-dev \
                       zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev \
                       tk-dev tcl-dev harfbuzz-dev fribidi-dev && \
pip install --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple -r ./D-Blog/requirements.txt && \
sed '35,36d' /usr/local/lib/python3.7/site-packages/django/db/backends/mysql/base.py > /usr/local/lib/python3.7/site-packages/django/db/backends/mysql/base.bak && \
mv /usr/local/lib/python3.7/site-packages/django/db/backends/mysql/base.bak /usr/local/lib/python3.7/site-packages/django/db/backends/mysql/base.py
WORKDIR /code/D-Blog
RUN python manage.py collectstatic --noinput
CMD ["uwsgi","--chdir=/code/D-Blog","--module=DjangoBlog.wsgi:application","--env","DJANGO_SETTINGS_MODULE=DjangoBlog.settings","--http=0:8000","--processes=5","--harakiri=20","--max-requests=5000","--vacuum"]