--
-- /home/ann/sk101/joinem.sql
--

-- Demo:
-- sqlite3 sk101.db '.read /home/ann/sk101/joinem.sql'

-- This script should create wide1.csv
-- This script should inner-join some csv files on cdate.

DROP TABLE MDY;
DROP TABLE XOM;
DROP TABLE gspc;

CREATE TABLE MDY (mdycdate date, mdyp float, mdyld float, mdy4 float, mdy5 float, mdy6 float, mdy7 float);
CREATE TABLE XOM (xomcdate date, xomp float, xomld float, xom4 float, xom5 float, xom6 float, xom7 float);
CREATE TABLE GSPC (gspccdate date, gspcp float, gspcld float, gspc4 float, gspc5 float, gspc6 float, gspc7 float);

.separator ","
.import MDY3.csv MDY
.import XOM3.csv XOM
.import GSPC3.csv GSPC

DROP TABLE wide1;
CREATE TABLE wide1 AS
SELECT
mdycdate as cdate
,gspcp   as cp
,gspcld  as pctlead
,strftime('%w',mdycdate) dow
,strftime('%d',mdycdate) dom
,strftime('%m',mdycdate) moy
,mdy4,mdy5,mdy6,mdy7
,xom4,xom5,xom6,xom7
,gspc4,gspc5,gspc6,gspc7
FROM mdy,xom,gspc
WHERE mdycdate = xomcdate
AND   mdycdate = gspccdate
;

.header ON
-- .header OFF
.mode   csv
.output wide1.csv

SELECT * FROM wide1 ORDER BY cdate DESC;

.quit


