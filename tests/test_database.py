import sqlite3

import database


def test_database_initialization(tmp_path, monkeypatch):
    test_db = tmp_path / "test.db"

    monkeypatch.setattr(
        database,
        "DB_PATH",
        test_db
    )

    database.initialize_database()

    conn = sqlite3.connect(test_db)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    tables = {
        row[0]
        for row in cursor.fetchall()
    }

    conn.close()

    assert "cost_runs" in tables
    assert "service_costs" in tables
    assert "anomalies" in tables


def test_save_cost_run(tmp_path, monkeypatch):
    test_db = tmp_path / "test.db"

    monkeypatch.setattr(
        database,
        "DB_PATH",
        test_db
    )

    database.initialize_database()

    summary = {
        "run_date": "2026-09-14",
        "total_cost": 100.0,
        "gross_positive_cost": 110.0,
        "credits_adjustments": -10.0,
        "previous_total": 80.0,
        "cost_change_percent": 25.0,
        "services": [
            {
                "service": "Amazon EC2",
                "cost": 100.0
            }
        ]
    }

    anomalies = [
        {
            "service": "Amazon EC2",
            "severity": "HIGH",
            "previous_cost": 50.0,
            "current_cost": 100.0,
            "change_percent": 100.0
        }
    ]

    run_id = database.save_cost_run(
        summary,
        anomalies
    )

    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT total_cost FROM cost_runs WHERE id = ?",
        (run_id,)
    )

    cost_run = cursor.fetchone()

    cursor.execute(
        "SELECT service, cost FROM service_costs WHERE run_id = ?",
        (run_id,)
    )

    service = cursor.fetchone()

    cursor.execute(
        "SELECT service, severity FROM anomalies WHERE run_id = ?",
        (run_id,)
    )

    anomaly = cursor.fetchone()

    conn.close()

    assert cost_run == (100.0,)
    assert service == ("Amazon EC2", 100.0)
    assert anomaly == ("Amazon EC2", "HIGH")
