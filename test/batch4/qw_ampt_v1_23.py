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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4600.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4601.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4602.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4603.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4604.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4605.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4606.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4607.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4608.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4609.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4610.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4611.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4612.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4613.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4614.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4615.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4616.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4617.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4618.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4619.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4620.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4621.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4622.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4623.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4624.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4625.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4626.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4627.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4628.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4629.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4630.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4631.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4632.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4633.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4634.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4636.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4637.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4638.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4639.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4640.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4641.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4642.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4643.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4644.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4645.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4646.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4647.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4648.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4649.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4650.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4651.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4652.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4653.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4654.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4655.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4656.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4657.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4658.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4659.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4660.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4661.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4662.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4663.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4664.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4665.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4666.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4667.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4668.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4669.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4671.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4672.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4674.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4675.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4676.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4678.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4679.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4680.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4681.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4682.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4683.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4684.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4685.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4686.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4687.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4688.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4689.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4690.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4691.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4692.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4693.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4694.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4695.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4696.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4697.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4698.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4699.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4700.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4701.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4702.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4703.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4705.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4706.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4707.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4708.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4709.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4710.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4711.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4712.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4713.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4714.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4715.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4716.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4717.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4718.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4719.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4720.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4721.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4722.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4723.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4724.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4725.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4726.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4727.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4728.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4729.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4730.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4732.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4733.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4734.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4735.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4736.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4737.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4738.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4739.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4740.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4741.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4742.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4743.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4744.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4745.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4746.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4747.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4748.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4749.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4750.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4751.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4752.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4753.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4754.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4755.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4756.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4757.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4758.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4759.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4760.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4761.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4762.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4764.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4765.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4766.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4767.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4768.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4769.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4770.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4771.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4772.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4773.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4774.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4775.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4776.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4777.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4778.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4779.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4780.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4781.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4782.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4783.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4784.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4785.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4786.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4787.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4788.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4789.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4790.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4791.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4792.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4793.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4794.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4795.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4796.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4797.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4798.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0004/amptDefault_cfi_py_GEN_4799.root'
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
    fileName = cms.string('AMPTsample_batch4_23_v3.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
