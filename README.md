# Zero Trust Identity Access Lab

Zero Trust Identity Access Lab is a hands-on cybersecurity project demonstrating Identity and Access Management (IAM) principles including authentication, authorization, federation, conditional access, and privileged access management in a simulated enterprise environment.

---

## Project Overview

This project demonstrates how identity acts as the control plane in modern cybersecurity. It simulates a secure records portal and applies layered access controls using Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC).

---

## Key Features

- Role-Based Access Control (RBAC) for Student, Staff, and Admin users  
- Attribute-Based Access Control (ABAC) using department and time-based conditions  
- Conditional access logic aligned with Zero Trust principles  
- Access denial handling for unauthorized requests  
- Audit logging of user activity and access decisions  
- Structured Flask application with separated logic and templates  

---

## Security Controls

Detailed documentation of implemented controls is available here:

 [Security Controls Overview](docs/security-controls.md)

---

## Technologies Used

- Python  
- Flask  
- HTML/CSS  
- JSON (data storage)  

---

## Application Structure

```
zero-trust-identity-access-lab/
├── app/
│   ├── app.py
│   ├── data.py
│   ├── authorization.py
│   ├── audit.py
│   └── templates/
│       ├── home.html
│       ├── student.html
│       ├── staff.html
│       ├── admin.html
│       └── access_denied.html
├── sample_data/
│   └── users.json
├── docs/
│   └── security-controls.md
├── requirements.txt
├── README.md
└── LICENSE
```

---

---

## Security Principles Demonstrated

- Least Privilege  
- Defense in Depth  
- Zero Trust (verify explicitly, never assume trust)  
- Role-based and attribute-based access control  
- Audit and accountability  

---

## Future Enhancements

- Federated login using OpenID Connect (OIDC)  
- Multi-Factor Authentication (MFA) simulation  
- Privileged Access Management (PAM) with just-in-time elevation  
- SIEM integration for log monitoring  

---

## Project Status

Complete (Initial Version)

