%{
Author: Max Chen
E-mail: max.chen.l.w@gmail.com
%}


path = 'test.CR2';
dcraw_command = 'dcraw -v -4 -T';

try
    system([dcraw_command ' ' path]);
    disp('dcraw command executed successfully!');
catch ME
    disp(['An error occurred while executing the dcraw command: ' ME.message]);
end


tiff_file = 'test.tiff';
rgb = imread(tiff_file);


figure;
imshow(rgb); 
title('Result');
axis off;