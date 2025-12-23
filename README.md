# Smartsheet Clone Project

This is a full-stack project management application inspired by Smartsheet. It is built with a Django backend and a React frontend, and it includes features like real-time collaboration, multiple views (Grid, Gantt, Kanban), and dependency tracking.

## Features

### Core MVP
- [x] User authentication (registration, login with JWT)
- [x] Projects/Sheets: Create, edit, share sheets as project plans.
- [ ] Grid View: Spreadsheet-like editable grid.
- [ ] Column types: Text, Date, Dropdown, Contact List, Checkbox, Duration.
- [ ] Hierarchical rows (parent/child tasks).
- [ ] Attachments/comments per row.
- [ ] Dependencies: Predecessor column.
- [ ] Multiple Views per Sheet:
    - [ ] Gantt View
    - [ ] Card View (Kanban)
- [ ] Critical Path Highlighting.
- [ ] Dashboards with widgets.

### Advanced Features
- [ ] Real-time collaboration for simultaneous editing.
- [ ] Automation triggers on status change.
- [ ] Sharing & Publishing sheets and dashboards.
- [ ] Resource Management basics.

## Tech Stack

### Backend
- **Framework:** Django 5.x
- **API:** Django REST Framework (DRF)
- **Real-time:** Django Channels with Redis for WebSockets
- **Database:** PostgreSQL
- **Async Tasks:** Celery with Redis
- **Authentication:** Simple JWT (JSON Web Tokens)
- **Environment Variables:** python-dotenv

### Frontend
- **Framework:** React 18+
- **Build Tool:** Vite
- **Language:** TypeScript
- **API Communication:** Axios (to be added)
- **WebSocket Communication:** socket.io-client (to be added)
- **UI Components:**
    - **Grid View:** Handsontable / ag-Grid (to be added)
    - **Gantt View:** react-gantt-timeline / framer-motion (to be added)
    - **Card View:** react-beautiful-dnd (to be added)
    - **Dashboards:** react-grid-layout, Recharts (to be added)

## Project Structure

```
/
|-- project_manager_clone/  # Django project
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- auth_app/             # Django app for authentication
|   |-- ...
|-- core/                 # Django app for core models
|   |-- ...
|-- sheets/               # Django app for sheets, rows, columns, etc.
|   |-- ...
|-- api/                  # Django app for API routing
|   |-- urls.py
|-- pm-frontend/          # React frontend application
|   |-- src/
|   |   |-- main.tsx
|   |-- package.json
|   |-- ...
|-- manage.py
|-- requirements.txt
|-- README.md
```

## API Endpoints

The API is built with Django REST Framework and provides the following endpoints:

- `POST /api/auth/register/`: Register a new user.
- `POST /api/auth/token/`: Obtain a JWT token pair (access and refresh).
- `POST /api/auth/token/refresh/`: Refresh an access token.

### Sheets
- `GET, POST /api/sheets/`: List all sheets for the user, or create a new sheet.
- `GET, PUT, PATCH, DELETE /api/sheets/{id}/`: Retrieve, update, or delete a sheet.
- `POST /api/sheets/{id}/share/`: Share a sheet with other users.

### Columns
- `GET, POST /api/sheets/{sheet_pk}/columns/`: List all columns for a sheet, or create a new column.
- `GET, PUT, PATCH, DELETE /api/sheets/{sheet_pk}/columns/{id}/`: Retrieve, update, or delete a column.

### Rows
- `GET, POST /api/sheets/{sheet_pk}/rows/`: List all rows for a sheet, or create a new row.
- `GET, PUT, PATCH, DELETE /api/sheets/{sheet_pk}/rows/{id}/`: Retrieve, update, or delete a row.

### Cells
- `GET, POST /api/sheets/{sheet_pk}/rows/{row_pk}/cells/`: List all cells for a row, or create a new cell.
- `GET, PUT, PATCH, DELETE /api/sheets/{sheet_pk}/rows/{row_pk}/cells/{id}/`: Retrieve, update, or delete a cell.

## Real-time Collaboration

Real-time collaboration is handled using Django Channels and WebSockets. When a user connects to a sheet, they are added to a group for that sheet. When a change is made to the sheet (e.g., a cell is updated), a message is broadcast to all users in the group, and the frontend updates in real-time.

The WebSocket connection is established at `ws/sheets/{sheet_id}/`.

## Database Schema

The database schema is designed to be flexible and scalable. The main models are:

- **User:** Stores user information.
- **Sheet:** The main container for a project plan.
- **Column:** Defines the columns in a sheet, including their type (text, date, etc.).
- **Row:** Represents a row in a sheet, and can have a parent-child relationship with other rows.
- **Cell:** Stores the value for a specific row and column.
- **Dependency:** Defines the relationship between rows (e.g., Finish-to-Start).
- **Attachment:** Stores files attached to a row.
- **Comment:** Stores comments made on a row.

## Getting Started

To get the project up and running locally, you will need to have Python, Node.js, PostgreSQL, and Redis installed on your system.

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    - Make sure you have PostgreSQL installed and running.
    - Create a new database and user for the project.
    - Create a `.env` file in the root of the project and add the following environment variables:
      ```
      SECRET_KEY=your-secret-key
      DATABASE_URL=postgres://user:password@localhost:5432/your-db-name
      REDIS_URL=redis://localhost:6379/0
      ```

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Start the backend server:**
    ```bash
    python manage.py runserver
    ```
    The backend will be running at `http://localhost:8000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd pm-frontend
    ```

2.  **Install frontend dependencies:**
    ```bash
    npm install
    ```

3.  **Start the frontend development server:**
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://localhost:5173`.

## Backend Configuration

The backend is configured using environment variables. These are loaded from a `.env` file in the root of the project using `python-dotenv`.

- `SECRET_KEY`: Django's secret key.
- `DATABASE_URL`: The URL for the PostgreSQL database.
- `REDIS_URL`: The URL for the Redis instance used by Celery and Channels.

## Running Tests

(Coming soon)

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
