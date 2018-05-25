package Hdfs24;


import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class HdfsClientDemo {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Configuration conf=new Configuration();
		//�ϴ��ļ�����ĸ�����
		conf.set("dfs.replication","1");
		//�ϴ��ļ��п�Ĺ���С
		conf.set("dfs.blocksize","64m");
		//����ָ��HDFSϵͳ�ͻ��˶���
		FileSystem fs=FileSystem.get(new URI("hdfs://BIGDATA:9000"), conf, "root");
		//�ϴ�һ���ļ�HDFS�ļ�ϵͳ
		fs.copyFromLocalFile(new Path("F:\\�ڲ�����\\������\\Hadoop-day01-��Ⱥ��װ����\\09.ҵ��ϵͳ����־���ɻ��ƺʹ���չʾ.mp4"), new Path("/"));
		fs.close();
	}

}
