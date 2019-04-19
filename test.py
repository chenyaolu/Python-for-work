from jira import JIRA
from change_format import change_Created, change_data
from createJQL import create_jql, timeList
import pandas as pd
import time
import CONFIG
timenow = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
jira = JIRA(basic_auth=(CONFIG.UID, CONFIG.PW), options = {'server':'https://jira.nevint.com'})
# def mkdir(path):
#     path = path.strip()
#     path = path.rstrip("\\")
#     isExists = os.path.exists(path)
#     if not isExists:
#         os.makedirs(path)
#         return True
#     else:
#         return False
# mkpath = "D:\\csvdata\\{}".format(timenow)
# mkdir(mkpath)
# csvfile = os.path.join(mkpath, 'JIRAinfo{}.csv'.format(timenow))
# 'project in ("Advanced Intelligent Systems") AND affectedVersion ~ "*190115A*" AND issuetype in (Bug, Task, Sub-Task) AND VehicleProject != ES6 AND reporter in (linchao.zhang.o, changwei.chen.o, zhao.yang.o, dong.guo.o, xiaoqian.yan.o, jingxian.chen, Cherry.Xue.o, shangren.lu.o, frank.fu)',

name = ""
def writetoxlsx():
    for it in CONFIG.jqlist:
        data = []
        jqlValue, name = create_jql(timeList(), it)
        xlsfile = 'D:/SWC/数据整理/每周data/{}.xlsx'.format(name)
        for j in range(len(jqlValue)):
            issues = jira.search_issues(jqlValue[j], maxResults=300)
            # print(jqlValue[j])
            for i in issues:
                issue = jira.issue(i)
                Created = issue.fields.created
                Status = issue.fields.status
                Summary = issue.fields.summary
                Issuetype = issue.fields.issuetype
                VehicleProject = issue.fields.customfield_14741
                Labels = issue.fields.labels
                Priority = issue.fields.priority
                Reporter = issue.fields.reporter
                Assignee = issue.fields.assignee
                Creator = issue.fields.creator
                Linkedto = issue.fields.customfield_13109
                AffectsVersion = issue.fields.versions
                FixVersion = issue.fields.fixVersions
                Components = issue.fields.components
                Updated = issue.fields.updated

                item = [issue, change_Created(Created), Status, Summary, Issuetype, VehicleProject, ",".join(Labels),\
                       Priority, Reporter, Assignee, Creator, Linkedto[1:-2], Linkedto[1:-2], str(AffectsVersion),str(FixVersion),str(Components),change_Created(Updated)]
                data.append(item)
        df = pd.DataFrame(data)
        df.columns = ["Key", "Created", "Status", "Summary", "Issuetype", "VehicleProject", "Labels", "Priority",
                      "Reporter", "Assignee", "Creator", "Linkedto", "LinkedIssues", "AffectsVersion","FixVersion", "Components","Updated"]
        AffectsVersion = []
        FixVersion = []
        Components = []
        for item in df["AffectsVersion"].tolist():
            item = ",".join(change_data(item))
            AffectsVersion.append(item)
        for item in df["FixVersion"].tolist():
            item = ",".join(change_data(item))
            FixVersion.append(item)
        for item in df["Components"].tolist():
            item = ",".join(change_data(item))
            Components.append(item)
        df["AffectsVersion"] = AffectsVersion
        df["FixVersion"] = FixVersion
        df["Components"] = Components
        df.to_excel(xlsfile, index=False)
        # print("文件已写入")



# if __name__ == "__main__":
#     writetocsv(data)
