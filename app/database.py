import sqlite3
from pathlib import Path


DB_PATH = Path("data/costs.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    return conn

def initialize_database():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cost_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_date TEXT NOT NULL,
            total_cost REAL NOT NULL,
            gross_service_cost REAL NOT NULL,
            adjustments REAL NOT NULL,
            previous_total REAL NOT NULL,
            cost_change_percent REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS service_costs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER NOT NULL,
            service TEXT NOT NULL,
            cost REAL NOT NULL,
            FOREIGN KEY (run_id) REFERENCES cost_runs(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anomalies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER NOT NULL,
            service TEXT NOT NULL,
            severity TEXT NOT NULL,
            previous_cost REAL NOT NULL,
            current_cost REAL NOT NULL,
            change_percent REAL NOT NULL,
            FOREIGN KEY (run_id) REFERENCES cost_runs(id)
        )
    """)

    conn.commit()
    conn.close()


def save_cost_run(summary, anomalies):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cost_runs (
            run_date,
            total_cost,
            gross_service_cost,
            adjustments,
            previous_total,
            cost_change_percent
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        summary["run_date"],
        summary["total_cost"],
        summary["gross_positive_cost"],
        summary["credits_adjustments"],
        summary["previous_total"],
        summary["cost_change_percent"]
    ))

    run_id = cursor.lastrowid

    for service in summary["services"]:
        cursor.execute("""
            INSERT INTO service_costs (
                run_id,
                service,
                cost
            )
            VALUES (?, ?, ?)
        """, (
            run_id,
            service["service"],
            service["cost"]
        ))

    for anomaly in anomalies:
        cursor.execute("""
            INSERT INTO anomalies (
                run_id,
                service,
                severity,
                previous_cost,
                current_cost,
                change_percent
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            run_id,
            anomaly["service"],
            anomaly["severity"],
            anomaly["previous_cost"],
            anomaly["current_cost"],
            anomaly["change_percent"]
        ))

    conn.commit()
    conn.close()

    return run_id
