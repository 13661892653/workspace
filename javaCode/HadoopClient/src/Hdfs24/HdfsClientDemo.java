package Hdfs24;


import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class HdfsClientDemo {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Configuration conf=new Configuration();
		//上传文件保存的副本数
		conf.set("dfs.replication","1");
		//上传文件切块的规格大小
		conf.set("dfs.blocksize","64m");
		//访问指定HDFS系统客户端对象
		FileSystem fs=FileSystem.get(new URI("hdfs://BIGDATA:9000"), conf, "root");
		//上传一个文件HDFS文件系统
		fs.copyFromLocalFile(new Path("F:\\内部资料\\大数据\\Hadoop-day01-集群安装部署\\09.业务系统中日志生成机制和代码展示.mp4"), new Path("/"));
		fs.close();
	}

}
