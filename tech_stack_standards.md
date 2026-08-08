# NovaBank Digital Lending Platform — Tech Stack & Coding Standards

## Stack

- **Backend:** Python 3.11, FastAPI
- **Database:** PostgreSQL, accessed exclusively via SQLAlchemy ORM
  through the repository pattern (`LoanRepository`,
  `CustomerRepository`, etc.) — **never raw SQL strings, anywhere,
  under any circumstances.**
- **Cache:** Redis, used for session state and short-lived eligibility
  check results
- **Messaging:** Kafka — `loan-status-changed` events are published on
  every status transition and consumed by the notification service
- **Auth:** JWT-based sessions; every loan-related endpoint must sit
  behind KYC session middleware
- **Secrets management:** HashiCorp Vault — credentials are injected at
  runtime as environment variables. Nothing resembling an API key,
  password, or token may appear as a string literal in source code.

## Coding Standards

- Type hints are required on all function signatures.
- No bare `except:` — always catch specific exception types.
- Logging goes through `structlog`, never `print()`. PII fields must be
  masked before logging (see business context rule on PII handling).
- Every new microservice lives under `services/<service_name>/main.py`
  and gets its own Dockerfile.
- Minimum 80% test coverage required for any module that touches
  financial calculations (interest, fees, disbursement amounts).

## Architecture Pattern

Each service is independently deployable, communicates with others via
either direct REST calls (synchronous, for request/response flows like
eligibility checks) or Kafka events (asynchronous, for status changes
that trigger downstream side effects like notifications).
