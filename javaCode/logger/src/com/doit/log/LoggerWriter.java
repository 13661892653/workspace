package com.doit.log;

import org.apache.log4j.Logger;

public class LoggerWriter {
	public static void main(String[] args) throws Exception {

		while (true) {
			Logger logger = Logger.getLogger("logRollingFile");
			logger.info("视频类目----"+ System.currentTimeMillis());
			logger.info("蔬菜类目----"+ System.currentTimeMillis());
			logger.info("水果类目----"+ System.currentTimeMillis());
			logger.info("智能家电----"+ System.currentTimeMillis());
			logger.info("交通工具----"+ System.currentTimeMillis());
			Thread.sleep(50);
		}
	}

}
