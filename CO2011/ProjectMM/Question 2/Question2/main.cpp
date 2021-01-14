#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
//using texas data set in [Van11]
//constants
const double Aflr=0.0; // Area of green house (m2)
const double g=9.8;//gravitational acceleration(m/s2)
const double N_heat_Co2=0.057;//mgCo2/j
const double phi_ext_Co2=4.3*pow(10,5);//third party ability to pump Co2 mg/s
const double phi_pad=0;//
//
double Co2_Air=0.0;//change over time
double Co2_Top=0.0;//when init has asssign it ==Co2_Air
double Co2_Out=0.0;
//
const double K_thermalScreen=0.25*pow(10,-3);//thermal screen flux coefficient
double T_Air=0.0;
double T_Top=0.0;
double T_Out=0.0;
//
double Rho_Top=0.0;
double Rho_Air=0.0;
const double Rho_Mean=0.0;
double Rho_1=0.0;
double Rho_2=0.0;
double Rho_MeanAir=0.0;
//

double L=0.0;
const double SO=0.0;
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


vector<double>res(2);//result head is Co2_Air,last is Co2_Top

double MC_BlowAir(double U,double P)///3
{
    return (N_heat_Co2*U*P)/Aflr;
}

double MC_ExtAir(double U )///4
{
    return (U*phi_ext_Co2)/Aflr;
}

double MC_PadAir(double U)///5
{
    return ((U*phi_pad)/Aflr)*(Co2_Out-Co2_Air);
}

double f_ThermalScreen(double U)///7
{
    double tempt=(g*(1-U)/2*Rho_MeanAir)*(abs(Rho_Air-Rho_Top));
    return U*K_thermalScreen*pow(abs(T_Air-T_Top),2/3)+(1-U)*pow(tempt,1/2);
}

double MC_AirTop()///(6)
{
    return f_ThermalScreen(-1)*(Co2_Air-Co2_Top);
}

double crack()///8
{
    return (L*SO/Rho_Mean)*pow(0.5*Rho_Mean*SO*g*(Rho_1-Rho_2),0.5);

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

double MC_AirOut()///9
{
    return (f_VentForced(-1)+f_VentSide(-1))*(Co2_Air-Co2_Out);
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

double MC_TopOut()///15
{
    return f_VentRoof(-1)*(Co2_Top-Co2_Out);
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

float dydx(float x, float y)
{
    return((x - y)/2);
}
float rk4(float x0, float y0, float x, float h)
{
    // Count number of iterations using step size or
    // step height h
    int n = (int)((x - x0) / h);

    float k1, k2, k3, k4, k5;

    // Iterate for number of iterations
    float y = y0;
    for (int i=1; i<=n; i++)
    {
        // Apply Runge Kutta Formulas to find
        // next value of y
        k1 = h*dydx(x0, y);
        k2 = h*dydx(x0 + 0.5*h, y + 0.5*k1);
        k3 = h*dydx(x0 + 0.5*h, y + 0.5*k2);
        k4 = h*dydx(x0 + h, y + k3);

        // Update next value of y
        y = y + (1.0/6.0)*(k1 + 2*k2 + 2*k3 + k4);;

        // Update next value of x
        x0 = x0 + h;
    }

    return y;
}

void euler(float x0, float y, float h, float x)
{
    float temp = -0;

    // Iterating till the point at which we
    // need approximation
    while (x0 < x) {
        temp = y;
        y = y + h * func(x0, y);
        x0 = x0 + h;
    }

    // Printing approximation
    cout << "Approximate solution at x = "
         << x << "  is  " << y << endl;
}

void dx(double Cap_Co2_Air,double Cap_Co2_Top)///dx function
{
    double Co2_Air=-1;
    double Co2_Top=-1;
    Co2_Air=(MC_BlowAir(-1,-1)+MC_ExtAir(-1)+MC_PadAir(-1)-MC_AirCan(-1,-1,-1)-MC_AirTop()-MC_AirOut())/Cap_Co2_Air;
    Co2_Top=MC_AirTop()-MC_TopOut();
    res.push_back(Co2_Air);
    res.push_back(Co2_Top);
}


int main()
{
    cout<<"Co2_Air : "<<res[0]<<'\n';
    cout<<"Co2_Top : "<<res[1];
    return 0;
}
