//  Natron
//
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
/*
 *Created by Alexandre GAUTHIER-FOICHAT on 6/1/2012.
 *contact: immarespond at gmail dot com
 *
 */

#ifndef NATRON_ENGINE_OFXNODE_H_
#define NATRON_ENGINE_OFXNODE_H_

#include <map>
#include <string>
#include <boost/shared_ptr.hpp>
#include <boost/scoped_ptr.hpp>
#include <QtCore/QMutex>
#include <QtCore/QString>
#include <QtCore/QObject>
#include <QtCore/QStringList>
//ofx
#include "ofxhImageEffect.h"

#include "Engine/Node.h"
#include "Engine/EffectInstance.h"

class Tab_Knob;
class QHBoxLayout;
class QImage;
class OfxClipInstance;
class QKeyEvent;
namespace Natron {
class Node;
class OfxImageEffectInstance;
class OfxOverlayInteract;
}


class OfxEffectInstance : public Natron::OutputEffectInstance {
    
    Natron::OfxImageEffectInstance* effect_;
    bool _isOutput;//if the OfxNode can output a file somehow

    bool _penDown; // true when the overlay trapped a penDow action
    boost::scoped_ptr<Natron::OfxOverlayInteract> _overlayInteract; // ptr to the overlay interact if any

    Tab_Knob* _tabKnob; // for nuke tab extension: it creates all Group param as a tab and put it into this knob.
    QHBoxLayout* _lastKnobLayoutWithNoNewLine; // for nuke layout hint extension
    bool _initialized; //true when the image effect instance has been created and populated
public:
    
    
    OfxEffectInstance(Natron::Node* node);
    
    virtual ~OfxEffectInstance();
    
    void createOfxImageEffectInstance(OFX::Host::ImageEffect::ImageEffectPlugin* plugin,
                                      const std::string& context);
    
    Natron::OfxImageEffectInstance* effectInstance() WARN_UNUSED_RETURN { return effect_; }
    
    const Natron::OfxImageEffectInstance* effectInstance() const WARN_UNUSED_RETURN { return effect_; }

    void setAsOutputNode() {_isOutput = true;}

    void setTabKnob(Tab_Knob* k){_tabKnob = k;}

    Tab_Knob* getTabKnob() const WARN_UNUSED_RETURN {return _tabKnob;}

    void setLastKnobLayoutWithNoNewLine(QHBoxLayout* layout) {_lastKnobLayoutWithNoNewLine = layout;}

    QHBoxLayout* getLastKnobLayoutWithNoNewLine() const WARN_UNUSED_RETURN {return _lastKnobLayoutWithNoNewLine;}
    
    
    const std::string& getShortLabel() const WARN_UNUSED_RETURN;
    
    typedef std::vector<OFX::Host::ImageEffect::ClipDescriptor*> MappedInputV;
    MappedInputV inputClipsCopyWithoutOutput() const WARN_UNUSED_RETURN;
    
    void ifInfiniteclipRectToProjectDefault(OfxRectD* rod) const;
    
    /*If the OpenFX effect is an output effect (a writer), this will return the pattern of
     the output file sequence. */
    std::string getOutputFileName() const WARN_UNUSED_RETURN;

    /********OVERRIDEN FROM EFFECT INSTANCE*************/
    virtual bool isGenerator() const OVERRIDE FINAL WARN_UNUSED_RETURN;
    
    virtual bool isOutput() const OVERRIDE FINAL WARN_UNUSED_RETURN;
    
    virtual bool isGeneratorAndFilter() const OVERRIDE FINAL WARN_UNUSED_RETURN;
    
    virtual bool isOpenFX() const OVERRIDE FINAL WARN_UNUSED_RETURN {return true;}

    virtual bool makePreviewByDefault() const OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual int maximumInputs() const OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual std::string pluginID() const OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual std::string pluginLabel() const OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual std::string description() const OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual std::string inputLabel (int inputNb) const OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual bool isInputOptional(int inputNb) const OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual Natron::Status getRegionOfDefinition(SequenceTime time,RectI* rod) OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual Natron::EffectInstance::RoIMap getRegionOfInterest(SequenceTime time,RenderScale scale,const RectI& renderWindow) OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual void getFrameRange(SequenceTime *first,SequenceTime *last) OVERRIDE FINAL;

    virtual Natron::Status preProcessFrame(SequenceTime /*time*/) OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual void drawOverlay() OVERRIDE FINAL;

    virtual bool onOverlayPenDown(const QPointF& viewportPos,const QPointF& pos) OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual bool onOverlayPenMotion(const QPointF& viewportPos,const QPointF& pos) OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual bool onOverlayPenUp(const QPointF& viewportPos,const QPointF& pos) OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual void onOverlayKeyDown(QKeyEvent* e) OVERRIDE FINAL;

    virtual void onOverlayKeyUp(QKeyEvent* e) OVERRIDE FINAL;

    virtual void onOverlayKeyRepeat(QKeyEvent* e) OVERRIDE FINAL;

    virtual void onOverlayFocusGained() OVERRIDE FINAL;

    virtual void onOverlayFocusLost() OVERRIDE FINAL;

    virtual void beginKnobsValuesChanged(Natron::ValueChangedReason reason) OVERRIDE FINAL;

    virtual void endKnobsValuesChanged(Natron::ValueChangedReason reason) OVERRIDE FINAL;

    virtual void onKnobValueChanged(Knob* k,Natron::ValueChangedReason reason) OVERRIDE FINAL;

    virtual Natron::Status render(SequenceTime time,RenderScale scale,
                                   const RectI& roi,int view,boost::shared_ptr<Natron::Image> output) OVERRIDE FINAL WARN_UNUSED_RETURN;

    virtual Natron::EffectInstance::RenderSafety renderThreadSafety() const OVERRIDE FINAL WARN_UNUSED_RETURN;


    /*********OVERLAY INTERACT FUNCTIONS********/

    void swapBuffersOfAttachedViewer();

    void redrawInteractOnAttachedViewer();

    void pixelScaleOfAttachedViewer(double &x,double &y);

    void viewportSizeOfAttachedViewer(double &w,double &h);

    void backgroundColorOfAttachedViewer(double &r,double &g,double &b);

    static QStringList getPluginGrouping(const std::string& pluginLabel,const std::string& grouping) WARN_UNUSED_RETURN;

    static std::string getPluginLabel(const std::string& shortLabel,
                                      const std::string& label,
                                      const std::string& longLabel) WARN_UNUSED_RETURN;

    static std::string generateImageEffectClassName(const std::string& shortLabel,
                                                const std::string& label,
                                                const std::string& longLabel,
                                                const std::string& grouping) WARN_UNUSED_RETURN;

private:

    void tryInitializeOverlayInteracts();


};


/*group is a string as such:
 Toto/Superplugins/blabla
 This functions extracts the all parts of such a grouping, e.g in this case
 it would return [Toto,Superplugins,blabla].*/
QStringList ofxExtractAllPartsOfGrouping(const QString& group,const QString& bundlePath);

#endif // NATRON_ENGINE_OFXNODE_H_
