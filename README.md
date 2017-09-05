# JRN4SR
Test code of the paper [1].

## Requirements
- tensorflow 0.12.0
- opencv 2.4

## Files
- test.py : test file
- ./Models : Models' directory
- ./Data/Set5_Dx : Low-resolution images of 'Set5'
- ./Data/Set5_Gx : Groud truth images of 'Set5'
- ./Data/SR : Super-resolved images

## How To Use

### Testing
```shell
# Arguments:
# --LR_path, path to the low-resolution images; --save_path, path to save the super-resolved images; --model_path, path to model.
# 
# X2:
python test.py --LR_path ./Data/Set5_D2/ --save_path ./Data/SR/Set5_X2/ --model_path ./Models/X2
# X3:
python test.py --LR_path ./Data/Set5_D3/ --save_path ./Data/SR/Set5_X3/ --model_path ./Models/X3
# X4:
python test.py --LR_path ./Data/Set5_D4/ --save_path ./Data/SR/Set5_X4/ --model_path ./Models/X4
```
# 


[1] Zhimin Tang, Linkai Luo, Hong Peng, Shaohui Li. A joint residual network with paired ReLUs activation for image super-resolution, Neurocomputing (2017). https://doi.org/10.1016/j.neucom.2017.07.061
