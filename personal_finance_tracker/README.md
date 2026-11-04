# Personal Finance Tracker

Personal Finance Tracker is a command-line application for tracking personal income and expenses.

The project focuses on practicing Python Core concepts, object-oriented programming, and application architecture.

**Project 2/3** of the Python Core project set.

## Features

- Add and remove financial transactions.
- Organize transactions into income and expense categories.
- View all transactions and filter them by date, category, type, and value.
- Calculate total income, expenses, and balance for a selected period.
- View a financial summary with a breakdown by category.
- Save and load data using JSON files.

## Concepts & Skills

Through this project, I practiced:

- **Object-Oriented Programming (OOP)** — designing classes, working with objects, encapsulation, and properties.
- **Application Architecture** — separating models, business logic, data storage, and the command-line interface.
- **Data Handling** — working with JSON, serialization, and deserialization.
- **Data Validation** — handling invalid input, validating object attributes, and raising exceptions.
- **Working with Dates and Numbers** — using `datetime` and `Decimal` for date handling and accurate financial calculations.
- **Python Modules and Packages** — organizing code into reusable modules and managing imports.

## Technologies

- Python
- JSON
- Standard Library

## Project Structure

```text
personal_finance_tracker/
├── data/
│   └── transactions.json
├── src/
│   ├── models/
│   │   ├── category.py
│   │   └── transaction.py
│   ├── services/
│   │   └── finance_manager.py
│   ├── storage/
│   │   └── json_handler.py
│   ├── cli/
│   │   └── menu.py
│   └── main.py
├── README.md
└── pyproject.toml
```

## Getting Started

1. Clone the repository or download the project.
2. Navigate to the project directory.
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m src.main
   ```