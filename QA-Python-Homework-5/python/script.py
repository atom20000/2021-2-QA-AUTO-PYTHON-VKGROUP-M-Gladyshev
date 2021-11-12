from struct_log import StructLog
import os

list_log = []

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','log','access.log')),'r') as file:
    for f in file:
        list_oblog = f.replace('"','').rstrip().split()
        list_oblog.insert(3,' '.join([list_oblog.pop(3),list_oblog.pop(3)]))
        list_log.append(StructLog(list_oblog))

#print(len(list_log))

print(list(set(list(map(lambda x: x.type_request, list_log)))))
#print(list_log[list(set(list(map(lambda x : list_log.index(x) if x.type_request == 'g369g=%40eval%01%28base64_decode%28%24_POST%5Bz0%5D%29%29%3B&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2bfCIpOztlY2hvKCJlNTBiNWYyYjRmNjc1NGFmMDljYzg0NWI4YjU4ZTA3NiIpOztlY2hvKCJ8PC0iKTs7ZGllKCk7GET'else 0 , list_log))))[1]])

