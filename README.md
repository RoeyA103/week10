# Project Overview

This project consists of **two Dockerized servers**:

- **SQL Server**
- **API Server**

The system is designed with **strict separation of access**:
- The **host communicates only with the API server**
- The **SQL server is accessible exclusively through the API**

This architecture improves security and enforces proper data flow.

---

## Architecture

- Both servers run using **Docker Compose**
- The SQL server is initialized automatically at container creation
- All configuration is centralized in a `.env` file

```
Host → API Server → SQL Server
```

---

## SQL Initialization

- The initial SQL startup file is located in the **SQL/** directory
- Docker automatically loads this file when the SQL container is created

---

## Configuration

- Configuration for **both servers** is stored in the `.env` file
- Values can be modified as needed without changing source code

---

## API Access

The API server is accessible via standard **HTTP requests**.

### Available Routes

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/` | Health check |
| GET | `/contacts` | Retrieve all contacts |
| POST | `/contacts` | Create a new contact |
| PUT | `/contacts/{id}` | Update an existing contact |
| DELETE | `/contacts/{id}` | Delete a contact |

---

## Creating a Contact

To create a new contact, send a **JSON payload** with the following fields:

```json
{
  "name": "John",
  "surname": "Doe",
  "mobile": "123456789"
}
```

---

## Example cURL Requests

### Health Check

```bash
curl http://localhost:8000/
```

### Get All Contacts

```bash
curl http://localhost:8000/contacts
```

### Create a New Contact

```bash
curl -X POST http://localhost:8000/contacts \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John",
    "surname": "Doe",
    "mobile": "123456789"
  }'
```

### Update a Contact

```bash
curl -X PUT http://localhost:8000/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane",
    "surname": "Doe",
    "mobile": "987654321"
  }'
```

### Delete a Contact

```bash
curl -X DELETE http://localhost:8000/contacts/1
```

---

## Running the Application

Start the application using Docker Compose:

```bash
docker compose up
```

Run in the background (detached mode):

```bash
docker compose up -d
```
