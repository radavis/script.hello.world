import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "Waddup."
line2 = "This is a Scripty McScriptface."
line3 = "Written using a type of Amazon snake."

xbmcgui.Dialog().ok(addonname, line1, line2, line3)
