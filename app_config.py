from os import getenv

if (REGION_NAME := getenv("REGION_NAME")) is None:
    raise Exception("REGION_NAME is not set")

if (DYNAMODB_ENDPOINT := getenv("DYNAMODB_ENDPOINT")) is None:
    raise Exception("DYNAMODB_ENDPOINT it not set")

if (TABLE_NAME := getenv("TABLE_NAME")) is None:
    raise Exception("TABLE_NAME it not set")