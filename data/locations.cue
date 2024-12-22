package regioncodes

//// Data Inputs ////

_countries: #Countries & {
	de: name: "Germany"
	us: name: "United States"
	uk: name: "United Kingdom"
	ie: name: "Ireland"
	nl: name: "Netherlands"
}

locations: #Locations & {
	fra: {
		name:         "Frankfurt"
		country_code: "de"
	}
	dub: {
		name:         "Dublin"
		country_code: "ie"
	}
	eem: {
		name:         "Eemshaven"
		country_code: "nl"
	}
	fsn: {
		name:         "Falkenstein"
		country_code: "de"
	}
}
