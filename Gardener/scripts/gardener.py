#!/usr/bin/env python

from LatinoAnalysis.Gardener.gardening         import gardener_cli
from LatinoAnalysis.Gardener.gardening         import ModuleManager,Pruner,Grafter,AliasGrafter,RootWeighter
from LatinoAnalysis.Gardener.pileup            import PUpper
#from LatinoAnalysis.Gardener.ww                import WWPruner, WWFlagsGrafter
#from LatinoAnalysis.Gardener.efficiencies      import EffLepFiller,EffTrgFiller

# new variables
from LatinoAnalysis.Gardener.variables.WW2jVar    import WW2jVarFiller


if __name__ == '__main__':

    print "gardener"
    
    modules = ModuleManager()
    modules['filter']           = Pruner()
    modules['adder']            = Grafter()
    modules['alias']            = AliasGrafter()
    modules['rootweighter']     = RootWeighter()
    #modules['wwfilter']         = WWPruner()
    #modules['wwflagger']        = WWFlagsGrafter()
    modules['puadder']          = PUpper()
    #modules['effwfiller']       = EffLepFiller()
    #modules['efftfiller']       = EffTrgFiller()

# new variables
    modules['ww2jvarfiller']    = WW2jVarFiller()



    gardener_cli( modules )