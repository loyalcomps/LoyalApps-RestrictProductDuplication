# -*- coding: utf-8 -*-
#############################################################################
#
#    Loyal IT Solutions Pvt Ltd
#
#    Copyright (C) 2023-TODAY Loyal IT Solutions Pvt Ltd(<https://www.loyalitsolutions.com>).
#    Author: Loyal IT Solutions Pvt Ltd
#
#   The entire module or part of the module can be modified under the terms of the GNU AFFERO

#   GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#

#
#############################################################################


{
    'name':'Avoid Product Duplication',
    'author':'Loyal IT Solutions Pvt Ltd',
    'depends':['base','mail','sale_management'],
    'summary':"Avoid product name duplication | Avoid interal reference duplication | Restrict duplication of the product",
    'description': """Restrict duplication of the products with name or internal reference.""",
    'category':'sales',
    'company': 'Loyal IT Solutions Pvt Ltd',
    'maintainer': 'Loyal IT Solutions Pvt Ltd',
    'website': "https://loyalitsolutions.com",
    'license': 'AGPL-3',
    'version': '16.0.1.0.0',
    'data':[
        'security/ir.model.access.csv',
        'views/duplication_settings.xml',
    ],
    'images': ['static/description/banner.png'],
}
