PassWarden

A secure web-based password manager that demonstrates how modern applications protect credentials using hashing, encryption at rest, and controlled access enforcement.

This project focuses on how sensitive data is protected after it is submitted by a user, and how confidentiality and access control are enforced within a web application.

Table of Contents

Overview
What Problem This Project Addresses
Objectives
Important Scope Disclaimer
How PassWarden Works
Authentication and Credential Protection
Encryption Model
Key Management
Session and Access Control
Data Ownership Enforcement
Password Generation Logic
Core Security Concepts Explained
Why Symmetric Encryption Is Used
What This Project Is Not
Intended Audience
Learning Outcomes
Final Note

Overview

Traditional applications often store sensitive credentials insecurely or rely solely on passwords for protection.

PassWarden is a simplified but security-conscious password manager that demonstrates:

Secure password hashing

Encryption of stored credentials

Session-based authentication

Access control enforcement

Contextual understanding of data confidentiality

It focuses on applying foundational cybersecurity principles in a structured and practical way.

What Problem This Project Addresses

Many web applications fail at one or more of the following:

Storing passwords in plaintext

Failing to isolate user data

Lacking encryption for stored secrets

Allowing unauthorized data access

Treating authentication as sufficient without enforcing authorization

PassWarden addresses these weaknesses by separating authentication, encryption, and authorization responsibilities clearly.

It models how secure credential storage should function in a controlled environment.

Objectives

Demonstrate secure password hashing using bcrypt
Implement encryption at rest using symmetric cryptography
Enforce route-level access control
Prevent horizontal privilege escalation
Illustrate separation between authentication and authorization
Provide a usable interface without compromising core security principles

Important Scope Disclaimer

This project is designed for learning and demonstration purposes.

It intentionally focuses on backend security logic rather than:

HTTPS enforcement

Production deployment hardening

CSRF protection

Advanced session security

Enterprise-grade key management systems

The goal is to demonstrate security reasoning clearly rather than simulate a production identity platform.

How PassWarden Works

The application operates in the following sequence:

User registers → password is hashed using bcrypt
User logs in → hashed password is verified securely
User stores credentials → password is encrypted before storage
Encrypted data is stored in database
User dashboard retrieves encrypted values
Encrypted values are decrypted in memory for display
Access to routes requires active authenticated session

This layered structure separates identity verification, data confidentiality, and access enforcement.

Authentication and Credential Protection

User account passwords are protected using bcrypt.

Key properties:

One-way hashing

Automatic salting

Computationally expensive verification

Resistant to brute-force attacks

Passwords are never stored in plaintext and cannot be reversed from the stored hash.

Encryption Model

Stored website passwords are encrypted using Fernet symmetric encryption from the cryptography library.

Key characteristics:

AES-based encryption

Built-in integrity verification via HMAC

Symmetric encryption model

Decryption occurs only in application memory

This protects stored credentials from exposure at rest.

Even if the database is accessed directly, stored secrets remain unreadable without the encryption key.

Key Management

A master encryption key is generated and stored locally in a secret.key file.

If the key does not exist, it is generated automatically.

This key is excluded from version control and is required to decrypt stored credentials.

The encryption key acts as the cryptographic trust anchor for the system.

Session and Access Control

PassWarden uses Flask sessions to maintain authenticated state.

Upon successful login:

The user ID is stored in a signed session cookie.

Protected routes validate session presence before granting access.

Session integrity is enforced using Flask’s secret key.

Data Ownership Enforcement

Every credential stored in the system is associated with a specific user ID.

Database operations enforce ownership:

Update and delete operations validate both record ID and user ID.

Users cannot modify credentials belonging to another account.

This prevents horizontal privilege escalation.

Authentication confirms identity.
Authorization confirms permission.

Password Generation Logic

PassWarden includes a built-in password generator.

It generates high-entropy passwords using:

Uppercase characters

Lowercase characters

Numbers

Symbols

The generator increases credential strength and reduces password reuse risk.

Core Security Concepts Explained

Hashing vs Encryption
Hashing is one-way and protects login passwords.
Encryption is reversible and protects stored credentials.

Confidentiality
Encryption ensures sensitive data remains unreadable at rest.

Integrity
Fernet includes built-in message authentication to prevent tampering.

Authentication
Verifies identity through password hashing.

Authorization
Ensures users can access only their own data.

Separation of Concerns
Authentication, encryption, and access control are implemented independently.

Why Symmetric Encryption Is Used

This project uses symmetric encryption because:

It is efficient for encrypting application data

It is easy to implement securely with established libraries

It reflects how many vault systems encrypt stored secrets internally

In production systems, encryption keys may be managed through dedicated key management services.

This project focuses on demonstrating encryption logic clearly.

What This Project Is Not

To maintain clarity and scope, this project does not:

Implement zero-knowledge encryption

Use machine learning for anomaly detection

Implement CSRF protection

Enforce HTTPS transport security

Provide enterprise-grade key rotation

Act as a production authentication service

The focus is on demonstrating backend security principles.

Intended Audience

Students learning web application security
Beginners exploring applied cryptography
Developers wanting to understand secure credential storage
Cybersecurity learners building practical portfolio projects

Learning Outcomes

By building and exploring PassWarden, you will understand:

Why hashing is necessary for user passwords
How encryption protects stored secrets
How access control prevents cross-user data exposure
Why authentication alone is not sufficient for security
How symmetric encryption works in practical systems
How to structure a secure web application logically

Final Note

Security is not a single mechanism.

It is a layered system of:

Identity verification
Confidentiality enforcement
Access control
Data isolation

PassWarden exists to make those layers visible and understandable.

Modern security thinking does not stop at passwords.

It begins there.