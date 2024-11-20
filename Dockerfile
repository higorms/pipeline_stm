FROM python:3.10-slim-bullseye
COPY /etl /etl
COPY requirements.txt requirements.txt
COPY entrypoint_ingestão_informakon_drive.py entrypoint_ingestão_informakon_drive.py
COPY entrypoint_ingestão_estoque_drive.py entrypoint_ingestão_estoque_drive.py
COPY entrypoint_ingestão_construtor_de_vendas.py entrypoint_ingestão_construtor_de_vendas.py
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "entrypoint_ingestão_informakon_drive.py"]