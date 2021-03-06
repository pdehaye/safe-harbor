from collections import namedtuple
from industry_sectors import industry_sectors

all_properties = [ #'CertificationStatus',
                   'Content1',
                   'Content2',
                   'Content3',
                   'Content4',
                   'Content4_1',
                   'Content5_1',
                   'Content5_10',
                   'Content5_11',
                   'Content5_12',
                   'Content5_13',
                   'Content5_2',
                   'Content5_4',
                   'Content5_5',
                   'Content5_6',
                   'Content5_7',
                   'Content5_8',
                   'Content5_9',
                   'Fax',
                   'Label1',
                   'OrgName',
                   'PPLoc',
                   'Phone',
                   'activities',
                   'address',
                   'city',
                   'contactemail',
                   'contactemail1',
                   'contactfax',
                   'contactfax1',
                   'contactname',
                   'contactname1',
                   'contactoff',
                   'contactoff1',
                   'contactphone',
                   'contactphone1',
                   'contacttitle1',
                   'corpoffemail',
                   'corpoffemail1',
                   'corpofffax',
                   'corpofffax1',
                   'corpoffname',
                   'corpoffname1',
                   'corpoffphone',
                   'corpoffphone1',
                   'corpofftitle1',
                   'eucountries',
                   'euprotection',
                   'hrdata',
                   'asp_index',
                   'industrysector',
                   'nextcertification',
                   'orgverification',
                   'personaldata',
                   'ppdate',
                   'privacyprograms',
                   'recoursemech',
                   'signup',
                   'signupdate',
                   'state',
                   'statutorybody',
                   'zip',
		   'CertifiedThroughLabel'
                   ]


# The true corp_properties, which excludes purely HTML tags from above, and introduces the new key: 'asp_index'

corp_properties = ['asp_index',
                   #####
                   'OrgName',
                   #'CertificationStatus',
                   'industrysector',
                   'PPLoc',
                   'privacyprograms',
                   'recoursemech',
                   'activities',
                   'address',
                   'city',
                   'state',
                   'zip',
                   'Phone',
                   'Fax',
                   'contactname1',
                   'contacttitle1',
                   'contactoff1',
                   'contactemail1',
                   'contactfax1',
                   'contactphone1',
                   'corpoffname1',
                   'corpofftitle1',
                   'corpoffemail1',
                   'corpofffax1',
                   'corpoffphone1',
                   'eucountries',
                   'euprotection',
                   'hrdata',
                   'orgverification',
                   'nextcertification',
                   'personaldata',
                   'ppdate',
                   'signupdate',
                   'statutorybody',
                   'CertifiedThroughLabel'
]

corp_properties_set = set(corp_properties)

