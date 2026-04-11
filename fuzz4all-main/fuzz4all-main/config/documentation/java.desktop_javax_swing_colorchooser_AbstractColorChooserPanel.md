# Class AbstractColorChooserPanel

**Source:** `java.desktop\javax\swing\colorchooser\AbstractColorChooserPanel.html`

### Class Description

```java
public abstract class
AbstractColorChooserPanel

extends
JPanel
```

This is the abstract superclass for color choosers. If you want to add
a new color chooser panel into a

JColorChooser

, subclass
this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final
String
TRANSPARENCY_ENABLED_PROPERTY

Identifies that the transparency of the color (alpha value) can be
selected

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public AbstractColorChooserPanel()

*No description found.*

---

### Method Details

#### public abstract void updateChooser()

Invoked automatically when the model's state changes.
It is also called by

installChooserPanel

to allow
you to set up the initial state of your chooser.
Override this method to update your

ChooserPanel

.

---

#### protected abstract void buildChooser()

Builds a new chooser panel.

---

#### public abstract
String
getDisplayName()

Returns a string containing the display name of the panel.

**Returns:**
- the name of the display panel

---

#### public int getMnemonic()

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel. A return value <= 0 indicates there is no mnemonic.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way.

This implementation returns 0, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:**
- KeyEvent.VK constant identifying the mnemonic; <= 0 for no
mnemonic

**See Also:**
- getDisplayedMnemonicIndex()

**Since:**
- 1.4

---

#### public int getDisplayedMnemonicIndex()

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic. The look and feel should only use this if

getMnemonic

returns a value > 0.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way. For example,
a look and feel may wish to render each

AbstractColorChooserPanel

in a

JTabbedPane

,
and further use this return value to underline a character in
the

getDisplayName

.

This implementation returns -1, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:**
- Character index to render mnemonic for; -1 to provide no
visual identifier for this panel.

**See Also:**
- getMnemonic()

**Since:**
- 1.4

---

#### public abstract
Icon
getSmallDisplayIcon()

Returns the small display icon for the panel.

**Returns:**
- the small display icon

---

#### public abstract
Icon
getLargeDisplayIcon()

Returns the large display icon for the panel.

**Returns:**
- the large display icon

---

#### public void installChooserPanel​(
JColorChooser
enclosingChooser)

Invoked when the panel is added to the chooser.
If you override this, be sure to call

super

.

**Parameters:**
- enclosingChooser

- the chooser to which the panel is to be added

**Throws:**
- RuntimeException

- if the chooser panel has already been
installed

---

#### public void uninstallChooserPanel​(
JColorChooser
enclosingChooser)

Invoked when the panel is removed from the chooser.
If override this, be sure to call

super

.

**Parameters:**
- enclosingChooser

- the chooser from which the panel is to be removed

---

#### public
ColorSelectionModel
getColorSelectionModel()

Returns the model that the chooser panel is editing.

**Returns:**
- the

ColorSelectionModel

model this panel
is editing

---

#### protected
Color
getColorFromModel()

Returns the color that is currently selected.

**Returns:**
- the

Color

that is selected

---

#### @BeanProperty
(
description
="Sets the transparency of a color selection on or off.")
public void setColorTransparencySelectionEnabled​(boolean b)

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.
This method fires a property-changed event, using the string value of

TRANSPARENCY_ENABLED_PROPERTY

as the name
of the property.

The value is a hint and may not be applicable to all types of chooser
panel.

The default value is

true

.

**Parameters:**
- b

- true if the transparency of a color can be selected

**See Also:**
- isColorTransparencySelectionEnabled()

---

#### public boolean isColorTransparencySelectionEnabled()

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

**Returns:**
- true if the transparency of a color can be selected

**See Also:**
- setColorTransparencySelectionEnabled(boolean)

---

#### public void paint​(
Graphics
g)

Draws the panel.

**Overrides:**
- paint

in class

JComponent

**Parameters:**
- g

- the

Graphics

object

**See Also:**
- JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

---

### Additional Sections

#### Class AbstractColorChooserPanel

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPanel
- - javax.swing.colorchooser.AbstractColorChooserPanel

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPanel
- - javax.swing.colorchooser.AbstractColorChooserPanel

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JPanel
- - javax.swing.colorchooser.AbstractColorChooserPanel

javax.swing.JComponent

- javax.swing.JPanel
- - javax.swing.colorchooser.AbstractColorChooserPanel

javax.swing.JPanel

- javax.swing.colorchooser.AbstractColorChooserPanel

javax.swing.colorchooser.AbstractColorChooserPanel

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
public abstract class
AbstractColorChooserPanel

