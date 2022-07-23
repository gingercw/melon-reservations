# 🍉 Melon Reservations
Welcome to Melon Reservations. Melon Reservations allows users to book a 30-minute melon tasting appointment, where they can try the most exclusive melons.

# 🧭 Table of Contents
- Tech Stack
- Features
- Installation

# 🤖 Tech Stack
- Python
- Flask
- Jinja
- PostgreSQL
- SQLAlchemy
- HTML
- CSS
- Bootstrap

# 🏔️ Features

### Sign In
Users given access to Melon Reservations can sign in to book an appointment with their name

### Appointment Search
Users can select a date for a melon tasting and a preferred time in the day to search for available tasting appointments. This feature leverages the datetime library in Python. 

### Book a Tasting
Users can book a 30-minute appointment. Once booked, the timeslot is removed from the list.

### See Appointments
Users can see their upcoming tastings. 

# 🪛 Installation
**Requirements:**
- PostgreSQL

**1. Clone or fork the repo and open it in your IDE.**
```
https://github.com/gingercw/melon-reservations
```

**2. Create and activate a virtual environment inside the directory.**
```
$ virtualenv env
$ source env/bin/activate
```

**3. Install the dependencies.**
```
$ pip install -r requirements.txt
```
