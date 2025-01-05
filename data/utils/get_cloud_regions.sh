#!/usr/bin/env bash

DATA_DIR="./data"

DATA_URL="https://www.cloudinfrastructuremap.com/api/service/cloud-regions.js"

http $DATA_URL | jq -r > $DATA_DIR/regions.json
cue import -f -l cloudRegions: $DATA_DIR/regions.json
rm -rf $DATA_DIR/regions.json

# Azure regions
az account list-locations > $DATA_DIR/azure.json
cue import -f -l azureRegions: $DATA_DIR/azure.json
rm -rf $DATA_DIR/azure.json

# AWS regions
touch $DATA_DIR/aws.toml
aws ssm get-parameters-by-path --path /aws/service/global-infrastructure/services/ec2/regions --output json | jq -r '.Parameters[].Value' > $DATA_DIR/aws.list
for ITEM in $(cat data/aws.list)
do
    DISPLAY_NAME=$(aws ssm get-parameter --name /aws/service/global-infrastructure/regions/$ITEM/longName --output json | jq '.Parameter.Value')
    echo "$ITEM=$DISPLAY_NAME" >> $DATA_DIR/aws.toml
done
cue import -f -l awsRegions: $DATA_DIR/aws.toml
rm -rf $DATA_DIR/aws.toml $DATA_DIR/aws.list
