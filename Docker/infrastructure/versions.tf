terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.95.0"
    }
    azurecaf = {
      source  = "aztfmod/azurecaf"
      version = "2.0.0-preview3"
    }

    null = {
      source  = "hashicorp/null"
      version = "3.2.2"
    }
    vault = {
      source  = "hashicorp/vault"
      version = "4.2.0"
    }
    template = {
      source  = "hashicorp/template"
      version = "2.2.0"
    }
  }
}
