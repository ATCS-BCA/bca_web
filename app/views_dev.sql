
DROP VIEW IF EXISTS user;
CREATE VIEW user AS SELECT * FROM atcsdevb_dev_shared.user where usr_active = 1;

DROP VIEW IF EXISTS users_all;
CREATE VIEW users_all AS SELECT * FROM atcsdevb_dev_shared.user;

DROP VIEW IF EXISTS user_type;
CREATE VIEW user_type AS SELECT * FROM atcsdevb_dev_shared.user_type;

DROP VIEW IF EXISTS user_role;
CREATE VIEW user_role AS SELECT * FROM atcsdevb_dev_shared.user_role;

DROP VIEW IF EXISTS log_lvl;
CREATE VIEW log_lvl AS SELECT * FROM atcsdevb_dev_shared.log_lvl;

DROP VIEW IF EXISTS log;
CREATE VIEW log AS SELECT * FROM atcsdevb_dev_shared.log;

DROP VIEW IF EXISTS application;
CREATE VIEW application AS SELECT * FROM atcsdevb_dev_shared.application;

DROP VIEW IF EXISTS role_application_user_xref;
CREATE VIEW role_application_user_xref AS SELECT * FROM atcsdevb_dev_shared.role_application_user_xref;

DROP VIEW IF EXISTS section_mods;
CREATE VIEW section_mods AS SELECT * FROM atcsdevb_dev_shared.section_mods;

DROP VIEW IF EXISTS day;
CREATE VIEW day AS SELECT * FROM atcsdevb_dev_shared.day;

DROP VIEW IF EXISTS section;
CREATE VIEW section AS SELECT * FROM atcsdevb_dev_shared.section;

DROP VIEW IF EXISTS ps_year;
CREATE VIEW ps_year AS SELECT * FROM atcsdevb_dev_shared.ps_year;

DROP VIEW IF EXISTS section_students;
CREATE VIEW section_students AS SELECT * FROM atcsdevb_dev_shared.section_students;

DROP VIEW IF EXISTS course;
CREATE VIEW course AS SELECT * FROM atcsdevb_dev_shared.course;

DROP VIEW IF EXISTS trimester;
CREATE VIEW trimester AS SELECT * FROM atcsdevb_dev_shared.trimester;

DROP VIEW IF EXISTS menu_item;
CREATE VIEW menu_item AS SELECT * FROM atcsdevb_dev_shared.menu_item;

DROP VIEW IF EXISTS audit;
CREATE VIEW audit AS SELECT * FROM atcsdevb_dev_shared.audit;

DROP VIEW IF EXISTS menu_item_user_role_xref;
CREATE VIEW menu_item_user_role_xref AS SELECT * FROM atcsdevb_dev_shared.menu_item_user_role_xref;

DROP VIEW IF EXISTS menu_item_user_type_xref;
CREATE VIEW menu_item_user_type_xref AS SELECT * FROM atcsdevb_dev_shared.menu_item_user_type_xref;

DROP VIEW IF EXISTS team;
CREATE VIEW team AS SELECT * FROM atcsdevb_dev_shared.team;

DROP VIEW IF EXISTS academy;
CREATE VIEW academy AS SELECT * FROM atcsdevb_dev_shared.academy;

DROP VIEW IF EXISTS variable;
CREATE VIEW variable AS SELECT * FROM atcsdevb_dev_shared.variable;