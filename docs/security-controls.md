# Security Controls Overview

## Purpose
This document explains the core security controls implemented in the Zero Trust Identity Access Lab and how they support identity-driven access management in a simulated enterprise environment.

## Controls Implemented

### 1. Role-Based Access Control (RBAC)
The application enforces access decisions based on user roles.

- Student users can access the student dashboard
- Staff users can access the staff dashboard
- Admin users can access the admin dashboard

RBAC is implemented through route protection logic in the application.

### 2. Attribute-Based Access Control (ABAC)
The application applies additional access decisions based on user attributes and contextual conditions.

Examples:
- Staff access requires the user to belong to the registrar department
- Admin access requires the user to belong to the it-security department
- Admin access is restricted to business hours

This demonstrates that access decisions should consider more than a role alone.

### 3. Access Denial Handling
When a user does not meet authorization requirements, the application returns an access denied page.

This helps demonstrate:
- least privilege
- controlled access failure
- clear user feedback for unauthorized requests

### 4. Audit Logging
The application records access events for protected routes.

Logged details include:
- username
- action attempted
- access result
- timestamp

This supports:
- accountability
- audit review
- security monitoring

## Security Design Principles Demonstrated

### Least Privilege
Users are granted only the access appropriate to their role and attributes.

### Defense in Depth
Access decisions are layered. Role checks, department checks, and time-based conditions are combined for stronger protection.

### Zero Trust Thinking
The application demonstrates the principle of verifying access explicitly instead of assuming trust.

## Future Enhancements
Planned enhancements may include:
- federated login with OpenID Connect (OIDC)
- simulated MFA workflow
- temporary privileged access elevation
- expanded audit reporting
