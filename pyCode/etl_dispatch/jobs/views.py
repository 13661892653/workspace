#coding=utf-8
from django.shortcuts import render
import ibm_db
# Create your views here.




def jobInfo(request):
    conn = ibm_db.connect("DATABASE=metadata;HOSTNAME=172.16.11.170;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;", "", "")
    if conn:
        sql = "select JOB_SEQ_ID,JOB_STS,JOB_NM,DATA_PRD,ACT_ST_DT,ACT_ST_TM,ACT_ED_DT,ACT_ED_TM,JOB_LG,RW_RD,RW_IST,RW_UPT from dwmm.job_log"
        statement = ibm_db.exec_immediate(conn,sql)
        #print(type(stmt))
        #print(stmt)
        result = ibm_db.fetch_both(statement)
        print(type(result))
        print(type(ibm_db.fetch_both(statement)))
        while ( result ):
            #
            print(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11])
            #result = ibm_db.fetch_both(stmt)
            #for i in range(len(result)):
                #recordDir[stmt[i][2]]=stmt[i][4]
                #print(recordDir[stmt[i][2]])
            result = ibm_db.fetch_both(statement)
            print(result)
            ibm_db.close(conn)
        return render(request,'/jobInfo/',{'data':result})