# API Gateway

## What Is an API Gateway?

An API Gateway is the main entry point that the frontend uses to reach backend services. It receives a request and forwards it to the service responsible for that part of the work.

## Why This Project Plans to Use One

The platform is planned as several services, each with a different responsibility. A gateway gives the React frontend one planned place to send backend requests instead of requiring it to contact each internal service directly. It also provides a clear place to route those requests to the appropriate service.

## Planned Responsibilities

The API Gateway is planned to:

- Receive backend requests from the React frontend.
- Route each request to the backend service responsible for it, such as the User, Data, Analytics, ML, or AI Service.
- Return the service response to the frontend.

The exact routes, request formats, and gateway behavior have not yet been decided.

## Communication Plan

The frontend is planned to communicate with the API Gateway over HTTP. Backend communication is planned to use HTTP REST APIs, with JSON as the request and response data format. The gateway will forward requests to backend services through their agreed service interfaces.

The frontend is not planned to connect directly to service databases or bypass the gateway to call internal service endpoints.

## What the Gateway Will Not Do

The gateway coordinates requests; it does not own the services' core business work. For example, it should not:

- Clean or validate datasets. That work belongs to the Data Service.
- Calculate analytics. That work belongs to the Analytics Service.
- Train machine learning models. That work belongs to the ML Service.

Keeping these responsibilities in their services helps make the system easier to understand and maintain.

## Current Status

The API Gateway is planned, not implemented. This document describes its intended role only. No gateway application, API endpoints, or configuration have been created yet, and implementation details such as ports and URLs have not been decided.
