import torch

import model
import utility
from option import args

checkpoint = utility.checkpoint(args)

def main():
    _model = model.Model(args, checkpoint)
    print(_model)

if __name__ == '__main__':
    main()