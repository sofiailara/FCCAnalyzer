
import sys,array,ROOT,math,os,copy

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

import plotter


def getHist(proc, sel, hName, rebin):

    fIn = ROOT.TFile("%s/%s_hists.root" % (histDir, proc))
    h = copy.deepcopy(fIn.Get("%s_%s" % (hName, sel)))
    h.Rebin(rebin)
    h.Scale(lumi*ds.datasets[proc]['xsec']*1e6/ds.datasets[proc]['nevents'])
    fIn.Close()
    return h



def recoil_log(sel):

    fOut = "zed_leptonic_recoil_m"
    xMin, xMax = 0, 150
    rebin = 500

    hName = "zed_leptonic_recoil_m"

    st = ROOT.THStack()
    st.SetName("stack")
        
    leg = ROOT.TLegend(.4, 0.97-(len(bkgs)+2)*0.055, .7, .90)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.035)
    


    h_sig = None
    for sig in sigs:
    
        h = getHist(sig, sel, hName, rebin)
        if h_sig == None: h_sig = h
        else: h_sig.Add(h)
		
    h_sig.SetLineColor(ROOT.TColor.GetColor("#BF2229"))
    h_sig.SetLineWidth(4)
    h_sig.SetLineStyle(1)
    leg.AddEntry(h_sig, sigLegend, "L") #  (10#times)

    
    # Get all bkg histograms
    st = ROOT.THStack()
    st.SetName("stack")
    h_bkg = None
    for i,bkg in enumerate(bkgs):
		
        hist = None
        for x in bgks_cfg[bkg]:
            
            h = getHist(x, sel, hName, rebin)
		
            if hist == None: hist = h
            else: hist.Add(h)
		
        hist.SetName(bkg)
        hist.SetFillColor(bkgs_colors[i])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(1)
        hist.SetLineStyle(1)
		
        leg.AddEntry(hist, bkgs_legends[i], "F")
        st.Add(hist)
        if h_bkg == None:
            h_bkg = copy.deepcopy(hist)
            h_bkg.SetName("h_bkg")
        else: h_bkg.Add(hist)
        

    
    yMax = math.ceil(h_bkg.GetMaximum()*100)/10.
    

    cfg = {

        'logy'              : True,
        'logx'              : False,
        
        'xmin'              : xMin,
        'xmax'              : xMax,
        'ymin'              : 1e2,
        'ymax'              : 1e5,
            
        'xtitle'            : "m_{rec} (GeV)",
        'ytitle'            : "Events / 0.5 GeV",
            
        'topRight'          : "#sqrt{s} = 240 GeV, 5 ab^{#minus1}",
        'topLeft'           : "#bf{FCC-ee} #scale[0.7]{#it{Simulation}}",

    }
        

    plotter.cfg = cfg
    canvas = plotter.canvas()
        
    dummy = plotter.dummy()
    dummy.Draw("HIST")
        
    st.Draw("HIST SAME")
    
    
    '''
    hTot_err = hTot.Clone("hTot_err")
    hTot_err.SetFillColor(ROOT.kBlack)
    hTot_err.SetMarkerColor(ROOT.kBlack)
    hTot_err.SetFillStyle(3004)
    leg.AddEntry(hTot_err, "Stat. Unc.", "F")
    '''
    
    h_bkg.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(0)
    h_bkg.SetLineWidth(2)
    #hTot_err.Draw("E2 SAME")
    h_bkg.Draw("HIST SAME")
    
    h_sig.Draw("HIST SAME")
    
    leg.Draw("SAME")
        
    canvas.SetGrid()
    canvas.Modify()
    canvas.Update()

    plotter.aux()
    ROOT.gPad.SetTicks()
    ROOT.gPad.RedrawAxis()

    canvas.SaveAs("%s/recoil_%s.png" % (outDir, sel))
    canvas.SaveAs("%s/recoil_%s.pdf" % (outDir, sel))
    canvas.Close()



