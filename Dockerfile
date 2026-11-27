FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN useradd --uid 10001 appuser
USER 10001
CMD ["python", "-c", "from app import hours_saved; print('Hours saved:', hours_saved(10000, 6, 80))"]
