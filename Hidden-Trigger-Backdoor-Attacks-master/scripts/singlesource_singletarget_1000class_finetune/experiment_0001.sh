#!/bin/bash

cd ../..

CUDA_VISIBLE_DEVICES=0 python generate_poison.py cfg/singlesource_singletarget_1000class_finetune/experiment_0001.cfg
CUDA_VISIBLE_DEVICES=0 python finetune_and_test.py cfg/singlesource_singletarget_1000class_finetune/experiment_0001.cfg