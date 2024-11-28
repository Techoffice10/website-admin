show databases;

use website_db;
DESCRIBE core_userinfo;
SHOW COLUMNS FROM core_userinfo;

SET SQL_SAFE_UPDATES = 0; -- Safe mode is OFF
SET SQL_SAFE_UPDATES = 1; -- Safe mode is On

INSERT INTO core_userinfo (
    user_name,
    full_name,
    phone_no,
    email,
    node,
    branch,
    ext_no,
    port_ip,
    password,
    power_broker_id,
    applied_rating_id,
    user_creation_date,
    suspended_date,
    status
)
VALUES (
    'janedoe',                    -- user_name
    'Jane Doe',                   -- full_name
    '9876543210',                 -- phone_no
    'janedoe@example.com',        -- email
    'node_02',                    -- node
    'East Branch',                -- branch
    'ext_002',                    -- ext_no
    '192.168.1.101',              -- port_ip
    'hashed_password_example',    -- password 
    'broker_02',                  -- power_broker_id
    'rating_02',                  -- applied_rating_id
    '2024-11-20',                 -- user_creation_date
    NULL,                         -- suspended_date 
    'active'                      -- status
);

INSERT INTO core_billingmodel (
    client_name,
    client_address,
    billing_to,
    service_type,
    bill_description,
    ticket_id,
    created_date,
    emailed,
    comments,
    invoice_no,
    invoice_date
)
VALUES (
    'CIC Toronto',     -- client_name,
    '155-2960 Drew Road Malton Mississauga,ON L4T 0A5',  -- client_address,
    'CIC Toronto',    -- billing_to,
    NULL,             -- service_type,
    'Outlook & Storage Issue 75.00',       -- bill_description,
    '#21368',         -- ticket_id,
    NULL,            -- created_date,
     'Email &Hand Submitted',    -- emailed,
    '',              -- comments,
    '',              -- invoice_no,
    NULL,            -- invoice_date
);


ALTER TABLE core_userinfo
ADD COLUMN history VARCHAR(255);

describe core_billingmodel;
ALTER TABLE core_billingmodel DROP COLUMN emailed;
DROP TABLE IF EXISTS core_billingmodel;
ALTER TABLE core_billingmodel MODIFY ticket_id VARCHAR(50);
DELETE FROM core_billingmodel;

DROP TABLE core_billingmodel;

show tables;
INSERT INTO core_billingmodel (client_name, client_address, billing_to, service_type, bill_description, ticket_id, created_date, emailed, comments, invoice_no, invoice_date)
VALUES
('John Doe', '123 Maple Street, Springfield, IL', 'ACME Corp', 'Consulting', 'Consulting services for Q3 2024', 'TICKET123', '2024-11-01 10:30:00', 'NO', 'Payment pending', 'INV001', '2024-11-01'),
('Henry Wilson', '789 Maple Avenue, San Francisco, CA', 'DataPros', 'Consulting', 'Consulting for database migration project', 'TICKET132', '2024-11-25 12:00:00', 'YES', 'Payment received', 'INV010', '2024-11-25');



select * from core_userinfo;



ALTER TABLE core_billingmodel
MODIFY invoice_no VARCHAR(50);



select * from core_billingmodel;