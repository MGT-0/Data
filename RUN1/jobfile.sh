
today=$(date +"%d-%m-%Y %H:%M")

echo "starting min1 at $today" 

sander -O -i min1.in -o min1.out -p clean_6mdx_sol.prmtop -c clean_6mdx_sol.rst7 -r 6mdx_min1.rst7 -inf min1.info -ref clean_6mdx_sol.rst7 -x mdcrd.min1
echo "ending min1 at $today"

today=$(date +"%d-%m-%Y %H:%M")

echo "starting min2 at $today"
sander -O -i min2.in -o min2.out -p clean_6mdx_sol.prmtop -c 6mdx_min1.rst7 -r 6mdx_min2.rst7 -inf min2.info -ref 6mdx_min1.rst7 -x mdcrd.min2
echo "ending min2 at $today"

today=$(date +"%d-%m-%Y %H:%M")

echo "starting heat at $today"
export CUDA_VISIBLE_DEVICES=0
$AMBERHOME/bin/pmemd.cuda -O -i heat.in -o heat.out -p clean_6mdx_sol.prmtop -c 6mdx_min2.rst7 -r 6mdx_heat.rst7 -inf heat.info -ref 6mdx_min2.rst7 -x mdcrd.heat
echo "ending heat at $today"

today=$(date +"%d-%m-%Y %H:%M")

echo "starting prod1 1-20ns at 1 gpu on $today"
export CUDA_VISIBLE_DEVICES=0
$AMBERHOME/bin/pmemd.cuda -O -i prod1.in -o prod1.out -p clean_6mdx_sol.prmtop -c 6mdx_heat.rst7 -r 6mdx_prod1.rst7 -inf prod1.info -ref 6mdx_heat.rst7 -x mdcrd.prod1
echo "ending prod1 1-20ns at $today"
<<com
today=$(date +"%d-%m-%Y %H:%M")

echo "starting prod2 20-40ns at 1 gpu on $today"
export CUDA_VISIBLE_DEVICES=0
mpirun $AMBERHOME/bin/pmemd.cuda -O -i prod1.in -o prod2.out -p clean_6mdx_sol.prmtop -c 6mdx_heat.rst7 -r 6mdx_prod2.rst7 -inf prod2.info -ref 6mdx_prod1.rst7 -x mdcrd.prod2
echo "ending prod2 20-40ns at $today"

today=$(date +"%d-%m-%Y %H:%M")

echo "starting prod3 40-60ns at 1 gpu on $today"
export CUDA_VISIBLE_DEVICES=0
$AMBERHOME/bin/pmemd.cuda -O -i prod1.in -o prod3.out -p clean_6mdx_sol.prmtop -c 6mdx_prod2.rst7 -r 6mdx_prod3.rst7 -inf prod3.info -ref 6mdx_prod2.rst7 -x mdcrd.prod3
echo "ending prod3 40-60ns at $today"

today=$(date +"%d-%m-%Y %H:%M")

echo "starting prod4 60-80ns at 1 gpu on $today"
export CUDA_VISIBLE_DEVICES=0
$AMBERHOME/bin/pmemd.cuda -O -i prod1.in -o prod4.out -p clean_6mdx_sol.prmtop -c 6mdx_prod3.rst7 -r 6mdx_prod4.rst7 -inf prod4.info -ref 6mdx_prod3.rst7 -x mdcrd.prod4
echo "ending prod4 60-80ns at $today"

today=$(date +"%d-%m-%Y %H:%M")

echo "starting prod5 80-100ns at 1 gpu on $today"
export CUDA_VISIBLE_DEVICES=0
$AMBERHOME/bin/pmemd.cuda -O -i prod1.in -o prod5.out -p clean_6mdx_sol.prmtop -c 6mdx_prod4.rst7 -r 6mdx_prod5.rst7 -inf prod5.info -ref 6mdx_prod4.rst7 -x mdcrd.prod5
echo "ending prod5 80-100ns  at $today"


echo "starting prod6 50-60ns at 'date'"
export CUDA_VISIBLE_DEVICES=0,1
mpirun -np 2 $AMBERHOME/bin/pmemd.cuda.MPI -O -i prod1.in -o prod6.out -p clean_6mdx_sol.prmtop -c 6mdx_prod5.rst7 -r 6mdx_prod6.rst7 -inf prod6.info -ref 6mdx_prod5.rst7 -x mdcrd.prod6
echo "ending prod6 50-600ns at 'date'"

echo "starting prod7 60-70ns at 'date'"

export CUDA_VISIBLE_DEVICES=0,1
mpirun -np 2 $AMBERHOME/bin/pmemd.cuda.MPI -O -i prod1.in -o prod7.out -p clean_6mdx_sol.prmtop -c 6mdx_prod6.rst7 -r 6mdx_prod7.rst7 -inf prod7.info -ref 6mdx_prod6.rst7 -x mdcrd.prod7
echo "ending prod7 60-70ns at 'date'"

echo "starting prod8 70-80ns at 'date'"
export CUDA_VISIBLE_DEVICES=0,1
mpirun -np 2 $AMBERHOME/bin/pmemd.cuda.MPI -O -i prod1.in -o prod8.out -p clean_6mdx_sol.prmtop -c 6mdx_prod7.rst7 -r 6mdx_prod8.rst7 -inf prod8.info -ref 6mdx_prod7.rst7 -x mdcrd.prod8
echo "ending prod8 70-80ns at 'date'"

echo "starting prod9 80-90ns at 'date'"
export CUDA_VISIBLE_DEVICES=0,1
mpirun -np 2 $AMBERHOME/bin/pmemd.cuda.MPI -O -i prod1.in -o prod9.out -p clean_6mdx_sol.prmtop -c 6mdx_prod8.rst7 -r 6mdx_prod9.rst7 -inf prod9.info -ref 6mdx_prod8.rst7 -x mdcrd.prod9
echo "ending prod9 80-90ns at 'date'"

echo "starting prod10 90-100ns at 'date'"
export CUDA_VISIBLE_DEVICES=0,1
mpirun -np 2 $AMBERHOME/bin/pmemd.cuda.MPI -O -i prod1.in -o prod10.out -p clean_6mdx_sol.prmtop -c 6mdx_prod9.rst7 -r 6mdx_prod10.rst7 -inf prod10.info -ref 6mdx_prod9.rst7 -x mdcrd.prod10
echo "ending prod10 90-100ns  at 'date'"
com
