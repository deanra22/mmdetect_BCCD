_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
gpu_assign_thr=5
optimizer = dict(type='SGD', lr=0.00125, momentum=0.9, weight_decay=0.0001)
total_epochs = 100
checkpoint_config = dict(interval=10)