package regioncodes

//// Schema ////
#ThreeLetterCode: =~"^[a-z][a-z][a-z]$"

#TwoLetterCode: =~"^[a-z][a-z]$"

#Countries: [ID=#TwoLetterCode]: {
	name!:        string
	description?: string
	id:           ID
}

#Locations: [ID=#ThreeLetterCode]: {
	name!:         string
	country_code!: or(_countriesObjectKeys)
	country:       _countries[country_code].name
	id:            ID
}

#CloudProviders: [ID=#ThreeLetterCode]: {
	name!:        string
	description?: string
	id:           ID
}

#RegionCodes: [ID=string]: {
	name!:               string
	cloudProvider!:      or(_cloudProvidersObjectKeys)
	location!:           or(_locationsObjectKeys)
	cloudProviderRegion: regionsByLocation[location][cloudProvider]
	description?:        string
	id:                  ID
}

#RegionsByLocation: [or(_locationsObjectKeys)]: [or(_cloudProvidersObjectKeys)]: #CloudProviderRegion

#CloudProviderRegion: {
	name!:        string
	displayName!: string
	id:           name
}

//// Data Computed ////

_cloudProvidersObjectKeys: [for k, v in cloudProviders {k}]

_countriesObjectKeys: [for k, v in _countries {k}]

_locationsObjectKeys: [for k, v in locations {k}]
