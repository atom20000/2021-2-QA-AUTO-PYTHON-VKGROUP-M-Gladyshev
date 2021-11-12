from struct_log import StructLog
from exlist import ExList
import os

list_log = ExList()

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','log','access.log')),'r') as file:
    for f in file:
        list_oblog = f.replace('"','').rstrip().split()
        list_oblog.insert(3,' '.join([list_oblog.pop(3),list_oblog.pop(3)]))
        list_log.append(StructLog(list_oblog))

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','output','python_out.txt')),'w') as file:
    file.write('Общее количество запросов\n')
    file.write(''.join([str(len(list_log)),'\n']))
    file.write('\n')
    file.write('Общее количество запросов по типу\n')
    file.writelines(list(map(lambda x: ''.join([str(x[0]),'-',str(x[1]),'\n']), list_log.mapped_list('type_request').ex_count())))
    file.write('\n')
    file.write('Топ 10 самых частых запросов\n')
    file.writelines(list(map(lambda x: '\n'.join([
        f'url-{str(x[0])}',
        f'count-{str(x[1])}',
        '-'*10,'']), list_log.mapped_list('request_url').ex_count().sorted_list(lambda x : -x[1])[:10])))
    file.write('\n')
    file.write('Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой\n')
    file.writelines(list(map(lambda x: '\n'.join([
        f'url-{getattr(x,"request_url")}',
        f'status_code-{getattr(x,"status_code")}',
        f'size_request-{getattr(x,"size_response")}',
        f'ip-{getattr(x,"ip_client")}',
        '-'*10,'']), list_log.filter_list('status_code',r'4\d\d').sorted_list(lambda x: -int(x.size_response))[:5])))
    file.write('\n')
    file.write('Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой\n')
    file.writelines(list(map(lambda x: '\n'.join([
        f'ip-{str(x[0])}',
        f'count-{str(x[1])}',
        '-'*10,'']), list_log.filter_list('status_code', r'5\d\d').mapped_list('ip_client').ex_count().sorted_list(lambda x : -x[1])[:5])))

#print(len(list_log)) #Общее число запросов

#print(list_log.mapped_list('type_request').ex_count()) #Запросы по типам

#print(list_log.mapped_list('request_url').ex_count().sorted_list(lambda x : -x[1])[:10]) # url количество

#print(list_log.filter_list('status_code',r'4\d\d').sorted_list(lambda x: -int(x.size_response))[:5])# по размеру

#print(list_log.filter_list('status_code', r'5\d\d').mapped_list('ip_client').ex_count().sorted_list(lambda x : -x[1])[:5])


#print(list(set(list(map(lambda x: x.type_request, list_log)))))
#print(list(set(list(map(lambda x : list_log.index(x) if x.type_request == 'g369g=%40eval%01%28base64_decode%28%24_POST%5Bz0%5D%29%29%3B&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2bfCIpOztlY2hvKCJlNTBiNWYyYjRmNjc1NGFmMDljYzg0NWI4YjU4ZTA3NiIpOztlY2hvKCJ8PC0iKTs7ZGllKCk7GET'else 0 , list_log))))[1])

# проблемый лог 110200