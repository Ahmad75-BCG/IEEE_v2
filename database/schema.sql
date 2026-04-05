CREATE TABLE energy_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    energy_kwh FLOAT NOT NULL,
    temperature FLOAT,
    occupancy INTEGER,
    level_source INTEGER -- 1: Manual/Estimated, 2: Wi-Fi, 3: IoT
);

CREATE TABLE energy_recommendations (
    id SERIAL PRIMARY KEY,
    log_id INTEGER REFERENCES energy_logs(id),
    recommendation_text TEXT,
    is_resolved BOOLEAN DEFAULT FALSE
);