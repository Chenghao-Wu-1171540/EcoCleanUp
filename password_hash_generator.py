"""
Script to generate bcrypt password hashes for initial user accounts in EcoCleanUp Hub.
COMP639 S1 2026 Individual Assignment - Chenghao

This script generates secure bcrypt hashes for:
- 20 Volunteers
- 5 Event Leaders
- 2 Administrators

Run this script once, copy the generated hashes into populate_database.sql
"""

from collections import namedtuple
from flask import Flask
from flask_bcrypt import Bcrypt

# Simple data structure for user accounts
UserAccount = namedtuple('UserAccount', ['username', 'password', 'role', 'full_name', 'email'])

app = Flask(__name__)
flask_bcrypt = Bcrypt(app)

# ────────────────────────────────────────────────
# init user（27 account）
# ────────────────────────────────────────────────
users = [

    # Volunteers (20)
    UserAccount('volunteer01', 'VolGreen2026!', 'volunteer', 'Emma Wilson', 'emma.w@example.nz'),
    UserAccount('volunteer02', 'CleanEarth25$', 'volunteer', 'Liam Thompson', 'liam.t@example.nz'),
    UserAccount('volunteer03', 'EcoHero2026!', 'volunteer', 'Olivia Chen', 'olivia.c@example.nz'),
    UserAccount('volunteer04', 'RecycleNow22', 'volunteer', 'Noah Harris', 'noah.h@example.nz'),
    UserAccount('volunteer05', 'GreenSteps!26', 'volunteer', 'Ava Martinez', 'ava.m@example.nz'),
    UserAccount('volunteer06', 'TrashFree2026', 'volunteer', 'Lucas Walker', 'lucas.w@example.nz'),
    UserAccount('volunteer07', 'EcoWarrior$25', 'volunteer', 'Isabella Lee', 'isabella.l@example.nz'),
    UserAccount('volunteer08', 'PlantMore2026', 'volunteer', 'Mason King', 'mason.k@example.nz'),
    UserAccount('volunteer09', 'CleanNZ!2026', 'volunteer', 'Sophia Patel', 'sophia.p@example.nz'),
    UserAccount('volunteer10', 'ZeroWaste26$', 'volunteer', 'Ethan Nguyen', 'ethan.n@example.nz'),
    UserAccount('volunteer11', 'NatureLove2026', 'volunteer', 'Mia Robinson', 'mia.r@example.nz'),
    UserAccount('volunteer12', 'EcoFriend$26', 'volunteer', 'James White', 'james.w@example.nz'),
    UserAccount('volunteer13', 'RubbishGone25!', 'volunteer', 'Charlotte Scott', 'charlotte.s@example.nz'),
    UserAccount('volunteer14', 'GreenCanterbury', 'volunteer', 'Benjamin Adams', 'benjamin.a@example.nz'),
    UserAccount('volunteer15', 'CleanUp2026!', 'volunteer', 'Amelia Clark', 'amelia.c@example.nz'),
    UserAccount('volunteer16', 'SavePlanet26$', 'volunteer', 'Daniel Lewis', 'daniel.l@example.nz'),
    UserAccount('volunteer17', 'EcoActive2026', 'volunteer', 'Harper Turner', 'harper.t@example.nz'),
    UserAccount('volunteer18', 'NoTrashZone!', 'volunteer', 'Alexander Hall', 'alex.h@example.nz'),
    UserAccount('volunteer19', 'GreenHeart25', 'volunteer', 'Evelyn Young', 'evelyn.y@example.nz'),
    UserAccount('volunteer20', 'CleanFuture26!', 'volunteer', 'Logan Wright', 'logan.w@example.nz'),

    # Event Leaders (5)
    UserAccount('leader01', 'LeadClean2026!', 'event_leader', 'Sarah Mitchell', 'sarah.m@example.nz'),
    UserAccount('leader02', 'EventEco$2026', 'event_leader', 'Jacob Green', 'jacob.g@example.nz'),
    UserAccount('leader03', 'CleanupBoss26!', 'event_leader', 'Zoe Campbell', 'zoe.c@example.nz'),
    UserAccount('leader04', 'GreenLeader2026', 'event_leader', 'Henry Baker', 'henry.b@example.nz'),
    UserAccount('leader05', 'EcoManager$25', 'event_leader', 'Lily Evans', 'lily.e@example.nz'),

    # Administrators (2)
    UserAccount('admin01', 'SuperEco2026!', 'admin', 'Admin One', 'admin1@ecocleanup.nz'),
    UserAccount('admin02', 'EcoControl2026$', 'admin', 'Admin Two', 'admin2@ecocleanup.nz'),
]

print('=' * 100)
print('EcoCleanUp Hub - Initial Password Hashes Generator')
print('COMP639 S1 2026 - For assignment population script only')
print('=' * 100)
print(f"{'Username':<15} | {'Plain Password':<18} | {'Role':<12} | {'Full Name':<20} | {'Email':<30} | {'Hash':<60} | Matches")
print('-' * 160)

for user in users:
    # create bcrypt hash（default rounds=12）
    password_hash = flask_bcrypt.generate_password_hash(user.password)

    # valid
    password_matches = flask_bcrypt.check_password_hash(password_hash, user.password)

    # print（hash.decode()）
    print(f"{user.username:<15} | {user.password:<18} | {user.role:<12} | {user.full_name:<20} | {user.email:<30} | {password_hash.decode():<60} | {password_matches}")