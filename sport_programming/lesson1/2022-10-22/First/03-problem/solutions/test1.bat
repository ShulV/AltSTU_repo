if exist input.txt del input.txt
if exist output.txt  del output.txt
copy ..\tests\%1  input.txt
%2
rem  copy output.txt  ..\tests\%1.a  
fc /w output.txt  ..\tests\%1.a >>res.txt
