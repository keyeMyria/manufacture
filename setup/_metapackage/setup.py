import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-manufacture",
    description="Meta package for oca-manufacture Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-mrp_auto_assign',
        'odoo10-addon-mrp_bom_location',
        'odoo10-addon-mrp_bom_note',
        'odoo10-addon-mrp_mto_with_stock',
        'odoo10-addon-mrp_production_note',
        'odoo10-addon-mrp_production_request',
        'odoo10-addon-mrp_progress_button',
        'odoo10-addon-mrp_repair_calendar_view',
        'odoo10-addon-mrp_repair_discount',
        'odoo10-addon-product_quick_bom',
        'odoo10-addon-quality_control',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)