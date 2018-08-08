import argparse
import boto3.ec2
access_key = ''
secret_key = ''

# 
# Application to list all running EC2 instances in all regions
#
# usage: ec2list.py <access key> <secret key>
#
 
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('access_key', help='Access Key');
    parser.add_argument('secret_key', help='Secret Key');

    args = parser.parse_args()
    access_key = args.access_key
    secret_key = args.secret_key

    client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                                  region_name='us-east-1')

    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                              region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state["Name"] == "running":
                print (instance.id, instance.instance_type, region)



if  __name__ =='__main__':main()
