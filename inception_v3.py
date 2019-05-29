#谷歌提供的训练好的模型地址。
CKPT_FILE = '/path/to/inception_v3.ckpt'
#定义训练中使用的参数
LEARNING_RATE = 0.0001
STEPS = 30
BATCH = 32
N_CLASSES = 5

#不需要从谷歌训练好的模型中加载的参数，这里就是最后的全连接层，因为在
#新的问题中要重新训练这一层中的参数，这里给出的是参数的前缀
CHECKPOINT_EXCLUDE_SCOPES = 'Ínception/Logits,InceptionV3/Auxlogits'
#需要训练的网络层的参数名称， 在fine-tuning的过程中就是最后的全连接层。
#这里给出的是参数的前缀
TRAINABLE_SCOPES='Ínception/Logits,InceptionV3/Auxlogits'

#获取所有需要从谷歌训练好的模型中加载的参数。
def get_tuned_variables():


