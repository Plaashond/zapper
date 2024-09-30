
INSERT INTO transaction_database.customers VALUES (1,'jhon','jhon@email.com', B'00000001');
INSERT INTO transaction_database.customers VALUES ( 2,'james','james@email.com',0xFF);
INSERT INTO transaction_database.customers VALUES ( 3,'justin','justin@email.com',0x80);

-- example of how to read specific settings from database
SELECT
    settings & X'01' = X'01' AS 'SMS Notifications',
    settings & X'02' = X'02' AS 'Push Notifications',
    settings & X'04' = X'04' AS 'Bio-metrics',
    settings & X'08' = X'08' AS 'Camera',
    settings & X'10' = X'10' AS 'Location',
    settings & X'20' = X'20' AS 'NFC',
    settings & X'40' = X'40' AS 'Vouchers',
    settings & X'80' = X'80' AS 'Loyalty'
FROM transaction_database.customers;


--Question2.1
CREATE PROCEDURE transaction_database.check_user_setting(IN user_id INT, IN setting TEXT)
BEGIN
  DECLARE binary_value BINARY(1);
  SET binary_value = CASE
    WHEN setting = 'SMS Notifications' THEN X'01'
    WHEN setting = 'Push Notifications' THEN X'02'
    WHEN setting = 'Bio-metrics' THEN X'04'
    WHEN setting = 'Camera' THEN X'08'
    WHEN setting = 'Location' THEN X'10'
    WHEN setting = 'NFC' THEN X'20'
    WHEN setting = 'Vouchers' THEN X'40'
    WHEN setting = 'Loyalty' THEN X'80'
    ELSE 0
  END;
  SELECT CASE WHEN settings & binary_value = binary_value  THEN 'Enabled' ELSE 'Disabled' END AS setting_status
  FROM transaction_database.customers
  WHERE id = user_id;
END;

CALL transaction_database.check_user_setting(2, 'SMS Notifications');
CALL transaction_database.check_user_setting(3, 'SMS Notifications');
