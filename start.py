# -*- coding: utf-8 -*-

import re
import mysql.connector
from mysql.connector import errorcode

class dbMySQL():
	def __init__(self, server, user, passwd, dbname):
		try:
			self.__cnx = mysql.connector.connect(user=user, password=passwd, host=server, database=dbname)
			self.__cursor = self.__cnx.cursor(dictionary=True)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
	
	
	def __strReplace(self, keyMass=[], dataMass=[], result = ''):
		if isinstance(keyMass, str):
			keyMass = [keyMass]
		if isinstance(dataMass, str):
			dataMass = [dataMass]
		
		vKey = len(dataMass) - 1
		for i in range(0, len(keyMass)):
			if i > vKey:
				if vKey == 0:
					dataMass.append(dataMass[vKey])
				else:
					dataMass.append('')
			result = result.replace(keyMass[i], str(dataMass[i]))
		
		return result
	
	
	def create_table(self, nameTable, structure, encoding):
		try:
			sql = 'CREATE TABLE '+nameTable+' ('+structure+') ENGINE='+encoding
			self.__cursor.execute(sql)
			self.__cnx.commit()
			result = True
		except mysql.connector.Error as e:
			result = 'Error: create_table ('+str(e)+')'
		
		return result
	
	
	def insert(self, variable, nameTable, rows = None, values = None):
		try:
			sql = 'INSERT INTO '+nameTable
			sql += ' ('+rows+')' if rows != None else ''
			sql += ' VALUES ('+values+')'
			variable = {} if variable == None else variable
			
			arrElem = re.findall("(\:(\w+)*)", sql)
			if len(arrElem) > 0:
				arrayElem = [[],[]]
				for elem in arrElem:
					arrayElem[0].append(elem[0])
					arrayElem[1].append('%('+str(elem[1])+')s')
				
				sql = self.__strReplace(arrayElem[0], arrayElem[1], sql)
			
			self.__cursor.execute(sql, variable)
			result = self.__cursor.lastrowid
			self.__cnx.commit()
		except Exception as e:
			result = 'Error: insert ('+str(e)+')'
		
		return result
	
	
	def select(self, variable, what, nameTable, where = None, order = None):
		try:
			sql = 'SELECT '+what+' FROM '+nameTable
			sql += ' WHERE '+where if where != None else ''
			sql += ' ORDER BY '+order if order != None else ''
			variable = {} if variable == None else variable
			
			arrElem = re.findall("(\:(\w+)*)", sql)
			if len(arrElem) > 0:
				arrayElem = [[],[]]
				for elem in arrElem:
					arrayElem[0].append(elem[0])
					arrayElem[1].append('%('+str(elem[1])+')s')
				
				sql = self.__strReplace(arrayElem[0], arrayElem[1], sql)
			
			self.__cursor.execute(sql, variable)
			result = self.__cursor.fetchall()
		except Exception as e:
			result = 'Error: select ('+str(e)+')'
		
		return result
	
	
	def update(self, variable, nameTable, params, where = None):
		try:
			sql = 'UPDATE '+nameTable+' SET '+params
			sql += ' WHERE '+where if where != None else ''
			variable = {} if variable == None else variable
			
			arrElem = re.findall("(\:(\w+)*)", sql)
			if len(arrElem) > 0:
				arrayElem = [[],[]]
				for elem in arrElem:
					arrayElem[0].append(elem[0])
					arrayElem[1].append('%('+str(elem[1])+')s')
				
				sql = self.__strReplace(arrayElem[0], arrayElem[1], sql)
			
			self.__cursor.execute(sql, variable)
			self.__cnx.commit()
			result = True
		except Exception as e:
			result = 'Error: update ('+str(e)+')'
		
		return result
	
	
	def delete(self, variable, nameTable, where):
		try:
			sql = 'DELETE FROM '+nameTable+' WHERE '+where
			variable = {} if variable == None else variable
			
			arrElem = re.findall("(\:(\w+)*)", sql)
			if len(arrElem) > 0:
				arrayElem = [[],[]]
				for elem in arrElem:
					arrayElem[0].append(elem[0])
					arrayElem[1].append('%('+str(elem[1])+')s')
				
				sql = self.__strReplace(arrayElem[0], arrayElem[1], sql)
			
			self.__cursor.execute(sql, variable)
			self.__cnx.commit()
			result = True
		except Exception as e:
			result = 'Error: delete ('+str(e)+')'
		
		return result
	
	
	def disconnect(self):
		try:
			self.__cnx.close()
			result = True
		except Exception as e:
			result = 'Error: disconnect ('+str(e)+')'
		
		return result
	
	
	def __del__(self):
		try:
			self.__cnx.close()
			result = True
		except Exception as e:
			result = 'Error: disconnect ('+str(e)+')'
