# Premier Top Ten Application

A Flask + Bootstrap web application for managing and tracking Premier Martial Arts Top Ten tournament results.  
This project allows admins to manage divisions, belt ranks, schools, events, tournaments, and contestant results, while also providing filtering and ranking functionality.

---

## Features

- **Tournament Results**
  - View results in a searchable and filterable table
  - Filter by division, belt rank, school, event, tournament, or name
  - Refresh table without reloading the page

- **Admin Center**
  - Manage (CRUD) data for:
    - Top Ten results
    - Divisions
    - Belt Ranks
    - Schools
    - Events
    - Tournaments
  - Edit existing entries through a modal form
  - Certain fields use dropdowns (populated dynamically from the database)
  - Temporary restrictions to prevent editing of sensitive fields

- **Data Entry**
  - Add new contestants with form fields linked to database tables
  - Dropdowns ensure consistent entries for divisions, belt ranks, schools, events, and tournaments

- **Ranking Updates**
  - One-click button to trigger recalculation of Top Ten rankings via Flask API

- **Help / About Page**
  - Known issues & fixes
  - Future improvements roadmap

---

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap 5, Vanilla JS
- **Database**: PostgreSQL
- **Deployment**: Local / Server (Flask app + PostgreSQL)

---

## API Endpoints (Sample)

- `/api/topten` → Get all Top Ten results (supports query filters)
- `/api/divisions` → Get divisions
- `/api/events` → Get events
- `/api/schools` → Get schools
- `/api/belt_ranks` → Get belt ranks
- `/api/all_tourn` → Get all tournaments
- `/api/add_data` → Add a new contestant (POST)
- `/api/<table>/<id>` → Update an entry (POST)

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/etaylor224/premier_top_ten_application.git
   cd premier_top_ten_application
