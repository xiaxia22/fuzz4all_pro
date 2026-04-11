# Class JSpinner.DateEditor

**Source:** `java.desktop\javax\swing\JSpinner.DateEditor.html`

### Class Description

```java
public static class
JSpinner.DateEditor

extends
JSpinner.DefaultEditor
```

An editor for a

JSpinner

whose model is a

SpinnerDateModel

. The value of the editor is
displayed with a

JFormattedTextField

whose format
is defined by a

DateFormatter

instance whose

minimum

and

maximum

properties
are mapped to the

SpinnerDateModel

.

**All Implemented Interfaces:** ImageObserver

,

LayoutManager

,

MenuContainer

,

PropertyChangeListener

,

Serializable

,

EventListener

,

Accessible

,

ChangeListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public DateEditor​(
JSpinner
spinner)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:**
- spinner

- the spinner whose model

this

editor will monitor

**Throws:**
- IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel

**See Also:**
- getModel()

,

getFormat()

,

SpinnerDateModel

---

#### public DateEditor​(
JSpinner
spinner,

String
dateFormatPattern)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:**
- spinner

- the spinner whose model

this

editor will monitor
- dateFormatPattern

- the initial pattern for the

SimpleDateFormat

object that's used to display
and parse the value of the text field.

**Throws:**
- IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel

**See Also:**
- getModel()

,

getFormat()

,

SpinnerDateModel

,

SimpleDateFormat

---

### Method Details

#### public
SimpleDateFormat
getFormat()

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

**Returns:**
- the value of

getTextField().getFormatter().getFormat()

.

**See Also:**
- JSpinner.DefaultEditor.getTextField()

,

SimpleDateFormat

---

#### public
SpinnerDateModel
getModel()

Return our spinner ancestor's

SpinnerDateModel

.

**Returns:**
- getSpinner().getModel()

**See Also:**
- JSpinner.DefaultEditor.getSpinner()

,

JSpinner.DefaultEditor.getTextField()

---

### Additional Sections

#### Class JSpinner.DateEditor

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPanel
- - javax.swing.JSpinner.DefaultEditor
- - javax.swing.JSpinner.DateEditor

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPanel
- - javax.swing.JSpinner.DefaultEditor
- - javax.swing.JSpinner.DateEditor

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JPanel
- - javax.swing.JSpinner.DefaultEditor
- - javax.swing.JSpinner.DateEditor

javax.swing.JComponent

- javax.swing.JPanel
- - javax.swing.JSpinner.DefaultEditor
- - javax.swing.JSpinner.DateEditor

javax.swing.JPanel

- javax.swing.JSpinner.DefaultEditor
- - javax.swing.JSpinner.DateEditor

javax.swing.JSpinner.DefaultEditor

- javax.swing.JSpinner.DateEditor

javax.swing.JSpinner.DateEditor

**All Implemented Interfaces:** ImageObserver

,

LayoutManager

,

MenuContainer

,

PropertyChangeListener

,

Serializable

,

EventListener

,

Accessible

,

ChangeListener

**Enclosing class:** JSpinner

```java
public static class
JSpinner.DateEditor

extends
JSpinner.DefaultEditor
```

An editor for a

JSpinner

whose model is a

SpinnerDateModel

. The value of the editor is
displayed with a

JFormattedTextField

whose format
is defined by a

DateFormatter

instance whose

minimum

and

maximum

properties
are mapped to the

SpinnerDateModel

.

**Since:** 1.4
**See Also:** Serialized Form

public static class

JSpinner.DateEditor

extends

JSpinner.DefaultEditor

An editor for a

JSpinner

whose model is a

SpinnerDateModel

. The value of the editor is
displayed with a

JFormattedTextField

whose format
is defined by a

DateFormatter

instance whose

minimum

and

maximum

properties
are mapped to the

SpinnerDateModel

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.

JPanel

JPanel.AccessibleJPanel

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DateEditor

​(

JSpinner

spinner)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

DateEditor

​(

JSpinner

spinner,

String

dateFormatPattern)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SimpleDateFormat

getFormat

()

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

SpinnerDateModel

getModel

()

Return our spinner ancestor's

SpinnerDateModel

.

- Methods declared in class javax.swing.

JSpinner.DefaultEditor

addLayoutComponent

,

commitEdit

,

dismiss

,

getBaseline

,

getBaselineResizeBehavior

,

getSpinner

,

getTextField

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

propertyChange

,

removeLayoutComponent

,

stateChanged

- Methods declared in class javax.swing.

JPanel

getAccessibleContext

,

getUI

,

getUIClassID

,

paramString

,

setUI

,

updateUI

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.

JPanel

JPanel.AccessibleJPanel

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.

JPanel

JPanel.AccessibleJPanel

---

#### Nested classes/interfaces declared in class javax.swing. JPanel

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

DateEditor

​(

JSpinner

spinner)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

DateEditor

​(

JSpinner

spinner,

String

dateFormatPattern)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

---

#### Constructor Summary

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SimpleDateFormat

getFormat

()

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

SpinnerDateModel

getModel

()

Return our spinner ancestor's

SpinnerDateModel

.

- Methods declared in class javax.swing.

JSpinner.DefaultEditor

addLayoutComponent

,

commitEdit

,

dismiss

,

getBaseline

,

getBaselineResizeBehavior

,

getSpinner

,

getTextField

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

propertyChange

,

removeLayoutComponent

,

stateChanged

- Methods declared in class javax.swing.

