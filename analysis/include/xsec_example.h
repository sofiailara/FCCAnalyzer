#ifndef XSEC_EXAMPLE_H
#define XSEC_EXAMPLE_H

#include <cmath>
#include <vector>

#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticleData.h"
#include "edm4hep/MCParticleData.h"
#include "edm4hep/ParticleIDData.h"


#include "ReconstructedParticle2MC.h"

namespace FCCAnalyses {
  


Vec_tlv makeLorentzVectors(Vec_rp in) {
	
	Vec_tlv result;
	for (auto & p: in) {
		TLorentzVector tlv;
		tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
		result.push_back(tlv);
	}
	return result;
}

float inv_mass(Vec_tlv in) {
    TLorentzVector tlv;
    for (int i = 0;i < in.size(); i++){
        tlv = tlv + in[i];
        }
    return tlv.M();
}    

float max_pt(Vec_tlv leps_tlv) {
    float max = leps_tlv[0].Pt();
    for (int i = 0; i < leps_tlv.size(); i++){
        if (leps_tlv[i].Pt() >= max) {
        max = leps_tlv[i].Pt();
        }
    }
    return max;
}

float max_p(Vec_f im) {
    float p = im[0];
    for (int i = 1; i < im.size(); i++){
        if (im[i] >p){
            p = im[i];
        }
    }
    return p/45.6;
}
       
}

#endif
