package com.doit.log;

import org.apache.log4j.Logger;

public class LoggerWriter {
	public static void main(String[] args) throws Exception {

		while (true) {
			Logger logger = Logger.getLogger("logRollingFile");
			logger.error("��Ƶ��Ŀ----"+ System.currentTimeMillis());
			logger.info("�߲���Ŀ----"+ System.currentTimeMillis());
			logger.info("ˮ����Ŀ----"+ System.currentTimeMillis());
			logger.error("���ܼҵ�----"+ System.currentTimeMillis());
			logger.info("��ͨ����----"+ System.currentTimeMillis());
			Thread.sleep(50);
		}
	}

}
