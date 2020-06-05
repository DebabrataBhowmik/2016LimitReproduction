###Limit_Plots_MonoHgg.py working lines


ROOT.gROOT.LoadMacro( "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/plotting/bandUtils.cxx+" )

if options.model=="2HDM": 
            flist = [ "%s/higgsCombineMonoHgg%s_sig_2HDMCombined.%s.2HDM_mA0%s.root" % (options.input_dir,options.suffix, options.method,options.mDM)]
 
 print options.input_dir, flist

tflist = {}
        for fname in flist:
            bname = os.path.basename(fname)
            coup = bname.split("_",1)
            print coup
            coup = coup[1].split(".")
            print coup
            coup = coup[2].replace("2HDM_mA0","")
            print coup
            tfin = self.open(fname)
            if not tfin: 
                print ("unable to open %s" % fname)
                sys.exit(-1)
            tree = tfin.Get("limit")
            if not tree: 
                print ("unable to find limit tree in %s" % fname)
                sys.exit(-1)
        
            tflist[coup] = tfin

        self.graphs = []
        for coup,tfile in tflist.iteritems():
          print coup, tfile
          self.plotLimit(options,coup,tfile)
          
          
 def plotLimit(self,options,coup,tfile):
     ROOT.use_precomputed_quantiles = True
     bandType = ROOT.Median 
            
     expected68Orig = ROOT.theBand( tfile, 1, 0, bandType,      0.68 )
     expected95Orig = ROOT.theBand( tfile, 1, 0, bandType,      0.95 )
     observedOrig   = ROOT.theBand( tfile, 1, 0, ROOT.Observed, 0.95 )       
     print "-------------------------------------------------------"
     print "N obs  = ",observedOrig.GetN()
     print "N ex68 = ",expected68Orig.GetN()
     print "N ex95 = ",expected95Orig.GetN()
     print "-------------------------------------------------------"       
     
     observed   = scaleGraph2(observedOrig,2)   
     expected68 = scaleGraph2(expected68Orig,2) 
     expected95 = scaleGraph2(expected95Orig,2) 
     
     unit = "fb" if options.use_fb else "pb"
     basicStyle = [["SetMarkerSize",0.6],["SetLineWidth",3],
                    ["SetTitle",";M_{Z`} (GeV);95%% C.L. #sigma(pp#rightarrow AH #rightarrow#chi#chi#gamma#gamma ) (%s)" % unit]]   
     commonStyle = [[self.scaleByXsec,coup]]+basicStyle
     
     expected = ROOT.TGraph(expected68)
     style_utils.apply( expected, [["colors",ROOT.kBlack],["SetLineStyle",7],["SetName","expected_%s"%coup]])        
     style_utils.apply( observed, [["SetName","observed_%s"%coup]]+observedStyle)
     
     canv  = ROOT.TCanvas("limits_2HDM_mA%s%s%s"%(options.mDM,options.model,options.addName),"limits_2HDM_mA%s%s%s"%(options.mDM,options.model,options.addName))

     expected95.Draw("AE3")
     expected95.GetXaxis().SetRangeUser(600,4000)            
     expected68.Draw("E3L")
     expected.Draw("L")       
            
     observed.Draw("L")

     if coup in self.xsections_:
        grav = self.xsections_[coup]
        style_utils.apply( grav, basicStyle+[["SetLineStyle",9],["colors",ROOT.myColorB2]] )
        grav.Draw("L")
        legend.AddEntry(grav,"G_{RS}#rightarrow#gamma#gamma (LO)","l").SetLineStyle(0)
            
            
     canv.SaveAs("%slimits_%s_m%s%s.png"%(options.outdir,options.model,options.mDM,options.addName))       
