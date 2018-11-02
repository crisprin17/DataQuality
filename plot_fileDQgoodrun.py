#!/usr/bin/env python
from ROOT import *
import sys
import re

def print_usage():
    print "Usage: get_last_line_fromfile.py"
    
def plot_95(can,hist,hist2,title=""):

    gStyle.SetLegendBorderSize(0);
    gStyle.SetLegendFillColor(0);
    gStyle.SetTitleSize(.07,"t");
    gStyle.SetOptStat(0);

    gROOT.cd()
    hist2.Draw()
    
    legend = TLegend(0.51,0.65,0.88,0.88)
    legend.SetTextSize(0.045)
    #header_string="95 percent CL:%2.1f" %limit
    #legend.SetHeader(header_string);
    legend.SetHeader("Good run vs All")
    legend.AddEntry(hist,"GOOD runs","l")
    legend.AddEntry(hist2,"ALL runs","l")
    legend.Draw()
    can.Update()

    hist.SetLineColor(kRed)
    hist.Draw("SAME")
    can.Update()
    return(can)

def Read(line,hist):
    for i in range(0,len(line)):
        text = str(line[i])
        ext = "fardet"
        a = text[text.find(ext):]
        run1 = a.split('_')[1:2]
        run = str(run1).lstrip('[\'r000').rstrip('\']') 
        hist.Fill(int(run))
    return hist

filename1 = open("/nova/app/users/crisprin/python/HorizonFile_WithDQgoodRUN.txt","r+");
filename2 = open("/nova/app/users/crisprin/python/HorizonFile_WithDQgoodRUN2.txt","r+");
filename3 = open("/nova/app/users/crisprin/python/HorizonFile_WithDQgoodRUN3.txt","r+");
filename4 = open("/nova/app/users/crisprin/python/HorizonFile_WithDQgoodRUN4.txt","r+");

filename5 = open("/nova/app/users/crisprin/python/HorizonFile_WithoutDQgoodRUN.txt","r+");
filename6 = open("/nova/app/users/crisprin/python/HorizonFile_WithoutDQgoodRUN2.txt","r+");
filename7 = open("/nova/app/users/crisprin/python/HorizonFile_WithoutDQgoodRUN3.txt","r+");
filename8 = open("/nova/app/users/crisprin/python/HorizonFile_WithoutDQgoodRUN4.txt","r+");
filename9 = open("/nova/app/users/crisprin/python/HorizonFile_WithoutDQgoodRUN5.txt","r+");

title= "DQ.IsGoodRun"

flines1 = filename1.readlines()
flines2 = filename2.readlines()
flines3 = filename3.readlines()
flines4 = filename4.readlines()

flines5 = filename5.readlines()
flines6 = filename6.readlines()
flines7 = filename7.readlines()
flines8 = filename8.readlines()
flines9 = filename9.readlines()

GoodRunTRUE1 = TH1I('GoodRunTRUE1', title, 12000, 18000, 30000 )
GoodRunTRUE2 = TH1I('GoodRunTRUE2', title, 12000, 18000, 30000 )
GoodRunTRUE3 = TH1I('GoodRunTRUE3', title, 12000, 18000, 30000 )
GoodRunTRUE4 = TH1I('GoodRunTRUE4', title, 12000, 18000, 30000 )

GoodRunBAD1 = TH1I('GoodRunBAD1', title, 12000, 18000, 30000 )
GoodRunBAD2 = TH1I('GoodRunBAD2', title, 12000, 18000, 30000 )
GoodRunBAD3 = TH1I('GoodRunBAD3', title, 12000, 18000, 30000 )
GoodRunBAD4 = TH1I('GoodRunBAD4', title, 12000, 18000, 30000 )
GoodRunBAD5 = TH1I('GoodRunBAD5', title, 12000, 18000, 30000 )

GoodRunTRUETOT1 = TH1I('GoodRunTRUETOT1', title, 12000, 18000, 30000 )
GoodRunTRUETOT2 = TH1I('GoodRunTRUETOT2', title, 12000, 18000, 30000 )
GoodRunTRUETOT = TH1I('GoodRunTRUETOT', title, 12000, 18000, 30000 )

GoodRunBADTOT1 = TH1I('GoodRunBADTOT1', title, 12000, 18000, 30000 )
GoodRunBADTOT2 = TH1I('GoodRunBADTOT2', title, 12000, 18000, 30000 )
GoodRunBADTOT3 = TH1I('GoodRunBADTOT3', title, 12000, 18000, 30000 )
GoodRunBADTOT = TH1I('GoodRunBADTOT', title, 12000, 18000, 30000 )

GoodRunTRUE1 = Read(flines1,GoodRunTRUE1)
GoodRunTRUE2 = Read(flines2,GoodRunTRUE2)
GoodRunTRUE3 = Read(flines3,GoodRunTRUE3)
GoodRunTRUE4 = Read(flines4,GoodRunTRUE4)

GoodRunBAD1 = Read(flines5,GoodRunBAD1)
GoodRunBAD2 = Read(flines6,GoodRunBAD2)
GoodRunBAD3 = Read(flines7,GoodRunBAD3)
GoodRunBAD4 = Read(flines8,GoodRunBAD4)
GoodRunBAD5 = Read(flines9,GoodRunBAD5)

GoodRunTRUETOT1.Add( GoodRunTRUE1, GoodRunTRUE2, 1.0, 1.0)
GoodRunTRUETOT2.Add( GoodRunTRUE3, GoodRunTRUE4, 1.0, 1.0 )
GoodRunTRUETOT.Add( GoodRunTRUETOT1,GoodRunTRUETOT2, 1.0, 1.0 )

GoodRunBADTOT1.Add( GoodRunBAD1, GoodRunBAD2, 1.0, 1.0)
GoodRunBADTOT2.Add( GoodRunBAD3, GoodRunBAD4, 1.0, 1.0)
GoodRunBADTOT3.Add( GoodRunBADTOT1, GoodRunBAD5, 1.0, 1.0)

GoodRunBADTOT.Add( GoodRunBADTOT2, GoodRunBADTOT3, 1.0, 1.0)

c0=TCanvas( "c0","GoodRun" , 200, 10, 700, 500 )
can=plot_95(c0,GoodRunTRUETOT,GoodRunBADTOT,title)

c0.Print("GoodrunsGOODvsBAD.png")
c0.Update()


filename1.close()
filename2.close()
filename3.close()
filename4.close()
filename5.close()
filename6.close()
filename7.close()
filename8.close()

#outfilenameGOOD.close()
#outfilenameBAD.close()
