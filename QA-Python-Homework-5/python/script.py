from parser_ import parser
from struct_log import StructLog
from exlist import ExList
import os
import json

list_log = ExList()
(options, args) = parser()

def main():
    if os.path.exists(options.filedir):
        with open(options.filedir,'r') as file:
            for f in file:
                list_oblog = f.replace('"','').rstrip().split()
                list_oblog.insert(3,' '.join([list_oblog.pop(3),list_oblog.pop(3)]))
                list_log.append(StructLog(list_oblog))
    else:
        print('Input file not exist')
        return

    output_dir =os.path.abspath(os.path.join('.','output'))
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    if not options.json:
        with open(os.path.join(output_dir,'python_out.txt'),'w') as file:
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
    else:
        with open(os.path.join(output_dir,'python_out.json'),'w') as file:
            file.write(json.dumps({
                'Общее количество запросов':len(list_log),
                'Общее количество запросов по типу':[
                    {i[0]:i[1]} for i in list_log.mapped_list('type_request').ex_count()
                ],
                'Топ 10 самых частых запросов':[
                    {i[0]:i[1]} for i in list_log.mapped_list('request_url').ex_count().sorted_list(lambda x : -x[1])[:10]
                ],
                'Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой':[
                 {j[0]:getattr(i,j[1]) for j in list(zip(['url','status_code','size_request','ip'],['request_url','status_code','size_response','ip_client']))}  
                    for i in list_log.filter_list('status_code',r'4\d\d').sorted_list(lambda x: -int(x.size_response))[:5]
                ],
                'Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой':[
                    {i[0]:i[1]} for i in list_log.filter_list('status_code', r'5\d\d').mapped_list('ip_client').ex_count().sorted_list(lambda x : -x[1])[:5]
                ]
            }, ensure_ascii=False, indent=4))
            
if __name__=='__main__':
    main()
#print(len(list_log)) #Общее число запросов

#print(list_log.mapped_list('type_request').ex_count()) #Запросы по типам

#print(list_log.mapped_list('request_url').ex_count().sorted_list(lambda x : -x[1])[:10]) # url количество

#print(list_log.filter_list('status_code',r'4\d\d').sorted_list(lambda x: -int(x.size_response))[:5])# по размеру

#print(list_log.filter_list('status_code', r'5\d\d').mapped_list('ip_client').ex_count().sorted_list(lambda x : -x[1])[:5])

#print(list(set(list(map(lambda x: x.type_request, list_log)))))
#print(list(set(list(map(lambda x : list_log.index(x) if x.type_request == 'g369g=%40eval%01%28base64_decode%28%24_POST%5Bz0%5D%29%29%3B&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2bfCIpOztlY2hvKCJlNTBiNWYyYjRmNjc1NGFmMDljYzg0NWI4YjU4ZTA3NiIpOztlY2hvKCJ8PC0iKTs7ZGllKCk7GET'else 0 , list_log))))[1])

# проблемый лог 110200