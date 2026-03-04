# EcoCleanUp Hub - COMP639 S1 2026 Individual Assignment

**Author:** Chenghao Wu (Student ID: 1171540)  
**Course:** COMP639 - Web Application Development  
**Submission Date:** March 4, 2026  
**Project Type:** Flask + PostgreSQL web application for organizing and participating in community clean-up events

## Project Overview

EcoCleanUp Hub is a web platform designed to help Canterbury residents organize and join local environmental clean-up events (beach, river, park, track, etc.).

**Main features:**
- User registration & role-based login (volunteer / event_leader / admin)
- Browse upcoming events with filters (location, date, event type)
- Register / unregister for events
- Event leaders can create, edit, cancel events and record outcomes
- Admins can manage users and view platform reports
- Feedback submission after attending events
- Responsive UI with Bootstrap 5

**Technology stack:**
- Backend: Flask (Python)
- Database: PostgreSQL
- Frontend: Jinja2 templates + Bootstrap 5 + custom CSS/JS
- Authentication: flask_bcrypt for password hashing
- Deployment: Local development server (flask run)

## Login Information (Test Accounts)

Use these accounts to test different roles. All passwords are pre-hashed in the database population script.

| Role          | Username      | Password         | Full Name / Purpose                          |
|---------------|---------------|------------------|----------------------------------------------|
| Admin         | admin01       | SuperEco2026!    | Full platform management                     |
| Admin         | admin02       | EcoControl2026$  | Secondary admin account                      |
| Event Leader  | leader01      | LeaderGreen26!   | Can create/edit own events                   |
| Event Leader  | leader02      | CleanupBoss26!   | Another event organizer                      |
| Volunteer     | volunteer01   | VolGreen2026!    | Regular volunteer account                    |
| Volunteer     | volunteer02   | CleanEarth25$    | Test account for registration & participation|

More users can view the "password.txt" file of this project.

**Note:** More test accounts (volunteers 01–20, leaders 01–05, admins 01–02) are pre-populated in `populate_database.sql`. Passwords are generated via `password_hash_generator.py`.

## Setup Instructions

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Unix)
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file with database connection (see `.env.example`)
6. Initialize database: run `create_database.sql` then `populate_database.sql`
7. Run the app: `flask run`

## GenAI Acknowledgement Statement

**Generative Artificial Intelligence (GenAI) Usage**

In accordance with the COMP639 S1 2026 assignment guidelines, the use of GenAI tools is permitted and has been used in this submission.

**Tools used:**
- Grok (built by xAI)
- GitHub Copilot (occasionally for code completion)

**How and when GenAI was used:**
- **Grok (primary tool)**:
  - Used extensively from February 20, 2026 to March 4, 2026
  - Purpose: Debugging Flask routing errors, fixing Jinja2 template issues, optimizing SQL queries, designing modal behavior, improving CSS layout coordination, generating code snippets for Bootstrap modals and event handling JavaScript, suggesting improvements to README structure, and helping with error trace analysis
  - Typical prompts examples:
    - "Design pages with Bootstrap 5 and Jinja2 templates"
    - "The error is 'TemplateNotFound: event_detail.html' after adding the route. Help me create the template."
    - "Clicking Join button has no response. Modal doesn't pop up. Check my JavaScript."
    - "Give me a weighted random SQL to assign event_type from enum to all existing events."
    - "Help me write a proper GenAI acknowledgement statement for COMP639 assignment."

- **GitHub Copilot**:
  - Used occasionally during code writing in PyCharm
  - Purpose: Auto-completing repetitive code (e.g. Flask route boilerplate, SQL SELECT statements, Bootstrap class names)
  - No complete functions or large blocks were accepted without review and modification

**All code, templates, SQL, and documentation** were reviewed, modified, and understood by the author. No code was copied verbatim without comprehension or customization. GenAI was used as an assistant for problem-solving, debugging, and suggestion — not as a replacement for original work.

**Declaration:**
I, Chenghao Wu, confirm that I have read and understood the GenAI usage policy. I have appropriately acknowledged its use in this README file. I accept that my submission may be analyzed for GenAI content, and I am prepared to attend an oral follow-up interview if requested.
