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
    input = cms.untracked.int32(20)
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

# AMPT input parameters
process.generator = cms.EDFilter("AMPTGeneratorFilter",
                                 diquarky = cms.double(0.0),
                                 diquarkx = cms.double(0.0),
                                 diquarkpx = cms.double(7.0),
                                 ntmax = cms.int32(150),
                                 dpcoal = cms.double(1000000.0),
                                 diquarkembedding = cms.int32(0),
                                 maxmiss = cms.int32(1000),
                                 ktkick = cms.int32(1),
                                 mu = cms.double(2.265),
                                 quenchingpar = cms.double(2.0),
                                 popcornpar = cms.double(1.0),
                                 drcoal = cms.double(1000000.0),
                                 amptmode = cms.int32(4),
                                 izpc = cms.int32(0),
                                 popcornmode = cms.bool(True),
                                 minijetpt = cms.double(-7.0),
                                 ks0decay = cms.bool(False),
                                 alpha = cms.double(0.33),
                                 dt = cms.double(0.2),
                                 rotateEventPlane = cms.bool(True),
                                 shadowingmode = cms.bool(True),
                                 diquarkpy = cms.double(0.0),
                                 deuteronfactor = cms.int32(0),
                                 stringFragB = cms.double(0.9), #default value in Hijing. Good for pA
                                 quenchingmode = cms.bool(False),
                                 stringFragA = cms.double(0.15),
                                 deuteronmode = cms.int32(0),
                                 doInitialAndFinalRadiation = cms.int32(3),
                                 phidecay = cms.bool(True),
                                 deuteronxsec = cms.int32(1),
                                 pthard = cms.double(2.0),
                                 firstRun = cms.untracked.uint32(1),
                                 frame = cms.string('CMS'),
                                 targ = cms.string('A'),
                                 izp = cms.int32(82),
                                 bMin = cms.double(0),
                                 firstEvent = cms.untracked.uint32(1),
                                 izt = cms.int32(82),
                                 proj = cms.string('A'),
                                 comEnergy = cms.double(5020.0),
                                 iat = cms.int32(208),
                                 bMax = cms.double(30),
                                 iap = cms.int32(208)
                                 )

# output definition
process.RAWSIMountput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string('testoutput.root'),
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
