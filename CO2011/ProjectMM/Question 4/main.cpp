#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;
///using texas data set in [Van11]
//constants
///remove pad and fan
const double Aflr=7.8*pow(10,4); /// Area of green house (m2)
const double g=9.81;///gravitational acceleration(m/s2)
const double e=2.72;///euler number
const double M_CH20=30.02598; ///
const double R=8.3114598;///molar gas constant
const double N_heat_Co2=0.057;///mgCo2/j
const double phi_ext_Co2=4.3*pow(10,5);///third party ability to pump Co2 mg/s
const double phi_pad=0;///no pad
const double P_blow=0.0f;///not available
const double Cap_Top=0.0f;//heat capacity of top compartment
//
double Co2_Air=7.1;///CO2 Air
double Co2_Top=6.1;///CO2 Top was initialize to be Co2_Air-1

double Cap_Co2_Air=4.7;///=h_air[Van11]
double Cap_Co2_Top=0.4;///h_mean-h_air[Van11]

const double Co2_Out=668;///mg/m^3 assumed to be
double c_maxBuff=20*pow(10,3);///maximum buffer capacity
double Cr=1.7;///

//
const double K_thermalScreen=0.25*pow(10,-3);///thermal screen flux coefficient
double T_Air=6;///or 6.8
double T_Top=5;///T_top = T_air +- 1
double T_Out=5.4;///or 23.9 'C
double T_Can=7;///T_Can , T_ThrScr was assumed to be T_Air since constant
double T_MeanAir=0.5;///temperature was given as a condition
double T_ThrScr=7;///
//
double Cd=0.65;///equal discharge coefficient C_gh_d
double Cw=0.09;///equal global wind pressure coefficient C_gh_w

//
double Rho_Air0=1.2;///
double M_Air=28.96;///
double h_elevation=1470;///
double Rho_Air=Rho_Air0*pow(e,g*M_Air*h_elevation/(293.15*R));///
double Rho_Top=Rho_Air-1;///constant air density
//
const double Rho_Mean=0.1;
double Rho_1=0.1;
double Rho_2=0.1;
double Rho_MeanAir=0.1;
//
double S_InScr=1;///
double c_leakage=pow(10,-4);///
double L=0.0;///no need
const double SO=0.0;///no need
//
const double A_roof=1.4*pow(10,4);///
const double A_side=0.0;///
double h_SideRoof=0.0f;///not available
const double vWind=2.9;///

double N_side=0.0;
const double N_roof=0.0;
const double N_roofThr=0.9;///
const double N_Co2_AirStom=0.67;///

const double Phi_VentForce=0.0;///not available
double h_Vent=0.97;///

vector<double>co2_air_t;

double Co2_Stom()
{
        return N_Co2_AirStom*Co2_Air;
}

double MC_BlowAir(double U)///3
{
    return (N_heat_Co2*U*P_blow)/Aflr;
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
    return f_ThermalScreen(1)*(Co2_Air-Co2_Top);
}

double crack()///8
{
    return (L*SO/Rho_Mean)*pow(0.5*Rho_Mean*SO*g*(Rho_1-Rho_2),0.5);

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

double MC_AirOut()///9
{
    return (f_VentForced(1)+f_VentSide(1))*(Co2_Air-Co2_Out);
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

double MC_TopOut()///15
{
    return f_VentRoof(1)*(Co2_Top-Co2_Out);
}

double hC_Buf(double c_Buff)///19
{
    if(c_Buff>c_maxBuff)
    {
        return 0;
    }else
    {
        return 1;
    }
}
double P()
{
    double res=(Co2_Air-Co2_Stom())/res;
    return res;
}
double r()
{
    return Cr*T_Can;
}
double Rate()
{
    return P()*r()/Co2_Stom();
}
double MC_AirCan()///18
{
    return M_CH20*hC_Buf(-1)*(P()-Rate());
}

float dydx(float x, float y)
{//predetermine formula to calculate the mean of x ,y
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

float func(float x, float y)
{//predetermin function to calculate x+y+x*y
    return (x + y + x * y);
}

void euler(float x0, float y, float h, float x,vector<double>& tempt)
{
    float temp = 0;
    // Iterating till the point at which we
    // need approximation
    while (x0 < x) {//for loop until the final step is reached
        temp = y;//tempt= y
        y = y + h * func(x0, y);//using euler formula to calculate the result
        //after calculation
        x0 = x0 + h;//increase step
        tempt.push_back(y);//put the result of each step into a vector of float
        //this way we can check the answer of every step
    }
}

vector<double> dx(double Cap_Co2_Air,double Cap_Co2_Top)///dx function
{
    double Co2d_Air=-1;
    double Co2d_Top=-1;
    vector<double> res;
    Co2d_Air=(MC_BlowAir(1)+MC_ExtAir(1)+MC_PadAir(1)-MC_AirCan()-MC_AirTop()-MC_AirOut())/Cap_Co2_Air;
    Co2d_Top=MC_AirTop()-MC_TopOut();
    res.push_back(Co2d_Air);
    res.push_back(Co2d_Top);
    return res;
}


int main()
{
    //a vector to hold the final result
    ofstream myfile ("output.txt");//output to file
    euler(0,Co2_Air,0.016,0.3,co2_air_t);//using euler to init the Co2_Air and Co2_Top
    //the step is 1 minute, raise Co2_Air and Co2_Top until the 20th step which is 20 minute.
    ofstream file("output.txt");
    int counter=1;
    if(file.is_open())
    {
        file<<setw(14)<<"Co2_Air"<<setw(10)<<"Co2_Top"<<'\n';
        for(auto i: co2_air_t)
        {
            Co2_Air=i;
            Co2_Top=Co2_Air;
            vector<double> res=dx(Cap_Co2_Air,Cap_Co2_Top);
            file<<"Step "<<counter<<':'<<res[0]<<setfill('.')<<setw(10)<<res[1]<<endl;
            counter++;
        }
    }


    return 0;
}
