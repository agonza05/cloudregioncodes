package regioncodes

//// Data Inputs ////

cloudProviders: #CloudProviders & {
	gcp: name: "Google Cloud Platform"
	azr: name: "Microsoft Azure"
	aws: name: "Amazon Web Services"
	// htz: name: "Hetzner"
}

regionsByLocation: #RegionsByLocation & {
	fra: {
		aws: {displayName: "Europe Central (Frankfurt)", name: "eu-central-1"}
		gcp: {displayName: "Frankfurt", name: "europe-west3"}
		azr: {displayName: "Germany West Central (Frankfurt)", name: "germanywestcentral"}
	}
	dub: {
		aws: {displayName: "Europe West (Ireland)", name: "eu-west-1"}
		azr: {displayName: "North Europe (Dublin)", name: "northeurope"}
	}
}
