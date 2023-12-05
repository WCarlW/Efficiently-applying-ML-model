# syntax=docker/dockerfile:1

FROM python:3.11.6

WORKDIR /app
RUN pip install --no-cache-dir --upgrade fastapi uvicorn pydantic transformers tensorflow scikit-learn torch torchvision torchaudio keras matplotlib numpy pandas 
COPY . /app
CMD ["uvicorn", "docker_api:app", "--host", "0.0.0.0", "--port", "3000"]