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
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_4.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_40.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_400.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_401.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_402.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_403.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_404.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_405.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_406.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_407.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_408.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_409.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_41.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_410.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_411.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_412.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_413.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_414.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_415.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_416.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_417.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_418.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_419.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_42.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_420.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_421.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_422.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_423.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_424.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_425.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_426.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_427.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_428.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_429.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_43.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_430.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_431.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_432.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_434.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_435.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_436.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_437.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_438.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_439.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_44.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_440.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_441.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_442.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_443.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_444.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_445.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_446.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_447.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_448.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_449.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_45.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_450.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_451.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_452.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_453.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_454.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_455.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_456.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_457.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_458.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_459.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_46.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_460.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_461.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_462.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_463.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_464.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_465.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_466.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_467.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_468.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_469.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_470.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_472.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_473.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_475.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_476.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_477.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_478.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_479.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_48.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_480.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_481.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_482.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_483.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_484.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_485.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_486.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_487.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_488.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_489.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_49.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_490.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_491.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_492.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_493.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_494.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_495.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_496.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_497.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_498.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_499.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_5.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_50.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_500.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_501.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_502.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_503.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_504.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_505.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_506.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_507.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_508.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_509.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_51.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_510.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_511.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_512.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_513.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_514.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_515.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_516.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_517.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_518.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_519.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_52.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_520.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_521.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_522.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_523.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_524.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_525.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_526.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_527.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_529.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_53.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_530.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_531.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_532.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_533.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_534.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_535.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_536.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_537.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_538.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_539.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_54.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_540.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_541.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_542.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_543.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_544.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_545.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_546.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_547.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_549.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_55.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_550.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_551.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_553.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_554.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_555.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_556.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_557.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_558.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_559.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_56.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_560.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_561.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_562.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_563.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_564.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_565.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_566.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_567.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_568.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_569.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_57.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_570.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_571.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_572.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_573.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_574.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_575.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_576.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_577.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_578.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_579.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_58.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_580.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_581.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_582.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_583.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_584.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_585.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_586.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_587.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_588.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_589.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_590.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_591.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_592.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_593.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_594.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_595.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_596.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_597.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_598.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0000/amptDefault_cfi_py_GEN_599.root'
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
    fileName = cms.string('AMPTsample_batch1_02.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
