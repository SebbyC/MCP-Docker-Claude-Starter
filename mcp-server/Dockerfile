FROM python:3.10-slim
RUN pip install mcp psycopg2-binary uvicorn
COPY server.py /srv/
WORKDIR /srv
EXPOSE 7000
CMD ["python", "server.py"]