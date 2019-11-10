import sys
import re
import subprocess

if __name__ == '__main__':

    zone = sys.argv[1]

    # create zones in /etc/bind/named.conf.mrt-zones
    with open('/etc/bind/named.conf.mrt-zones', 'a') as mrt_zones:
        new_zone = f'zone "{zone}.romano-rendace.sb.uclllabs.be" {{\n\ttype master;\n\tfile "/etc/bind/zones/{zone}.romano-rendace.sb.uclllabs.be";\n}};\n'
        mrt_zones.write(new_zone)

    # create soa file /etc/bind/zones/zone.romano-rendace.sb.uclllabs.be
    file_name = f'/etc/bind/zones/{zone}.romano-rendace.sb.uclllabs.be'
    subprocess.call(["cp", "/etc/bind/db.local", f"{file_name}"])

    # add NS record to /etc/bind/zones/romano-rendace.sb.uclllabs.be & bump serial
    master_file_name = '/etc/bind/zones/romano-rendace.sb.uclllabs.be'
    with open(master_file_name, 'r') as master_file:
        content = master_file.read()
        pattern = '(\d+)\s+; Serial'

        index = int(re.search(pattern, content).group(1))
        index += 1

        bumped = re.sub('\d*\s+; Serial', f'{index}\t\t; Serial', content, count=1)
        record = f'{zone}.romano-rendace.sb.uclllabs.be.\tIN\tNS\tns.romano-rendace.sb.uclllabs.be.\n'

    with open(master_file_name, 'w') as writer:
        new_content = bumped + record
        writer.write(new_content)

    subprocess.call(["systemctl", "restart", "bind9"])
