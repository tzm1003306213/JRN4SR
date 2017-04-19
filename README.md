# JRN4SR

##
Testing code for JRN


## Requirements
- tensorflow 0.12.0
- opencv 2.4

## Files
- test.py : test file
- ./Models : Models' directory
- train_X2.py : training file
- ./train : training data generating files

## How To Use

### Testing
```shell
# Arguments:
# --LR_path, path to the low-resolution images; --save_path, path to save the super-resolved images; --model_path, path to model.
# 
# Example X2:
python test.py --LR_path ./Data/Set5_D2/ --save_path ./Data/SR/Set5_X2/ --model_path ./Models/X2
# Example X3:
python test.py --LR_path ./Data/Set5_D3/ --save_path ./Data/SR/Set5_X3/ --model_path ./Models/X3
# Example X4:
python test.py --LR_path ./Data/Set5_D4/ --save_path ./Data/SR/Set5_X4/ --model_path ./Models/X4
```
# 



