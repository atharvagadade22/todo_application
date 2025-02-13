# Todo Application

This is a simple Todo application built using Python (Django) for the backend and JavaScript (React) for the frontend.

## Features

- Create, read, update, and delete (CRUD) todo items
- Simple and intuitive user interface
- Responsive design

## Tech Stack

- **Backend**: Python, Django, Django REST framework
- **Frontend**: React, Axios
- **Styling**: CSS

## Getting Started

### Prerequisites

- Python 3.x
- Node.js
- npm or yarn

### Backend Setup

1. Clone the repository:

```bash
git clone https://github.com/atharvagadade22/todo_application.git
cd todo_application/todo_backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the migrations:

```bash
python manage.py migrate
```

5. Start the Django development server:

```bash
python manage.py runserver
```

### Frontend Setup

1. Navigate to the frontend directory:

```bash
cd ../todo_frontend
```

2. Install the dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

## Usage

- Navigate to `http://127.0.0.1:8000` to access the backend API.
- Navigate to `http://localhost:3000` to access the frontend application.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

---

Feel free to modify the content as per your project's requirements.
