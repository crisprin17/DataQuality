#!/usr/bin/env python

from ROOT import *
import novastyle

# upmu selection criteria
def is_selected_reco(t):
    return (
        t.Length > 700 and
        t.Nhits > 70 and
        t.TrackHitsX > 20 and
        t.TrackHitsY > 20 and
        t.Chi2 < 1.5 and
        t.Chi2X < 2 and
        t.Chi2Y < 2 and
        t.R2X > 0.99 and
        t.R2Y > 0.99 and
        abs(t.EndX - t.StartX) > 200 and
        abs(t.EndY - t.StartY) > 500 and
        abs(t.EndZ - t.StartZ) > 120 and
        t.ProbUp > 0.0001 and
        t.LLR > 7 and
        t.LLRX > 3 and
        t.LLRY > 3)

def is_selected_ana(t):
    return (
        t.Length > 500 and
        t.Nhits > 60 and
        t.TrackHitsX > 15 and
        t.TrackHitsY > 15 and
        t.Chi2 < 1.5 and
        t.R2X > 0.99 and
        t.R2Y > 0.99 and
        abs(t.EndX - t.StartX) > 20 and
        abs(t.EndY - t.StartY) > 40 and
        abs(t.EndZ - t.StartZ) > 35 and
        #t.ProbUp > 0.0001 and
        t.LLR > 10 and
        t.LLRX > 5 and
        t.LLRY > 5)

# little statistics
def mean(arr):
    return sum(arr)/len(arr)
def stderr(arr):
    m = mean(arr)
    return (sum([(x - m)**2 for x in arr])/len(arr))**0.5

# extract info on mean track lengths etc from root file
def get_run_info(tree):
    # for each run:
    #  - number of tracks
    #  - number of subruns
    #  - number of events
    #  - average length of track
    #  - average slope of tracks
    #  - average number of hits per track
    #  - average number of triggered tracks per event
    runs = {}
    i = 0
    # get values looping through records
    for e in tree:
        i += 1
        #if i > 10000: break
        if not str(int(e.Run)) in runs:
            runs[str(int(e.Run))] = [0,[],[],0,0,0,0]
            
        arr = runs[str(int(e.Run))]
        arr[0] += 1
        if not int(e.SubRun) in arr[1]: arr[1].append(int(e.SubRun))
        if not int(e.Event) in arr[2]: arr[2].append(int(e.Event))
        arr[3] += float(e.Length)
        arr[4] += float(e.Slope)
        arr[5] += float(e.Nhits)
        if is_selected_ana(e): arr[6] += float(1)

    for r in runs:
        arr = runs[r]
        
        arr[3] = arr[3]/arr[0]
        arr[4] = arr[4]/arr[0]
        arr[5] = arr[5]/arr[0]
        arr[6] = arr[6]/len(arr[2])

    return runs

# ROOT boolshit
gROOT.Reset()
gStyle.SetOptStat(0)

# getting info from root file
chain = TChain('read/ntp_track')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist1.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_184.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_185.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_186.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_187.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_188.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_189.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_279.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_280.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_281.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_282.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_283.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_284.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist_285.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist3.root')
chain.Add('/pnfs/nova/users/crisprin/DDUpmu_bkgr_2018/crisprin_DDUpmu_Bckg_AboveHorizon101520_COMBO_13aug2018_upmuhist4.root')


outfile = open("Runoutsiderange.txt", "w")

#tree = chain.Get('read/ntp_track')

print "tree got"

# getting info about mean values of stuff
runs = get_run_info(chain) #tree

# arrays of lengths etc
run_nums = [int(x, 10) for x in runs]
min_run = min(run_nums)
max_run = max(run_nums)

lengths = [runs[x][3] for x in runs]
slopes = [runs[x][4] for x in runs]
nohs = [runs[x][5] for x in runs]
trigs = [runs[x][6] for x in runs]

print 'Track lengths:           %f +- %f' % (mean(lengths), stderr(lengths))
print 'Track betas:             %f +- %f' % (mean(slopes), stderr(slopes))
print 'Track number of hits:    %f +- %f' % (mean(nohs), stderr(nohs))
print 'Track seleceted:         %f +- %f' % (mean(trigs), stderr(trigs))

# create 2D histos
hist_run_length = TH2F('hist_run_length', 'Run number vs mean track length', max_run-min_run, min_run, max_run, 100, mean(lengths) - stderr(lengths)*10, mean(lengths) + stderr(lengths)*10)
hist_run_length.GetYaxis().SetTitle('Mean track length per run, cm')
hist_run_length.GetXaxis().SetTitle('Run #')
hist_run_length.SetMarkerStyle(7)
hist_run_length.SetMarkerColor(4)
hist_run_length.SetFillStyle(3003)
hist_run_length.SetFillColor(2)
line = TLine(min_run,mean(lengths) - stderr(lengths)*1.5,max_run,mean(lengths) - stderr(lengths)*1.5);
line.SetLineColor(kRed);
line2 = TLine(min_run,mean(lengths) + stderr(lengths)*1.5,max_run,mean(lengths) + stderr(lengths)*1.5);
line2.SetLineColor(kRed);

