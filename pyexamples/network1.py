import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("input", 64, 3, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=1),

    to_Conv("conv1", 64, 64, offset="(5,0,0)", to="(input-east)", height=64, depth=64, width=4),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=32, depth=32, width=4),
    
    to_Conv("conv2", 32, 128, offset="(4,0,0)", to="(pool1-east)", height=32, depth=32, width=8),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=16, depth=16, width=8),

    to_Conv("conv3", 16, 256, offset="(2,0,0)", to="(pool2-east)", height=16, depth=16, width=12),
    to_Pool("pool3", offset="(0,0,0)", to="(conv3-east)", height=8, depth=8, width=12),

    to_Conv("conv4", 8, 512, offset="(1,0,0)", to="(pool3-east)", height=8, depth=8, width=16),
    to_Pool("pool4", offset="(0,0,0)", to="(conv4-east)", height=4, depth=4, width=16),

    to_Conv("conv5", 4, 1024, offset="(1,0,0)", to="(pool4-east)", height=4, depth=4, width=20),
    to_Pool("pool5", offset="(0,0,0)", to="(conv5-east)", height=2, depth=2, width=16),

    to_Conv("flattened1", 1, 4096, offset="(1,0,0)", to="(pool5-east)", height=1, depth=60, width=1),

    to_SoftMax("soft1", 3107 , offset="(1,0,0)", to="(flattened1-east)", height=1, depth=40, width=1),

    to_connection("input", "conv1"),
    to_connection("pool1", "conv2"),
    to_connection("pool2", "conv3"),
    to_connection("pool3", "conv4"),
    to_connection("pool4", "conv5"),
    to_connection("conv5", "flattened1"),
    to_connection("flattened1", "soft1"),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()