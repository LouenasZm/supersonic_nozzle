mkdir Project_npr
cp -r Project_base Project_npr/ 
cd Project_npr
for n in 130000 140000 150000 160000 170000 180000 190000 200000 
do 
	cp -r Project_base Project_p_$n
	cd Project_p_$n 
	./Allclean
	sed s/pression_totale/$n/g 0.orig/something > 0.orig/p 
	./Allrun
	cd ..
done 	
