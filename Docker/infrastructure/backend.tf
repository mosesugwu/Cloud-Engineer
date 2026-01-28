terraform {
  backend "azurerm" {
    resource_group_name  = "rg-moses-state"
    storage_account_name = "mosesstor"
    container_name       = "terraformstate"
    key                  = "dev.terraform.tfstate"
  }
}






