locals {
  virtual_machines = {
    vm-1 = {
      name           = "resumeapp-vm01"
      public_key     = file("moseskey.pub")
      admin_username = "mosesugwu"
      username       = "mosesugwu"
      size           = "Standard_F2"
      custom_data    = local.custom_data_vm_1
      vars           = {}
    },
    vm-2 = {
      name           = "ghrunner1"
      size           = "Standard_F2"
      public_key     = file("moseskey.pub")
      admin_username = "mosesugwu"
      username       = "mosesugwu"
      custom_data    = local.custom_data_vm_2
      vars = {
        RUNNER_URL = "https://github.com/actions/runner/releases/download/v2.322.0/actions-runner-linux-x64-2.322.0.tar.gz"
        RUNNER_SHA = "b13b784808359f31bc79b08a191f5f83757852957dd8fe3dbfcc38202ccf5768"
        RUNNER_TAR = "./actions-runner-linux-x64-2.322.0.tar.gz"
      }
    },
    vm-3 = {
      name           = "hashicorpvault-vm01"
      size           = "Standard_F2"
      public_key     = file("moseskey.pub")
      admin_username = "mosesugwu"
      username       = "mosesugwu"
      custom_data    = local.custom_data_vm_1
      vars           = {}


    }
  }
  network_interface_ids = {
    vm-1 = {
      name                 = data.azurecaf_name.nic_1.result
      public_ip_address_id = azurerm_public_ip.vm_1.id
      subnet_id            = module.subnet.snet_id

    },
    vm-2 = {
      name                 = data.azurecaf_name.nic_2.result
      public_ip_address_id = azurerm_public_ip.vm_2.id
      subnet_id            = module.subnet.snet_id

    },
    vm-3 = {
      name                 = data.azurecaf_name.nic_3.result
      public_ip_address_id = azurerm_public_ip.vm_3.id
      subnet_id            = module.subnet.snet_id

    }

  }

  db_name          = "mosesdb"
  custom_data_vm_1 = var.custom_data_vm_1
  custom_data_vm_2 = var.custom_data_vm_2
  custom_data_vm_3 = var.custom_data_vm_3
  disk_name        = "hashidisk"
}




