import FWCore.ParameterSet.Config as cms

process = cms.Process('v1SIM');

# import standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
# process.load('Configuration.StandardSequences.Reconstruction_cff')
# process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.Generator_cff')


# set number of events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

from GeneratorInterface.AMPTInterface.amptDefaultParameters_cff import *
amptStringMelting = amptDefaultParameters.clone()
amptStringMelting.amptmode = cms.int32(4)

# AMPT input parameters
process.generator = cms.EDFilter("AMPTGeneratorFilter",
                                 amptStringMelting,
                                 firstEvent = cms.untracked.uint32(1),
                                 firstRun = cms.untracked.uint32(1),

                                 comEnergy = cms.double(5020.0),
                                 frame = cms.string('CMS'),
                                 proj = cms.string('A'),
                                 targ = cms.string('A'),
                                 iap = cms.int32(208),
                                 izp = cms.int32(82),
                                 iat = cms.int32(208),
                                 izt = cms.int32(82),
                                 bMin = cms.double(0),
                                 bMax = cms.double(30)
                                 )

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1$'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/GeneratorInterface/AMPTInterface/python/amptDefault_cfi.py,v $'),
    annotation = cms.untracked.string('AMPT XeXe 5442 GeV Minimum Bias')
)

# output definition
process.RAWSIMountput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string('output.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# analyzer goes here
#process.WMAna = cms.EDAnalyzer("WMv1")



process.pgen = cms.Sequence(process.generator + cms.SequencePlaceholder("randomEngineStateProducer") + process.GeneInfo)
# process.pgen = cms.Sequence(cms.SequencePlaceholder("randomEngineStateProducer")+process.GeneInfo + process.WMAna)

from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()

process.generation_step = cms.Path(process.pgen)
process.RAWSIMountput_step = cms.EndPath(process.RAWSIMountput)

process.schedule = cms.Schedule(process.generation_step, process.RAWSIMountput_step)

#for path in process.paths:
#    getattr(process,path)._seq = process.generator * getattr(process,path._seq)
