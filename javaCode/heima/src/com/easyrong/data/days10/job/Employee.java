package com.easyrong.data.days10.job;

public abstract class Employee {
    /*
     *员工超类
     */
    private String name;
    private String id;

    public abstract void work();

    public void setId(String id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }
}