def recoil_lin(sel):

    fOut = "zed_leptonic_recoil_m"
    xMin, xMax = 0, 150
    rebin = 500

    hName = "zed_leptonic_recoil_m"

    st = ROOT.THStack()
    st.SetName("stack")
        
    leg = ROOT.TLegend(.4, 0.97-(len(bkgs)+2)*0.055, .7, .90)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.035)
    


    h_sig = None
    for sig in sigs:
    
        h = getHist(sig, sel, hName, rebin)
        if h_sig == None: h_sig = h
        else: h_sig.Add(h)
		
    h_sig.SetLineColor(ROOT.TColor.GetColor("#BF2229"))
    h_sig.SetLineWidth(4)
    h_sig.SetLineStyle(1)
    leg.AddEntry(h_sig, sigLegend, "L") #  (10#times)

    
    # Get all bkg histograms
    st = ROOT.THStack()
    st.SetName("stack")
    h_bkg = None
    for i,bkg in enumerate(bkgs):
		
        hist = None
        for x in bgks_cfg[bkg]:
            
            h = getHist(x, sel, hName, rebin)
		
            if hist == None: hist = h
            else: hist.Add(h)
		
        hist.SetName(bkg)
        hist.SetFillColor(bkgs_colors[i])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(1)
        hist.SetLineStyle(1)
		
        leg.AddEntry(hist, bkgs_legends[i], "F")
        st.Add(hist)
        if h_bkg == None:
            h_bkg = copy.deepcopy(hist)
            h_bkg.SetName("h_bkg")
        else: h_bkg.Add(hist)
        

    
    yMax = math.ceil(h_bkg.GetMaximum()*100)/10.
    

    cfg = {

        'logy'              : False,
        'logx'              : False,
        
        'xmin'              : xMin,
        'xmax'              : xMax,
        'ymin'              : 0,
        'ymax'              : 1.5e4,
            
        'xtitle'            : "m_{rec} (GeV)",
        'ytitle'            : "Events / 0.5 GeV",
            
        'topRight'          : "#sqrt{s} = 240 GeV, 5 ab^{#minus1}",
        'topLeft'           : "#bf{FCC-ee} #scale[0.7]{#it{Simulation}}",

    }
        

    plotter.cfg = cfg
    canvas = plotter.canvas()
        
    dummy = plotter.dummy()
    dummy.Draw("HIST")
        
    st.Draw("HIST SAME")
    
    
    '''
    hTot_err = hTot.Clone("hTot_err")
    hTot_err.SetFillColor(ROOT.kBlack)
    hTot_err.SetMarkerColor(ROOT.kBlack)
    hTot_err.SetFillStyle(3004)
    leg.AddEntry(hTot_err, "Stat. Unc.", "F")
    '''
    
    h_bkg.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(0)
    h_bkg.SetLineWidth(2)
    #hTot_err.Draw("E2 SAME")
    h_bkg.Draw("HIST SAME")
    
    h_sig.Draw("HIST SAME")
    
    leg.Draw("SAME")
        
    canvas.SetGrid()
    canvas.Modify()
    canvas.Update()

    plotter.aux()
    ROOT.gPad.SetTicks()
    ROOT.gPad.RedrawAxis()

    canvas.SaveAs("%s/recoil_lin_%s.png" % (outDir, sel))
    canvas.SaveAs("%s/recoil_lin_%s.pdf" % (outDir, sel))
    canvas.Close()



