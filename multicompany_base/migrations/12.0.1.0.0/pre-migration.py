from openupgradelib import openupgrade

@openupgrade.migrate(use_env=True)
def migrate(env, version):

    openupgrade.update_module_names(
        env.cr,
        [
            ('company_security', 'multicompany_base'),
            ('company_languages', 'multicompany_language'),
            ('company_website', 'multicompany_website_mail'),
            ('hr_payroll_account_analytic', 'payroll_account_analytic'),
            ('hr_payroll_new_fields', 'payroll_new_fields'),
            ('l10n_no_hr_payroll', 'l10n_no_payroll'),
            ('mail_template_replace', 'multicompany_mail'),
        ],
    )
    openupgrade.rename_xmlids(
        env.cr,
        [
            ('multicompany_base.user_support', 'multicompany_base.support_user'),
            # ('', ''),
        ]
    )
