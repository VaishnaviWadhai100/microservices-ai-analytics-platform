# User Service

## What Is the User Service?

The User Service is the planned part of the platform responsible for user accounts and authentication-related work. It will provide user-related operations through an agreed service interface when those features are designed and implemented.

This document describes the intended design. The User Service has not been implemented.

## Why the Platform Needs It

People need accounts to use platform features and manage their profile information. Keeping user-related work in one service gives that work a clear owner and lets the other services request the operations or information they need through a defined interface.

## Planned Responsibilities

The User Service is planned to handle:

- User registration.
- Login and authentication-related operations.
- Account and profile management.
- Other operations related to users, as the platform's requirements are defined.

The exact workflows, rules, and service interface have not yet been designed.

## User Data Ownership

The User Service is planned to own user-related and authentication-related data in the logical database named `user_db`. The platform's current database plan uses one MySQL server for local development, with separate logical databases assigned to services.

No tables or database schema have been designed. The User Service's data model will be decided during implementation planning.

Other services should not read or write the User Service's internal database tables directly. If another service needs a user-related operation or information, it should use an agreed service interface. This keeps the User Service responsible for its data and allows its internal storage to change without requiring other services to depend on its tables.

## Relationship with the API Gateway

The API Gateway is planned as the main backend entry point for the React frontend. It will route requests to the service responsible for the requested work. User-related frontend requests are therefore expected to reach the User Service through the gateway, according to the routes and interfaces agreed during later design.

The gateway routes requests; the User Service remains responsible for user and authentication-related work. The gateway and User Service have not been implemented, and their specific request paths have not been defined.

## Planned Communication

Services are planned to communicate primarily through HTTP REST APIs using JSON request and response data. The API Gateway will route frontend requests to backend services, and services that need to coordinate will use each other's agreed interfaces.

Specific endpoints, payloads, authentication between services, and error handling have not yet been defined.

## Responsibilities of Other Services

The User Service is not responsible for the platform's data and analysis work. Those responsibilities are planned for other services:

- The **Data Service** will handle dataset upload and management, validation, and cleaning.
- The **Analytics Service** will perform analytics and manage analytics-specific results.
- The **ML Service** will handle machine learning tasks and related results.
- The **AI Service** will handle AI-assisted interactions about datasets or analytical results.

The exact features and interactions between services remain future design work.

## Security Considerations for Implementation

Security requirements still need to be designed and implemented. At a minimum, implementation planning should address:

- Protecting passwords using an appropriate secure password-storage approach; passwords should not be stored as plain text.
- Authenticating users before allowing access to protected account or platform operations.
- Defining how authentication information is handled and how access is checked by the gateway and services.
- Protecting user-related data and limiting access to the operations each user is permitted to perform.

These are considerations for future implementation, not features that are already in place. Detailed security mechanisms and authorization rules have not yet been selected.

## Current Status

The User Service is **planned, not implemented**. No application, API endpoints, database schema, or service configuration have been created. This README records the intended responsibility and architecture boundaries only.