def recoil_lin_zoom(sel):

    fOut = "zed_leptonic_recoil_m"
    xMin, xMax = 120, 140
    rebin = 100

    hName = "zed_leptonic_recoil_m"

    st = ROOT.THStack()
    st.SetName("stack")
        
    leg = ROOT.TLegend(.4, 0.97-(len(bkgs)+2)*0.055, .7, .90)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.035)
    


    h_sig = None
    for sig in sigs:
    
        h = getHist(sig, sel, hName, rebin)
        if h_sig == None: h_sig = h
        else: h_sig.Add(h)
		
    h_sig.SetLineColor(ROOT.TColor.GetColor("#BF2229"))
    h_sig.SetLineWidth(4)
    h_sig.SetLineStyle(1)
    leg.AddEntry(h_sig, sigLegend, "L") #  (10#times)

    
    # Get all bkg histograms
    st = ROOT.THStack()
    st.SetName("stack")
    h_bkg = None
    for i,bkg in enumerate(bkgs):
		
        hist = None
        for x in bgks_cfg[bkg]:
            
            h = getHist(x, sel, hName, rebin)
		
            if hist == None: hist = h
            else: hist.Add(h)
		
        hist.SetName(bkg)
        hist.SetFillColor(bkgs_colors[i])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(1)
        hist.SetLineStyle(1)
		
        leg.AddEntry(hist, bkgs_legends[i], "F")
        st.Add(hist)
        if h_bkg == None:
            h_bkg = copy.deepcopy(hist)
            h_bkg.SetName("h_bkg")
        else: h_bkg.Add(hist)
        

    
    yMax = math.ceil(h_bkg.GetMaximum()*100)/10.
    

    cfg = {

        'logy'              : False,
        'logx'              : False,
        
        'xmin'              : xMin,
        'xmax'              : xMax,
        'ymin'              : 0,
        'ymax'              : 1000,
            
        'xtitle'            : "m_{rec} (GeV)",
        'ytitle'            : "Events / 0.1 GeV",
            
        'topRight'          : "#sqrt{s} = 240 GeV, 5 ab^{#minus1}",
        'topLeft'           : "#bf{FCC-ee} #scale[0.7]{#it{Simulation}}",

    }
        

    plotter.cfg = cfg
    canvas = plotter.canvas()
        
    dummy = plotter.dummy()
    dummy.Draw("HIST")
        
    st.Draw("HIST SAME")
    
    
    '''
    hTot_err = hTot.Clone("hTot_err")
    hTot_err.SetFillColor(ROOT.kBlack)
    hTot_err.SetMarkerColor(ROOT.kBlack)
    hTot_err.SetFillStyle(3004)
    leg.AddEntry(hTot_err, "Stat. Unc.", "F")
    '''
    
    h_bkg.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(0)
    h_bkg.SetLineWidth(2)
    #hTot_err.Draw("E2 SAME")
    h_bkg.Draw("HIST SAME")
    
    h_sig.Draw("HIST SAME")
    
    leg.Draw("SAME")
        
    canvas.SetGrid()
    canvas.Modify()
    canvas.Update()

    plotter.aux()
    ROOT.gPad.SetTicks()
    ROOT.gPad.RedrawAxis()

    canvas.SaveAs("%s/recoil_lin_zoom_%s.png" % (outDir, sel))
    canvas.SaveAs("%s/recoil_lin_zoom_%s.pdf" % (outDir, sel))
    canvas.Close()



def mll(sel):

    fOut = "zed_leptonic_m"
    xMin, xMax = 0, 250
    rebin = 1500 # 3000 = /1GeV, 300 = 0.1 GeV

    hName = "zed_leptonic_m"

    st = ROOT.THStack()
    st.SetName("stack")
        
    leg = ROOT.TLegend(.47, 0.97-(len(bkgs)+2)*0.055, 0.47+0.3, .90)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.035)
    


    h_sig = None
    for sig in sigs:
    
        h = getHist(sig, sel, hName, rebin)
        if h_sig == None: h_sig = h
        else: h_sig.Add(h)
		
    h_sig.SetLineColor(ROOT.TColor.GetColor("#BF2229"))
    h_sig.SetLineWidth(4)
    h_sig.SetLineStyle(1)
    #h_sig.Scale(10)
    leg.AddEntry(h_sig, sigLegend, "L") #  (10#times)

    
    # Get all bkg histograms
    st = ROOT.THStack()
    st.SetName("stack")
    h_bkg = None
    for i,bkg in enumerate(bkgs):
		
        hist = None
        for x in bgks_cfg[bkg]:
            
            h = getHist(x, sel, hName, rebin)
		
            if hist == None: hist = h
            else: hist.Add(h)
		
        hist.SetName(bkg)
        hist.SetFillColor(bkgs_colors[i])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(1)
        hist.SetLineStyle(1)
		
        leg.AddEntry(hist, bkgs_legends[i], "F")
        st.Add(hist)
        if h_bkg == None:
            h_bkg = copy.deepcopy(hist)
            h_bkg.SetName("h_bkg")
        else: h_bkg.Add(hist)
        

    
    yMax = math.ceil(h_bkg.GetMaximum()*100)/10.
    

    cfg = {

        'logy'              : True,
        'logx'              : False,
        
        'xmin'              : xMin,
        'xmax'              : xMax,
        'ymin'              : 1e3,
        'ymax'              : 1e7, # 3e6
            
        'xtitle'            : "m_{#mu^{+},#mu^{#minus}} (GeV)",
        'ytitle'            : "Events / 0.5 GeV",
            
        'topRight'          : "#sqrt{s} = 240 GeV, 5 ab^{#minus1}", 
        'topLeft'           : "#bf{FCC-ee} #scale[0.7]{#it{Simulation}}",

    }
        

    plotter.cfg = cfg
    canvas = plotter.canvas()
        
    dummy = plotter.dummy()
    dummy.Draw("HIST")
        
    st.Draw("HIST SAME")
    
    ROOT.TGaxis.SetExponentOffset(-0.07,0.015)
    
    
    '''
    hTot_err = hTot.Clone("hTot_err")
    hTot_err.SetFillColor(ROOT.kBlack)
    hTot_err.SetMarkerColor(ROOT.kBlack)
    hTot_err.SetFillStyle(3004)
    leg.AddEntry(hTot_err, "Stat. Unc.", "F")
    '''
    
    h_bkg.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(0)
    h_bkg.SetLineWidth(2)
    #hTot_err.Draw("E2 SAME")
    h_bkg.Draw("HIST SAME")
    
    h_sig.Draw("HIST SAME")
    
    leg.Draw("SAME")
        
    canvas.SetGrid()
    canvas.Modify()
    canvas.Update()

    plotter.aux()
    ROOT.gPad.SetTicks()
    ROOT.gPad.RedrawAxis()

    canvas.SaveAs("%s/mll_%s.png" % (outDir, sel))
    canvas.SaveAs("%s/mll_%s.pdf" % (outDir, sel))
    canvas.Close()



