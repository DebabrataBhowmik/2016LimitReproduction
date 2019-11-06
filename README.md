MonoHiggs_Analysis_Procedure
-----------------------------------------------------------------------------------------------------------------------------

Once you have the nTuples from the microAOD, you need to get the Xsec of the MC generated

Once you get the xsec go to directory : /afs/cern.ch/work/d/dbhowmik/public/Analysis/MHgg/2016Analysis/CMSSW_8_0_28/src/MonoHiggsToGG/analysis/work/macros

check the path inside myrunAddWeightsAll_sig.sh and run

./myrunAddWeightsAll_sig.sh 35.9(lumi)

./myrunSkimAll.sh

Then go to ../../fits/Test_producedNtuplesFrom2016MicroAOD i.e. (analysis/fits/Test_producedNtuplesFrom2016MicroAOD) and run

./myformatNtupleForFitting_METcat.sh 50 130

cd /afs/cern.ch/work/d/dbhowmik/public/Analysis/MHgg/2017Analysis/Fit_DiPhotonTools/CMSSW_9_4_9/src/diphotons/Analysis/macros/Test_producedNtuplesFrom2016MicroAOD

cp -r /afs/cern.ch/work/d/dbhowmik/public/Analysis/MHgg/2016Analysis/CMSSW_8_0_28/src/MonoHiggsToGG/analysis/fits/Test_producedNtuplesFrom2016MicroAOD/ntuples4fit_pho_newSig_test_met50_met130 .

./combine_maker_MonoHgg.sh "ntuples4fit_pho_newSig_test_met50_met130" --lumi 35.9 --fit-name cic --mc-file Output_MC.root --fit-background --redo-input 1

./mycombineall_MonoHgg.sh "ntuples4fit_pho_newSig_test_met50_met130_cic_default_shapes_lumi_35.9" --hadd --model 2HDM -C 0.9 -M AsymptoticLimits --run both

./mylimit_plots_MonoHgg.sh "ntuples4fit_pho_newSig_test_met50_met130_cic_default_shapes_lumi_35.9"