hist_run_slopes = TH2F('hist_run_slopes', 'Run number vs mean track beta', max_run-min_run, min_run, max_run, 100, abs(mean(slopes)) - stderr(slopes)*10, abs(mean(slopes)) + stderr(slopes)*10)
hist_run_slopes.GetYaxis().SetTitle('Mean track beta per run')
hist_run_slopes.GetXaxis().SetTitle('Run #')
hist_run_slopes.SetMarkerStyle(7)
hist_run_slopes.SetMarkerColor(4)
hist_run_slopes.SetFillStyle(3003)
hist_run_slopes.SetFillColor(3)
line3 = TLine(min_run, abs(mean(slopes)) - stderr(slopes)*1.5, max_run, abs(mean(slopes)) - stderr(slopes)*1.5);
line3.SetLineColor(kRed);
line4 = TLine(min_run, abs(mean(slopes)) + stderr(slopes)*1.5, max_run, abs(mean(slopes)) + stderr(slopes)*1.5);
line4.SetLineColor(kRed);

hist_run_nofhit = TH2F('hist_run_nofhit', 'Run number vs mean # of hits', max_run-min_run, min_run, max_run, 100, mean(nohs) - stderr(nohs)*10, mean(nohs) + stderr(nohs)*10)
hist_run_nofhit.GetYaxis().SetTitle('Mean track number of hits per run')
hist_run_nofhit.GetXaxis().SetTitle('Run #')
hist_run_nofhit.SetMarkerStyle(7)
hist_run_nofhit.SetMarkerColor(4)
hist_run_nofhit.SetFillStyle(3003)
hist_run_nofhit.SetFillColor(4)
line5 = TLine(min_run, mean(nohs) - stderr(nohs)*1.5, max_run, mean(nohs) - stderr(nohs)*1.5);
line5.SetLineColor(kRed);
line6 = TLine(min_run, mean(nohs) + stderr(nohs)*1.5, max_run, mean(nohs) + stderr(nohs)*1.5);
line6.SetLineColor(kRed);

hist_run_triggs = TH2F('hist_run_triggs', 'Run number vs # of selected track per event in a run', max_run-min_run, min_run, max_run, 100, mean(trigs) - stderr(trigs)*10, mean(trigs) + stderr(trigs)*10)
hist_run_triggs.GetYaxis().SetTitle('# of selected tracks per event in a run')
hist_run_triggs.GetXaxis().SetTitle('Run #')
hist_run_triggs.SetMarkerStyle(7)
hist_run_triggs.SetMarkerColor(4)
hist_run_triggs.SetFillStyle(3003)
hist_run_triggs.SetFillColor(5)
line7 = TLine(min_run, mean(trigs) - stderr(trigs)*1.5, max_run, mean(trigs) - stderr(trigs)*1.5);
line7.SetLineColor(kRed);
line8 = TLine(min_run, mean(trigs) + stderr(trigs)*1.5, max_run, mean(trigs) + stderr(trigs)*1.5);
line8.SetLineColor(kRed);

# create 1D histos
hist_length = TH1F('hist_length', 'Mean length distribution', 50, mean(lengths) - stderr(lengths)*10, mean(lengths) + stderr(lengths)*10)
hist_length.GetXaxis().SetTitle('Mean track length per run, cm')
hist_length.SetFillStyle(3003)
hist_length.SetFillColor(5)

hist_slopes = TH1F('hist_slopes', 'Mean beta distribution', 50, abs(mean(slopes)) - stderr(slopes)*10, abs(mean(slopes)) + stderr(slopes)*10)
hist_slopes.GetXaxis().SetTitle('Mean track beta per run')
hist_slopes.SetFillStyle(3003)
hist_slopes.SetFillColor(4)

hist_nofhit = TH1F('hist_nofhit', 'Mean # of hits per track distribution', 50, mean(nohs) - stderr(nohs)*10, mean(nohs) + stderr(nohs)*10)
hist_nofhit.GetXaxis().SetTitle('Mean track number of hits per run')
hist_nofhit.SetFillStyle(3003)
hist_nofhit.SetFillColor(3)

hist_triggs = TH1F('hist_triggs', '# of selected tracks per event distribution', 50, mean(trigs) - stderr(trigs)*10, mean(trigs) + stderr(trigs)*10)
hist_triggs.GetXaxis().SetTitle('# of selected tracks per event in a run')
hist_triggs.SetFillStyle(3003)
hist_triggs.SetFillColor(2)

# applying novastyle
novastyle.CenterTitles(hist_run_length)
novastyle.CenterTitles(hist_run_slopes)
novastyle.CenterTitles(hist_run_nofhit)
novastyle.CenterTitles(hist_run_triggs)
novastyle.CenterTitles(hist_length)
novastyle.CenterTitles(hist_slopes)
novastyle.CenterTitles(hist_nofhit)
novastyle.CenterTitles(hist_triggs)

