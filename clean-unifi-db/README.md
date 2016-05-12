Unifi running slow?  Out of disk space?  Just want to purge old logs from the
database?

Contrary to what you'd expect, with the Unifi service running, run the following:

$ mongo --port 27117 < clean-unifi-db.js
