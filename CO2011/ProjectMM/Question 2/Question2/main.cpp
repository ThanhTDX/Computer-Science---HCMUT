#include <iostream>
#include <cmath>
using namespace std;
double Aflr=0; // Area of green house (m2)
double g=0;

double MC_BlowAir(double n,double U,double P)//(3)
{
    return (n*U*P)/Aflr;
}
double MC_ExtAir(double U , double phi)//(4)
{
    return (U*phi)/Aflr;
}
double MC_PadAir(double U,double phi,double Co2_Out,double Co2_Air)//(5)
{
    return ((U*phi)/Aflr)*(Co2_Out-Co2_Air);
}
double f_ThermalScreen(double U,double K,double T_Air,double T_Top,double P_Air,double P_Top)//(7)
{
    double tempt=(g*(1-U)/2*P_Air)*(P_Air-P_Top);
    return U*K*pow(T_Air-T_Top,2/3)+(1-U)*pow(tempt,1/2);
}
double MC_AirTop(double Co2_Air,double Co2_Top)//(6)
{
    return f_ThermalScreen(-1,-1,-1,-1,-1,-1)*(Co2_Air-Co2_Top);
}
int main()
{

    return 0;
}
