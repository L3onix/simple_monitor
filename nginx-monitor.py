import re
import subprocess
import time

def restart_service(service_name):
    service_return = str(subprocess.run(['sudo', 'systemctl', 'start', service_name]))

def check_service(service_name):
    try:
        service_status = str(subprocess.check_output(['systemctl', 'status', service_name]))
    except:
        print('Serviço não está funcionando.\nReinicializando serviço...')
        restart_service(service_name)
        return False
    
    check_status = re.findall(r'active', service_status)
    
    if(check_status == ['active']):
        return True
    else:
        print('Problema ao tentar reinicializar serviço.')
        return False

while(True):
    time.sleep(5)
    status = check_service('cups')
    if(not status):
        check_service('cups')
    else:
        print('Status [OK]')
