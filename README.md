<div align="center">
     <h1 align="center">Material Symbols for Home Assistant</h1>
</div>

**Material Symbols for Home Assistant** is a collection of 14,376 Google Material Symbols for use within Home Assistant. It uses the icon-set produced and maintained by [iconify](https://github.com/iconify/icon-sets).

Credit goes to @beecho01. Symbols were taken from his [Material Symbols](https://github.com/beecho01/material-symbols) repository. This is repackaged so it works as a frontend module. Icons use `m3s` prefix and each type is suffixed with `-{type}`. Readme below is from his repository and may not fully be updated.

There is a [Icon Finder Tool](https://beecho01.github.io/material-symbols-iconfinder/) hosted by @beech01 to help you select the correct icon. Simply type in what you're looking for, click the icon of choice, and the icon entry for home assistant will be copied to your clipboard (e.g., `m3o:light`). The copied text can be pasted for use in your YAML configuration or into you UI frontend interface.


<div align="left">
  <br>
  <img src="https://img.shields.io/badge/built_for-Home_Assistant-47BFF5?style=for-the-badge"> &nbsp;
  <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/license-CC--BY--NC--SA--4.0-lightgrey?style=for-the-badge"></a> &nbsp;
  <img src="https://img.shields.io/github/v/release/droans/material-3-symbols?style=for-the-badge"> &nbsp;
  <img src="https://img.shields.io/github/repo-size/droans/material-3-symbols?style=for-the-badge"> &nbsp;
  <img src="https://img.shields.io/github/last-commit/droans/material-3-symbols?style=for-the-badge"> &nbsp;
  <br>
  <br>
</div>

## <a name="table-of-contents"></a>Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
    - [HACS Installation (Recommended)](#hacs-installation-recommended)
    - [Manual Installation](#manual-installation)
- [Usage](#usage)
    - [Example](#example)
- [Troubleshooting](#troubleshooting)
    - [Icons Not Showing?](#icons-not-showing)
- [Feedback and Contributions](#feedback-and-contributions)
- [Thanks](#thanks)
  - [Stargazers](#stargazers)
- [Copyright and License](#copyright-and-license)
    - [License Summary](#license-summary)


## <a name="installation"></a>Installation

#### <a name="hacs-installation-recommended"></a>HACS Installation (Recommended)

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/info.svg">
>   <img alt="Info" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/info.svg">
> </picture><br>
>

1. Add this to your HACS repositories.
    * In Home Assistant, navigate to your HACS dashboard
    * In the upper-right corner, select the three-dot overflow button and click "Custom Repositories".
    * For the "Repository", type in `https://github.com/droans/mass_queue`. 
    * For the "Type", select "Integration"
    * Click "Add"
2. Search for "Material 3 Symbols" and install.
<br>

---

#### <a name="manual-installation"></a>Manual Installation

If you prefer to install the integration manually:

1. **Download the Integration:**

   - Download `dist/material-symbols.js`.

2. **Copy to Home Assistant:**

   - Place the `material_symbols.js` file into your Home Assistant `config/www/` directory. The final path should be `config/www/material_symbols.js`.

3. **Update your Resources:**

   - Add the following to your Home Assistant `configuration.yaml` file:

```
frontend:
  extra_module_url:
    - /local/material-symbols.js
```
  - In Home Assistant, navigate to Settings -> Dashboards. Select the overflow menu from the top right and click "Resources". Select Add and use the options below:
      * URL: `/local/material-symbols.js`
      * Resource Type: JavaScript Module
  - Restart Home Assistant and clear your browser cache.
## <a name="usage"></a>Usage

Once installed, you can use the Material Symbols icons in your Lovelace UI.

  The icons come in six distinct styles, each with its own suffix:
- Outlined: `m3o`
- Outlined and filled: `m3of`
- Rounded: `m3r`
- Rounded and filled: `m3rf`
- Sharp: `m3s`
- Sharp and filled: `m3sf`

**Using an Icon:**

  In your entity configuration, specify the icon using the appropriate suffix and icon name:

  ```yaml
  icon: 'm3s:icon_name-{suffix}'
  ```

  Replace `suffix` with one of the suffixes above and `icon_name` with the desired icon. There is a [Icon Finder Tool](https://beecho01.github.io/material-symbols-iconfinder/) hosted by @beech01 to help you select the correct icon for your needs.

#### <a name="example"></a>Example
  ```yaml
  type: entities
  title: Lights
  entities:
    - entity: light.living_room
      name: Living Room Light
      icon: 'm3s:light-m3o'
    - entity: light.kitchen
      name: Kitchen Light
      icon: 'm3s:light-m3of'
    - entity: light.bedroom
      name: Bedroom Light
      icon: 'm3s:light-m3r'
    - entity: light.garage
      name: Garage Light
      icon: 'm3s:light-m3rf'
    - entity: light.porch
      name: Porch Light
      icon: 'm3s:light-m3s'
    - entity: light.garden
      name: Garden Light
      icon: 'm3s:light-m3sf'
  ```


## <a name="troubleshooting"></a>Troubleshooting
#### <a name="icons-not-showing"></a>Icons Not Showing?
 - **Clear Browser Cache**: If icons are not displaying, clear your browser cache and reload the Home Assistant interface.
 - **Check Resources**: Verify that your Dashboard Resources (Settings -> Dashboards -> Overflow Menu -> Resources) contain `material-symbols.js`.
 - **Check Installation**: Verify that the resources are installed correctly and that the icons are in the right directories.

## <a name="feedback-and-contributions"></a>Feedback and Contributions
If you encounter issues or have suggestions, please open an issue on GitHub.
Contributions are welcome! Feel free to submit pull requests.

## <a name="thanks"></a>Thanks
- Big thanks to [@beech01](https://github.com/beech01) for providing the icons and initial component.
- Thanks also to to [@vigonotion](https://github.com/vigonotion) and his repository [hass-simpleicons](https://github.com/vigonotion/hass-simpleicons) and [@thomasloven](https://github.com/thomasloven) for his repository [hass-fontawesome](https://github.com/thomasloven/hass-fontawesome), of which the original integration and github repository is based.

## <a name="copyright-and-license"></a>Copyright and License
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

#### <a name="license-summary"></a>License Summary
 - **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
 - **NonCommercial**: You may not use the material for commercial purposes.
 - **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license.
