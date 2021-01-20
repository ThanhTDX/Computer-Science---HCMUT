#include <iostream>
#include <vector>
#include <cmath>
///no pad and fan and fog
using namespace std;
const double Aflr=7.8*pow(10,4); /// Area of green house (m2)
const double K_thermalScreen=0.25*pow(10,-3);///
const double g=9.8;///
const double R=8.3114598;///molar gas constant
const double e=2.72;///euler number
const double phi_ext_Co2=4.3*pow(10,5);///third party ability to pump Co2 mg/s
const double Y=65.8;///psychometric constant
const double phi_pad=0;///
double LAI=2.5;///m^2 m^-2
double rb=275;///boundary layer resistance
double rs_min=82;///minimum canopy resistance
double Cp_Air=pow(10,3);///(J/(Kkg)
//
double c_HECin=1.86;///convective heat exchange
double Acov=9*pow(10,4);///
double Co2_Air=7.1;///
double Co2_Top=6.1;///
const double Co2_Out=668;///mg/m^3
//
double N_side=0.0;
const double N_roof=0.0;
const double N_roofThr=0.9;///
const double N_Co2_AirStom=0.67;///
//
double S_InScr=1;///
double c_leakage=pow(10,-4);///
double Cd=0.65;///
double Cw=0.09;///
//
double Rho_Air0=1.2;
double M_Air=28.96;
double h_elevation=1470;
double Rho_Air=Rho_Air0*pow(e,g*M_Air*h_elevation/(293.15*R));///
double Rho_Top=Rho_Air-1;///
const double Rho_Mean=0.0;
double Rho_1=0.0;
double Rho_2=0.0;
double Rho_MeanAir=(Rho_Air+Rho_Top)/2;///
//
double M_water=18.02;///molar mass of water(gam)
double h_air=4.7;///height from floor to thermal screen
double h_top=5.5;///mean height*2- h_air
//
double T_Air=6;///or 6.8
double T_Top=5;///T_top = T_air +- 1
double T_Out=5.4;///or 23.9 'C
double T_Can=7;///
double T_MeanAir=0.5;///
double T_ThrScr=7;///
double T_CovIn=7;///
//
double delta_H=2256;///
double n_HeatVap=0.0;
double n_Pad=0.0;///
double P_Blow=0.0f;///
double phi_Pad=0;///
double x_pad=0;///No pad -> 0
double x_out=0;///
double COP_MechAir=0.0f;///
double P_MechCool=0.0f;///not available
double T_MechCool=0.0f;///
double VP_MechCool=0.0f;///
double phi_fog=0.0f;///
double VP_Can=999.74;///Pa
double VP_Air=679.8;///Pa
double VP_ThrScr=999.74;///Pa
double VP_Top=554.4;///Rh=(VP/VPsaturate)*100% 679.8
double VP_Out=600;///Pa
double VP_CovIn=999.74;///Pa
//
const double A_roof=1.4*pow(10,4);///
const double A_side=0.0;///
double h_SideRoof=0.0f;///not available
const double vWind=2.9;///
const double Phi_VentForce=0.0;
double h_Vent=0.97;

vector<double>VP_Air_t;
vector<double>VP_Top_t;

double cap(double h,double rho,double cp)
{
    return h*rho*cp;
}
double f_Pad(double U)
{
    return U*phi_pad/Aflr;
}

double f_ThermalScreen(double U)///7
{
    double tempt=(g*(1-U)/2*Rho_MeanAir)*(abs(Rho_Air-Rho_Top));
    return U*K_thermalScreen*pow(abs(T_Air-T_Top),2/3)+(1-U)*pow(tempt,1/2);
}

double f_VentRoofSided(double U_roof,double U_side)///10
{
    double tempt=((U_roof*U_roof*U_side*U_side*A_roof*A_roof*A_side*A_side)/(U_roof*U_roof*A_roof*A_roof+U_side*U_side*A_side*A_side))
    *(2*g*h_SideRoof*(T_Air-T_Out)/T_MeanAir)+(pow((U_roof*A_roof+U_side*A_side)/2,2)*Cw*pow(vWind,2));
    return (Cd/Aflr)*pow(tempt,0.5);
}

double N_InsectScreen()///11
{
    return S_InScr*(2-S_InScr);
}

double f_leakage()///12
{
    if(vWind<0.25)
    {
        return 0.25*c_leakage;
    }else
    {
        return vWind*c_leakage;
    }
}

double ff_VentSide(double U)
{
    return (Cd*U*A_side*vWind/(2*Aflr))*pow(Cw,0.5);
}