LenghtMIN = mean(lengths) - stderr(lengths)*1.5 
LenghtMAX = mean(lengths) + stderr(lengths)*1.5
SlopeMIN  = abs(mean(slopes)) - stderr(slopes)*1.5
SlopeMAX  = abs(mean(slopes)) + stderr(slopes)*1.5
NHitsMIN  = mean(nohs) - stderr(nohs)*1.5
NHitsMAX  = mean(nohs) + stderr(nohs)*1.5
TrigMIN   = mean(trigs) - stderr(trigs)*1.5
TrigMAX   = mean(trigs) + stderr(trigs)*1.5

outfile.write("LenghtMIN="+str(LenghtMIN)+" LenghtMAX="+str(LenghtMAX)+" SlopeMIN="+str(SlopeMIN)+" SlopeMAX="+str(SlopeMAX)+" NHitsMIN="+str(NHitsMIN)+" NHitsMAX="+str(NHitsMAX)+" TrigMIN="+str(TrigMIN)+" TrigMAX="+str(TrigMAX)+"\n")

# filling histos
for r in runs:
    arr = runs[r]
    run_n = float(r)
    hist_run_length.Fill(run_n, arr[3])
    if (arr[3] > LenghtMAX or arr[3] < LenghtMIN):  
        outfile.write("Run:"+str(run_n)+"; Track Length:"+str(arr[3])+"\n")
    hist_run_slopes.Fill(run_n, abs(arr[4]))
    if (arr[4] > SlopeMAX or arr[4] < SlopeMIN):
        outfile.write('Run:'+str(run_n)+'; Track Slope:'+str(arr[4])+'\n')
    hist_run_nofhit.Fill(run_n, arr[5])
    if (arr[5] > NHitsMAX or arr[5] < NHitsMIN):
        outfile.write('Run:'+str(run_n)+'; Track NHits:'+str(arr[5])+'\n')
    hist_run_triggs.Fill(run_n, arr[6])
    if (arr[6] > TrigMAX or arr[6] < TrigMIN):
        outfile.write('Run:'+str(run_n)+'; Track Slope:'+str(arr[6])+'\n')
        print 'Run:'+str(run_n)+'; Track Slope:'+str(arr[6])

    hist_length.Fill(arr[3])
    hist_slopes.Fill(abs(arr[4]))
    hist_nofhit.Fill(arr[5])
    hist_triggs.Fill(arr[6])

# draw histos
c1 = TCanvas('c1', 'Run number vs mean track length', 200, 10, 900, 500)
hist_run_length.Draw()
line.Draw("SAME")
line2.Draw("SAME")
novastyle.PreliminarySide()
c1.Print("Run_vs_tracklength.png")

c2 = TCanvas('c2', 'Run number vs mean track beta', 200, 10, 900, 500)
hist_run_slopes.Draw()
novastyle.PreliminarySide()
line3.Draw("SAME")
line4.Draw("SAME")
c2.Print("Run_vs_beta.png")

c3 = TCanvas('c3', 'Run number vs mean # of hits', 200, 10, 900, 500)
hist_run_nofhit.Draw()
novastyle.PreliminarySide()
line5.Draw("SAME")
line6.Draw("SAME")
c3.Print("Run_vs_nhits.png")

c4 = TCanvas('c4', 'Run number vs # of selected track per event in a run', 200, 10, 900, 500)
hist_run_triggs.Draw()
novastyle.PreliminarySide()
line7.Draw("SAME")
line8.Draw("SAME")
c4.Print("run_vs_selectedtrackinarun.png")

gStyle.SetOptStat(1101)

c5 = TCanvas('c5', 'Mean length distribution', 200, 10, 900, 500)
hist_length.Draw()
hist_length.Fit('gaus')
#hist_length.SetStats(1)
novastyle.PreliminarySide()
c5.Print("MeanLengthDistribution.png")

c6 = TCanvas('c6', 'Mean beta distribution', 200, 10, 900, 500)
hist_slopes.Draw()
hist_slopes.Fit('gaus')
#hist_slopes.SetStats(1)
novastyle.PreliminarySide()
c6.Print("MeanBetaDistribution.png")

c7 = TCanvas('c7', 'Mean # of hits per track distribution', 200, 10, 900, 500)
hist_nofhit.Draw()
hist_nofhit.Fit('gaus')
#hist_nofhit.SetStats(1)
novastyle.PreliminarySide()
c7.Print("MeanNhitspertrackdistribution.png")

c8 = TCanvas('c8', '# of selected tracks per event distribution', 200, 10, 900, 500)
hist_triggs.Draw()
hist_triggs.Fit('gaus')
#hist_triggs.SetStats(1)
novastyle.PreliminarySide()
c8.Print("NumberofSelectedtracksperevents.png")

outfile.close()
