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
                                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4400.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4401.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4402.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4403.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4404.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4406.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4407.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4408.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4409.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4410.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4411.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4412.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4413.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4415.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4416.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4417.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4418.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4419.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4420.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4421.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4422.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4423.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4424.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4425.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4426.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4427.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4429.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4430.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4431.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4432.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4433.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4434.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4435.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4436.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4437.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4438.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4439.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4440.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4441.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4442.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4443.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4444.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4445.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4446.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4447.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4448.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4449.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4450.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4451.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4452.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4453.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4454.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4455.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4456.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4457.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4458.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4459.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4460.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4461.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4462.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4463.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4464.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4465.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4466.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4467.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4468.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4469.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4470.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4471.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4472.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4473.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4474.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4475.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4476.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4477.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4478.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4479.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4480.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4481.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4482.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4483.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4484.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4485.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4488.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4489.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4490.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4491.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4492.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4493.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4494.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4495.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4496.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4497.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4498.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4499.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4501.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4502.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4503.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4504.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4505.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4506.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4507.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4508.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4509.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4510.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4511.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4512.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4513.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4514.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4515.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4516.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4517.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4518.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4519.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4520.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4521.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4522.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4523.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4524.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4525.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4526.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4527.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4528.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4529.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4530.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4531.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4532.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4533.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4534.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4535.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4536.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4537.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4538.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4539.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4540.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4541.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4542.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4543.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4544.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4545.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4546.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4547.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4548.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4549.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4550.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4551.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4552.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4553.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4554.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4555.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4556.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4557.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4559.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4560.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4561.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4562.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4563.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4564.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4565.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4566.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4567.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4568.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4569.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4570.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4571.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4572.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4573.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4574.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4575.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4576.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4577.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4578.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4579.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4580.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4581.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4582.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4583.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4584.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4585.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4586.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4587.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4588.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4589.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4590.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4591.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4592.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4593.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4594.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4595.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4596.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4597.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0004/amptDefault_cfi_py_GEN_4599.root'
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
    fileName = cms.string('AMPTsample_27.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
