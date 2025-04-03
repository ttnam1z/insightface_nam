from easydict import EasyDict as edict
import os
# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.margin_list = (1.0, 0.5, 0.0)
config.network = "r50"
config.resume = False
config.output = None
config.embedding_size = 512
config.sample_rate = 0.7
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 5e-4
config.batch_size = 128
config.lr = 0.02
config.verbose = 2000
config.dali = False

# config.rec = "/train_tmp/ms1m-retinaface-t1"
# config.rec = "/mnt/d/Work/machine_learning/ArcFace/recognition/arcface_torch/faces_webface"
config.rec = os.getcwd()+"/faces_webface"
print(config.rec)
config.num_classes = 1000
config.num_image = 10000
config.num_epoch = 20
config.warmup_epoch = 0
config.val_targets = ['lfw', 'cfp_fp', "agedb_30"]

