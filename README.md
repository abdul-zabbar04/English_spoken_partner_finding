# English Spoken Partner Finding Web App

An industry-standard Django REST Framework (DRF) backend for a web application designed to help users find and practice English speaking with language partners.

## 🚀 Key Features (Planned)
- **User Authentication:** Secure authentication using JWT (SimpleJWT).
- **Modular Architecture:** Clean, scalable, and domain-driven apps structure.
- **Dual Environments:** Separate configurations for Development (Local) and Production.

## 🛠️ Tech Stack
- **Backend Framework:** Django & Django REST Framework (DRF)
- **Database:** SQLite3 (Development) / Supabase PostgreSQL (Production)
- **Environment Management:** django-environ

## 💻 Local Setup & Installation

1. **Clone the repository:**
```bash
   git clone [https://github.com/abdul-zabbar04/English_spoken_partner_finding.git](https://github.com/abdul-zabbar04/English_spoken_partner_finding.git)
   cd English_spoken_partner_finding

2. Create and Activate Virtual Environment:

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies:

pip install -r requirements.txt

4. Run Migrations:

python3 manage.py migrate

5. Start Development Server:

python3 manage.py runserver