#!/bin/bash
rsync -av -delete -e 'ssh -p 22345' /etc/ r0310082@leia.uclllabs.be:/home/LDAP/r0310082/backup-etc/
exit 0
