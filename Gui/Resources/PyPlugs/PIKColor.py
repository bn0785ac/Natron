# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named PIKColorExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from PIKColorExt import *
except ImportError:
    pass

def getPluginID():
    return "fr.inria.PIKColor"

def getLabel():
    return "PIKColor"

def getVersion():
    return 1

def getIconPath():
    return "PIKColor.png"

def getGrouping():
    return "Keyer"

def getPluginDescription():
    return "This node provides the PIK per-pixel keyer a pseudo clean-plate to be used as color reference.\nThe idea is to remove the foreground image and only leave the shades and hues of the original blue/greenscreen.\nAttach the output of this node to the \'C\' input of a PIK node. Attach the input of this node and the \'PFg\' input of PIK to the original screen, or preferably the denoised screen.\nPick which color your screen type is in both nodes and then while viewing the alpha output from PIK lower the darks.b (if a bluescreen - adjust darks.g if a greenscreen) in this node until you see a change in the garbage area of the matte. Once you see a change then you have gone too far -back off a step. If you are still left with discolored edges you can use the other colors in the lights and darks to eliminate them. Remember the idea is to be left with the original shades of the screen and the foreground blacked out. While swapping between viewing the matte from the PIK and the rgb output of PIKColor adjust the other colors until you see a change in the garbage area of the matte. Simple rule of thumb - if you have a light red discolored area increase the lights.r - if you have a dark green discolored area increase darks.g. If your screen does not have a very saturated hue you may still be left with areas of discoloration after the above process. The \'erode\' slider can help with this - while viewing the rgb output adjust the erode until those areas disappear.\nThe \'Patch Black\' slider allows you to fill in the black areas with screen color. This is not always necessary but if you see blue squares in your composite increase this value and it\'ll fix it.\nThe optional \'InM\' input can be used to provide an inside mask (a.k.a. core matte or holdout matte), which is excluded from the clean plate. If an inside mask is fed into the Keyer (PIK or another Keyer), the same inside mask should be fed inside PIKColor.\nThe above is the only real workflow for this node - working from the top parameter to the bottom parameter- going back to tweak darks/lights with \'erode\' and \'patch black\' activated is not really going to work."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.controls = lastNode.createPageParam("controls", "Controls")
    param = lastNode.createChoiceParam("screenType", "Screen Type")
    entries = [ ("Green", ""),
    ("Blue", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("Blue")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.screenType = param
    del param

    param = lastNode.createDoubleParam("size", "Size")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Size of color expansion.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.size = param
    del param

    param = lastNode.createColorParam("off", "Darks", False)
    param.setDisplayMinimum(-1, 0)
    param.setDisplayMaximum(1, 0)
    param.setDisplayMinimum(-1, 1)
    param.setDisplayMaximum(1, 1)
    param.setDisplayMinimum(-1, 2)
    param.setDisplayMaximum(1, 2)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("adjust the color values to get the best separation between black and the screen type color.\nYou want to be left with only shades of the screen color and black. \nIf a green screen is selected start by bringing down darks->green\nIf a blue screen is selected start by bringing down darks->blue")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.off = param
    del param

    param = lastNode.createColorParam("mult", "Lights", False)
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(0, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(2, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setMinimum(0, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(2, 2)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("adjust the color values to get the best separation between black and the screen type color.\nYou want to be left with only shades of the screen color and black. \nIf a green screen is selected start by bringing down darks->green\nIf a blue screen is selected start by bringing down darks->blue")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.mult = param
    del param

    param = lastNode.createSeparatorParam("sep1", "")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep1 = param
    del param

    param = lastNode.createDoubleParam("erode", "Erode")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(5, 0)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("increase this value if you still see traces of the foreground edge color in the output")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.erode = param
    del param

    param = lastNode.createSeparatorParam("sep2", "")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep2 = param
    del param

    param = lastNode.createDoubleParam("multi", "Patch Black")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(5, 0)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Increase this to optionally remove the black from the output.\nThis should only be used once the the above darks/lights have been set.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.multi = param
    del param

    param = lastNode.createBooleanParam("filt", "Filter")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.filt = param
    del param

    param = lastNode.createSeparatorParam("sep3", "")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep3 = param
    del param

    param = lastNode.createDoubleParam("level", "Level")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("multiply the rgb output. Helps remove noise from main key")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.level = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['controls', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Grade11"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade11")
    lastNode.setLabel("Grade11")
    lastNode.setPosition(14, -192)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade11 = lastNode

    param = lastNode.getParam("multiply")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(0, 3)
        del param

    param = lastNode.getParam("offset")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("clampBlack")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("mix")
    if param is not None:
        param.setValue(0.326, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">*mult+off</font>")
        del param

    del lastNode
    # End of node "Grade11"

    # Start of node "Clamp2"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp2")
    lastNode.setLabel("Clamp2")
    lastNode.setPosition(14, -118)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp2 = lastNode

    param = lastNode.getParam("maximumEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">>0 (rgb)</font>")
        del param

    del lastNode
    # End of node "Clamp2"

    # Start of node "Invert1"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert1")
    lastNode.setLabel("Invert1")
    lastNode.setPosition(126, -33)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(a)</font>")
        del param

    del lastNode
    # End of node "Invert1"

    # Start of node "Erode1"
    lastNode = app.createNode("eu.cimg.ErodeBlur", 4, group)
    lastNode.setScriptName("Erode1")
    lastNode.setLabel("Erode1")
    lastNode.setPosition(138, 33)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupErode1 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">erode (a)</font>")
        del param

    del lastNode
    # End of node "Erode1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(187, -224)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(59, -226)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "ShuffleCopy3"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("ShuffleCopy3")
    lastNode.setLabel("ShuffleCopy3")
    lastNode.setPosition(272, 35)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffleCopy3 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(A.a->B.a)</font>")
        del param

    del lastNode
    # End of node "ShuffleCopy3"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(317, -224)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Premult3"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult3")
    lastNode.setLabel("Premult3")
    lastNode.setPosition(272, 99)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupPremult3 = lastNode

    del lastNode
    # End of node "Premult3"

    # Start of node "Unpremult4"
    lastNode = app.createNode("net.sf.openfx.Unpremult", 2, group)
    lastNode.setScriptName("Unpremult4")
    lastNode.setLabel("Unpremult4")
    lastNode.setPosition(272, 227)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupUnpremult4 = lastNode

    del lastNode
    # End of node "Unpremult4"

    # Start of node "Clamp1"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp1")
    lastNode.setLabel("Clamp1")
    lastNode.setPosition(700, 225)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp1 = lastNode

    param = lastNode.getParam("maximum")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        param.setValue(0, 3)
        del param

    param = lastNode.getParam("minClampToEnable")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("maxClampToEnable")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(a != 0 -> a)</font>")
        del param

    del lastNode
    # End of node "Clamp1"

    # Start of node "ChannelCopy1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("ChannelCopy1")
    lastNode.setLabel("ChannelCopy1")
    lastNode.setPosition(411, 292)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupChannelCopy1 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(A.a->B.a)</font>")
        del param

    del lastNode
    # End of node "ChannelCopy1"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(317, 299)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "ShuffleCopy2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("ShuffleCopy2")
    lastNode.setLabel("ShuffleCopy2")
    lastNode.setPosition(413, 602)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffleCopy2 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(A.a->B.a)</font>")
        del param

    del lastNode
    # End of node "ShuffleCopy2"

    # Start of node "Unpremult1"
    lastNode = app.createNode("net.sf.openfx.Unpremult", 2, group)
    lastNode.setScriptName("Unpremult1")
    lastNode.setLabel("Unpremult1")
    lastNode.setPosition(413, 423)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupUnpremult1 = lastNode

    del lastNode
    # End of node "Unpremult1"

    # Start of node "Invert2"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert2")
    lastNode.setLabel("Invert2")
    lastNode.setPosition(700, 328)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert2 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(a)</font>")
        del param

    del lastNode
    # End of node "Invert2"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(690, 602)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(filt)</font>")
        del param

    del lastNode
    # End of node "Switch1"

    # Start of node "Premult1"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult1")
    lastNode.setLabel("Premult1")
    lastNode.setPosition(411, 727)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupPremult1 = lastNode

    del lastNode
    # End of node "Premult1"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(272, 717)
    lastNode.setSize(104, 56)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "ChannelCopy2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("ChannelCopy2")
    lastNode.setLabel("ChannelCopy2")
    lastNode.setPosition(272, 886)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupChannelCopy2 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    del lastNode
    # End of node "ChannelCopy2"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(171, 894)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Start of node "Grade1"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade1")
    lastNode.setLabel("Grade1")
    lastNode.setPosition(272, 946)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade1 = lastNode

    param = lastNode.getParam("multiply")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    param = lastNode.getParam("clampBlack")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(145, -282)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output")
    lastNode.setPosition(272, 1014)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "PIK2"
    lastNode = app.createNode("net.sf.openfx.PIK", 1, group)
    lastNode.setScriptName("PIK2")
    lastNode.setLabel("PIK2")
    lastNode.setPosition(26, -35)
    lastNode.setSize(80, 34)
    lastNode.setColor(0, 1, 0)
    groupPIK2 = lastNode

    param = lastNode.getParam("screenType")
    if param is not None:
        param.set("C-Blue")
        del param

    param = lastNode.getParam("redWeight")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("blueGreenWeight")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("luma")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "PIK2"

    # Start of node "Blur2"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur2")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(411, 351)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur2 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("Quadratic")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">size*3*multi</font>")
        del param

    del lastNode
    # End of node "Blur2"

    # Start of node "Blur4"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur4")
    lastNode.setLabel("Blur4")
    lastNode.setPosition(272, 159)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur4 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(10, 0)
        param.setValue(10, 1)
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("Quadratic")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">size</font>")
        del param

    del lastNode
    # End of node "Blur4"

    # Start of node "InM"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("InM")
    lastNode.setLabel("InM")
    lastNode.setPosition(-171, -35)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInM = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "InM"

    # Start of node "Dot7"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7")
    lastNode.setLabel("Dot7")
    lastNode.setPosition(317, 370)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7 = lastNode

    del lastNode
    # End of node "Dot7"

    # Start of node "BlurBox1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("BlurBox1")
    lastNode.setLabel("BlurBox1")
    lastNode.setPosition(579, 509)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlurBox1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("cropToFormat")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(size/5)*multi*4</font>")
        del param

    del lastNode
    # End of node "BlurBox1"

    # Start of node "BlurBox2"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("BlurBox2")
    lastNode.setLabel("BlurBox2")
    lastNode.setPosition(803, 511)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlurBox2 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(4, 0)
        param.setValue(4, 1)
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("Box")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("cropToFormat")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(size/5)*2</font>")
        del param

    del lastNode
    # End of node "BlurBox2"

    # Start of node "Unpremult2"
    lastNode = app.createNode("net.sf.openfx.Unpremult", 2, group)
    lastNode.setScriptName("Unpremult2")
    lastNode.setLabel("Unpremult2")
    lastNode.setPosition(272, 803)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupUnpremult2 = lastNode

    del lastNode
    # End of node "Unpremult2"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(418, 225)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputComponents")
    if param is not None:
        param.set("Alpha")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(g or b->a)</font>")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "DilateFast1"
    lastNode = app.createNode("net.sf.cimg.CImgDilate", 2, group)
    lastNode.setScriptName("DilateFast1")
    lastNode.setLabel("DilateFast1")
    lastNode.setPosition(579, 428)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupDilateFast1 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">(size/5)*multi*2</font>")
        del param

    del lastNode
    # End of node "DilateFast1"

    # Start of node "DilateFast2"
    lastNode = app.createNode("net.sf.cimg.CImgDilate", 2, group)
    lastNode.setScriptName("DilateFast2")
    lastNode.setLabel("DilateFast2")
    lastNode.setPosition(803, 431)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupDilateFast2 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<font size=\"6\" color=\"#000000\" face=\"Droid Sans\">size/5</font>")
        del param

    del lastNode
    # End of node "DilateFast2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupGrade11.connectInput(0, groupDot2)
    groupClamp2.connectInput(0, groupGrade11)
    groupInvert1.connectInput(0, groupPIK2)
    groupErode1.connectInput(0, groupInvert1)
    groupDot1.connectInput(0, groupSource)
    groupDot2.connectInput(0, groupDot1)
    groupShuffleCopy3.connectInput(0, groupDot3)
    groupShuffleCopy3.connectInput(1, groupErode1)
    groupDot3.connectInput(0, groupDot1)
    groupPremult3.connectInput(0, groupShuffleCopy3)
    groupUnpremult4.connectInput(0, groupBlur4)
    groupClamp1.connectInput(0, groupShuffle1)
    groupChannelCopy1.connectInput(0, groupDot4)
    groupChannelCopy1.connectInput(1, groupClamp1)
    groupDot4.connectInput(0, groupUnpremult4)
    groupShuffleCopy2.connectInput(0, groupUnpremult1)
    groupShuffleCopy2.connectInput(1, groupSwitch1)
    groupUnpremult1.connectInput(0, groupBlur2)
    groupInvert2.connectInput(0, groupClamp1)
    groupSwitch1.connectInput(0, groupBlurBox1)
    groupSwitch1.connectInput(1, groupBlurBox2)
    groupPremult1.connectInput(0, groupShuffleCopy2)
    groupMerge1.connectInput(0, groupDot7)
    groupMerge1.connectInput(1, groupPremult1)
    groupChannelCopy2.connectInput(0, groupUnpremult2)
    groupChannelCopy2.connectInput(1, groupDot6)
    groupDot6.connectInput(0, groupErode1)
    groupGrade1.connectInput(0, groupChannelCopy2)
    groupOutput1.connectInput(0, groupGrade1)
    groupPIK2.connectInput(0, groupClamp2)
    groupPIK2.connectInput(1, groupClamp2)
    groupPIK2.connectInput(2, groupClamp2)
    groupPIK2.connectInput(4, groupInM)
    groupBlur2.connectInput(0, groupChannelCopy1)
    groupBlur4.connectInput(0, groupPremult3)
    groupDot7.connectInput(0, groupChannelCopy1)
    groupBlurBox1.connectInput(0, groupDilateFast1)
    groupBlurBox2.connectInput(0, groupDilateFast2)
    groupUnpremult2.connectInput(0, groupMerge1)
    groupShuffle1.connectInput(1, groupUnpremult4)
    groupDilateFast1.connectInput(0, groupInvert2)
    groupDilateFast2.connectInput(0, groupInvert2)

    param = groupGrade11.getParam("multiply")
    param.setExpression("thisGroup.mult.get().r", False, 0)
    param.setExpression("thisGroup.mult.get().g", False, 1)
    param.setExpression("thisGroup.mult.get().b", False, 2)
    del param
    param = groupGrade11.getParam("offset")
    param.setExpression("thisGroup.off.get().r", False, 0)
    param.setExpression("thisGroup.off.get().g", False, 1)
    param.setExpression("thisGroup.off.get().b", False, 2)
    del param
    param = groupErode1.getParam("size")
    param.setExpression("thisGroup.erode.get()", False, 0)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("1-thisGroup.filt.get()", False, 0)
    del param
    param = groupGrade1.getParam("multiply")
    param.setExpression("thisGroup.level.get()", False, 0)
    param.setExpression("thisGroup.level.get()", False, 1)
    param.setExpression("thisGroup.level.get()", False, 2)
    param.setExpression("thisGroup.level.get()", False, 3)
    del param
    param = groupPIK2.getParam("screenType")
    param.setExpression("thisGroup.screenType.getValue()", False, 0)
    del param
    param = groupBlur2.getParam("size")
    param.setExpression("thisGroup.size.get()*3*thisGroup.multi.get()", False, 0)
    param.setExpression("thisGroup.size.get()*3*thisGroup.multi.get()", False, 1)
    del param
    param = groupBlur4.getParam("size")
    param.setExpression("thisGroup.size.get()", False, 0)
    param.setExpression("thisGroup.size.get()", False, 1)
    del param
    param = groupBlurBox1.getParam("size")
    param.setExpression("(thisGroup.size.get()/5)*thisGroup.multi.get()*4", False, 0)
    param.setExpression("(thisGroup.size.get()/5)*thisGroup.multi.get()*4", False, 1)
    del param
    param = groupBlurBox2.getParam("size")
    param.setExpression("(thisGroup.size.get()/5)*2", False, 0)
    param.setExpression("(thisGroup.size.get()/5)*2", False, 1)
    del param
    param = groupShuffle1.getParam("outputA")
    param.setExpression("thisGroup.screenType.get()+1", False, 0)
    del param
    param = groupDilateFast1.getParam("size")
    param.setExpression("(thisGroup.size.get()/5)*thisGroup.multi.get()*2", False, 0)
    param.setExpression("(thisGroup.size.get()/5)*thisGroup.multi.get()*2", False, 1)
    del param
    param = groupDilateFast2.getParam("size")
    param.setExpression("thisGroup.size.get()/5", False, 0)
    param.setExpression("thisGroup.size.get()/5", False, 1)
    del param

    try:
        extModule = sys.modules["PIKColorExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
