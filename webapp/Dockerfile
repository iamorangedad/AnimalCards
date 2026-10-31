# AnimalCards Globe —— 构建上下文为仓库根目录：docker build -f webapp/Dockerfile .
# 镜像里只放代码；卡片 PNG/PDF（动物/）通过 volume 挂载，不重复打包。
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    ANIMALCARDS_ROOT=/repo WEBAPP_DIR=/app/webapp HOST=0.0.0.0 PORT=8000
WORKDIR /app/webapp
COPY webapp/backend/requirements.txt backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt
COPY webapp/backend backend
COPY webapp/frontend frontend
COPY webapp/data data
COPY webapp/thumbs thumbs
RUN useradd -r -u 10001 app && chown -R app /app
USER app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -c "import urllib.request,os;urllib.request.urlopen('http://127.0.0.1:%s/healthz'%os.environ.get('PORT','8000'))"
CMD ["sh", "-c", "cd backend && exec uvicorn app:app --host $HOST --port $PORT --workers ${WORKERS:-2} --proxy-headers --forwarded-allow-ips='*'"]
