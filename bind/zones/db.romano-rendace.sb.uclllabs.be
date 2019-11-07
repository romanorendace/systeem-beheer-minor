;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     ns.romano-rendace.sb.uclllabs.be. root.romano-rendace.sb.uclllabs.be. (
                              3         ; Serial
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
test.romano-rendace.sb.uclllabs.be.  IN      A       193.191.177.254
