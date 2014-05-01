#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
import os
import random
 

exam_file = open(r'test.txt')

lines = []
i = 0

for line in exam_file.readlines():
    if line.startswith('<question'):
        lines.append(line)
        i+=1
        
exam_file.close()
        
question_file = open(r'questions.txt','w')
question_file.writelines(lines)
question_file.write(str(i))
question_file.close()
      