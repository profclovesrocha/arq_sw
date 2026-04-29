# Fintech Payment API

A **Payment API** built with **Spring Boot**, using **PostgreSQL**, **RabbitMQ**, and **Docker**.

This project demonstrates an **Event-Driven Architecture (EDA)** where order creation generates events that are sent to a message broker and processed asynchronously.

---

# Technologies

- Java 21
- Spring Boot 3
- Spring Data JPA
- PostgreSQL
- RabbitMQ
- Docker
- Swagger / OpenAPI
- Lombok
- Maven

---

# Architecture

The system follows an **Event-Driven Architecture** using **RabbitMQ** for asynchronous communication.

It also follows a **layered architecture**, separating responsibilities into:

- Controllers
- Services
- Repositories

Project structure:

```bash
src/main/java/com/pay/payment_api
├── controller
├── service
├── repository
├── dto
├── mapper
├── entity
├── event
├── consume
└── exception
```
# Application Flow

1. Client sends a request to create an order

2. The order is stored in PostgreSQL

3. An OrderCreatedEvent is published to RabbitMQ

4. A consumer receives and processes the event

Simplified flow:

```bash
Client → API → Database
              ↓
           RabbitMQ
              ↓
           Consumer
```

# Features

- Create orders

- List orders

- Update order status

- Publish events to RabbitMQ

- Consume events asynchronously

- Global exception handling

- API documentation with Swagger

- Running the Project

```bash
1 Clone the repository
git clone https://github.com/marconi-prog/fintech-payment-api.git
cd fintech-payment-api
```

2 Start containers
```bash
docker compose up -d
```
**This will start:**

- PostgreSQL

- RabbitMQ

3 Run the application
```bash
mvn spring-boot:run
```

**API Documentation**

Swagger UI available at:
```bash
http://localhost:8080/swagger-ui/index.html
```

Endpoints
Create Order

POST /orders

Request body:
```bash
{
  "customerId": "UUID",
  "amount": 100.50
}
```
**List Orders**

### GET ` /orders `

**Update Order Status**

### PATCH ` /orders/{id}/status `

Available status values:
```bash
PENDING

PAYMENT_PROCESSING

PAYMENT_APPROVED

PAYMENT_FAILED
```

**Error Handling**

The application includes a Global Exception Handler to standardize error responses.

Example response:
```bash
{
  "message": "Order not found",
  "status": 400,
  "timestamp": "2026-03-05T03:40:00"
}
```
### Author

**Marconi Farias** `Backend Developer`
