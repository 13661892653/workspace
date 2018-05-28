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
		 * ——定时探测日志源目录
		 * ——获取需要采集的文件
		 * ——移动这些文件到一个待上传临时目录
		 * ——遍历待上传目录中各文件，逐一传输到HDFS的目标路径，同时将传输完成的文件移动到备份目录
		 */
		//构建log4j对象
		Logger logger = Logger.getLogger("logRollingFile");
		
		//获取本次采集时的日期
		SimpleDateFormat sdf=new SimpleDateFormat("yyyy-MM-dd-HH");
		String day=sdf.format(new Date());
		
		File srcDir=new File("E:/testlog");
		//列出日志源目录中需要采集的文件
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
		//将要采集的文件移动到待上传的临时目录
		File toUploadDir=new File("E:/toupload/");
		for (File file:listFiles){
			FileUtils.moveFileToDirectory(file, toUploadDir,true);
		}
		
		//构造一个HDFS的客户端对象
		
			FileSystem fs=FileSystem.get(new URI("hdfs://BIGDATA:9000"), new Configuration(), "root");
			File[] touploadFiles=toUploadDir.listFiles();
			
			//检查HDFS的日期目录是否存在，如果不存在则创建
			Path hdfsDesPath=new Path("/logs/"+day);
			if (!fs.exists(hdfsDesPath)){
				fs.mkdirs(hdfsDesPath);
			}
			//检查本地的备份目录是否存在，如果不存在则创建
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
