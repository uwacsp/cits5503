import os
from argparse import ArgumentParser, ArgumentError
from contextlib import ExitStack

import boto3
from botocore.exceptions import ClientError


def create_security_group(name, description, **kwargs):
    """
    Create a security group
    :param name: Name of the security group
    :param description: Description for the security group
    :return: The created Security Group
    """
    sg = ec2.create_security_group(
        Description=description,
        GroupName=name,
        **kwargs
    )

    # Add the cleanup for the security group when it's created
    def clean_security_group():
        print("Deleting Security Group %s (%s)..." % (sg.group_name, sg.id))
        sg.delete()
        print("Deleted.")

    CLEANUP.callback(clean_security_group)
    # Always print out the created resources so if the program doesn't clean up you can manually do so
    print("Created security group %s (%s)" % (sg.group_name, sg.id))
    return sg


def create_instance(security_group, name, wait=True, **kwargs):
    """
    Create an ec2 instance
    :param security_group: Security Group that the instance belongs to
    :param name: Name to tag the group with
    :param wait: If cleanup should wait for termination
    :return: The created Instance
    """
    inst = ec2.create_instances(
        ImageId='ami-d38a4ab1',  # Replace this with the image you want to use
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        # Placement={'AvailabilityZone': zone}, # If you want to use a specific zone
        SecurityGroupIds=[security_group.id],
        InstanceInitiatedShutdownBehavior='terminate',
        **kwargs
    )[0]

    # Add the cleanup for the instance when it's created
    def clean_instance():
        print("Terminating Instance %s (%s)..." % (name, inst.id))
        inst.terminate()
        # This blocks till the instance is terminated
        if wait:
            inst.wait_until_terminated()
            print("Terminated")
            # The performance could be improved by requesting termination of all instances at once
            # Take a look in the main part of this program for how

    CLEANUP.callback(clean_instance)

    # Label the instance
    inst.create_tags(Tags=[{'Key': 'Name', 'Value': name}])

    # Wait for instance to start
    if wait:
        inst.wait_until_running()
    # Print out the instances created
    print("Created Instance %s (%s)" % (name, inst.id))
    return inst


if __name__ == '__main__':
    # Process args
    # This allows you to make your submission modular, this would be useful for labs like the cloudstorage lab
    args = ArgumentParser(description="Workshop X: Run a bunch of ec2 instances to download pictures of cats and dogs")

    args.add_argument("-sn", "--student-number", type=str,
                      help="Student Number (overrides the STUDENT_NUMBER env variable)")


    def integer_at_least_one(param: str) -> int:
        val = int(param)
        if val < 1:
            raise ArgumentError(param, "Number of instances should be at least 1")
        return val


    args.add_argument("-ni", "--num-instances", type=integer_at_least_one, default="5",
                      help="Number of instances [0, max_instances]")

    args = vars(args.parse_args())

    # Constants
    STUDENT_NUMBER = args["student_number"]
    if STUDENT_NUMBER is None:
        # Attempt to get it from environment variable if it is not set
        STUDENT_NUMBER = os.getenv('STUDENT_NUMBER')
    if STUDENT_NUMBER is None:
        print("WARNING: Student Number env/arg is not set!")
        STUDENT_NUMBER = '00000000'
    print("Using Student Number: " + STUDENT_NUMBER)

    RESOURCE_PREFIX = STUDENT_NUMBER + "-wX"  # Used to identify your resources

    NUM_INSTANCES = args["num_instances"]

    # Clean up stack with deferred cleanup methods
    # Main code is in a try so that cleanup can be done when something goes wrong
    with ExitStack() as CLEANUP:
        # Init
        ec2c = boto3.client('ec2')
        ec2 = boto3.resource('ec2')  # Try to use the higher level resource API wherever possible

        # Here could make sure the current region supports running the project
        # e.g. max_instance limit, at least two active regions, etc

        # Create Security Group
        sg = create_security_group(RESOURCE_PREFIX + "-sg", "Security Group for workshop X")

        # Set up the security group properties here...

        # Bulk wait for instances to terminate
        INSTANCES_CREATED = []


        def wait_for_all_instances_to_terminate():
            print("Waiting for instances to terminate...")
            for inst in INSTANCES_CREATED:
                inst.wait_until_terminated()
            print("All instances terminated.")


        CLEANUP.callback(wait_for_all_instances_to_terminate)

        # Create Instances
        for i in range(0, NUM_INSTANCES):
            inst = create_instance(sg, RESOURCE_PREFIX + "_" + str(i), wait=False)
            INSTANCES_CREATED.append(inst)

        # Do stuff that doesn't require instances to be running here...

        # When the instances need to be used, wait for them to be fully running
        print("Waiting for instances run...")
        for inst in INSTANCES_CREATED:
            inst.wait_until_running()
        print("All instances running.")

        # Make use of the running instances here...

        input("Press Enter when done to clean up...")

        print("Cleaning Up...")

    print("Done!")
