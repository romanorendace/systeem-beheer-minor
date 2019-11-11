import sys
import re
import subprocess

if __name__ == '__main__':

    match = re.match('(.+).(romano-rendace.sb.uclllabs.be)', sys.argv[1])

    if match:
        vhost = match.group(1)
        domain = match.group(2)

        print(vhost)
        # create DocumentRoot & index.html with <p>vhost</p>
        subprocess.call(["mkdir", f"/var/www/html/{vhost}"])
        with open(f'/var/www/html/{vhost}/index.html', 'a+') as f:
            f.write(f'<p>welcome {vhost}.{domain}</p>')

        # create vhost.conf file, ServerName, DocumentRoot, vhost-error.log, vhost-acces.log
        subprocess.call(["cp", "/etc/apache2/sites-available/templates/000-default.conf", f"/etc/apache2/sites-available/{vhost}.conf"])
        with open(f'/etc/apache2/sites-available/{vhost}.conf', 'r') as f:
            content = f.read()

        with open(f'/etc/apache2/sites-available/{vhost}.conf', 'w') as f:
            content = re.sub('#ServerName', 'ServerName', content, count=1)
            content = re.sub('www.example.com', sys.argv[1], content, count=1)
            content = re.sub('/var/www/html', f'/var/www/html/{vhost}', content, count=1)
            content = re.sub('error.log', f'{vhost}-error.log', content, count=1)
            content = re.sub('access.log', f'{vhost}-access.log', content, count=1)
            f.write(content)
            
        # activate vhost & restart apache & DNS A record
        subprocess.call(["a2ensite", f"{vhost}.conf"])
        subprocess.call(["systemctl", "restart", "apache2"])
        subprocess.call(["sudo", "dns_add_record", f"{vhost}", "193.191.177.201", f"{domain}"])
