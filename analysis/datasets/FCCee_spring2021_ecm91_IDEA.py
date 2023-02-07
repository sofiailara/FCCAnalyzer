
# http://fcc-physics-events.web.cern.ch/fcc-physics-events/FCCee/spring2021/Delphesevents_IDEA.php

def get_datasets(baseDir = ""):

    datasets = []
    subDir = "/spring2021/IDEA/"
    baseDir = "%s/%s" % (baseDir, subDir)

    datasets.append({
        "name"      : "p8_ee_Zee_ecm91",
        "datadir"   : "%s/p8_ee_Zee_ecm91" % baseDir,
        "xsec"      : 1462.09
    })
    
    datasets.append({
        "name"      : "p8_ee_Zmumu_ecm91",
        "datadir"   : "%s/p8_ee_Zmumu_ecm91" % baseDir,
        "xsec"      : 1462.08
    })
    
    datasets.append({
        "name"      : "p8_ee_Ztautau_ecm91",
        "datadir"   : "%s/p8_ee_Ztautau_ecm91" % baseDir,
        "xsec"      : 1476.58
    })
    
    
    
    datasets.append({
        "name"      : "p8_ee_Zuds_ecm91",
        "datadir"   : "%s/p8_ee_Zuds_ecm91" % baseDir,
        "xsec"      : 18616.5
    })
    
    datasets.append({
        "name"      : "p8_ee_Zcc_ecm91",
        "datadir"   : "%s/p8_ee_Zcc_ecm91" % baseDir,
        "xsec"      : 5215.46
    })
    
    datasets.append({
        "name"      : "p8_ee_Zbb_ecm91",
        "datadir"   : "%s/p8_ee_Zbb_ecm91" % baseDir,
        "xsec"      : 6645.46
    })

    datasets.append({
        "name"      : "wzp6_gaga_mumu_5_ecm91p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/wzp6_gaga_mumu_5_ecm91p2/",
        "xsec"      : 5.3393669E+02
    })
    datasets.append({
        "name"      : "wzp6_ee_mumu_ecm91p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_mumu_ecm91p2",
        "xsec"      : 1.69E+03
    })
    datasets.append({
        "name"      : "wzp6_ee_tautau_ecm91p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_tautau_ecm91p2",
        "xsec"      : 1.70E+03
    })
    datasets.append({
        "name"      : "wzp6_gaga_mumu_5_ecm91p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_gaga_mumu_5_ecm91p2",
        "xsec"      : 5.34E+02
    })
    datasets.append({
        "name"      : "wzp6_ee_qq_ecm91p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_qq_ecm91p2",
        "xsec"      : 3.45E+04
    })
    datasets.append({
        "name"      : "wzp6_ee_mumu_ecm89p5",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_mumu_ecm89p5",
        "xsec"      : 5.15E+02
    })
    datasets.append({
        "name"      : "wzp6_ee_mumu_ecm90p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_mumu_ecm90p2",
        "xsec"      : 8.82E+03
    })
    datasets.append({
        "name"      : "wzp6_ee_mumu_ecm92p0",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_mumu_ecm92p0",
        "xsec"      : 1.39E+03
    })
    datasets.append({
        "name"      : "wzp6_ee_mumu_ecm93p0",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_mumu_ecm93p0",
        "xsec"      : 7.82E+02
    })
    datasets.append({
        "name"      : "wzp6_ee_tautau_ecm89p5",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_tautau_ecm89p5",
        "xsec"      : 5.09E+02
    })
    datasets.append({
        "name"      : "wzp6_ee_tautau_ecm90p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_tautau_ecm90p2",
        "xsec"      : 8.76E+03
    })
    datasets.append({
        "name"      : "wzp6_ee_tautau_ecm92p0",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_tautau_ecm92p0",
        "xsec"      : 1.39E+03
    })
    datasets.append({
        "name"      : "wzp6_ee_tautau_ecm93p0",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_ee_tautau_ecm93p0",
        "xsec"      : 7.73E+03
    })
    datasets.append({
        "name"      : "wzp6_gaga_mumu_5_ecm89p5",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_gaga_mumu_5_ecm89p5",
        "xsec"      : 5.31E+02
    })
    datasets.append({
        "name"      : "wzp6_gaga_mumu_5_ecm90p2",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_gaga_mumu_5_ecm90p2",
        "xsec"      : 5.32E+02
    })
    datasets.append({
        "name"      : "wzp6_gaga_mumu_5_ecm92p0",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_gaga_mumu_5_ecm92p0",
        "xsec"      : 5.36E+02
    })
    datasets.append({
        "name"      : "wzp6_gaga_mumu_5_ecm93p0",
        "datadir"   : "/data/submit/cms/store/fccee/winter2023/IDEA/wzp6_gaga_mumu_5_ecm93p0",
        "xsec"      : 5.38E+02
    })
    
    return datasets