def ptll(sel):

    fOut = "zed_leptonic_pt"
    xMin, xMax = 0, 120
    rebin = 1000

    hName = "zed_leptonic_pt"

    st = ROOT.THStack()
    st.SetName("stack")
        
    leg = ROOT.TLegend(.4, 0.97-(len(bkgs)+2)*0.055, .7, .90)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.035)
    


    h_sig = None
    for sig in sigs:
    
        h = getHist(sig, sel, hName, rebin)
        if h_sig == None: h_sig = h
        else: h_sig.Add(h)
		
    h_sig.SetLineColor(ROOT.TColor.GetColor("#BF2229"))
    h_sig.SetLineWidth(4)
    h_sig.SetLineStyle(1)
    #h_sig.Scale(10)
    leg.AddEntry(h_sig, sigLegend, "L") #  (10#times)

    
    # Get all bkg histograms
    st = ROOT.THStack()
    st.SetName("stack")
    h_bkg = None
    for i,bkg in enumerate(bkgs):
		
        hist = None
        for x in bgks_cfg[bkg]:
            
            h = getHist(x, sel, hName, rebin)
		
            if hist == None: hist = h
            else: hist.Add(h)
		
        hist.SetName(bkg)
        hist.SetFillColor(bkgs_colors[i])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(1)
        hist.SetLineStyle(1)
		
        leg.AddEntry(hist, bkgs_legends[i], "F")
        st.Add(hist)
        if h_bkg == None:
            h_bkg = copy.deepcopy(hist)
            h_bkg.SetName("h_bkg")
        else: h_bkg.Add(hist)
        


    cfg = {

        'logy'              : True,
        'logx'              : False,
        
        'xmin'              : xMin,
        'xmax'              : xMax,
        'ymin'              : 1e2,
        'ymax'              : 1e7, # 3e6
            
        'xtitle'            : "p_{T}^{#mu^{+},#mu^{#minus}} (GeV)",
        'ytitle'            : "Events / 0.5 GeV",
            
        'topRight'          : "#sqrt{s} = 240 GeV, 5 ab^{#minus1}", 
        'topLeft'           : "#bf{FCC-ee} #scale[0.7]{#it{Simulation}}",

    }
        

    plotter.cfg = cfg
    canvas = plotter.canvas()
        
    dummy = plotter.dummy()
    dummy.Draw("HIST")
        
    st.Draw("HIST SAME")
    
    ROOT.TGaxis.SetExponentOffset(-0.07,0.015)
    
    
    '''
    hTot_err = hTot.Clone("hTot_err")
    hTot_err.SetFillColor(ROOT.kBlack)
    hTot_err.SetMarkerColor(ROOT.kBlack)
    hTot_err.SetFillStyle(3004)
    leg.AddEntry(hTot_err, "Stat. Unc.", "F")
    '''
    
    h_bkg.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(0)
    h_bkg.SetLineWidth(2)
    #hTot_err.Draw("E2 SAME")
    h_bkg.Draw("HIST SAME")
    
    h_sig.Draw("HIST SAME")
    
    leg.Draw("SAME")
        
    canvas.SetGrid()
    canvas.Modify()
    canvas.Update()

    plotter.aux()
    ROOT.gPad.SetTicks()
    ROOT.gPad.RedrawAxis()

    canvas.SaveAs("%s/ptll_%s.png" % (outDir, sel))
    canvas.SaveAs("%s/ptll_%s.pdf" % (outDir, sel))
    canvas.Close()



