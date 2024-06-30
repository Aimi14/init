CREATE TABLE funds (
    fund_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manager_name VARCHAR(255),
    description TEXT,
    nav DECIMAL,
    date_of_creation DATE,
    performance DECIMAL
);
