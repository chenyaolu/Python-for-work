# 帐户密码
UID = "your account"
PW = "your password"

# 最早查询的时间
startdate = "2016-05-01"

# 查询时间间隔
days = 10

# 需要查询的jql
jqlist = [
    'project in ("Advanced Intelligent Systems") AND affectedVersion ~ "*190115A*" AND issuetype in (Bug, Task, Sub-Task) AND VehicleProject != ES6 AND reporter in (linchao.zhang.o, changwei.chen.o, zhao.yang.o, dong.guo.o, xiaoqian.yan.o, jingxian.chen, Cherry.Xue.o, shangren.lu.o, frank.fu)',
    'project in (SQE-HU-ES8) AND affectedVersion ~ "*190115A*" AND issuetype in (Bug, Task, Sub-Task) AND VehicleProject != ES6',
    'project in ("Navigation Defect Management System") AND affectedVersion ~ "*190115A*" AND VehicleProject != ES6 AND issuetype in (Bug, Task, Sub-Task)',
    'project in ("Navigation Defect Management System",SQE-HU-ES8,SQE-Navigation-Navinfo) AND affectedVersion ~ "*190115A*" AND VehicleProject != ES6 AND issuetype in (Bug, Task, Sub-Task)',
]

# 'project in ("Advanced Intelligent Systems") AND affectedVersion ~ "*190115A*" AND issuetype in (Bug, Task, Sub-Task) AND VehicleProject != ES6 AND reporter in (linchao.zhang.o, changwei.chen.o, zhao.yang.o, dong.guo.o, xiaoqian.yan.o, jingxian.chen, Cherry.Xue.o, shangren.lu.o, frank.fu)',