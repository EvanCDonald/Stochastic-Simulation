#include <iostream>
#include <cmath>
#include <random>



int main(){

    int i= 1;
    int T=0;
    std::default_random_engine generator;
    std::normal_distribution<double> normal(0,.1); 
    std::cout<<"\nEnter an endpoint for the time interval"<<std::endl;
    std::cin >> T;
    double time[T*100+1];
    double path[T*100+1];
    time[0]=0;
    path[0]=0;
    double *ppath=path;
    for(double *ptime=&time[1], *ptime_end=time+(T*100+1);ptime !=ptime_end; ++ptime and ++ppath){
        *ptime=i*(.01);
        *ppath=*(ppath-1)+normal(generator);
        std::cout   <<i
                    <<':'
                    <<*ptime
                    <<':'
                    <<*ppath
                    << std::endl;
        i=i+1;
    }
    return 0;
}