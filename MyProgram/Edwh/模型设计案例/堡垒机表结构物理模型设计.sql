drop table if exists Relationship_user;

drop table if exists Relationship_user_group;

drop table if exists host_info;

drop table if exists local_user_info;

drop table if exists log_info;

drop table if exists remote_user_info;

drop table if exists user_group;

/*==============================================================*/
/* Table: Relationship_user                                     */
/*==============================================================*/
create table Relationship_user
(
   id                   int not null,
   rem_id               int not null,
   primary key (id, rem_id)
);

/*==============================================================*/
/* Table: Relationship_user_group                               */
/*==============================================================*/
create table Relationship_user_group
(
   id                   int not null,
   use_id               int not null,
   primary key (id, use_id)
);

/*==============================================================*/
/* Table: host_info                                             */
/*==============================================================*/
create table host_info
(
   id                   int not null,
   host_ip              varchar(64),
   host_name            varchar(64),
   host_port            varchar(64),
   primary key (id)
);

/*==============================================================*/
/* Table: local_user_info                                       */
/*==============================================================*/
create table local_user_info
(
   id                   int not null,
   user_name            varchar(64),
   password             varchar(64),
   primary key (id)
);

/*==============================================================*/
/* Table: log_info                                              */
/*==============================================================*/
create table log_info
(
   id                   int not null,
   host_ip              varchar(64),
   user_name            varchar(64),
   remote_user_name     varchar(64),
   cpntent              varchar(64),
   primary key (id)
);

/*==============================================================*/
/* Table: remote_user_info                                      */
/*==============================================================*/
create table remote_user_info
(
   id                   int not null,
   user_name            varchar(64),
   password             varchar(64),
   ip                   varchar(64),
   primary key (id)
);

/*==============================================================*/
/* Table: user_group                                            */
/*==============================================================*/
create table user_group
(
   id                   int not null,
   host_ip              varchar(64),
   user_name            varchar(64),
   user_group           varchar(64),
   primary key (id)
);

alter table Relationship_user add constraint FK_Relationship_3 foreign key (rem_id)
      references remote_user_info (id) on delete restrict on update restrict;

alter table Relationship_user add constraint FK_Relationship_5 foreign key (id)
      references local_user_info (id) on delete restrict on update restrict;

alter table Relationship_user_group add constraint FK_Relationship_4 foreign key (use_id)
      references user_group (id) on delete restrict on update restrict;

alter table Relationship_user_group add constraint FK_Relationship_6 foreign key (id)
      references remote_user_info (id) on delete restrict on update restrict;