def costhetamissing(sel):

    fOut = "costheta_missing"
    xMin, xMax = 0, 1
    rebin = 500

    hName = "cosTheta_miss"

    st = ROOT.THStack()
    st.SetName("stack")
        
    leg = ROOT.TLegend(.3, 0.97-(len(bkgs)+2)*0.055, .6, .90)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.035)
    


    h_sig = None
    for sig in sigs:
    
        h = getHist(sig, sel, hName, rebin)
        if h_sig == None: h_sig = h
        else: h_sig.Add(h)
		
    h_sig.SetLineColor(ROOT.TColor.GetColor("#BF2229"))
    h_sig.SetLineWidth(4)
    h_sig.SetLineStyle(1)
    #h_sig.Scale(10)
    leg.AddEntry(h_sig, sigLegend, "L") #  (10#times)

    
    # Get all bkg histograms
    st = ROOT.THStack()
    st.SetName("stack")
    h_bkg = None
    for i,bkg in enumerate(bkgs):
		
        hist = None
        for x in bgks_cfg[bkg]:
            
            h = getHist(x, sel, hName, rebin)
		
            if hist == None: hist = h
            else: hist.Add(h)
		
        hist.SetName(bkg)
        hist.SetFillColor(bkgs_colors[i])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(1)
        hist.SetLineStyle(1)
		
        leg.AddEntry(hist, bkgs_legends[i], "F")
        st.Add(hist)
        if h_bkg == None:
            h_bkg = copy.deepcopy(hist)
            h_bkg.SetName("h_bkg")
        else: h_bkg.Add(hist)
        


    cfg = {

        'logy'              : True,
        'logx'              : False,
        
        'xmin'              : xMin,
        'xmax'              : xMax,
        'ymin'              : 1e2,
        'ymax'              : 1e6, # 3e6
            
        'xtitle'            : "|cos#theta_{missing}|",
        'ytitle'            : "Events",
            
        'topRight'          : "#sqrt{s} = 240 GeV, 5 ab^{#minus1}", 
        'topLeft'           : "#bf{FCC-ee} #scale[0.7]{#it{Simulation}}",

    }
        

    plotter.cfg = cfg
    canvas = plotter.canvas()
        
    dummy = plotter.dummy()
    dummy.Draw("HIST")
        
    st.Draw("HIST SAME")
    
    ROOT.TGaxis.SetExponentOffset(-0.07,0.015)
    
    
    '''
    hTot_err = hTot.Clone("hTot_err")
    hTot_err.SetFillColor(ROOT.kBlack)
    hTot_err.SetMarkerColor(ROOT.kBlack)
    hTot_err.SetFillStyle(3004)
    leg.AddEntry(hTot_err, "Stat. Unc.", "F")
    '''
    
    h_bkg.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(0)
    h_bkg.SetLineWidth(2)
    #hTot_err.Draw("E2 SAME")
    h_bkg.Draw("HIST SAME")
    
    h_sig.Draw("HIST SAME")
    
    leg.Draw("SAME")
        
    canvas.SetGrid()
    canvas.Modify()
    canvas.Update()

    plotter.aux()
    ROOT.gPad.SetTicks()
    ROOT.gPad.RedrawAxis()

    canvas.SaveAs("%s/costheta_missing_%s.png" % (outDir, sel))
    canvas.SaveAs("%s/costheta_missing_%s.pdf" % (outDir, sel))
    canvas.Close()





