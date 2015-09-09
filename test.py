#!/usr/bin/python
# coding: utf8
import func

con = func.sql_connect('zuul.db')
func.sql(con,'''INSERT INTO token (tID, userID, tKey) VALUES ('1234567','1','')''')

func.sql_close(con)