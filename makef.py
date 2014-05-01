#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
import os
import random

test_file = open(r'test.txt') # 
right_answers =  open(r'right_answers.txt','w')


for line in test_file.readlines():
	if line.find('question') != -1:
		question_block = True
		current_question = line
		right_answers.writelines(current_question)
		vars_count = 0
	if line.find('variant') != -1 and vars_count == 0:
		right_answers.writelines(line)
		vars_count +=1
		

test_file.close()
right_answers.close()