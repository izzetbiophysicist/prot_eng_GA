#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 03:52:23 2023

@author: lucas
"""

import os


os.chdir('/home/lucas/genetic_algo/') 

from genetic_algorithm_rosetta_2 import *
from apt_function import *

from pyrosetta import *
from rosetta.core.pack.task import TaskFactory
from rosetta.core.pack.task import operation

import numpy as np
from numpy.random import uniform
from random import sample

pyrosetta.init()


scorefxn = pyrosetta.create_score_function("ref2015_cart.wts")
starting_pose = pose_from_pdb('/home/lucas/genetic_algo/7lm9a_atom.pdb')
starting_pose_seq = [x for x in starting_pose.sequence()]
gene_values = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']


pop_size = 4
vector_size = len(starting_pose_seq)

init_pop = [list(starting_pose_seq)]
new_indiv = [[gene_values[int(np.round(uniform(low=0, high=len(gene_values)-1)))] for i in range(vector_size)] for indiv in range(pop_size)]

init_pop = list(init_pop) + list(new_indiv)


### If using threads, use apt_threads, if not use APT

GA = genetic_algo(pose=starting_pose, opt_direction='down', gene_values=gene_values, gene_type='discrete', 
             vector_size=len(starting_pose_seq), pop_size=pop_size+1, mutation_rate=0.4, segment_fluctuation=0, 
             apt_function=apt, selection_method='tournament', threads=False,
             convergence_threshold=0, n_cycles=5, n_survivors=1, tournament_size=2,
             initial_population=init_pop)

GA.execute()