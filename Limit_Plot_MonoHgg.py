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
          
          

        
