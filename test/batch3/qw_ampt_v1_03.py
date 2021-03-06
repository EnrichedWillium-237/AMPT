import FWCore.ParameterSet.Config as cms

process = cms.Process("AMPT")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.Generator_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100000))
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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_6.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_60.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_600.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_601.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_602.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_603.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_604.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_605.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_606.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_607.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_608.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_609.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_61.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_610.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_611.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_613.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_614.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_615.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_616.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_617.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_618.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_619.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_62.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_620.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_621.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_622.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_623.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_624.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_625.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_626.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_627.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_628.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_63.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_630.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_631.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_632.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_633.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_634.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_635.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_636.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_637.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_638.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_639.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_64.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_640.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_641.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_642.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_643.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_644.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_645.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_646.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_647.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_648.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_649.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_65.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_650.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_651.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_652.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_653.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_654.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_655.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_656.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_657.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_658.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_659.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_66.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_660.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_662.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_663.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_664.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_665.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_666.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_667.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_668.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_669.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_67.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_671.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_672.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_673.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_674.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_675.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_676.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_677.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_678.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_679.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_68.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_680.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_681.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_682.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_683.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_684.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_685.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_686.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_687.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_688.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_689.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_69.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_690.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_691.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_692.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_693.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_694.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_695.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_696.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_697.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_698.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_699.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_7.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_70.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_700.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_701.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_702.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_703.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_704.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_705.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_706.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_707.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_708.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_709.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_71.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_710.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_711.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_712.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_713.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_714.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_715.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_716.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_717.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_718.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_719.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_72.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_720.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_721.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_722.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_723.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_724.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_725.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_726.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_727.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_728.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_729.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_73.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_730.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_731.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_732.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_733.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_734.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_735.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_736.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_737.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_738.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_739.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_74.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_740.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_741.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_742.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_743.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_744.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_745.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_746.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_747.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_748.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_749.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_75.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_750.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_751.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_752.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_753.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_754.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_755.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_756.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_757.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_758.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_759.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_760.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_761.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_762.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_763.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_764.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_765.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_766.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_767.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_768.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_769.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_77.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_770.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_771.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_772.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_773.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_774.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_775.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_776.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_777.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_778.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_779.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_78.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_780.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_781.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_782.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_783.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_785.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_786.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_787.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_788.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_789.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_79.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_790.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_791.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_792.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_793.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_794.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_795.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_796.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_797.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_798.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_799.root'
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
    fileName = cms.string('AMPTsample_batch3_03_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