double f_VentSide(double U)///13
{
    if(N_roof>=N_roofThr)
    {
        return N_InsectScreen()*ff_VentSide(1)+0.5*f_leakage();
    }else
    {
        return N_InsectScreen()*(U*ff_VentSide(1)+(1-U)*f_VentRoofSided(1,1)*N_side)+0.5*f_leakage();
    }
}
double f_VentForced(double U)///14
{
    return  N_InsectScreen()*U*Phi_VentForce/Aflr;
}

double ff_VentRoof(double U)///17
{
    double tempt=((g*h_Vent*(T_Air-T_Out))/2*T_MeanAir)+Cw*pow(vWind,2);
    return (Cd*U*A_roof*vWind/(2*Aflr))*pow(tempt,0.5);
}

double f_VentRoof(double U)///16
{
    if(N_roof>=N_roofThr)
    {
        return N_InsectScreen()*ff_VentSide(1)+0.5*f_leakage();
    }
    else
    {
        return N_InsectScreen()*(U*ff_VentRoof(1)+(1-U)*f_VentRoofSided(1,1)*N_roof)+0.5*f_leakage();
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
double HEC_AirThr(double U)
{
    return 1.7*U*pow(abs(T_Air-T_ThrScr),0.33);
}
double HEC_TopCovIn()
{
    return c_HECin*pow((T_Top-T_CovIn),0.33)*Acov/Aflr;
}
double MV_AirThrScr()
{
    return MV(VP_Air,VP_ThrScr,HEC_AirThr(1));
}
double MV_TopCovIn()
{
    return MV(VP_Top,VP_CovIn,HEC_TopCovIn());
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
double Cap_VPTop()
{
    return M_water*h_top/(R*(T_Top+273.15));
}
double H_blow(double U)
{
    return U*P_Blow/Aflr;
}

double VEC_CanAir()
{
    return 2*Rho_Air*Cp_Air*LAI/(delta_H*Y*(rb+rs_min));
}
double HEC_MechAir(double U)
{
    return (U*COP_MechAir*P_MechCool/Aflr)/(T_Air-T_MechCool+6.4*pow(10,-9)*delta_H*(-VP_MechCool));
}

double MV_BlowAir()
{
    return n_HeatVap*H_blow(-1);
}
double MV_PadAir()
{
    return Rho_Air*f_Pad(0)*(n_Pad*(x_pad-x_out)+x_out);
}
double MV_FogAir(double U)
{
    return U*phi_fog/Aflr;
}
double MV_AirMech()
{
    return MV(VP_Air,VP_MechCool,HEC_MechAir(0));
}
double MV_CanAir()
{
    return VEC_CanAir()*(VP_Can-VP_Air);
}
double MV_AirOut_Pad()
{
    return f_Pad(0)*(M_water/R)*(VP_Air/(T_Air+273.15));
}
double MV_AirTop()
{
    return MVairflux(f_ThermalScreen(1),T_Air,T_Top,VP_Air,VP_Top);
}
double MV_AirOut()
{
    return MVairflux(f_VentSide(1)+f_VentForced(1),T_Air,T_Out,VP_Air,VP_Out);
}
double MV_TopOut()
{
    return MVairflux(f_VentRoof(1),T_Top,T_Out,VP_Top,VP_Out);
}
vector<double> dx()
{
    vector<double> res;
    double VP_Air=(MV_CanAir()+MV_PadAir()+MV_FogAir(0)+MV_BlowAir()
                   -MV_AirThrScr()-MV_AirTop()-MV_AirOut()-MV_AirOut_Pad()-MV_AirMech())/Cap_VPair();
    double VP_Top=(MV_AirTop()-MV_TopCovIn()-MV_TopOut())/Cap_VPTop();
    res.push_back(VP_Air);
    res.push_back(VP_Top);
}

float func(float x, float y)
{
    return (x + y + x * y);
}

void euler(float x0, float y, float h, float x,vector<double>& tempt)
{
    float temp = 0;

    // Iterating till the point at which we
    // need approximation
    while (x0 < x) {
        temp = y;
        y = y + h * func(x0, y);
        x0 = x0 + h;
        tempt.push_back(y);
    }
}

void print(vector<double> t)
{
for(auto i: t)
    {
        cout<<i<<'\n';
    }
}

int main()
{
    vector<double> res;
    res=dx();
    cout<<VP_Air<<endl;
    euler(0,VP_Air,0.5,40,VP_Air_t);
    euler(0,VP_Top,0.5,40,VP_Top_t);


    return 0;
}
