#!/usr/bin/python
# Devan Willemburg 2015
# Make sure you run chmod +s /usr/bin/snmptrap

import sys
import subprocess

snmpManager = "<SNMP MANAGER HERE>"
snmpOID = "1.3.6.1.4.1.27389.1.1"
snmpOID1 = "1.3.6.1.4.1.27389.1.1.1"
snmpOID2 = "1.3.6.1.4.1.27389.1.1.2"
snmpOID3 = "1.3.6.1.4.1.27389.1.1.3"
snmpOID4 = "1.3.6.1.4.1.27389.1.1.4"
snmpOID5 = "1.3.6.1.4.1.27389.1.1.5"
snmpOID6= "1.3.6.1.4.1.27389.1.1.6"
snmpOID7 = "1.3.6.1.4.1.27389.1.1.7"
snmpOID8 = "1.3.6.1.4.1.27389.1.1.8"
trapOID = "1.3.6.1.4.1.27389.1.2"

searchCount = str(sys.argv[1])
searchTerms = str(sys.argv[2])
searchQuery = str(sys.argv[3])
searchName = str(sys.argv[4])
searchReason = str(sys.argv[5])
searchURL = str(sys.argv[6])
searchTags = str(sys.argv[7])
searchPath = str(sys.argv[8])



subprocess.call(["/usr/bin/snmptrap", "-v", "2c", "-c", "<COMMUNITY STRING HERE>", snmpManager, "''", trapOID, snmpOID1, "i", searchCount, snmpOID2, "s", searchTerms, snmpOID3, "s", searchQuery, snmpOID4, "s", searchName, snmpOID5, "s", searchReason, snmpOID6, "s", searchURL, snmpOID7, "s", searchTags, snmpOID8, "s", searchPath])