def makePlot(hName, outName, xMin=0, xMax=100, yMin=1, yMax=1e5, xLabel="xlabel", yLabel="Events", logX=False, logY=True, rebin=1, legPos=[0.4, 0.65, 0.9, 0.9]):


    st = ROOT.THStack()
    st.SetName("stack")
        
    leg = ROOT.TLegend(legPos[0], legPos[1], legPos[2], legPos[3])
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.03)
    leg.SetMargin(0.2)
    

    h_sig = plotter.getProc(fIn, hName, sigs)
    if "TH2" in h_sig.ClassName(): h_sig = h_sig.ProjectionX("h_sig")
    h_sig.SetLineColor(ROOT.TColor.GetColor("#BF2229"))
    h_sig.SetLineWidth(3)
    h_sig.SetLineStyle(1)
    h_sig.Scale(sig_scale)
    h_sig.Rebin(rebin)
    leg.AddEntry(h_sig, sig_legend, "L")

    st = ROOT.THStack()
    st.SetName("stack")
    h_bkg_tot = None
    for i,bkg in enumerate(bkgs):
		
        hist = plotter.getProc(fIn, hName, bgks_cfg[bkg])
        if "TH2" in hist.ClassName(): hist = hist.ProjectionX()
        hist.SetName(bkg)
        hist.SetFillColor(bkgs_colors[i])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(1)
        hist.SetLineStyle(1)
        hist.Rebin(rebin)
		
        leg.AddEntry(hist, bkgs_legends[i], "F")
        st.Add(hist)
        if h_bkg_tot == None:
            h_bkg_tot = copy.deepcopy(hist)
            h_bkg_tot.SetName("h_bkg_tot")
        else: h_bkg_tot.Add(hist)
        

    cfg = {

        'logy'              : logY,
        'logx'              : logX,
        
        'xmin'              : xMin,
        'xmax'              : xMax,
        'ymin'              : yMin,
        'ymax'              : yMax if yMax > 0 else ath.ceil(h_bkg_tot.GetMaximum()*100)/10.,
            
        'xtitle'            : xLabel,
        'ytitle'            : yLabel,
            
        'topRight'          : "#sqrt{s} = 240 GeV, 5 ab^{#minus1}",
        'topLeft'           : "#bf{FCC-ee} #scale[0.7]{#it{Simulation}}",

    }
        

    plotter.cfg = cfg
    canvas = plotter.canvas()
        
    dummy = plotter.dummy()
    dummy.Draw("HIST") 
    st.Draw("HIST SAME")
    
    
    '''
    hTot_err = hTot.Clone("hTot_err")
    hTot_err.SetFillColor(ROOT.kBlack)
    hTot_err.SetMarkerColor(ROOT.kBlack)
    hTot_err.SetFillStyle(3004)
    leg.AddEntry(hTot_err, "Stat. Unc.", "F")
    '''
    
    h_bkg_tot.SetLineColor(ROOT.kBlack)
    h_bkg_tot.SetFillColor(0)
    h_bkg_tot.SetLineWidth(2)
    #hTot_err.Draw("E2 SAME")
    h_bkg_tot.Draw("HIST SAME")
    h_sig.Draw("HIST SAME")
    leg.Draw("SAME")
        
    canvas.SetGrid()
    canvas.Modify()
    canvas.Update()

    plotter.aux()
    ROOT.gPad.SetTicks()
    ROOT.gPad.RedrawAxis()

    canvas.SaveAs("%s/%s.png" % (outDir, outName))
    canvas.SaveAs("%s/%s.pdf" % (outDir, outName))
    canvas.Close()


	
