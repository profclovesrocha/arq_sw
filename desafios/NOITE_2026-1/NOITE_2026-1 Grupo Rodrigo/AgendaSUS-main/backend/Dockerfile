FROM node:20-alpine AS frontend-builder

WORKDIR /app-frontend

COPY ../frontend/package*.json ./
RUN npm install

COPY ../frontend/ .
RUN npm run build

FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

COPY --from=frontend-builder /app-frontend/dist ./.frontend/dist

EXPOSE 8080

CMD ["python", "App.py"]