extends
JPanel
```

This is the abstract superclass for color choosers. If you want to add
a new color chooser panel into a

JColorChooser

, subclass
this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public abstract class

AbstractColorChooserPanel

extends

JPanel

This is the abstract superclass for color choosers. If you want to add
a new color chooser panel into a

JColorChooser

, subclass
this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

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

Fields

Modifier and Type

Field

Description

static

String

TRANSPARENCY_ENABLED_PROPERTY

Identifies that the transparency of the color (alpha value) can be
selected

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

AbstractColorChooserPanel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract void

buildChooser

()

Builds a new chooser panel.

protected

Color

getColorFromModel

()

Returns the color that is currently selected.

ColorSelectionModel

getColorSelectionModel

()

Returns the model that the chooser panel is editing.

int

getDisplayedMnemonicIndex

()

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic.

abstract

String

getDisplayName

()

Returns a string containing the display name of the panel.

abstract

Icon

getLargeDisplayIcon

()

Returns the large display icon for the panel.

int

getMnemonic

()

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel.

abstract

Icon

getSmallDisplayIcon

()

Returns the small display icon for the panel.

void

installChooserPanel

​(

JColorChooser

enclosingChooser)

Invoked when the panel is added to the chooser.

boolean

isColorTransparencySelectionEnabled

()

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

void

paint

​(

Graphics

g)

Draws the panel.

void

setColorTransparencySelectionEnabled

​(boolean b)

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.

void

uninstallChooserPanel

​(

JColorChooser

enclosingChooser)

Invoked when the panel is removed from the chooser.

abstract void

updateChooser

()

Invoked automatically when the model's state changes.

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

getBaseline

,

getBaselineResizeBehavior

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

Fields

Modifier and Type

Field

Description

static

String

TRANSPARENCY_ENABLED_PROPERTY

Identifies that the transparency of the color (alpha value) can be
selected

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

Identifies that the transparency of the color (alpha value) can be
selected

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

AbstractColorChooserPanel

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract void

buildChooser

()

Builds a new chooser panel.

protected

Color

getColorFromModel

()

Returns the color that is currently selected.

ColorSelectionModel

getColorSelectionModel

()

Returns the model that the chooser panel is editing.

int

getDisplayedMnemonicIndex

()

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic.

abstract

String

getDisplayName

()

Returns a string containing the display name of the panel.

abstract

Icon

getLargeDisplayIcon

()

Returns the large display icon for the panel.

int

getMnemonic

()

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel.

abstract

Icon

getSmallDisplayIcon

()

Returns the small display icon for the panel.

void

installChooserPanel

​(

JColorChooser

enclosingChooser)

Invoked when the panel is added to the chooser.

boolean

isColorTransparencySelectionEnabled

()

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

void

paint

​(

Graphics

g)

Draws the panel.

void

setColorTransparencySelectionEnabled

​(boolean b)

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.

void

uninstallChooserPanel

​(

JColorChooser

enclosingChooser)

Invoked when the panel is removed from the chooser.

abstract void

updateChooser

()

Invoked automatically when the model's state changes.

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

getBaseline

,

getBaselineResizeBehavior

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

Builds a new chooser panel.

Returns the color that is currently selected.

Returns the model that the chooser panel is editing.

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic.

Returns a string containing the display name of the panel.

Returns the large display icon for the panel.

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel.

Returns the small display icon for the panel.

Invoked when the panel is added to the chooser.

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

Draws the panel.

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.

Invoked when the panel is removed from the chooser.

Invoked automatically when the model's state changes.

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

getBaseline

,

getBaselineResizeBehavior

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

============ FIELD DETAIL ===========

- Field Detail

- TRANSPARENCY_ENABLED_PROPERTY

```java
public static final
String
TRANSPARENCY_ENABLED_PROPERTY
```

Identifies that the transparency of the color (alpha value) can be
selected

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractColorChooserPanel

```java
public AbstractColorChooserPanel()
```

============ METHOD DETAIL ==========

- Method Detail

- updateChooser

```java
public abstract void updateChooser()
```

Invoked automatically when the model's state changes.
It is also called by

installChooserPanel

to allow
you to set up the initial state of your chooser.
Override this method to update your

ChooserPanel

.

- buildChooser

```java
protected abstract void buildChooser()
```

Builds a new chooser panel.

- getDisplayName

```java
public abstract
String
getDisplayName()
```

Returns a string containing the display name of the panel.

**Returns:** the name of the display panel

- getMnemonic

```java
public int getMnemonic()
```

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel. A return value <= 0 indicates there is no mnemonic.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way.

This implementation returns 0, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:** KeyEvent.VK constant identifying the mnemonic; <= 0 for no
mnemonic
**Since:** 1.4
**See Also:** getDisplayedMnemonicIndex()

- getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic. The look and feel should only use this if

getMnemonic

returns a value > 0.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way. For example,
a look and feel may wish to render each

AbstractColorChooserPanel

in a

JTabbedPane

,
and further use this return value to underline a character in
the

getDisplayName

.

This implementation returns -1, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:** Character index to render mnemonic for; -1 to provide no
visual identifier for this panel.
**Since:** 1.4
**See Also:** getMnemonic()

- getSmallDisplayIcon

```java
public abstract
Icon
getSmallDisplayIcon()
```

Returns the small display icon for the panel.

**Returns:** the small display icon

- getLargeDisplayIcon

```java
public abstract
Icon
getLargeDisplayIcon()
```

Returns the large display icon for the panel.

**Returns:** the large display icon

- installChooserPanel

```java
public void installChooserPanel​(
JColorChooser
enclosingChooser)
```

Invoked when the panel is added to the chooser.
If you override this, be sure to call

super

.

**Parameters:** enclosingChooser

- the chooser to which the panel is to be added
**Throws:** RuntimeException

- if the chooser panel has already been
installed

- uninstallChooserPanel

```java
public void uninstallChooserPanel​(
JColorChooser
enclosingChooser)
```

Invoked when the panel is removed from the chooser.
If override this, be sure to call

super

.

**Parameters:** enclosingChooser

- the chooser from which the panel is to be removed

- getColorSelectionModel

```java
public
ColorSelectionModel
getColorSelectionModel()
```

Returns the model that the chooser panel is editing.

**Returns:** the

ColorSelectionModel

model this panel
is editing

- getColorFromModel

```java
protected
Color
getColorFromModel()
```

Returns the color that is currently selected.

**Returns:** the

Color

that is selected

- setColorTransparencySelectionEnabled

```java
@BeanProperty
(
description
="Sets the transparency of a color selection on or off.")
public void setColorTransparencySelectionEnabled​(boolean b)
```

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.
This method fires a property-changed event, using the string value of

TRANSPARENCY_ENABLED_PROPERTY

as the name
of the property.

The value is a hint and may not be applicable to all types of chooser
panel.

The default value is

true

.

**Parameters:** b

- true if the transparency of a color can be selected
**See Also:** isColorTransparencySelectionEnabled()

- isColorTransparencySelectionEnabled

```java
public boolean isColorTransparencySelectionEnabled()
```

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

**Returns:** true if the transparency of a color can be selected
**See Also:** setColorTransparencySelectionEnabled(boolean)

- paint

```java
public void paint​(
Graphics
g)
```

Draws the panel.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

object
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

Field Detail

- TRANSPARENCY_ENABLED_PROPERTY

```java
public static final
String
TRANSPARENCY_ENABLED_PROPERTY
```

Identifies that the transparency of the color (alpha value) can be
selected

**See Also:** Constant Field Values

---

#### Field Detail

TRANSPARENCY_ENABLED_PROPERTY

```java
public static final
String
TRANSPARENCY_ENABLED_PROPERTY
```

Identifies that the transparency of the color (alpha value) can be
selected

**See Also:** Constant Field Values

---

#### TRANSPARENCY_ENABLED_PROPERTY

public static final

String

TRANSPARENCY_ENABLED_PROPERTY

Identifies that the transparency of the color (alpha value) can be
selected

Constructor Detail

- AbstractColorChooserPanel

```java
public AbstractColorChooserPanel()
```

---

#### Constructor Detail

AbstractColorChooserPanel

```java
public AbstractColorChooserPanel()
```

---

#### AbstractColorChooserPanel

public AbstractColorChooserPanel()

Method Detail

- updateChooser

```java
public abstract void updateChooser()
```

Invoked automatically when the model's state changes.
It is also called by

installChooserPanel

to allow
you to set up the initial state of your chooser.
Override this method to update your

ChooserPanel

.

- buildChooser

```java
protected abstract void buildChooser()
```

Builds a new chooser panel.

- getDisplayName

```java
public abstract
String
getDisplayName()
```

Returns a string containing the display name of the panel.

**Returns:** the name of the display panel

- getMnemonic

```java
public int getMnemonic()
```

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel. A return value <= 0 indicates there is no mnemonic.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way.

This implementation returns 0, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:** KeyEvent.VK constant identifying the mnemonic; <= 0 for no
mnemonic
**Since:** 1.4
**See Also:** getDisplayedMnemonicIndex()

- getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic. The look and feel should only use this if

getMnemonic

returns a value > 0.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way. For example,
a look and feel may wish to render each

AbstractColorChooserPanel

in a

JTabbedPane

,
and further use this return value to underline a character in
the

getDisplayName

.

This implementation returns -1, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:** Character index to render mnemonic for; -1 to provide no
visual identifier for this panel.
**Since:** 1.4
**See Also:** getMnemonic()

- getSmallDisplayIcon

```java
public abstract
Icon
getSmallDisplayIcon()
```

Returns the small display icon for the panel.

**Returns:** the small display icon

- getLargeDisplayIcon

```java
public abstract
Icon
getLargeDisplayIcon()
```

Returns the large display icon for the panel.

**Returns:** the large display icon

- installChooserPanel

```java
public void installChooserPanel​(
JColorChooser
enclosingChooser)
```

Invoked when the panel is added to the chooser.
If you override this, be sure to call

super

.

**Parameters:** enclosingChooser

- the chooser to which the panel is to be added
**Throws:** RuntimeException

- if the chooser panel has already been
installed

- uninstallChooserPanel

```java
public void uninstallChooserPanel​(
JColorChooser
enclosingChooser)
```

Invoked when the panel is removed from the chooser.
If override this, be sure to call

super

.

**Parameters:** enclosingChooser

- the chooser from which the panel is to be removed

- getColorSelectionModel

```java
public
ColorSelectionModel
getColorSelectionModel()
```

Returns the model that the chooser panel is editing.

**Returns:** the

ColorSelectionModel

model this panel
is editing

- getColorFromModel

```java
protected
Color
getColorFromModel()
```

Returns the color that is currently selected.

**Returns:** the

Color

that is selected

- setColorTransparencySelectionEnabled

```java
@BeanProperty
(
description
="Sets the transparency of a color selection on or off.")
public void setColorTransparencySelectionEnabled​(boolean b)
```

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.
This method fires a property-changed event, using the string value of

TRANSPARENCY_ENABLED_PROPERTY

as the name
of the property.

The value is a hint and may not be applicable to all types of chooser
panel.

The default value is

true

.

**Parameters:** b

- true if the transparency of a color can be selected
**See Also:** isColorTransparencySelectionEnabled()

- isColorTransparencySelectionEnabled

```java
public boolean isColorTransparencySelectionEnabled()
```

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

**Returns:** true if the transparency of a color can be selected
**See Also:** setColorTransparencySelectionEnabled(boolean)

- paint

```java
public void paint​(
Graphics
g)
```

Draws the panel.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

object
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

---

#### Method Detail

updateChooser

```java
public abstract void updateChooser()
```

Invoked automatically when the model's state changes.
It is also called by

installChooserPanel

to allow
you to set up the initial state of your chooser.
Override this method to update your

ChooserPanel

.

---

#### updateChooser

public abstract void updateChooser()

Invoked automatically when the model's state changes.
It is also called by

installChooserPanel

to allow
you to set up the initial state of your chooser.
Override this method to update your

ChooserPanel

.

buildChooser

```java
protected abstract void buildChooser()
```

Builds a new chooser panel.

---

#### buildChooser

protected abstract void buildChooser()

Builds a new chooser panel.

getDisplayName

```java
public abstract
String
getDisplayName()
```

Returns a string containing the display name of the panel.

**Returns:** the name of the display panel

---

#### getDisplayName

public abstract

String

getDisplayName()

Returns a string containing the display name of the panel.

getMnemonic

```java
public int getMnemonic()
```

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel. A return value <= 0 indicates there is no mnemonic.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way.

This implementation returns 0, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:** KeyEvent.VK constant identifying the mnemonic; <= 0 for no
mnemonic
**Since:** 1.4
**See Also:** getDisplayedMnemonicIndex()

---

#### getMnemonic

public int getMnemonic()

Provides a hint to the look and feel as to the

KeyEvent.VK

constant that can be used as a mnemonic to
access the panel. A return value <= 0 indicates there is no mnemonic.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way.

This implementation returns 0, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way.

This implementation returns 0, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

This implementation returns 0, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic. The look and feel should only use this if

getMnemonic

returns a value > 0.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way. For example,
a look and feel may wish to render each

AbstractColorChooserPanel

in a

JTabbedPane

,
and further use this return value to underline a character in
the

getDisplayName

.

This implementation returns -1, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

**Returns:** Character index to render mnemonic for; -1 to provide no
visual identifier for this panel.
**Since:** 1.4
**See Also:** getMnemonic()

---

#### getDisplayedMnemonicIndex

public int getDisplayedMnemonicIndex()

Provides a hint to the look and feel as to the index of the character in

getDisplayName

that should be visually identified as the
mnemonic. The look and feel should only use this if

getMnemonic

returns a value > 0.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way. For example,
a look and feel may wish to render each

AbstractColorChooserPanel

in a

JTabbedPane

,
and further use this return value to underline a character in
the

getDisplayName

.

This implementation returns -1, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

The return value here is a hint, it is ultimately up to the look
and feel to honor the return value in some meaningful way. For example,
a look and feel may wish to render each

AbstractColorChooserPanel

in a

JTabbedPane

,
and further use this return value to underline a character in
the

getDisplayName

.

This implementation returns -1, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

This implementation returns -1, indicating the

AbstractColorChooserPanel

does not support a mnemonic,
subclasses wishing a mnemonic will need to override this.

getSmallDisplayIcon

```java
public abstract
Icon
getSmallDisplayIcon()
```

Returns the small display icon for the panel.

**Returns:** the small display icon

---

#### getSmallDisplayIcon

public abstract

Icon

getSmallDisplayIcon()

Returns the small display icon for the panel.

getLargeDisplayIcon

```java
public abstract
Icon
getLargeDisplayIcon()
```

Returns the large display icon for the panel.

**Returns:** the large display icon

---

#### getLargeDisplayIcon

public abstract

Icon

getLargeDisplayIcon()

Returns the large display icon for the panel.

installChooserPanel

```java
public void installChooserPanel​(
JColorChooser
enclosingChooser)
```

Invoked when the panel is added to the chooser.
If you override this, be sure to call

super

.

**Parameters:** enclosingChooser

- the chooser to which the panel is to be added
**Throws:** RuntimeException

- if the chooser panel has already been
installed

---

#### installChooserPanel

public void installChooserPanel​(

JColorChooser

enclosingChooser)

Invoked when the panel is added to the chooser.
If you override this, be sure to call

super

.

uninstallChooserPanel

```java
public void uninstallChooserPanel​(
JColorChooser
enclosingChooser)
```

Invoked when the panel is removed from the chooser.
If override this, be sure to call

super

.

**Parameters:** enclosingChooser

- the chooser from which the panel is to be removed

---

#### uninstallChooserPanel

public void uninstallChooserPanel​(

JColorChooser

enclosingChooser)

Invoked when the panel is removed from the chooser.
If override this, be sure to call

super

.

getColorSelectionModel

```java
public
ColorSelectionModel
getColorSelectionModel()
```

Returns the model that the chooser panel is editing.

**Returns:** the

ColorSelectionModel

model this panel
is editing

---

#### getColorSelectionModel

public

ColorSelectionModel

getColorSelectionModel()

Returns the model that the chooser panel is editing.

getColorFromModel

```java
protected
Color
getColorFromModel()
```

Returns the color that is currently selected.

**Returns:** the

Color

that is selected

---

#### getColorFromModel

protected

Color

getColorFromModel()

Returns the color that is currently selected.

setColorTransparencySelectionEnabled

```java
@BeanProperty
(
description
="Sets the transparency of a color selection on or off.")
public void setColorTransparencySelectionEnabled​(boolean b)
```

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.
This method fires a property-changed event, using the string value of

TRANSPARENCY_ENABLED_PROPERTY

as the name
of the property.

The value is a hint and may not be applicable to all types of chooser
panel.

The default value is

true

.

**Parameters:** b

- true if the transparency of a color can be selected
**See Also:** isColorTransparencySelectionEnabled()

---

#### setColorTransparencySelectionEnabled

@BeanProperty

(

description

="Sets the transparency of a color selection on or off.")
public void setColorTransparencySelectionEnabled​(boolean b)

Sets whether color chooser panel allows to select the transparency
(alpha value) of a color.
This method fires a property-changed event, using the string value of

TRANSPARENCY_ENABLED_PROPERTY

as the name
of the property.

The value is a hint and may not be applicable to all types of chooser
panel.

The default value is

true

.

The value is a hint and may not be applicable to all types of chooser
panel.

The default value is

true

.

The default value is

true

.

isColorTransparencySelectionEnabled

```java
public boolean isColorTransparencySelectionEnabled()
```

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

**Returns:** true if the transparency of a color can be selected
**See Also:** setColorTransparencySelectionEnabled(boolean)

---

#### isColorTransparencySelectionEnabled

public boolean isColorTransparencySelectionEnabled()

Gets whether color chooser panel allows to select the transparency
(alpha value) of a color.

paint

```java
public void paint​(
Graphics
g)
```

Draws the panel.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

object
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

---

#### paint

public void paint​(

Graphics

g)

Draws the panel.

---

