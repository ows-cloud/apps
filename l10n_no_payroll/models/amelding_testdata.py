# TEST ALLE NOEDVENDIGE LOENNSARTER: fastloenn, timeloenn, km, telefon, pensjon(aga), sykepenger(aga), feriepenger forrige aar, feriepenger dette aar
# hr_professional hr.employee: tax_table, tax_percent
# ag_4_professional: new company implement HR: base.key.value.field
    
    
    

testdata = {
    'l10n_no_payroll.amelding': {
        'leveringstidspunkt': '2008-09-29 03:49:45',
        'kalendermaaned': '2018-01',
        'company_id': ('res.company',0),
        'meldingsId': '2',
        'erstatterMeldingsId': False,
    },
    'res.company': [{
        'id': 0,
        'l10n_no_Grunnlagsprosent': '14.1',
        'vat': 'NO959984352',
        'l10n_no_virksomhet': '974302683',
        'l10n_no_Spraak': 'bokmaal',
        'l10n_no_BeregningskodeForArbeidsgiveravgift': 'generelleNaeringer',
        'l10n_no_Arbeidsgiveravgiftsone': '1',
    }],
    'hr.employee': [
        {
            'id': 0,
            'name': 'HENRIK NORLIN',
            'contract_ids': [('hr.contract',0)],
            'birthday': '1983-07-20',
        },
        # {
        #     'id': 1,
        #     'name': 'ALEXANDER FRIDRIKSSON',
        #     'contract_ids': [('hr.contract',1),('hr.contract',3)],
        # },
    ],
    'hr.contract': [
        {
            'id': 0,
            'date_start': '2010-01-01',
            #'date_end': False,
            'l10n_no_Arbeidsforholdtype': 'ordinaertArbeidsforhold',
            'l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer': 37.5,
            'l10n_no_Arbeidstidsordning': 'ikkeSkift',
        },
    ],
    'hr.payslip': [
        {
            'id': 0,
            'employee_id': ('hr.employee',0),
        },
    ],
    'hr.payslip.line': [
        {
            'id': 0,
            'slip_id': ('hr.payslip',0),
            'salary_rule_id': ('hr.salary.rule',0),
            'total': 5000.0,
        },
        {
            'id': 1,
            'slip_id': ('hr.payslip', 0),
            'salary_rule_id': ('hr.salary.rule', 1),
            'total': 1000.0,
        },
        {
            'id': 2,
            'slip_id': ('hr.payslip', 0),
            'salary_rule_id': ('hr.salary.rule', 2),
            'total': 500.0,
        },
        {
            'id': 3,
            'slip_id': ('hr.payslip', 0),
            'salary_rule_id': ('hr.salary.rule', 3),
            'total': -2000.0,
        },
        {
            'id': 4,
            'slip_id': ('hr.payslip', 0),
            'salary_rule_id': ('hr.salary.rule', 4),
            'total': -900.0,
        },
    ],
    'hr.salary.rule': [
        {
            'id': 0,
            'l10n_no_RegelType': 'loennsinntekt',
            'l10n_no_Fordel': 'kontantytelse',
            'l10n_no_Loennsbeskrivelse': 'fastloenn',
            'l10n_no_BeregnAga': 'loennOgGodtgjoerelse',
            'l10n_no_BeregnTrekk': 'tabelltrekk',
            'l10n_no_SkatteOgAvgiftsregel': 'skattefriOrganisasjon',
        },
        {
            # IKKE LOENN!
            'id': 1,
            'l10n_no_RegelType': 'loennsinntekt',
            'l10n_no_Fordel': 'naturalytelse',
            'l10n_no_Loennsbeskrivelse': 'annet',
            'l10n_no_BeregnAga': 'tilskuddOgPremieTilPensjon',
            'l10n_no_BeregnTrekk': False,
        },
        {
            'id': 2,
            'l10n_no_RegelType': 'loennsinntekt',
            'l10n_no_Fordel': 'utgiftsgodtgjoerelse',
            'l10n_no_Loennsbeskrivelse': 'kilometergodtgjoerelseBil',
        },
        {
            # IKKE LOENN!
            'id': 3,
            'l10n_no_RegelType': 'loennsinntekt',
            'l10n_no_Fordel': 'naturalytelse',
            'l10n_no_Loennsbeskrivelse': 'kilometergodtgjoerelseBil',
            'l10n_no_BeregnAga': 'fradragIGrunnlagetForSone',
            'l10n_no_BeregnTrekk': False,
        },
        {
            'id': 4,
            'l10n_no_RegelType': 'forskuddstrekk',
        },
    ],
    'ir.model.data': [],
    'res.field.value': [
        {'TEST': 'TRUE',}
    ],
    'res.field.selection_value': [
        {'TEST': 'TRUE', }
    ],
    'res.country': [
        {
            'id': 0,
            'code': 'NO',
        },
    ],
    'hr.job': [
        {
            'name': 'Assistent',
            'l10n_no_profession_code': '1234567',
        }
    ]
}
