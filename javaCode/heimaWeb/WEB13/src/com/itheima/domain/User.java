package com.itheima.domain;

public class User {
	private String id;
	private String username;
	private String phone;
	private String password;
	/*public User(String id, String username, String phone, String password) {
		super();
		this.id = id;
		this.username = username;
		this.phone = phone;
		this.password = password;
	}*/
	@Override
	public String toString() {
		return "User [id=" + id + ", username=" + username + ", phone=" + phone + ", password=" + password + "]";
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
}
