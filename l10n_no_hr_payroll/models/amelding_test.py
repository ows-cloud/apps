import amelding_logic
from amelding_testdata import testdata
import pyxb
pyxb.RequireValidWhenGenerating(True)


logic = amelding_logic.AmeldingLogikk(testdata['l10n_no_hr_payroll.amelding'])
print(logic.melding_xml())