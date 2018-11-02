# gimp-whatsapp-stickerator
This is a python plugin for GIMP that allows automation for image formatting and resizing for WhatsApp sticker packs.

**This project is not affiliated to WhatsApp® in any way and the code is under the GNU Public License**

WhatsApp Sticker documentation can be found [here](https://github.com/WhatsApp/stickers).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install [GIMP](https://www.gimp.org/).

### Installing

Follow the instructions on [this](https://en.wikibooks.org/wiki/GIMP/Installing_Plugins#Copying_the_plugin_to_the_GIMP_plugin_directory) page for plugin installation.

_Note that in Windows and probably in other OS as well, there is no difference between putting the plugin inside the folder "plug-ins" inside the installation folder or inside the home/appdata folder of the user. Just don't put the plugin inside both because there will be conflicts_

## Tests

Try the plugin by opening GIMP and by loading some images in the workspace. To activate the plugin you shoulg navigate to File __>__ Export All __>__ WhatsApp __>__ Export All as WhatsApp Stickers

## Built With

A generic text editor like [Notepad++](https://notepad-plus-plus.org).

## Contributing

Pull requests can be evaluated for approval so you can try improving the code.

## Authors

* **Luca Deluigi** - *Base code and tests*

_Many thanks to my friend who helped me figuring out how GIMP2 interpreted plugins directives and other cavils_

## License

This project is licensed under the GNU Public License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Got inspired by my frustration on editing with multiple images at once. Existing plugins didn't automate exporting and exporting in WebP in particular.
* GIMP plug-ins repositories helped me understanding basic mechanics of the software.
