Safe Harbor filings with the Federal Trade Commission
=====================================================

This GIT repository contains a scrape of the database of companies on the Federal Trade Commission's Safe Harbor site, located at
https://safeharbor.export.gov/list.aspx

For more information about the Safe Harbor Privacy Principles regulating EU-US and CH-US data exchange, please consult [Wikipedia](http://en.wikipedia.org/wiki/International_Safe_Harbor_Privacy_Principles). Compliance with those principles is a pre-requirement for running a business in the European Union that collects personal data. Any European citizen, regardless of where they live, is supposed to be protected by those principles, as well as any resident of the EU or Switzerland. 

The FTC database includes filings by [Google](json/25007.json), [Facebook](json/23019.json), [Yahoo](json/25558.json), [Amazon](json/27379.json), genetic testing company [23andMe](json/25442.json), sharing economy accomodation provider [Airbnb](json/25671.json), sharing economy transportation provider [Uber](json/27411.json), data broker [Axciom](json/23039.json) or MOOC provider [Coursera](json/26126.json). 

The information here is mostly information self-reported by the companies. It is then  spot checked by the FTC, but the EU is not always pleased with the level of oversight applied by the FTC.

The FTC database rolls the entries by key number: when a certification is updated, its key number is changed and the previous one is deleted. 

*All entries are collected here, even obsolete ones,* while this information is simply overwritten on the FTC site. In this way, one can track how the submissions evolve with time, for instance how Uber [recently updated](json/27411.json) its [previous "business activities"](json/23009.json) 
 

 
The `json` folder contains all these entries. The format used is `json`, and should be easily parsable into just about any tool. 

The `data` folder also contains a file in `csv` format grouping the same information.this actually conforms to the *datapackage* specification as defined by the Open Knowledge Foundation. The different fields are defined in machine readable format in the file `datapackage.json`. 

For compatibility reasons, I have kept the same keys as in the original HTML, and added a few more:
 - `asp_index`: This is actually the only key I have added, and also gives the name to the file: `{asp_index}.json`. The FTC uses an ASP .NET database, hence the name. Several different files and keys could correspond to the same company. 
 - `OrgName`: The official name of the registrant. Sometimes an "Inc" will change to a "Corp", but both records still represent the same company. Sometimes many different closely related companies are registered separately (for instance, all the Disney companies)
 - `latest`: Indicates if this is the latest entry for this organisation. Matches are based on `OrgName`
 - `previous`: The asp_index of the previous entry for the same organisation, if any. Blank otherwise.
 - `CertificationStatus`: companies can let their certification lapse, but the Safe Harbor principles remain in force for data that was collected during their certification period
 - `industrysector`: big set of possibilities, with more than one possible. This is then harder to parse. Note that 'Leasing Services - (LES)' and  'Legal Services - (LES)' clash for the shorthand. Of interest: 'Advertising Services - (ADV)'
 - `PPLoc`: the location of the privacy policy, normally on the organisation website
 - `privacyprograms`: a bit of a mix, indicates whether the organisation declares compliance with additional privacy programs, such as TRUSTe, HIPAA, SOC2, PCI, CJIS, IAPP,...
 - `recoursemech`: the recourse mechanism for arbitration, for instance TRUSTe, ICDR/AAA, BBB,...
 - `activities`: long form description of business activities
 - `address`, `city`, `state`, `zip`, `Phone`, `Fax`: contact information for the company
 - `contactname1`, `contacttitle1`, `contactoff1`, `contactemail1`, `contactfax1`, `contactphone1`: contact person at the company
 - `corpoffname1`, `corpofftitle1`, `corpoffemail1`, `corpofffax1`, `corpoffphone1`: corporate officer in charge, and contact information 
 - `eucountries`: relevant EU countries (and CH)
 - `euprotection`:companies have the option of delegating some authority to the EU rather than the FTC
 - `hrdata`: used for HR data
 - `orgverification`: the organ in charge of verification of compliance. Note that this could be in-house.
 - `nextcertification`: when is next certification due 
 - `personaldata`: clarification of personal data collected (self-reported)
 - `ppdate`: date on the privacy policy
 - `signupdate`: sign up date to the Safe Harbor program
 - `statutorybody`: Federal Trade Commission, Department of Transportation, etc.
 - `eucountries_parsed`: A more computer-friendly version of the eucountries field, formatted as an array of ISO3166-1-Alpha-3, coming from `country-codes` datapackage
 - `industrysectors_parsed`: A more computer-friendly version of the industrysectors field, formatted as an array of sectors
