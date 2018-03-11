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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_8.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_80.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_800.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_801.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_802.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_803.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_804.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_805.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_806.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_809.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_81.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_810.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_811.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_812.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_813.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_815.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_818.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_82.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_820.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_822.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_823.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_825.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_826.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_827.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_828.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_829.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_830.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_831.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_832.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_833.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_834.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_836.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_838.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_84.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_840.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_842.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_843.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_844.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_845.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_846.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_847.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_848.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_849.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_85.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_850.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_852.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_853.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_854.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_855.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_857.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_858.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_86.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_860.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_862.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_863.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_865.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_866.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_867.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_868.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_869.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_87.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_871.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_872.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_873.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_874.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_876.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_878.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_879.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_880.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_881.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_882.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_883.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_885.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_886.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_887.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_888.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_889.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_89.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_891.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_892.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_893.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_894.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_895.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_896.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_897.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_898.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_899.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_9.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_90.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_900.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_901.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_902.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_903.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_904.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_905.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_906.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_907.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_908.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_909.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_91.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_910.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_911.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_912.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_913.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_914.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_915.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_916.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_917.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_918.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_919.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_92.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_920.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_921.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_922.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_923.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_924.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_925.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_926.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_927.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_928.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_929.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_93.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_930.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_931.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_932.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_933.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_934.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_935.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_936.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_937.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_938.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_939.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_94.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_940.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_941.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_942.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_943.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_944.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_945.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_946.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_947.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_948.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_949.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_95.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_950.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_951.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_952.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_953.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_954.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_955.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_956.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_957.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_958.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_959.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_96.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_960.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_961.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_962.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_963.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_964.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_965.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_966.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_967.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_968.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_969.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_97.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_970.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_971.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_972.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_973.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_974.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_975.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_976.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_977.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_978.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_979.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_98.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_980.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_981.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_982.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_983.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_984.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_985.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_986.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_987.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_988.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_989.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_99.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_990.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_991.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_992.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_993.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_994.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_995.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_996.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_997.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_998.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0000/amptDefault_cfi_py_GEN_999.root'
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
    fileName = cms.string('AMPTsample_batch5_04_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
