* Design Problem, ee114/214A- 2012
* Please fill in the specification achieved by your circuit 
* before your submit the netlist.
**************************************************************
* The specifications that this script achieves are:
* 
* Power  =  1.3694 mW 
* Gain   =  20.24 K
* BandWidth = 90.107 MHz
***************************************************************


** Including the model file
.include ./ee114.hspice

* Defining Top level circuit parameters
.param Cin = 100f
.param CL  = 500f
.param RL  = 10K

* defining the supply voltages

vdd vdd 0 2.5
vss vss 0 -2.5

* Defining the input current source

** For ac simulation uncomment the following 2 lines**
 Iina		iina	vdd	ac	0.5	
 Iinb		vdd	iinb	ac	0.5	

** For transient simulation uncomment the following 2 lines**
*Iina		iina	vdd	sin(0 0.5u 1e6)
*Iinb		vdd	iinb	sin(0 0.5u 1e6)

* Defining Input capacitance

Cina	vdd	iina 'Cin'
Cinb	vdd	iinb 'Cin'

* Defining the differential load 

RL	vouta		voutb		'RL'
CL	vouta		voutb		'CL'

*** Your Trans-impedance Amplifier here ***
*.param W1 = 12.0u
*.param WL1 = 2.0u
*.param WB1 = 3.2u

*.param W2 = 4.0u
*.param WL2 = 2.8u
*.param WB2 = 5.8u

*.param W3 = 44.4u
*.param WB3 = 10.2u

.param W1  = 6.869021u
.param WL1 = 4.852143u
.param WB1 = 4.195982u

.param W2  = 3.795975u
.param WL2 = 2.468056u
.param WB2 = 3.247956u

.param W3  = 4.788013u
.param WB3 = 13.260290u

.param Len1  = 1.000000u
.param LenL1 = 1.000000u
.param LenB1 = 2.000000u

.param Len2  = 1.000000u
.param LenL2 = 1.000000u
.param LenB2 = 2.000000u

.param Len3  = 1.000000u
.param LenB3 = 2.000000u


*Using resistor (RB) in series with diode-connected MB to set VovB
*.param WB = 2.0u
*.param RB = 291k

.param WB = 3.803345u
.param RB = 312.421783k
.param LenB = 2.000000u

m1a vo1a 0 iina vss nmos114 w='W1' l='Len1'
m1La vo1a vo1a vdd vdd pmos114 w='WL1' l='LenL1'
mB1a iina nbias vss vss nmos114 w='WB1' l='LenB1'
m1b vo1b 0 iinb vss nmos114 w='W1' l='Len1'
m1Lb vo1b vo1b vdd vdd pmos114 w='WL1' l='LenL1'
mB1b iinb nbias vss vss nmos114 w='WB1' l='LenB1'

m2a vo2a vo1a v0d vss nmos114 w='W2' l='Len2'
m2La vo2a vo2a vdd vdd pmos114 w='WL2' l='LenL2'
mB2a v0d nbias vss vss nmos114 w='WB2' l='LenB2'
m2b vo2b vo1b v0d vss nmos114 w='W2' l='Len2'
m2Lb vo2b vo2b vdd vdd pmos114 w='WL2' l='LenL2'
mB2b v0d nbias vss vss nmos114 w='WB2' l='LenB2'

m3a vdd vo2a vouta vss nmos114 w='W3' l='Len3'
mB3a vouta nbias vss vss nmos114 w='WB3' l='LenB3'
m3b vdd vo2b voutb vss nmos114 w='W3' l='Len3'
mB3b voutb nbias vss vss nmos114 w='WB3' l='LenB3'

*** Your Bias Circuitry here ***

** For students enrolled in ee214A, you need to design your bias ciruit. You cannpt use Vbias_n as ideal voltage source.
mB nbias nbias vss vss nmos114 w='WB' l='LenB'
rB vdd nbias 'RB'


* defining the analysis

.op
.option post brief nomod

** For ac simulation uncomment the following line** 
*.ac dec 10 100 1g
.ac dec 1000 1 100meg
.measure ac gainmax max vdb(vouta)
.measure ac f3db when vdb(vouta)='gainmax-3'
.print ac PAR('v(vouta)/1') vp(vouta)

** For transient simulation uncomment the following line **
*.tran 0.01u 4u 

.end
