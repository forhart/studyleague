BEGIN;
CREATE TABLE "sl_pre_student" (
    "id" integer NOT NULL PRIMARY KEY,
    "first_name" varchar(60) NOT NULL,
    "last_name" varchar(60) NOT NULL,
    "age" integer NOT NULL,
    "gender" varchar(2) NOT NULL
)
;
CREATE TABLE "sl_pre_author" (
    "id" integer NOT NULL PRIMARY KEY,
    "first_name" varchar(60) NOT NULL,
    "last_name" varchar(60) NOT NULL,
    "age" integer NOT NULL,
    "gender" varchar(2) NOT NULL
)
;
CREATE TABLE "sl_pre_stream" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(60) NOT NULL,
    "description" text NOT NULL
)
;
CREATE TABLE "sl_pre_subject" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(60) NOT NULL,
    "description" text NOT NULL
)
;
CREATE TABLE "sl_pre_chapter" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(100) NOT NULL,
    "description" text NOT NULL,
    "subject_id" integer NOT NULL REFERENCES "sl_pre_subject" ("id")
)
;
CREATE TABLE "sl_pre_semester" (
    "id" integer NOT NULL PRIMARY KEY,
    "Semester_name" varchar(8) NOT NULL
)
;
CREATE TABLE "sl_pre_note_author" (
    "id" integer NOT NULL PRIMARY KEY,
    "note_id" integer NOT NULL,
    "author_id" integer NOT NULL REFERENCES "sl_pre_author" ("id"),
    UNIQUE ("note_id", "author_id")
)
;
CREATE TABLE "sl_pre_note" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(200) NOT NULL,
    "content" text NOT NULL,
    "subject_id" integer NOT NULL REFERENCES "sl_pre_subject" ("id"),
    "chapter_id" integer NOT NULL REFERENCES "sl_pre_chapter" ("id"),
    "semester_id" integer NOT NULL REFERENCES "sl_pre_semester" ("id"),
    "stream_id" integer NOT NULL REFERENCES "sl_pre_stream" ("id"),
    "is_free" bool NOT NULL
)
;
CREATE TABLE "sl_pre_plan" (
    "id" integer NOT NULL PRIMARY KEY
)
;
CREATE INDEX "sl_pre_chapter_638462f1" ON "sl_pre_chapter" ("subject_id");
CREATE INDEX "sl_pre_note_638462f1" ON "sl_pre_note" ("subject_id");
CREATE INDEX "sl_pre_note_93746074" ON "sl_pre_note" ("chapter_id");
CREATE INDEX "sl_pre_note_ec19e9ba" ON "sl_pre_note" ("semester_id");
CREATE INDEX "sl_pre_note_7371fd6" ON "sl_pre_note" ("stream_id");
COMMIT;
