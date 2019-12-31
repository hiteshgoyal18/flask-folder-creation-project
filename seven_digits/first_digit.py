# class A:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def full(self):
#         return "{} {}".format(self.first, self.last)
#
#     def __repr__(self):
#         return "{} {}".format('Lorem', 'Ipsum')
#
#     def __str__(self):
#         return "{} {}".format('Lorem', 'not Ipsum')
#
#
# a = A('Hitesh', 'Goyal')
# print(a.full)




#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

# def longestChain(words):
#     words = sorted(words,key=lambda x:len(x))
#     dp = [1]*len(words)
#     record = {}
#     for i, word in enumerate(words):
#         for j in range(len(word)):
#             predecessor = word[:j]+word[j+1:]
#             if predecessor in record:
#                 dp[i] = max(dp[record[predecessor]]+1,dp[i])
#         record[word] = i
#     return max(dp)
#
# if __name__ == '__main__':

from docx import Document

document = Document('msa_doc.docx')
print (document.paragraphs)