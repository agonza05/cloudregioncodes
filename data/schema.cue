package regioncodes

//// Schema ////

#ThreeLetterCode: =~"^[a-z]{3}$"

#TwoLetterCode: =~"^[a-z][a-z]$"

#Countries: [ID=#TwoLetterCode]: {
	name!:        string
	description?: string
	id:           ID
}

#Locations: [ID=#ThreeLetterCode]: {
	name!:       string
	countryCode: _countries[countryCode].id
	country:     _countries[countryCode].name
	id:          ID
}

#CloudProviders: [ID=#ThreeLetterCode]: {
	name!:        string
	description?: string
	id:           ID
}

#RegionCodes: [ID=string]: {
	name!:         string
	description?:  string
	cloudProvider: cloudProviders[cloudProvider].id
	location:      locations[location].id
	cloudRegion:   cloudRegions[location][cloudProvider]
	id:            ID
}

#CloudRegions: [or(_locationsObjectKeys)]: [or(_cloudProvidersObjectKeys)]: {
	displayName!: string
	name:         name
	id:           name
}

//// Data Computed ////

_cloudProvidersObjectKeys: [for k, v in cloudProviders {k}]
_locationsObjectKeys: [for k, v in locations {k}]
