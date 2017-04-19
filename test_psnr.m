clear

testfolder = './Data/SR/Set5_X2';
gt = './Data/Set5_G2';

up_scale = 2;

gt_paths = dir(fullfile(gt,'*.bmp'));
test_paths = dir(fullfile(testfolder,'*.bmp'));

for i = 1 : length(test_paths)
    im_gt= imread(fullfile(gt, gt_paths(i).name));
    im_test = imread(fullfile(testfolder, test_paths(i).name));
    im_gt = shave(im_gt, [up_scale, up_scale]);
    im_test = shave(im_test, [up_scale, up_scale]);
    psnr(i) = compute_psnr(im_gt, im_test);
end

mean(psnr)
