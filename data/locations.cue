package regioncodes

//// Data Inputs ////

_countries: #Countries & {
	de: name: "Germany"
	us: name: "United States"
	uk: name: "United Kingdom"
	ie: name: "Ireland"
	nl: name: "Netherlands"
}

_locations: #Locations & {
	fra: {
		name:    "Frankfurt"
		country: "de"
	}
	dub: {
		name:    "Dublin"
		country: "ie"
	}
	eem: {
		name:    "Eemshaven"
		country: "nl"
	}
	fsn: {
		name:    "Falkenstein"
		country: "de"
	}
}
