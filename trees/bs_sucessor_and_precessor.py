#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def successor(root):
  
  root = root.right
  while root:
      root = root.left
      
  return root


def predecessor(root):
  
  root = root.left
  while root:
      root = root.right
  
  return root