if __name__ == "__main__":

    flavor = "ee"
    fIn = ROOT.TFile("tmp/output_mass_xsec_%s.root" % flavor)
    outDir = "/eos/user/j/jaeyserm/www/FCCee/ZH_mass_xsec/plots_%s/" % flavor
    
    
    
    if flavor == "mumu":
    
        labels = ["All events", "#geq 1 #mu^{#pm}", "#geq 2 #mu^{#pm}", "86 < m_{#mu^{+}#mu^{#minus}} < 96", "20 < p_{T}^{#mu^{+}#mu^{#minus}} < 70", "|cos#theta_{missing}| < 0.98", "120 < m_{rec} < 140"]
    
        sigs = ["wzp6_ee_mumuH_ecm240"]
        sig_scale = 1
        sig_legend = "Z(#mu^{+}#mu^{#minus})H"
    
        bkgs = ["WW", "ZZ", "Zg", "rare"] # this is the order of the plot
        bkgs_legends = ["W^{+}W^{#minus}", "ZZ", "Z/#gamma^{*} #rightarrow #mu^{+}#mu^{#minus}, #tau^{+}#tau^{#minus}", "Rare (e(e)Z, #gamma#gamma #rightarrow #mu^{+}#mu^{#minus}, #tau^{+}#tau^{#minus})"]
        bkgs_colors = [ROOT.TColor.GetColor(248, 206, 104), ROOT.TColor.GetColor(222, 90, 106), ROOT.TColor.GetColor(100, 192, 232), ROOT.TColor.GetColor(155, 152, 204)] # from
        bgks_cfg = { 
            "WW"	    : ["p8_ee_WW_ecm240"],
            "ZZ"	    : ["p8_ee_ZZ_ecm240"],
            "Zg"        : ["wzp6_ee_mumu_ecm240", "wzp6_ee_tautau_ecm240"],
            "rare"      : ["wzp6_egamma_eZ_Zmumu_ecm240", "wzp6_gammae_eZ_Zmumu_ecm240", "wzp6_gaga_mumu_60_ecm240", "wzp6_gaga_tautau_60_ecm240", "wzp6_ee_nuenueZ_ecm240"]
        }
        
    if flavor == "ee":
    
        labels = ["All events", "#geq 1 e^{#pm}", "#geq 2 e^{#pm}", "86 < m_{e^{+}e^{#minus}} < 96", "20 < p_{T}^{e^{+}e^{#minus}} < 70", "|cos#theta_{missing}| < 0.98", "120 < m_{rec} < 140"]
    
        sigs = ["wzp6_ee_eeH_ecm240"]
        sig_scale = 1
        sig_legend = "Z(e^{+}e^{#minus})H"
    
        bkgs = ["WW", "ZZ", "Zg", "rare"] # this is the order of the plot
        bkgs_legends = ["W^{+}W^{#minus}", "ZZ", "Z/#gamma^{*} #rightarrow e^{+}e^{#minus}, #tau^{+}#tau^{#minus}", "Rare (e(e)Z, #gamma#gamma #rightarrow e^{+}e^{#minus}, #tau^{+}#tau^{#minus})"]
        
        bkgs_colors = [ROOT.TColor.GetColor(248, 206, 104), ROOT.TColor.GetColor(222, 90, 106), ROOT.TColor.GetColor(100, 192, 232), ROOT.TColor.GetColor(155, 152, 204)] # from
        bgks_cfg = { 
            "WW"	    : ["p8_ee_WW_ecm240"],
            "ZZ"	    : ["p8_ee_ZZ_ecm240"],
            "Zg"        : ["wzp6_ee_ee_Mee_30_150_ecm240", "wzp6_ee_tautau_ecm240"],
            "rare"      : ["wzp6_egamma_eZ_Zee_ecm240", "wzp6_gammae_eZ_Zee_ecm240", "wzp6_gaga_ee_60_ecm240", "wzp6_gaga_tautau_60_ecm240", "wzp6_ee_nuenueZ_ecm240"]
        }

    makePlot("zll_recoil_m", "zll_recoil_m", xMin=120, xMax=140, yMin=0, yMax=1.5e3, xLabel="m_{rec} (GeV)", yLabel="Events / 0.1 GeV", logY=False, rebin=100)
    makePlot("cosThetaMiss_cut4", "cosThetaMiss_cut4", xMin=0, xMax=1, yMin=0, yMax=5000, xLabel="|cos(#theta_{miss})|", yLabel="Events", logY=False, rebin=100)
    makePlot("photons_theta_cut6", "photons_theta_cut6", xMin=0, xMax=3.1415, yMin=0, yMax=2e3, xLabel="Photon #theta (rad)", yLabel="Events", logY=False, rebin=1)
    #makePlot("photons_phi_cut6", "photons_phi_cut6", xMin=-3.1415, xMax=3.1415, yMin=0, yMax=1e3, xLabel="Photon #phi (rad)", yLabel="Events", logY=False, rebin=1)
    makePlot("photons_p_cut6", "photons_p_cut6", xMin=0, xMax=20, yMin=0, yMax=1e3, xLabel="Photon p (GeV)", yLabel="Events", logY=False, rebin=10)
    #makePlot("photons_theta_cut5", "photons_theta_cut5", xMin=0, xMax=3.1415, yMin=0, yMax=2e3, xLabel="Photon #theta (rad)", yLabel="Events", logY=False, rebin=1)
    
   