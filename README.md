# English Spoken Partner Finding Web App

A modern and scalable **Django REST Framework (DRF)** backend for a web application that helps users find language partners and practice English speaking effectively.

---

## 🚀 Planned Features

- **User Authentication**
  - Secure authentication using JWT via SimpleJWT.

- **Modular Architecture**
  - Clean, scalable, and domain-driven application structure.

- **Dual Environment Configuration**
  - Separate settings for:
    - Development (Local)
    - Production

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Django | Backend Framework |
| Django REST Framework (DRF) | REST API Development |
| PostgreSQL | Database |
| Supabase PostgreSQL | Production Database |
| django-environ | Environment Variable Management |
| SimpleJWT | JWT Authentication |

---

## 📂 Project Structure

```text
English_spoken_partner_finding/
├── apps/
├── config/
├── requirements.txt
├── manage.py
└── README.md
```

> Project structure may evolve as development progresses.

---

## 💻 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/abdul-zabbar04/English_spoken_partner_finding.git
cd English_spoken_partner_finding
```

### 2. Create and Activate a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python3 manage.py migrate
```

### 5. Run the Development Server

```bash
python3 manage.py runserver
```

---

## 🔐 Authentication

The project uses **JWT (JSON Web Token)** authentication powered by **SimpleJWT**.

---

## 🌍 Environment Configuration

Environment variables are managed using **django-environ** to support separate configurations for:

- Development Environment
- Production Environment

---

## 🗄️ Database Configuration

| Environment | Database |
|------------|----------|
| Development | PostgreSQL (Local) |
| Production | Supabase PostgreSQL |

---

## 📌 Project Status

This project is currently under active development. Features and architecture may evolve as new requirements are added.

---

## 📄 License

Choose an appropriate license before releasing the project publicly (e.g., MIT License).