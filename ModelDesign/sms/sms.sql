drop table if exists Relationship_2;

drop table if exists class_record;

drop table if exists course;

drop table if exists course_record;

drop table if exists grade;

drop table if exists grade_course;

drop table if exists role;

drop table if exists score;

drop table if exists user;

/*==============================================================*/
/* Table: Relationship_2                                        */
/*==============================================================*/
create table user_grade
(
   user_id              int,
   grade_id             int
);

/*==============================================================*/
/* Table: class_record                                          */
/*==============================================================*/
create table class_record
(
   grade_id             int not null,
   course_id            int not null,
   user_id              int not null,
   primary key (grade_id, course_id, user_id)
);

/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/
create table course
(
   course_id            int not null,
   course_name          varchar(50),
   primary key (course_id)
);

/*==============================================================*/
/* Table: course_record                                         */
/*==============================================================*/
create table course_record
(
   course_id            int not null,
   section_id           varchar(50) not null,
   section_name         varchar(50),
   primary key (course_id)
);

/*==============================================================*/
/* Table: grade                                                 */
/*==============================================================*/
create table grade
(
   grade_id             int not null,
   course_id            int,
   user_id              int,
   grade_name           varchar(50),
   primary key (grade_id)
);

/*==============================================================*/
/* Table: grade_course                                          */
/*==============================================================*/
create table grade_course
(
   grade_id             int not null,
   course_id            int not null,
   primary key (grade_id)
);

/*==============================================================*/
/* Table: role                                                  */
/*==============================================================*/
create table role
(
   role_id              int not null,
   role_name            varchar(50),
   type_id              varchar(50),
   type_name            varchar(50),
   primary key (role_id)
);

/*==============================================================*/
/* Table: score                                                 */
/*==============================================================*/
create table score
(
   user_id              int not null,
   grade_id             int not null,
   class_id             int not null,
   score                int,
   primary key (user_id, grade_id, class_id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   user_id              int not null,
   password             varchar(50),
   user_name            varchar(50),
   role_id              int,
   qq                   varchar(50),
   sex                  varchar(50),
   age                  varchar(50),
   addr                 varchar(50),
   email                varchar(50),
   primary key (user_id)
);

