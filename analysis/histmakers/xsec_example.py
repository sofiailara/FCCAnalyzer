import uproot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
from scipy.stats import norm
from scipy.optimize import curve_fit
from scipy import stats

import analysis, functions
import ROOT
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nThreads", type=int, help="number of threads", default=None)
parser.add_argument("--maxFiles", type=int, help="Max number of files (per dataset)", default=-1)
args = parser.parse_args()

functions.set_threads(args)

# define histograms
bins_p_mu = (40000, 0, 200) # 10 MeV bins
bins_m_ll = (10000, 0, 100) # 10 MeV bins
bins_p_ll = (20000, 0, 200) # 10 MeV bins

bins_theta = (500, -5, 5)
bins_phi = (500, -5, 5)

bins_count = (50, 0, 50)
bins_pdgid = (60, -30, 30)
bins_charge = (10, -5, 5)
bins_energy = (60, 0, 100)
bins_emiss= (1000, 0, 100)
bins_weight= (1000, 0, 100)
bins_weight2= (1000, 0, 100)
bins_p= (1000, 0, 5)
bins_acol= (1000, -5, 5)


#make use of the variable “weight”, defined as 1.0 

bins_cos = (100, -1, 1)

def build_graph_ll(df, dataset):

    print("build graph", dataset.name)
    results = []

    df = df.Define("weight", "1.0")
    weightsum = df.Sum("weight")
    
    
    df = df.Alias("Particle0", "Particle#0.index")
    df = df.Alias("Particle1", "Particle#1.index")
    df = df.Alias("MCRecoAssociations0", "MCRecoAssociations#0.index")
    df = df.Alias("MCRecoAssociations1", "MCRecoAssociations#1.index")
    df = df.Alias("Lepton0", "Muon#0.index")

    # gen muons
    df = df.Define("gen_muons", "FCCAnalyses::get_gen_pdg(Particle, 13)") # muon pdg index=13
    df = df.Define("gen_muons_p", "FCCAnalyses::MCParticle::get_p(gen_muons)")
    df = df.Define("gen_muons_theta", "FCCAnalyses::MCParticle::get_theta(gen_muons)")
    df = df.Define("gen_muons_phi", "FCCAnalyses::MCParticle::get_phi(gen_muons)")
    df = df.Define("gen_muons_no", "FCCAnalyses::MCParticle::get_n(gen_muons)")
    
    # get the leptons leptons
    df = df.Define("leps_all", "FCCAnalyses::ReconstructedParticle::get(Lepton0, ReconstructedParticles)")
    df = df.Define("leps_all_p", "FCCAnalyses::ReconstructedParticle::get_p(leps_all)")
    df = df.Define("leps_all_theta", "FCCAnalyses::ReconstructedParticle::get_theta(leps_all)")
    df = df.Define("leps_all_phi", "FCCAnalyses::ReconstructedParticle::get_phi(leps_all)")
    df = df.Define("leps_all_q", "FCCAnalyses::ReconstructedParticle::get_charge(leps_all)")
    df = df.Define("leps_all_no", "FCCAnalyses::ReconstructedParticle::get_n(leps_all)")

    results.append(df.Histo1D(("gen_muons_p", "", *bins_p_mu), "gen_muons_p"))
    results.append(df.Histo1D(("gen_muons_theta", "", *bins_theta), "gen_muons_theta"))
    results.append(df.Histo1D(("gen_muons_phi", "", *bins_phi), "gen_muons_phi"))
    results.append(df.Histo1D(("gen_muons_no", "", *bins_count), "gen_muons_no"))
    
    results.append(df.Histo1D(("evts_initial", "", *bins_count), "weight"))
    
    
    #df = df.Define("missingEnergy", "FCCAnalyses::missingEnergy(91., ReconstructedParticles)")
    #df = df.Define("emiss", "missingEnergy[0].energy")
    df = df.Define("acolinearity", "FCCAnalyses::acolinearity(leps_all)")
    
    #momentum leading
    df = df.Define("muon_leading", "(leps_all_p[0] > leps_all_p[1]) ? leps_all_p[0] : leps_all_p[1]")
    df = df.Define("muon_subleading", "(leps_all_p[0] < leps_all_p[1]) ? leps_all_p[0] : leps_all_p[1]")

    

    
    
    
    
    #results.append(df.Histo1D(("weight", "", *bins_weight), "weight"))
    
    # construct Lorentz vectors of the leptons
    df = df.Define("leps_tlv", "FCCAnalyses::makeLorentzVectors(leps_all)")

    df = df.Define("m_inv", "FCCAnalyses::inv_mass(leps_tlv)")
    #df = df.Define("muon_acol", "FCCAnalyses::muon_acol(leps_all)")
    df = df.Define("max_p", "FCCAnalyses::max_p(leps_all_p)")              
    df = df.Define("missingEnergy", "FCCAnalyses::missingEnergy(91., ReconstructedParticles)")
    df = df.Define("emiss", "missingEnergy[0].energy")
    df = df.Define("visibleEnergy", "FCCAnalyses::visibleEnergy(ReconstructedParticles)")
    df = df.Define("max_pt", "FCCAnalyses::max_pt(leps_tlv)")
    
    
    
    #FILTERS
    #df = df.Filter("m_inv >= 50")
    df = df.Filter("leps_all_no == 2")
    df = df.Filter("muon_leading >= 27.3 ") #0.6*45.5= 27.3
    df = df.Filter("max_pt >= 3")
    #df = df.Filter("leps_all_p[1] == 0 ")
    df = df.Filter("acolinearity < 1.5707")
    
    
    df = df.Filter("abs(cos(leps_all_theta[0]))<0.98")
    df = df.Filter("abs(cos(leps_all_theta[1]))<0.98")
    #df = df.Filter("m_inv>=51.652499999999996")
    #df = df.Filter("emiss<=22.25")
    
    
    results.append(df.Histo1D(("leps_all_p", "", *bins_p_mu), "leps_all_p"))
    results.append(df.Histo1D(("leps_all_theta", "", *bins_theta), "leps_all_theta"))
    results.append(df.Histo1D(("leps_all_phi", "", *bins_phi), "leps_all_phi"))
    results.append(df.Histo1D(("leps_all_q", "", *bins_charge), "leps_all_q"))
    results.append(df.Histo1D(("leps_all_no", "", *bins_count), "leps_all_no"))
    results.append(df.Histo1D(("m_inv", "", *bins_m_ll), "m_inv"))
    #results.append(df.Histo1D(("missingEnergy", "", *bins_energy), "missingEnergy"))
    results.append(df.Histo1D(("emiss", "", *bins_emiss), "emiss"))
    #results.append(df.Histo1D(("weight", "", *bins_weight2), "weight"))
    #total and selected
    #results.append(df.Histo1D(("missingEnergy", "", *bins_m_ll), "missingEnergy"))
    results.append(df.Histo1D(("visibleEnergy", "", *bins_m_ll), "visibleEnergy"))
    
    df = df.Define("theta_plus", "(leps_all_q[0] > 0) ? leps_all_theta[0] : leps_all_theta[1]")
    df = df.Define("theta_minus", "(leps_all_q[0] < 0) ? leps_all_theta[0] : leps_all_theta[1]")
    df = df.Define("cos_theta_plus", "cos(theta_plus)")
    df = df.Define("cos_theta_minus", "cos(theta_minus)")
    df = df.Define("cosThetac", "(sin(theta_plus-theta_minus))/(sin(theta_plus)+sin(theta_minus))")
    
    results.append(df.Histo1D(("theta_plus", "", *bins_theta), "theta_plus"))
    results.append(df.Histo1D(("theta_minus", "", *bins_theta), "theta_minus"))
    results.append(df.Histo1D(("cos_theta_plus", "", *bins_cos), "cos_theta_plus"))
    results.append(df.Histo1D(("cos_theta_minus", "", *bins_cos), "cos_theta_minus"))
    results.append(df.Histo1D(("acolinearity", "", *bins_acol), "acolinearity"))
    results.append(df.Histo1D(("max_p", "", *bins_p_mu), "max_p"))
    results.append(df.Histo1D(("cosThetac", "", *bins_cos), "cosThetac"))
    
    results.append(df.Histo1D(("evts_final", "", *bins_count), "weight"))
    return results, weightsum
    




if __name__ == "__main__":

    baseDir = functions.get_basedir() # get base directory of samples, depends on the cluster hostname (mit, cern, ...)
    import FCCee_spring2021_ecm91_IDEA
    datasets_spring2021_ecm91 = FCCee_spring2021_ecm91_IDEA.get_datasets(baseDir=baseDir) # list of all datasets
    datasets = [] # list of datasets to be run over

    datasets += functions.filter_datasets(datasets_spring2021_ecm91, ["p8_ee_Zmumu_ecm91"])
    datasets += functions.filter_datasets(datasets_spring2021_ecm91, ["p8_ee_Ztautau_ecm91"])
    datasets += functions.filter_datasets(datasets_spring2021_ecm91, ["wzp6_gaga_mumu_5_ecm91p2"])
    #result = functions.build_and_run(datasets, build_graph_ll, "tmp/output_xsec_example.root", maxFiles=args.maxFiles)
    functions.build_and_run(datasets, build_graph_ll, "tmp/output_xsec_example.root", maxFiles=args.maxFiles, norm=True, lumi=150000000)

