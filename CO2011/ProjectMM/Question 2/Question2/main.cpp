#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
double Aflr=0; // Area of green house (m2)
double g=9.8;//gravitational acceleration(m/s2)
vector<double>res(2);//result head is Co2_Air,last is Co2_Top
double MC_BlowAir(double n,double U,double P)///3
{
    return (n*U*P)/Aflr;
}
double MC_ExtAir(double U , double phi)///4
{
    return (U*phi)/Aflr;
}
double MC_PadAir(double U,double phi,double Co2_Out,double Co2_Air)///5
{
    return ((U*phi)/Aflr)*(Co2_Out-Co2_Air);
}
double f_ThermalScreen(double U,double K,double T_Air,double T_Top,double P_Air,double P_Top,double P_MeanAir)///7
{
    double tempt=(g*(1-U)/2*P_MeanAir)*(P_Air-P_Top);
    return U*K*pow(T_Air-T_Top,2/3)+(1-U)*pow(tempt,1/2);
}
double MC_AirTop(double Co2_Air,double Co2_Top)//(6)
{
    return f_ThermalScreen(-1,-1,-1,-1,-1,-1,-1)*(Co2_Air-Co2_Top);
}
double crack(double L,double SO,double K,double P_Mean,double P1,double P2)///8
{
    return (K*SO/P_Mean)*pow(0.5*P_Mean*SO*g*(P1-P2),0.5);

}

double f_VentRoofSided(double Cd,double U_roof,double U_side,double A_roof,double A_side,double h_SideRoof
                       ,double T_MeanAir,double T_Air,double T_Out,double cW,double uWind)///10
{
    double tempt=((U_roof*U_roof*U_side*U_side*A_roof*A_roof*A_side*A_side)/(U_roof*U_roof*A_roof*A_roof+U_side*U_side*A_side*A_side))
    *(2*g*h_SideRoof*(T_Air-T_Out)/T_MeanAir)+(pow((U_roof*A_roof+U_side*A_side)/2,2)*cW*pow(uWind,2));
    return (Cd/Aflr)*pow(tempt,0.5);
}
double N_InsectScreen(double S)///11
{
    return S*(2-S);
}
double f_leakage(double c_leakage,double uWind)///12
{
    if(uWind<0.25)
    {
        return 0.25*c_leakage;
    }else
    {
        return uWind*c_leakage;
    }
}
double ff_VentSide(double Cd,double U,double A_Side,double uWind,double cW)
{
    return (Cd*U*A_Side*uWind/2*Aflr)*pow(cW,0.5);
}
double f_VentSide(double N_Side,double N_SideThermal,double U)///13
{
    if(N_Side>=N_SideThermal)
    {
        return N_InsectScreen(-1)*ff_VentSide(-1,-1,-1,-1,-1)+0.5*f_leakage(-1,-1);
    }else
    {
        return N_InsectScreen(-1)*(U*ff_VentSide(-1,-1,-1,-1,-1)+(1-U)*f_VentRoofSided(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)*N_Side)+0.5*f_leakage(-1,-1);
    }
}
double f_VentForced(double Phi_VentForced,double U)///14
{
    return  N_InsectScreen(-1)*U*Phi_VentForced/Aflr;
}
double MC_AirOut(double Co2_Air,double Co2_Out)///9
{
    return (f_VentForced(-1,-1)+f_VentSide(-1,-1,-1))*(Co2_Air-Co2_Out);
}
double ff_VentRoof(double Cd,double U,double A_Roof,double h_Vent,
                   double T_Air,double T_Out,double T_MeanAir,double cW,double uWind)///17
{
    double tempt=((g*h_Vent*(T_Air-T_Out))/2*T_MeanAir)+cW*pow(uWind,2);
    return (Cd*U*A_Roof*uWind/2*Aflr)*pow(tempt,0.5);
}
double f_VentRoof(double U,double N_Roof,double N_RoofThr,double N_Side)///16
{
    if(N_Roof>=N_RoofThr)
    {
        return N_InsectScreen(-1)*ff_VentSide(-1,-1,-1,-1,-1)+0.5*f_leakage(-1,-1);
    }
    else
    {
        return N_InsectScreen(-1)*(U*ff_VentRoof(-1,-1,-1,-1,-1,-1,-1,-1,-1)
                                   +(1-U)*f_VentRoofSided(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)*N_Side)+0.5*f_leakage(-1,-1);
    }
}
double MC_TopOut(double Co2_Top,double Co2_Out)
{
    return f_VentRoof(-1,-1,-1,-1)*(Co2_Top-Co2_Out);
}
double hC_Buf(double c_Buff,double c_maxBuff)///19
{
    if(c_Buff>c_maxBuff)
    {
        return 0;
    }else
    {
        return 1;
    }
}
double MC_AirCan(double M,double P,double R)
{
    return M*hC_Buf(-1,-1)*P*R;
}
void dx(double Cap_Co2_Air,double Cap_Co2_Top)///dx function
{
    double Co2_Air=-1;
    double Co2_Top=-1;
    Co2_Air=(MC_BlowAir(-1,-1,-1)+MC_ExtAir(-1,-1)+MC_PadAir(-1,-1,-1,-1)-MC_AirCan(-1,-1,-1)-MC_AirTop(-1,-1)-MC_AirOut(-1,-1))/Cap_Co2_Air;
    Co2_Top=MC_AirTop(-1,-1)-MC_TopOut(-1,-1);
    res.push_back(Co2_Air);
    res.push_back(Co2_Top);
}
int main()
{
    cout<<res.size();
    return 0;
}
