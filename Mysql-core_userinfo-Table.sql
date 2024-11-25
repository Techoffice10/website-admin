show databases;

use website_db;
DESCRIBE core_userinfo;
SHOW COLUMNS FROM core_userinfo;

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

select * from core_userinfo;