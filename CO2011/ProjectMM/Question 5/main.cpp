#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
vector<double> res;
const double K_thermalScreen=0.25*pow(10,-3);
const double g=9.8;
const double phi_ext_Co2=4.3*pow(10,5);//third party ability to pump Co2 mg/s
const double phi_pad=0;//
double Cap_VPTop=0.0f;
double LAI=0.0;
double rb=0.0;
double rs=0.0;
double Cp_Air=0.0;
//
double Rho_Top=0.0;
double Rho_Air=0.0;
const double Rho_Mean=0.0;
double Rho_1=0.0;
double Rho_2=0.0;
double Rho_MeanAir=0.0;
//
double M_water=18.02;//molar mass of water(gam)
double h_air=0.0f;//height from floor to thermal screen
double R=8.3114598;//molar gas constant
//
double T_Air=0.0;
double T_Top=0.0;
double T_Out=0.0;
//
double delta_H=2256;
double Aflr=0.0;
double n_HeatVap=0.0;
double n_Pad=0.0;
double P_Blow=0.0f;
double phi_Pad=0;
double x_pad=0;
double x_out=0;
double vp_air=0.0;
double COP_MechAir=0.0f;
double P_MechCool=0.0f;
double T_MechCool=0.0f;
double VP_MechCool=0.0f;
double phi_fog=0.0f;
double VP_ThrScr=0.0f;
double VP_Top=0.0f;
double VP_Out=0.0f;
double VP_CovIn=0.0;
double HEC_AirThr=0.0;
double HEC_TopCovIn=0.0;
//
const double A_roof=0.0;
const double A_side=0.0;
double h_SideRoof=0.0f;
const double vWind=0.0;
double T_MeanAir=0.0;
const double N_Side=0.0;
const double N_SideThermal=0.0;
const double N_roof=0.0;
const double N_roofThermal=0.0;
const double Phi_VentForce=0.0;
double h_Vent=0.0;

double cap(double h,double rho,double cp)
{
    return h*rho*cp;
}
double f_ThermalScreen(double U)///7
{
    double tempt=(g*(1-U)/2*Rho_MeanAir)*(abs(Rho_Air-Rho_Top));
    return U*K_thermalScreen*pow(abs(T_Air-T_Top),2/3)+(1-U)*pow(tempt,1/2);
}

double f_VentRoofSided(double U_roof,double U_side,double cW,double Cd)///10
{
    double tempt=((U_roof*U_roof*U_side*U_side*A_roof*A_roof*A_side*A_side)/(U_roof*U_roof*A_roof*A_roof+U_side*U_side*A_side*A_side))
    *(2*g*h_SideRoof*(T_Air-T_Out)/T_MeanAir)+(pow((U_roof*A_roof+U_side*A_side)/2,2)*cW*pow(vWind,2));
    return (Cd/Aflr)*pow(tempt,0.5);
}

double N_InsectScreen(double S)///11
{
    return S*(2-S);
}

double f_leakage(double c_leakage)///12
{
    if(vWind<0.25)
    {
        return 0.25*c_leakage;
    }else
    {
        return vWind*c_leakage;
    }
}

double ff_VentSide(double U,double Cd,double cW)
{
    return (Cd*U*A_side*vWind/2*Aflr)*pow(cW,0.5);
}

double f_VentSide(double U)///13
{
    if(N_Side>=N_SideThermal)
    {
        return N_InsectScreen(-1)*ff_VentSide(-1,-1,-1)+0.5*f_leakage(-1);
    }else
    {
        return N_InsectScreen(-1)*(U*ff_VentSide(-1,-1,-1)+(1-U)*f_VentRoofSided(-1,-1,-1,-1)*N_Side)+0.5*f_leakage(-1);
    }
}

double f_VentForced(double U)///14
{
    return  N_InsectScreen(-1)*U*Phi_VentForce/Aflr;
}
double ff_VentRoof(double Cd,double U,double cW)///17
{
    double tempt=((g*h_Vent*(T_Air-T_Out))/2*T_MeanAir)+cW*pow(vWind,2);
    return (Cd*U*A_roof*vWind/2*Aflr)*pow(tempt,0.5);
}
double f_VentRoof(double U)///16
{
    if(N_roof>=N_roofThermal)
    {
        return N_InsectScreen(-1)*ff_VentSide(-1,-1,-1)+0.5*f_leakage(-1);
    }
    else
    {
        return N_InsectScreen(-1)*(U*ff_VentRoof(-1,-1,-1)+(1-U)*f_VentRoofSided(-1,-1,-1,-1)*N_Side)+0.5*f_leakage(-1);
    }
}
double MV(double VP1,double VP2,double HEC)
{
    if(VP1<VP2)
    {
        return 0;
    }else
    {
        return 6.4*pow(10,-9)*HEC*(VP1-VP2);
    }
}
double MVairflux(double f,double t1,double t2,double VP1,double VP2)
{
    return (M_water/R)*f*(
                          (VP1/(t1+273.15))-
                          (VP2/(t2+273.15))
                          );
}
double Cap_VPair()
{
    return M_water*h_air/(R*(T_Air+273.15));
}
double H_blow(double U)
{
    return U*P_Blow/Aflr;
}

double Y(double cp_Air)
{
    return cp_Air/(2.26*0.622);
}
double f_Pad(double U)
{
    return U*phi_pad/Aflr;
}

double VEC_CanAir()
{
    return 2*Rho_Air*Cp_Air*LAI/(delta_H*Y(0.0)*(rb+rs));
}
double HEC_MechAir(double U)
{
    return (U*COP_MechAir*P_MechCool/Aflr)/(T_Air-T_MechCool+6.4*pow(10,-9)*delta_H*(vp_air-VP_MechCool));
}
double MV_AirThrScr()
{
    return MV(vp_air,VP_ThrScr,HEC_AirThr);
}
double MV_TopCovIn()
{
    return MV(VP_Top,VP_CovIn,HEC_TopCovIn);
}
double MV_BlowAir()
{
    return n_HeatVap*H_blow(-1);
}
double MV_PadAir()
{
    return Rho_Air*f_Pad(-1)*(n_Pad*(x_pad-x_out)+x_out);
}
double MV_FogAir(double U)
{
    return U*phi_fog/Aflr;
}
double MV_AirMech()
{
    return MV(vp_air,VP_MechCool,HEC_MechAir(-1));
}
double MV_CanAir(double VP_Can,double VP_Air)
{
    return VEC_CanAir()*(VP_Can-VP_Air);
}
double MV_AirOut_Pad()
{
    return f_Pad(-1)*(M_water/R)*(vp_air/(T_Air+273.15));
}
double MV_AirTop()
{
    return MVairflux(f_ThermalScreen(-1),T_Air,T_Top,vp_air,VP_Top);
}
double MV_AirOut()
{
    return MVairflux(f_VentSide(-1)+f_VentForced(-1),T_Air,T_Out,vp_air,VP_Out);
}
double MV_TopOut()
{
    return MVairflux(f_VentRoof(-1),T_Top,T_Out,VP_Top,VP_Out);
}
void dx()
{
    double VP_Air=(MV_CanAir(-1,-1)+MV_PadAir()+MV_FogAir(-1)+MV_BlowAir()
                   -MV_AirThrScr()-MV_AirTop()-MV_AirOut()-MV_AirOut_Pad()-MV_AirMech())/Cap_VPair();
    double VP_Top=(MV_AirTop()-MV_TopCovIn()-MV_TopOut())/Cap_VPTop;
    res.push_back(VP_Air);
    res.push_back(VP_Top);
}



int main()
{
    return 0;
}
