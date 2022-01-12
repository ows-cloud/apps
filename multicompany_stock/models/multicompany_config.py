from odoo import models
import logging

_logger = logging.getLogger(__name__)
SYSTEM_COMPANY = 1
ADMIN_USER = 2

class MulticompanyConfig(models.AbstractModel):
    _inherit = 'multicompany.config'




    # stock.location COMPANY_READ_SYSTEM_MODEL ?????????????????
    #
    # Endre ORM _check_company to accept company_id 1 instead of False ??? Or company_id 0 ?????

    # Shared records in company_id 0 ?
    # - ir.rule domains: does 0 equal False?
    # - citus sharding: is 0 an acceptable value in sharding column?
    # - inconsistencies check: False or 0 or company_id




    def _configure_stock(self, companies):
        for company in companies:
            self = self._prepare(company)
            # --------------------------------------------------
            self._stock_not_implemented_yet(company)
            # --------------------------------------------------

    def _stock_not_implemented_yet(self, company):
        # Create warehouse
        # Create missing locations
        # Set partner locations with ir.property for customer and supplier
        # <function model="res.company" name="create_missing_transit_location"/>
        # ok <function model="res.company" name="create_missing_warehouse"/>
        # <function model="res.company" name="create_missing_inventory_loss_location"/>
        # <function model="res.company" name="create_missing_production_location"/>
        # <function model="res.company" name="create_missing_scrap_location"/>
        # <function model="res.company" name="create_missing_scrap_sequence"/>
        warehouse = self._insert_first_record(
            model='stock.warehouse',
            search=[('company_id', '=', company.id)],
            values={
                'name': company.name,
                'code': self.env.context.get('default_code') or company.name[:5],
                'company_id': company.id,
                'partner_id': company.partner_id.id,
            },
        )
        # Create Partner Locations if not accessible or if company_id not False
        def check_location(location):
            