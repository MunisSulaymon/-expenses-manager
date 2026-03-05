# 💰 Expenses Manager

A Django web application to track personal income and expenses.

## Features

- User authentication (register, login, logout)
- Add, edit, and delete income records
- Add, edit, and delete expense records
- Categories with emoji icons
- Dashboard with total income, expenses, and balance
- Each user sees only their own data

## Apps

- `accounts` — user registration, login, profile
- `categories` — manage income/expense categories
- `income` — track money coming in
- `outcome` — track money going out

## Tech Stack

- Python
- Django
- SQLite
- HTML & CSS

## Setup

1. Clone the repository
```
   git clone https://github.com/YOUR_USERNAME/expenses-manager.git
```

2. Create and activate virtual environment
```
   python -m venv myenv
   myenv\Scripts\activate
```

3. Install dependencies
```
   pip install django
```

4. Run migrations
```
   python manage.py migrate
```

5. Create superuser
```
   python manage.py createsuperuser
```

6. Run the server
```
   python manage.py runserver
```


## Author

MunisSulaymon