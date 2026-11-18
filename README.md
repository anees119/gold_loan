# Gold CRM Backend (Flask + MySQL)

Starter REST API based on the Add Enquiry screen supplied for the project.

## 1. Requirements
- Python 3.10+
- XAMPP MySQL
- MySQL port configured in XAMPP (this starter defaults to `3307`)

## 2. Create the database
Start MySQL in XAMPP, open phpMyAdmin, and run:

```sql
CREATE DATABASE gold_crm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

If your MySQL uses port `3306`, change `DB_PORT` in `.env`.

## 3. Install (Windows PowerShell)

```powershell
cd gold-crm-backend
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` with your MySQL credentials and secrets. Generate a Fernet key:

```powershell
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Paste the generated value into `FIELD_ENCRYPTION_KEY`.

## 4. Create tables and first admin

```powershell
python scripts/create_admin.py
```

This creates the starter tables and prompts you to create an admin user. For ongoing schema changes, use Flask-Migrate (commands below).

## 5. Run API

```powershell
python run.py
```

API base URL: `http://127.0.0.1:5000`

Health check: `GET /api/health`

## 6. Initial endpoints

| Method | Endpoint | Auth |
|---|---|---|
| POST | `/api/auth/login` | No |
| GET | `/api/auth/me` | JWT |
| GET, POST | `/api/branches` | JWT |
| POST, GET | `/api/customers` | JWT |
| POST, GET | `/api/enquiries` | JWT |
| GET | `/api/enquiries/<id>` | JWT |

### Login request

```json
{
  "username": "admin",
  "password": "your-admin-password"
}
```

Use the returned `access_token` as:

`Authorization: Bearer YOUR_ACCESS_TOKEN`

### Create branch

```json
{
  "branch_name": "Main Branch",
  "address": "Thrissur",
  "phone": "9876543210"
}
```

### Create enquiry (creates customer if customer_id is omitted)

```json
{
  "branch_id": 1,
  "customer": {
    "customer_name": "Sample Customer",
    "contact_number": "9876543210",
    "gender": "Male",
    "aadhaar": "123412341234",
    "pan": "ABCDE1234F",
    "address": "Thrissur"
  },
  "priority_level": "High",
  "pawner_name": "Sample Pawner",
  "products": [
    {
      "product_name": "Gold chain",
      "gross_weight": 12.5,
      "deduction": 0.5
    }
  ],
  "loan_amount": 50000,
  "article_value": 60000,
  "interest_percent": 1.5,
  "interest_amount": 750,
  "other_charges": 100,
  "total_due": 50850,
  "remarks": "Sample enquiry"
}
```

The API calculates each row's net weight and the total gross, deduction and net weights. Aadhaar/PAN are encrypted at rest and are not returned in full.

## Notes before production
- Replace all development secrets.
- Restrict CORS to the real frontend origin.
- Use HTTPS and database backups.
- Add role/branch authorization checks before exposing the system to multiple branches.
- Do not log Aadhaar/PAN values.
- Add audit trails and formal migration history before production deployment.
