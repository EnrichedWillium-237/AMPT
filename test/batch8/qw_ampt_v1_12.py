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
                 '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4800.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4801.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4802.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4803.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4804.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4805.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4806.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4807.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4808.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4809.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4810.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4811.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4812.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4813.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4814.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4815.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4816.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4817.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4818.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4819.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4820.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4821.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4822.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4823.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4824.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4825.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4826.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4828.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4829.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4830.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4831.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4832.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4833.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4834.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4835.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4836.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4837.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4838.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4839.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4840.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4841.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4842.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4843.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4844.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4845.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4846.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4847.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4848.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4849.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4850.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4851.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4852.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4853.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4854.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4855.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4856.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4857.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4858.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4859.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4860.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4861.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4862.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4863.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4864.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4865.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4866.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4867.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4868.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4869.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4870.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4871.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4872.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4873.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4874.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4875.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4876.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4877.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4878.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4879.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4880.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4881.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4882.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4883.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4884.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4885.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4886.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4887.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4888.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4889.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4890.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4891.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4892.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4893.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4894.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4895.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4896.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4897.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4898.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4899.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4900.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4901.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4902.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4903.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4904.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4905.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4906.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4907.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4908.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4909.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4910.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4911.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4912.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4913.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4914.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4915.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4916.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4917.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4918.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4919.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4920.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4921.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4922.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4923.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4924.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4925.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4926.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4927.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4928.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4929.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4930.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4931.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4932.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4933.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4934.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4935.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4936.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4937.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4938.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4939.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4940.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4941.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4942.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4943.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4944.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4945.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4946.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4947.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4948.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4949.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4950.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4951.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4953.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4954.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4955.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4956.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4957.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4959.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4960.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4961.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4962.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4963.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4964.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4965.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4966.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4967.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4968.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4969.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4970.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4973.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4974.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4975.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4976.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4977.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4978.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4979.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4981.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4982.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4983.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4984.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4985.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4986.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4987.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4988.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4989.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4990.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4991.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4992.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4993.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4994.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4995.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4996.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4997.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4998.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0004/amptDefault_cfi_py_GEN_4999.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch8/160320_125912/0005/amptDefault_cfi_py_GEN_5000.root'
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
    fileName = cms.string('AMPTsample_12.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
