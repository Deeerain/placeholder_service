# Базовый образ с предустановленным uv
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Системные зависимости для Pillow
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости
COPY pyproject.toml README.md ./

# Устанавливаем зависимости (uv install == uv pip install)
RUN uv sync

# Копируем исходный код
COPY . .

EXPOSE 5000

CMD ["uv", "run", "gunicorn", "app:app", "-b", "0.0.0.0:5000"]
