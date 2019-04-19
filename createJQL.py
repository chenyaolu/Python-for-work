import re
from datetime import date, timedelta
import CONFIG
def timeList():
    add1day = timedelta(days=1)
    day = date.today() + add1day
    delta = timedelta(CONFIG.days)  # days表示时间段大小
    n_days_forward = day
    timelist=[]
    while  str(n_days_forward) >= CONFIG.startdate:  # 填入最开始的日期
        t1 = n_days_forward
        t2 = n_days_forward  - delta
        timelist.append("AND created <= {0} AND created > {1}".format(t1,t2))
        n_days_forward -= delta
    return timelist

def create_jql(timelist, test):
    p = re.compile("in (.*?) AND")
    nl = p.findall(test)[0]
    if nl == '("Advanced Intelligent Systems")':
        name = "export-AIS"
    if nl == '(SQE-HU-ES8)':
        name = "export-SQEH"
    if nl == '("Navigation Defect Management System")':
        name = "export-NDMS"
    if nl == '("Navigation Defect Management System",SQE-HU-ES8,SQE-Navigation-Navinfo)':
        name = "export-all1"
    if nl == '(EDMS)':   # project in (EDMS) AND issuetype in (Bug, "CDC Feature", Change, Sub-change, Sub-task) AND status in (Open, Review, Analysis, Design, Solution, Implementation, Verification, Monitoring)
        name = "export-EDMS"
    if nl == '(SQEH, AIS, SQENAV, "Navigation Defect Management System")':
        name = "export-SQE"
    sample = []
    for i in range(len(timelist)):
        sample.append(test + " " + timelist[i])
    return sample, name
