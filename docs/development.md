# Developing Locally
1. Clone the repository locally
2. If developing on a Unix-based computer, run `setup.sh`. If developing on Windows, you will need to manually perform the actions below. The commands may need to be updated for Windows.
    * Create a folder in this directory named `raw` and cd into it.
    * Perform a limited clone of the source repository. Run `git clone -n --depth=1 --filter=tree:0 https://github.com/beecho01/material-symbols`. 
    * Perform a sparse checkout to only grab the necessary files. Run `git sparse-checkout set --no-cone /custom_components/material_symbols/data/m3o /custom_components/material_symbols/data/m3of /custom_components/material_symbols/data/m3r /custom_components/material_symbols/data/m3rf /custom_components/material_symbols/data/m3s /custom_components/material_symbols/data/m3sf`. 
    * Checkout the source repository. Run `git checkout`