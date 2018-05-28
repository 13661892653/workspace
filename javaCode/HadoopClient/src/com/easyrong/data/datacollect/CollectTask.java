package com.easyrong.data.datacollect;

import java.io.File;
import java.io.FilenameFilter;
import java.net.URI;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimerTask;
import java.util.UUID;

import org.apache.commons.io.FileUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.log4j.Logger;

public class CollectTask extends TimerTask {

	@Override
	public void run() {
		// TODO Auto-generated method stub
		/**
		 * ������ʱ̽����־ԴĿ¼
		 * ������ȡ��Ҫ�ɼ����ļ�
		 * �����ƶ���Щ�ļ���һ�����ϴ���ʱĿ¼
		 * �����������ϴ�Ŀ¼�и��ļ�����һ���䵽HDFS��Ŀ��·����ͬʱ��������ɵ��ļ��ƶ�������Ŀ¼
		 */
		//����log4j����
		Logger logger = Logger.getLogger("logRollingFile");
		
		//��ȡ���βɼ�ʱ������
		SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd-HH");
		String day=sdf.format(new Date());
		
		File srcDir=new File("E:/testlog");
		//�г���־ԴĿ¼����Ҫ�ɼ����ļ�
		File[] listFiles=srcDir.listFiles(new FilenameFilter() {
			
			@Override
			public boolean accept(File dir,String name){
				if (name.startsWith("access.log.")){
					return true;
				}
				return false;
			}
		});
		
		try{
		//��Ҫ�ɼ����ļ��ƶ������ϴ�����ʱĿ¼
		File toUploadDir=new File("E:/toupload/");
		for (File file:listFiles){
			FileUtils.moveFileToDirectory(file, toUploadDir,true);
		}
		
		//����һ��HDFS�Ŀͻ��˶���
		
			FileSystem fs=FileSystem.get(new URI("hdfs://BIGDATA:9000"), new Configuration(), "root");
			File[] touploadFiles=toUploadDir.listFiles();
			
			//���HDFS������Ŀ¼�Ƿ���ڣ�����������򴴽�
			Path hdfsDesPath=new Path("/logs/"+day);
			if (!fs.exists(hdfsDesPath)){
				fs.mkdirs(hdfsDesPath);
			}
			//��鱾�صı���Ŀ¼�Ƿ���ڣ�����������򴴽�
			File backupDir=new File("e:/backup/"+day+"/");
			if (!backupDir.exists()){
				backupDir.mkdirs();
			}
			
			for(File file:touploadFiles){
				Path destPath=new Path(hdfsDesPath+"/access_log_"+UUID.randomUUID()+".log");
				fs.copyFromLocalFile(new Path(file.getAbsolutePath()),destPath);
				FileUtils.moveFileToDirectory(file, backupDir,true);
			}
		
		}catch(Exception e){
			e.printStackTrace();
		}
		

		
		
		
		
	}

}
