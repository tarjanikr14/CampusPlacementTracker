
import sqlite3

# Connect to the database
def connect_db():
    connection = sqlite3.connect("placements.db")
    connection.row_factory = sqlite3.Row
    return connection


# Create the applications table
def create_table():
    connection = connect_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            job_role TEXT NOT NULL,
            package REAL,
            application_date TEXT,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()


# Add a new company application
def add_application(company, role, package, date, status):
    connection = connect_db()

    connection.execute("""
        INSERT INTO applications
        (company_name, job_role, package, application_date, status)
        VALUES (?, ?, ?, ?, ?)
    """, (company, role, package, str(date), status))

    connection.commit()
    connection.close()


# Retrieve all applications
def get_applications():
    connection = connect_db()

    applications = connection.execute(
        "SELECT * FROM applications ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return [dict(row) for row in applications]


# Update an existing application
def update_application(app_id, company, role, package, date, status):
    connection = connect_db()

    connection.execute("""
        UPDATE applications
        SET company_name = ?,
            job_role = ?,
            package = ?,
            application_date = ?,
            status = ?
        WHERE id = ?
    """, (company, role, package, str(date), status, app_id))

    connection.commit()
    connection.close()


# Delete an application
def delete_application(app_id):
    connection = connect_db()

    connection.execute(
        "DELETE FROM applications WHERE id = ?",
        (app_id,)
    )

    connection.commit()
    connection.close()



# Create interview records table
def create_interview_table():

    connection = connect_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER NOT NULL,
            round_name TEXT NOT NULL,
            interview_date TEXT,
            status TEXT,
            notes TEXT,
            FOREIGN KEY (application_id)
                REFERENCES applications(id)
        )
    """)

    connection.commit()
    connection.close()


# Add an interview
def add_interview(app_id, round_name, interview_date, status, notes):

    connection = connect_db()

    connection.execute("""
        INSERT INTO interviews
        (application_id, round_name, interview_date, status, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (
        app_id,
        round_name,
        str(interview_date),
        status,
        notes
    ))

    connection.commit()
    connection.close()


# Retrieve all interviews

# Retrieve all interviews
def get_interviews():

    connection = connect_db()

    interviews = connection.execute("""
        SELECT
            interviews.id,
            interviews.application_id,
            applications.company_name,
            applications.job_role,
            interviews.round_name,
            interviews.interview_date,
            interviews.status,
            interviews.notes
        FROM interviews
        JOIN applications
        ON interviews.application_id = applications.id
        ORDER BY interviews.interview_date
    """).fetchall()

    connection.close()

    return [dict(row) for row in interviews]


# Update an existing interview
def update_interview(interview_id, app_id, round_name, interview_date, status, notes):

    connection = connect_db()

    connection.execute("""
        UPDATE interviews
        SET application_id = ?,
            round_name = ?,
            interview_date = ?,
            status = ?,
            notes = ?
        WHERE id = ?
    """, (
        app_id,
        round_name,
        str(interview_date),
        status,
        notes,
        interview_id
    ))

    connection.commit()
    connection.close()

# Delete an interview
def delete_interview(interview_id):

    connection = connect_db()

    connection.execute(
        "DELETE FROM interviews WHERE id = ?",
        (interview_id,)
    )

    connection.commit()
    connection.close()



# Create interview preparation table
def create_preparation_table():
    connection = connect_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS preparation_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER NOT NULL,
            topic TEXT NOT NULL,
            notes TEXT,
            is_completed INTEGER DEFAULT 0,
            FOREIGN KEY (application_id)
                REFERENCES applications(id)
        )
    """)

    connection.commit()
    connection.close()



# Add a preparation topic
def add_preparation_topic(app_id, topic, notes):
    connection = connect_db()

    connection.execute("""
        INSERT INTO preparation_notes
        (application_id, topic, notes)
        VALUES (?, ?, ?)
    """, (app_id, topic, notes))

    connection.commit()
    connection.close()


# Retrieve preparation topics
def get_preparation_topics():
    connection = connect_db()

    topics = connection.execute("""
        SELECT
            preparation_notes.id,
            preparation_notes.application_id,
            applications.company_name,
            applications.job_role,
            preparation_notes.topic,
            preparation_notes.notes,
            preparation_notes.is_completed
        FROM preparation_notes
        JOIN applications
        ON preparation_notes.application_id = applications.id
        ORDER BY preparation_notes.id DESC
    """).fetchall()

    connection.close()
    return [dict(row) for row in topics]


# Mark a topic as completed or incomplete
def update_preparation_status(topic_id, completed):
    connection = connect_db()

    connection.execute("""
        UPDATE preparation_notes
        SET is_completed = ?
        WHERE id = ?
    """, (1 if completed else 0, topic_id))

    connection.commit()
    connection.close()


def update_preparation_topic(topic_id, app_id, topic, notes):
    connection = connect_db()
    connection.execute("""
        UPDATE preparation_notes
        SET application_id = ?,
            topic = ?,
            notes = ?
        WHERE id = ?
    """, (
        app_id,
        topic,
        notes,
        topic_id
    ))
    connection.commit()
    connection.close()


# Delete a preparation topic
def delete_preparation_topic(topic_id):
    connection = connect_db()

    connection.execute(
        "DELETE FROM preparation_notes WHERE id = ?",
        (topic_id,)
    )

    connection.commit()
    connection.close()
