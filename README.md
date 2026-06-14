# security_logs_analyzer_opp_basic
Security Log Analyzer  A simple Object-Oriented Programming (OOP) project built with Python to analyze user login activities and generate basic security reports. This project demonstrates the implementation of classes, objects, attributes, methods, and interactions between objects in a cybersecurity-themed application.

## Features

* User activity management
* Failed login monitoring
* Risk score calculation
* Threat level classification
* Security report generation
* OOP implementation with multiple classes

## Project Structure

```text
security-log-analyzer/
│
├── main.py
├── README.md
```

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

## OOP Concepts Implemented

### Class

* User
* ThreatAnalyzer
* SecurityReport

### Object

Creating instances of classes to represent users, analyzers, and reports.

### Attributes

```python
username
ip_address
failed_login
```

### Methods

```python
show_info()
calculateScore()
threatLevel()
generate()
```

## Example Output

```text
==============================
SECURITY REPORT
==============================
Username   : admin
IP Address : 192.168.12.2
Attempts   : 7

Risk Score : 70
Threat Level : High
```

## Threat Classification

| Failed Login Attempts | Threat Level |
| --------------------- | ------------ |
| 0 - 2                 | Low          |
| 3 - 4                 | Medium       |
| 5 - 9                 | High         |
| 10+                   | Critical     |

## Learning Objectives

This project was created to practice:

* Classes and Objects
* Constructors (`__init__`)
* Attributes
* Methods
* Encapsulation fundamentals
* Object interaction
* Python programming fundamentals

## Future Improvements

* User input support
* CSV log processing
* File-based report generation
* Data visualization
* AI-based anomaly detection
* Machine learning integration


*"Turning security data into meaningful insights through code."*
