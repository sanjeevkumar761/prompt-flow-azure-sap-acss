from promptflow import tool
from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.workloads import WorkloadsMgmtClient

#import json
#from bson.json_util import dumps
import os
from dotenv import load_dotenv

load_dotenv()

@tool
# Get all resource groups 
# (here, we could also easily get all subs for a tenant, and go from there)

def get_acss_details():
    print("Getting ACSS Details")	
    os.environ['AZURE_CLIENT_ID'] = os.getenv("AZURE_CLIENT_ID")
    os.environ['AZURE_CLIENT_SECRET'] = os.getenv("AZURE_CLIENT_SECRET")
    os.environ['AZURE_TENANT_ID'] = os.getenv("AZURE_TENANT_ID")
    subId = os.getenv("AZURE_SUBSCRIPTION_ID")
    rg_list = []

    try:
        # Get list of all VIS from the subscription and disentangle the resource groups
        # For now, this is all we do. Further development will add more info.
        client = WorkloadsMgmtClient(
            credential=DefaultAzureCredential(),
            subscription_id=subId)

        response = client.sap_virtual_instances.list_by_subscription()

        all_objects = list(response)
        #print(all_objects)

        for object in all_objects:
            print("Showing object key details -- starting")
            print(object.name)
            print(object)
            print("Showing object key details -- ending")
            #vis_info = object.name + ";" + object.environment + ";" + str(object.configuration.infrastructure_configuration)
            vis_id = object.name
            vis_location = object.location
            vis_environment = object.environment
            vis_sap_product = object.sap_product
            vis_status = object.status
            vis_health = object.health 
            vis_provisioning_state = object.provisioning_state
            vis_state = object.state

            #infra_object = object.configuration.infrastructure_configuration
            #vis_rg = infra_object.app_resource_group
            #print("######VIS1")
            #print(object.system_data)
            print(object.name + " ######CONFIGURATION")
            print(object.configuration)
            #print(object.configuration.configuration_type)
            #print(object.configuration.infrastructure_configuration)
            #print(object.configuration.infrastructure_configuration.centralServer)
            #print(object.configuration.software_configuration)
            #print(object.configuration.infrastructure_configuration.os_sap_configuration)
            #print("######VIS3")
            #print(object.configuration.infrastructure_configuration)
            #print(object.configuration.infrastructure_configuration.virtual_machine_configuration)
            #vis_app_vm_size = object.configuration.infrastructure_configuration.virtual_machine_configuration.vm_size
            #print(vis_app_vm_size)
            #print("VIS4")
            #print(object.configuration.software_configuration)
            #vis_software = object.configuration.software_configuration.software_version

            #App
            #vis_app_vm_size = infra_object.application_server.virtual_machine_configuration.vm_size
            #vis_app_image = infra_object.application_server.virtual_machine_configuration.image_reference.publisher
            #vis_app_sku = infra_object.application_server.virtual_machine_configuration.image_reference.sku
            #vis_app_instance_count = infra_object.application_server.instance_count

            #DB
            #vis_db_vm_size = infra_object.database_server.virtual_machine_configuration.vm_size
            #vis_db_image = infra_object.database_server.virtual_machine_configuration.image_reference.publisher
            #vis_db_sku = infra_object.database_server.virtual_machine_configuration.image_reference.sku
            #vis_db_instance_count = infra_object.database_server.instance_count

            #vis_info = (vis_id, vis_rg, vis_location, vis_environment, vis_app_vm_size, vis_app_image, vis_app_sku, vis_app_instance_count, vis_db_vm_size, vis_db_image, vis_db_sku, vis_db_instance_count, vis_status, vis_health)
            #vis_info = (vis_id, vis_rg, vis_location, vis_environment, vis_app_vm_size, vis_software, vis_status, vis_health)
            vis_info = (vis_id, vis_location, vis_environment, vis_sap_product, vis_status, vis_health, vis_provisioning_state, vis_state)
            #vis_info = ("S01", "EastUS", "PRD", "S4", "Healthy", "Healthy", "Healthy", "Healthy")
            print("Objecte details")
            print(vis_info)
            rg_list.append(vis_info)

            #print(rg_list)
    except Exception as e:
        return ("Get VIS info failed with error: {}".format(e), os.environ['AZURE_TENANT_ID'], "No available content")

    return rg_list
    