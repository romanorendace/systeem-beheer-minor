import argparse
import sys
import re
import subprocess

def bump_serial(zone):
    with open(f'/etc/bind/zones/{zone}', 'r') as r:
        content = r.read()
        pattern = '(\d+)\s+; Serial'
        index = int(re.search(pattern, content).group(1)) + 1
        bumped = re.sub(pattern, f'{index}\t\t; Serial', content, count=1)

    with open(f'/etc/bind/zones/{zone}', 'w') as w:
        w.write(bumped)


def add_A_record(sub, ip, zone):
    with open(f'/etc/bind/zones/{zone}', 'a') as zone_file:
        record = f'{sub}.{zone}.\tIN\tA\t{ip}\n'
        zone_file.write(record)

def add_CNAME_record(alias, zone):
    with open(f'/etc/bind/zones/{zone}', 'a') as zone_file:
        _, domain = zone.split(".", 1)
        record = f'{alias}.{domain}.\tIN\tCNAME\t{zone}.\n'
        zone_file.write(record)

def add_MX_record(mail, zone):
    with open(f'/etc/bind/zones/{zone}', 'a') as zone_file:
        record = f'{zone}.\tIN\tMX\t{mail}.{zone}.\n'
        zone_file.write(record)
    

if __name__ == '__main__':

    if len(sys.argv) == 4:  #3 arguments > A by default
        sub = sys.argv[1]
        ip = sys.argv[2]
        zone = sys.argv[3]
        add_A_record(sub, ip, zone)
        bump_serial(zone)

    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--type', nargs='+', type=str, default='A')
        args = parser.parse_args()
        record_type = args.type[0]

        if record_type == 'A':
            sub = args.type[1]
            ip = args.type[2]
            zone = args.type[3]

            add_A_record(sub, ip, zone)
            bump_serial(zone)

        elif record_type == 'CNAME':
            alias = args.type[1]
            zone = args.type[2]

            add_CNAME_record(alias, zone)
            bump_serial(zone)

        elif record_type == 'MX':
            mail = args.type[1]
            ip = args.type[2]
            zone = args.type[3]

            add_MX_record(mail, zone)
            add_A_record(mail, ip, zone)
            bump_serial(zone)
    
    subprocess.call(["systemctl", "restart", "bind9"])
