.. code-block:: python

    # https://github.com/nimarosa/server-tools/tree/14.0-add-base_time_dependent_parameter

    tax_rate = float(company.get_time_dependent_parameter('tax_high_rate', tax_date))

    result = price_unit * tax_rate
