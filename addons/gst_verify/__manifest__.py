# -*- coding: utf-8 -*-
{
    'name': "GST Number Validation",
    'summary': """Checks the GST Number and fetches company details""",
    'description': """
        Performs the following checks when GSTIN number is entered:
	    1. Length
        2. Format
        3. Checksum
        4. Use master's India api to fetch company details and populates the fields.
		It will give you a simple warning if it finds a wrong entry.
    """,
    'author': "Youngman India Pvt Ltd",
    'website': "http://youngman.co.in",
    'category': 'Uncategorized',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
}