JPanel

getAccessibleContext

,

getUI

,

getUIClassID

,

paramString

,

setUI

,

updateUI

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

Return our spinner ancestor's

SpinnerDateModel

.

Methods declared in class javax.swing.

JSpinner.DefaultEditor

addLayoutComponent

,

commitEdit

,

dismiss

,

getBaseline

,

getBaselineResizeBehavior

,

getSpinner

,

getTextField

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

propertyChange

,

removeLayoutComponent

,

stateChanged

---

#### Methods declared in class javax.swing. JSpinner.DefaultEditor

Methods declared in class javax.swing.

JPanel

getAccessibleContext

,

getUI

,

getUIClassID

,

paramString

,

setUI

,

updateUI

---

#### Methods declared in class javax.swing. JPanel

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DateEditor

```java
public DateEditor​(
JSpinner
spinner)
```

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:** spinner

- the spinner whose model

this

editor will monitor
**Throws:** IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel
**See Also:** getModel()

,

getFormat()

,

SpinnerDateModel

- DateEditor

```java
public DateEditor​(
JSpinner
spinner,

String
dateFormatPattern)
```

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:** spinner

- the spinner whose model

this

editor will monitor
**Parameters:** dateFormatPattern

- the initial pattern for the

SimpleDateFormat

object that's used to display
and parse the value of the text field.
**Throws:** IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel
**See Also:** getModel()

,

getFormat()

,

SpinnerDateModel

,

SimpleDateFormat

============ METHOD DETAIL ==========

- Method Detail

- getFormat

```java
public
SimpleDateFormat
getFormat()
```

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

**Returns:** the value of

getTextField().getFormatter().getFormat()

.
**See Also:** JSpinner.DefaultEditor.getTextField()

,

SimpleDateFormat

- getModel

```java
public
SpinnerDateModel
getModel()
```

Return our spinner ancestor's

SpinnerDateModel

.

**Returns:** getSpinner().getModel()
**See Also:** JSpinner.DefaultEditor.getSpinner()

,

JSpinner.DefaultEditor.getTextField()

Constructor Detail

- DateEditor

```java
public DateEditor​(
JSpinner
spinner)
```

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:** spinner

- the spinner whose model

this

editor will monitor
**Throws:** IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel
**See Also:** getModel()

,

getFormat()

,

SpinnerDateModel

- DateEditor

```java
public DateEditor​(
JSpinner
spinner,

String
dateFormatPattern)
```

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:** spinner

- the spinner whose model

this

editor will monitor
**Parameters:** dateFormatPattern

- the initial pattern for the

SimpleDateFormat

object that's used to display
and parse the value of the text field.
**Throws:** IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel
**See Also:** getModel()

,

getFormat()

,

SpinnerDateModel

,

SimpleDateFormat

---

#### Constructor Detail

DateEditor

```java
public DateEditor​(
JSpinner
spinner)
```

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:** spinner

- the spinner whose model

this

editor will monitor
**Throws:** IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel
**See Also:** getModel()

,

getFormat()

,

SpinnerDateModel

---

#### DateEditor

public DateEditor​(

JSpinner

spinner)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

DateEditor

```java
public DateEditor​(
JSpinner
spinner,

String
dateFormatPattern)
```

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

**Parameters:** spinner

- the spinner whose model

this

editor will monitor
**Parameters:** dateFormatPattern

- the initial pattern for the

SimpleDateFormat

object that's used to display
and parse the value of the text field.
**Throws:** IllegalArgumentException

- if the spinners model is not
an instance of

SpinnerDateModel
**See Also:** getModel()

,

getFormat()

,

SpinnerDateModel

,

SimpleDateFormat

---

#### DateEditor

public DateEditor​(

JSpinner

spinner,

String

dateFormatPattern)

Construct a

JSpinner

editor that supports displaying
and editing the value of a

SpinnerDateModel

with a

JFormattedTextField

.

This

DateEditor

becomes both a

ChangeListener

on the spinner and a

PropertyChangeListener

on the new

JFormattedTextField

.

Method Detail

- getFormat

```java
public
SimpleDateFormat
getFormat()
```

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

**Returns:** the value of

getTextField().getFormatter().getFormat()

.
**See Also:** JSpinner.DefaultEditor.getTextField()

,

SimpleDateFormat

- getModel

```java
public
SpinnerDateModel
getModel()
```

Return our spinner ancestor's

SpinnerDateModel

.

**Returns:** getSpinner().getModel()
**See Also:** JSpinner.DefaultEditor.getSpinner()

,

JSpinner.DefaultEditor.getTextField()

---

#### Method Detail

getFormat

```java
public
SimpleDateFormat
getFormat()
```

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

**Returns:** the value of

getTextField().getFormatter().getFormat()

.
**See Also:** JSpinner.DefaultEditor.getTextField()

,

SimpleDateFormat

---

#### getFormat

public

SimpleDateFormat

getFormat()

Returns the

java.text.SimpleDateFormat

object the

JFormattedTextField

uses to parse and format
numbers.

getModel

```java
public
SpinnerDateModel
getModel()
```

Return our spinner ancestor's

SpinnerDateModel

.

**Returns:** getSpinner().getModel()
**See Also:** JSpinner.DefaultEditor.getSpinner()

,

JSpinner.DefaultEditor.getTextField()

---

#### getModel

public

SpinnerDateModel

getModel()

Return our spinner ancestor's

SpinnerDateModel

.

---

