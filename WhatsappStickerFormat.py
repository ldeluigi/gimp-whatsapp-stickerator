#!/usr/bin/env python

###Author: Luca Deluigi
###Date: 27-10-2018
###Version: 2.1
from __future__ import division
from gimpfu import *
import gtk
import os
import collections
import ntpath

def WhatsApp_Sticker_Format_resize_convert_export(name = None, lossless = 0, quality = 90, alphaquality = 100):
	chooser = gtk.FileChooserDialog(title="Choose Destination Folder",
					 action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
					 buttons=(gtk.STOCK_CANCEL,
					 gtk.RESPONSE_CANCEL,
					 gtk.STOCK_OPEN,
					 gtk.RESPONSE_OK))
	
	save_dir = choose_likely_save_dir()
	if save_dir :
		chooser.set_current_folder(save_dir)

	response = chooser.run()
	if response != gtk.RESPONSE_OK:
		return

	save_dir = chooser.get_filename()
	chooser.destroy()
	if not os.path.isdir(save_dir) :
		return

	i = len(gimp.image_list()) - 1
	for img in gimp.image_list() :
		if len(img.layers) == 0 :
			continue
		##Resize
		if max(img.width, img.height) > 512 :
			if img.width > img.height :
				pdb.gimp_image_scale(img, 512, img.height * (512 / img.width))
			else :
				pdb.gimp_image_scale(img, img.width * (512 / img.height), 512)
		
		posx = (512 - img.width)/2
		posy = (512 - img.height)/2
		pdb.gimp_image_resize(img, 512, 512, posx, posy)
		##Transparent Layer [Now useless]
		#layer = pdb.gimp_layer_new(img, 512, 512, 1, 'TransparentBG', 0.0, 0)
		#pdb.gimp_image_insert_layer(img, layer, None, 1)
		pdb.gimp_layer_resize_to_image_size(img.layers[0])

		##Export
		if img.filename :
			old_name = ntpath.basename(img.filename) + '-'
		else :
			old_name = ''

		if not name :
			name = old_name

		pdb.file_webp_save(img, pdb.gimp_image_merge_visible_layers(img, 0),
					 os.path.join(save_dir, name + '_' + str(i) + '.webp'),
					 '?', 0, lossless,
					 quality if lossless == 0 else 100,
					 alphaquality if lossless == 0 else 100,
					 0, 0, 0, 0, 0, 0, 0, 0, 0)
		##Debug code
		#dialog = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, "File saved at")
		#dialog.format_secondary_text(os.path.join(save_dir, old_name + 'WASticker' + str(i) + '.webp'))
		#dialog.run()
		#dialog.destroy()

		pdb.gimp_image_clean_all(img)
		i -= 1



def choose_likely_save_dir() :
	counts = collections.Counter()
	for img in gimp.image_list() :
		if img.filename :
			counts[os.path.dirname(img.filename)] += 1
	
	try :
		return counts.most_common(1)[0][0]
	except :
		return None



register(
		"WhatsApp_Sticker_Format_resize_convert_export",
		"Resizes and rewrites as .webp all the current edited images to 512x512",
		"Resizes and rewrites as .webp all the current edited images to 512x512",
		"Luca Deluigi",
		"Luca Deluigi",
		"2018",
		"Export all images as WhatsApp Stickers WebP",
		"*",
		[
				(PF_STRING, "name", "Base name", "Sticker"),
				(PF_TOGGLE, "lossless", "Lossless", 0),
				(PF_SLIDER, "quality",  "Quality", 90, (0, 100, 1)),
				(PF_SLIDER, "alpha-quality",  "Alpha Quality", 100, (0, 100, 1))
		],
		[],
		WhatsApp_Sticker_Format_resize_convert_export,
		"<Toolbox>/File/Export All/WhatsApp")

main()