import FWCore.ParameterSet.Config as cms

process = cms.Process("AMPT")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.Generator_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(500000))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

# process.source = cms.Source("PoolSource",
# 		fileNames = cms.untracked.vstring('file:output.root','),
# 		secondaryFileNames = cms.untracked.vstring()
# 		)
# process.source = cms.Source("PoolSource",
# 		fileNames = cms.untracked.vstring('/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0000/amptDefault_cfi_py_GEN_1.root'),
# 		)
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring( *(
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_1.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_10.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_100.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_101.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_102.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_103.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_104.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_105.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_106.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_107.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_108.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_109.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_11.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_110.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_111.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_112.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_113.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_114.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_115.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_116.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_117.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_118.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_119.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_12.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_120.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_121.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_122.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_123.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_124.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_125.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_126.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_127.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_128.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_129.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_13.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_130.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_131.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_132.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_133.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_134.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_135.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_136.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_137.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_138.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_139.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_14.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_140.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_141.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_142.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_143.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_144.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_145.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_146.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_147.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_148.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_149.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_15.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_150.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_151.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_152.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_153.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_154.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_155.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_156.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_157.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_158.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_159.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_16.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_160.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_161.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_162.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_163.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_164.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_165.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_166.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_167.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_168.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_169.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_17.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_170.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_171.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_172.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_173.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_174.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_175.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_176.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_177.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_178.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_179.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_18.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_180.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_181.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_182.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_183.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_184.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_185.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_186.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_187.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_188.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_189.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_19.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_190.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_191.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_192.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_193.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_194.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_195.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_196.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_197.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_198.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_199.root'
                ) )
        )

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string('ampt.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('ana')
    )
)


process.QWEvent = cms.EDProducer("QWGenEventProducer",
		trackSrc  = cms.untracked.InputTag("genParticles"),
		isPrompt  = cms.untracked.bool(False),
		Etamin = cms.untracked.double(-5.0),
		Etamax = cms.untracked.double(5.0),
		ptMin = cms.untracked.double(0.3),
		ptMax = cms.untracked.double(12.0),
		)

process.QWHepMC = cms.EDProducer('QWHepMCProducer',
		src = cms.untracked.InputTag('generator')
		)

process.QWTreeMaker = cms.EDAnalyzer('QWTreeMaker',
		src = cms.untracked.InputTag('QWEvent'),
		vTag = cms.untracked.vstring('phi', 'eta', 'pt', 'charge')
		)

process.QWHepMCMaker = cms.EDAnalyzer('QWDTreeMaker',
		src = cms.untracked.InputTag('QWHepMC'),
		vTag = cms.untracked.vstring('b', 'EP', 'Npart', 'Ncoll')
		)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('AMPTsample_batch1_00.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
