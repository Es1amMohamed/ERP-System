
# ERP System for Home Furniture Factory



This project is an ERP (Enterprise Resource Planning) system designed for a home furniture factory. The system focuses on managing user roles, permissions, and the organizational hierarchy efficiently. It includes features such as advanced access control, modular design for scalability, and critical permission management for superusers.
## Features
Role and Permission Management: Assign and manage permissions based on organizational roles, ensuring secure access control.

Critical Permissions: Restrict access to sensitive actions and data exclusively to superusers.

Modular Design: Built with scalability in mind, allowing future enhancements and feature additions.

Organizational Hierarchy: Supports multi-level hierarchies, including a mini board and HR management.

User Management: Create, edit, and manage users with specific roles and permissions.
## Technologies Used


Programming Language: Python

Framework: Django, Django Rest Framework

Database: PostgreSQL

Authentication: Django Signals, Advanced Role-Based Access Control (RBAC)
## Setup and Installation

1- Clone the repository:

git clone https://github.com/Es1amMohamed/ERP-System.git

cd ERP-System

2- Create and activate a virtual environment:

python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows  

3- Install the required dependencies:

pip install -r requirements.txt  

4- Apply migrations:

python manage.py migrate  

5- Run the development server:

python manage.py runserver  


## Usage


Admin Panel: Manage users, roles, and permissions.

API Endpoints: Accessible for authorized users to perform CRUD operations.

Future Features: Expand modules to include inventory management, financial tracking, and production scheduling.
## Current Status

This project is a work in progress. The focus is currently on building robust models and implementing core backend functionalities before extending to other features like views and integrations.
## Contributions


Contributions are welcome! Feel free to fork the repository and submit a pull request with your suggestions or improvements.
## License


This project is licensed under the MIT License.
