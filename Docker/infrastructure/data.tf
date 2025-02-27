data "azurecaf_name" "nic_1" {
  name          = "ce"
  resource_type = "azurerm_network_interface"
  suffixes      = ["mosesugwu", "01"]
  clean_input   = true
  separator     = "-"
}

data "azurecaf_name" "nic_2" {
  name          = "ce"
  resource_type = "azurerm_network_interface"
  suffixes      = ["mosesugwu", "02"]
  clean_input   = true
  separator     = "-"
}

data "azurecaf_name" "nic_3" {
  name          = "ce"
  resource_type = "azurerm_network_interface"
  suffixes      = ["mosesugwu", "03"]
  clean_input   = true
  separator     = "-"
}

data "azurecaf_name" "vm_1" {
  name          = "ce"
  resource_type = "azurerm_linux_virtual_machine"
  suffixes      = ["mosesugwu", "01"]
  clean_input   = true
  separator     = "-"
}

data "azurecaf_name" "vm_2" {
  name          = "ce"
  resource_type = "azurerm_linux_virtual_machine"
  suffixes      = ["mosesugwu", "02"]
  clean_input   = true
  separator     = "-"
}

data "azurecaf_name" "vm_3" {
  name          = "ce"
  resource_type = "azurerm_linux_virtual_machine"
  suffixes      = ["mosesugwu", "03"]
  clean_input   = true
  separator     = "-"
}

data "template_file" "custom_data" {
  for_each = local.virtual_machines
  template = file(each.value.custom_data)
  vars     = each.value.vars
}




# data "template_file" "custom_data" {
#   for_each = local.virtual_machines

#   template = file("${path.module}/${var.custom_data_vm_2}")

# }