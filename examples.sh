curl -sX POST -H 'Content-Type: application/json' -d '{"connection_string":"postgres://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs", "sql_query": "SELECT * FROM rnc_taxonomy LIMIT 1"}' https://sonnyksimon-dbq.herokuapp.com/  | jq '.'