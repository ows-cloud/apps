# from openupgradelib import openupgrade


# @openupgrade.migrate()
# def migrate(env, version):
#     cr = env.cr
#     try:
#         openupgrade.rename_models(
#             cr,
#             [
#                 ("l10n_no_payroll.amelding", "l10n.no.amelding"),
#                 ("l10n_no_payroll.amelding.wizard", "l10n.no.amelding.wizard"),
#                 ("l10n_no_payroll.tabelltrekk", "l10n.no.tabelltrekk"),
#             ]
#         )
#     except Exception:
#         pass
