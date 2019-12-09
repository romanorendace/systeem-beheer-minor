;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     ns.romano-rendace.sb.uclllabs.be. root.romano-rendace.sb.uclllabs.be. (
                             49		; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
; Name servers
romano-rendace.sb.uclllabs.be.       IN      NS      ns.romano-rendace.sb.uclllabs.be.
romano-rendace.sb.uclllabs.be.       IN      NS      ns1.uclllabs.be.
romano-rendace.sb.uclllabs.be.       IN      NS      ns2.uclllabs.be.
romano-rendace.sb.uclllabs.be.       IN      NS      thomas-nelen.sb.uclllabs.be.

; A records for name servers
romano-rendace.sb.uclllabs.be.       IN      A       193.191.177.201
ns.romano-rendace.sb.uclllabs.be.    IN      A       193.191.177.201

; Other A records
www.romano-rendace.sb.uclllabs.be.   IN      A       193.191.177.201
www1.romano-rendace.sb.uclllabs.be.   IN      A       193.191.177.201
www2.romano-rendace.sb.uclllabs.be.   IN      A       193.191.177.201
test.romano-rendace.sb.uclllabs.be.  IN      A       193.191.177.254

romano-rendace.sb.uclllabs.be.          IN      MX      10 mx.romano-rendace.sb.uclllabs.be.
mx.romano-rendace.sb.uclllabs.be.       IN      A       193.191.177.201

romano-rendace.sb.uclllabs.be.		IN	CAA	0 issue "letsencrypt.org"

romano-rendace.sb.uclllabs.be.		IN	AAAA	2001:6a8:2880:a077::c9
ns					IN	AAAA	2001:6a8:2880:a077::c9
www                                     IN      AAAA    2001:6a8:2880:a077::c9
mx					IN	AAAA	2001:6a8:2880:a077::c9
@	                                IN      AAAA    2001:6a8:2880:a077::c9
; Test records

subzonedesh5u.romano-rendace.sb.uclllabs.be.	IN	NS	ns.romano-rendace.sb.uclllabs.be.
fie8qu.subzonedesh5u.romano-rendace.sb.uclllabs.be.	IN	A	193.191.177.201
kobina.romano-rendace.sb.uclllabs.be.	IN	A	193.191.177.201
secure.romano-rendace.sb.uclllabs.be.	IN	A	193.191.177.201
supersecure.romano-rendace.sb.uclllabs.be.	IN	A	193.191.177.201
fie8qu.subzonedesh5u.romano-rendace.sb.uclllabs.be.	IN	A	193.191.177.201
000-default.romano-rendace.sb.uclllabs.be.	IN	A	193.191.177.201
