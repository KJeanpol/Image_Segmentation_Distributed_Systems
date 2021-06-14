//mpicxx prueba.cpp prueba2.cpp `pkg-config opencv4 --cflags --libs` -o prueba

//mpiexec -n 1 ./prueba2 oso.jpg 900 4 rest.jpg

#include <stdio.h>
#include <mpi.h>
#include <math.h>
#include <float.h>
#include "prueba2.h"

using namespace std;

int main(int argc, char** argv){
    
    int size, rank;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    Hi saludo;
    saludo.imprimir(size,rank,argv[1]);
    MPI_Finalize();
    return 0;
    
    }
