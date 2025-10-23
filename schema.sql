PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    name TEXT,
    email TEXT,
    education TEXT,
    skills TEXT,
    work TEXT,
    projects TEXT,
    links TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT OR IGNORE INTO profile (id, name, email, education, skills, work, projects, links)
VALUES (1, NULL, NULL, NULL, json('[]'), json('[]'), json('[]'), json('{}'));
