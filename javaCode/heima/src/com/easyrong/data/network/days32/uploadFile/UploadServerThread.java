package com.easyrong.data.network.days32.uploadFile;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class UploadServerThread {
	public static void main(String[] args) throws IOException {
		ServerSocket server = new ServerSocket(9999);
		while (true) {
			Socket socket = server.accept();
			new Thread(new Upload(socket)).start();
		}
	}
}
