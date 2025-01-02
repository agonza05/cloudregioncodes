package regioncodes

cloudProviders: #CloudProviders & {
	gcp: name: "Google Cloud Platform"
	azr: name: "Microsoft Azure"
	aws: name: "Amazon Web Services"
	oci: name: "Oracle Cloud Infrastructure"
}

regionsByLocation: #RegionsByLocation & {
	fra: {
		aws: {displayName: "Europe Central (Frankfurt)", name: "eu-central-1"}
		azr: {displayName: "Germany West Central (Frankfurt)", name: "germanywestcentral"}
		gcp: {displayName: "Frankfurt", name: "europe-west3"}
		oci: {displayName: "Germany Central (Frankfurt)", name: "eu-frankfurt-1"}
	}
	dub: {
		aws: {displayName: "Europe West (Ireland)", name: "eu-west-1"}
		azr: {displayName: "North Europe (Dublin)", name: "northeurope"}
	}
	hmx: {
		gcp: {displayName: "Finland", name: "europe-north1"}
	}
	osl: {
		azr: {displayName: "Norway East (Oslo)", name: "norwayeast"}
	}
	arn: {
		aws: {displayName: "Europe North (Stockholm)", name: "eu-north-1"}
		oci: {displayName: "Sweden Central (Stockholm)", name: "eu-stockholm-1"}
	}
	lon: {
		aws: {displayName: "Europe West (London)", name: "eu-west-2"}
		azr: {displayName: "UK South (London)", name: "uksouth"}
		gcp: {displayName: "London", name: "europe-west2"}
		oci: {displayName: "UK South (London)", name: "uk-london-1"}
	}
	syd: {
		aws: {displayName: "Asia Pacific (Sydney)", name: "ap-southeast-2"}
		azr: {displayName: "Australia East (Sydney)", name: "australiaeast"}
		gcp: {displayName: "Sydney", name: "australia-southeast1"}
		oci: {displayName: "Australia East (Sydney)", name: "ap-sydney-1"}
	}
}
