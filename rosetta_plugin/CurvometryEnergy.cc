// rosetta_plugin/CurvometryEnergy.cc  
#include <core/scoring/methods/EnergyMethod.hh>  
#include <core/pose/Pose.hh>  

class CurvometryEnergy : public core::scoring::methods::EnergyMethod {  
public:  
    void residue_energy(core::pose::Pose const& pose, core::scoring::EnergyMap & emap) const override {  
        for (core::Size i = 1; i <= pose.size(); ++i) {  
            double kappa = pose.residue(i).xyz("CA").z();  // Exemplo simplificado  
            emap[core::scoring::curvometry] += curvature_energy(kappa, 0.75);  
        }  
    }  
};
