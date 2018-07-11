package com.easyrong.data.datacollect;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimerTask;

import org.apache.commons.io.FileUtils;

public class BackupCleanTask extends TimerTask {

	@Override
	public void run() {
		
		SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd-HH");
		long now =new Date().getTime();
		// 探测备份目录
		try{
			File backupBaseDir=new File("e:/backup");
			File[] dayBackupDir=backupBaseDir.listFiles();
			
			//判断备份日期目录是否已超24小时
			for (File dir:dayBackupDir) {
				long time=sdf.parse(dir.getName()).getTime();
				if(now - time>24*60*60*1000L){
					FileUtils.deleteDirectory(dir);
				}
				
			}
		}catch(Exception e){
			e.printStackTrace();
		}
		
		
	}

}
