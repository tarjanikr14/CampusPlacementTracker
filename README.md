# Campus Placement Tracker

A Python-based web application that helps students organise and monitor their campus placement journey by managing job applications, interviews, and interview preparation through an interactive dashboard.

## Features

- **Dashboard:** View placement statistics, recent applications, and application activity.
- **Application Management:** Add, view, edit, delete, search, and filter company applications.
- **Interview Management:** Schedule, view, edit, and delete interview records.
- **Interview Preparation:** Manage preparation topics, maintain study notes, and track completion progress.
- **Analytics:** Monitor application statistics, interview insights, and preparation progress.
- **Export Reports:** Download application, interview, and preparation records as CSV files.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| SQLite | Database management |
| Pandas | Data handling and CSV exports |

## Project Structure

```text
CampusPlacementTracker/
│
├── app.py
├── database.py
├── theme.py
├── placements.db
├── .gitignore
│
└── pages/
    ├── 1_Dashboard.py
    ├── 2_View_Applications.py
    ├── 3_Add_Application.py
    ├── 4_Edit_Application.py
    ├── 5_Delete_Application.py
    ├── 6_View_Interviews.py
    ├── 10_Schedule_Interview.py
    ├── 11_Edit_Interview.py
    ├── 12_Delete_Interview.py
    ├── 13_View_Preparation.py
    ├── 14_Add_Preparation_Topic.py
    ├── 15_Edit_Preparation_Topic.py
    ├── 16_Delete_Preparation_Topic.py
    ├── 17_Placement_Overview.py
    ├── 18_Application_Analytics.py
    ├── 19_Interview_Analytics.py
    ├── 20_Preparation_Progress.py
    ├── 21_Export_Applications.py
    ├── 22_Export_Interviews.py
    └── 23_Export_Preparation.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/tarjanikr14/CampusPlacementTracker.git
```

### 2. Navigate to the project folder

```bash
cd CampusPlacementTracker
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install streamlit pandas
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your web browser.

## Database

The application uses SQLite to store company applications, interview schedules, and preparation topics locally.

## Future Enhancements

- User authentication
- Placement notifications and reminders
- Advanced placement analytics
- Resume management

---

**Developed as a student project using Python and Streamlit.**