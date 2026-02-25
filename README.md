# EcoCleanUp Hub - Community Cleanup Management System
**COMP639 S1 2026 Individual Assignment**

**Author:** Chenghao Wu (Student ID: 1171540)

## GenAI Acknowledgement（必须有，否则整份0分）
I did it it by myself to assist with this assessment.

- **Tools used**: Grok (primary), password_hash_generator.py (official)
- **How it was used**: Generated full database scripts (create + populate), all Flask routes & logic (registration, event conflict detection, role-based access, reports, feedback, etc.), Bootstrap templates, README structure.
- **Specific prompts** (examples):
  - "Write full PostgreSQL create_database.sql matching the exact ERD in COMP639 assignment"
  - "Generate 20 realistic volunteers + 5 leaders + 2 admins for populate_database.sql"
  - "Provide complete Flask code for volunteer event registration with time conflict check"
  - "Create responsive Bootstrap home page for EcoCleanUp with green sustainability theme"
- **When**: 25-26 February 2026
- I reviewed, tested, and modified all GenAI output myself. I can fully explain every line of code.

## Setup Instructions
1. `python -m venv venv && source venv/bin/activate` (Windows 用 venv\Scripts\activate)
2. `pip install -r requirements.txt`
3. Run `create_database.sql` on PythonAnywhere Postgres
4. Run `populate_database.sql`
5. Edit `connect.py` with your Postgres details
6. `python run.py`

**Test Accounts** (after populate):
- Volunteer: volunteer1 / VolGreen2026!
- Event Leader: leader1 / LeadClean2026!
- Admin: admin1 / SuperEco2026!

PythonAnywhere: https://wuwu38392.pythonanywhere.com/login 
GitHub: https://github.com/Chenghao-Wu-1171540/EcoCleanUp

App name “EcoCleanUp” is displayed everywhere with green sustainability theme.