package Hdfs24;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.Arrays;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocatedFileStatus;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.RemoteIterator;
import org.junit.Before;
import org.junit.Test;

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
		//hadoop fs.copyFromLocalFile(new Path("F:\\�ڲ�����\\������\\Hadoop-day01-��Ⱥ��װ����\\09.ҵ��ϵͳ����־���ɻ��ƺʹ���չʾ.mp4"), new Path("/"));
		fs.close();
	}
	
	
	FileSystem fs = null;
	
	@Before
	public void init() throws Exception {
		Configuration conf = new Configuration();
		conf.set("dfs.replication", "2");
		conf.set("dfs.blocksize", "64m");

		fs = FileSystem.get(new URI("hdfs://BIGDATA:9000/"), conf, "root");

	}
	
	/**
	 * ��hdfs�д����ļ���
	 *//*
	@Test
	public void testMkdir() throws Exception {

		fs.mkdirs(new Path("/xx/yy/zz"));

		fs.close();
	}*/
	
	@Test
	public void testReadData() throws IllegalArgumentException, IOException {

		FSDataInputStream in = fs.open(new Path("/logs/2018-05-28-09/access_log_0d9b716f-fa57-4a1c-b7c7-cc713afa5c67.log"));

		BufferedReader br = new BufferedReader(new InputStreamReader(in, "utf-8"));

		String line = null;
		while ((line = br.readLine()) != null) {
			System.out.println(line);
		}

		br.close();
		in.close();
		fs.close();

	}
	

}
