# Class DefaultListCellRenderer

**Source:** `java.desktop\javax\swing\DefaultListCellRenderer.html`

### Class Description

```java
public class
DefaultListCellRenderer

extends
JLabel

implements
ListCellRenderer
<
Object
>,
Serializable
```

Renders an item in a list.

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,

isOpaque

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default list cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

,

ListCellRenderer

<

Object

>

,

SwingConstants

---

### Field Details

#### protected static
Border
noFocusBorder

No focus border

---

### Constructor Details

#### public DefaultListCellRenderer()

Constructs a default renderer object for an item
in a list.

---

### Method Details

#### public boolean isOpaque()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- isOpaque

in class

JComponent

**Returns:**
- true

if the background is completely opaque
and differs from the JList's background;

false

otherwise

**See Also:**
- JComponent.setOpaque(boolean)

**Since:**
- 1.5

---

#### public void validate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- validate

in class

Container

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

---

#### public void invalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- invalidate

in class

Container

**See Also:**
- Container.validate()

,

Container.layout()

,

LayoutManager2

**Since:**
- 1.5

---

#### public void repaint()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

Component

**See Also:**
- Component.update(Graphics)

**Since:**
- 1.5

---

#### public void revalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- revalidate

in class

JComponent

**See Also:**
- Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

---

#### public void repaint​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

JComponent

**Parameters:**
- tm

- this parameter is not used
- x

- the x value of the dirty region
- y

- the y value of the dirty region
- width

- the width of the dirty region
- height

- the height of the dirty region

**See Also:**
- JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### public void repaint​(
Rectangle
r)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

JComponent

**Parameters:**
- r

- a

Rectangle

containing the dirty region

**See Also:**
- JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

#### public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a byte)
- newValue

- the new value of the property (as a byte)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a char)
- newValue

- the new value of the property (as a char)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a short)
- newValue

- the new value of the property (as a short)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

JComponent

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

#### public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a long)
- newValue

- the new value of the property (as a long)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a float)
- newValue

- the new value of the property (as a float)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a double)
- newValue

- the new value of the property (as a double)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

JComponent

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

### Additional Sections

#### Class DefaultListCellRenderer

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.DefaultListCellRenderer

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.DefaultListCellRenderer

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.DefaultListCellRenderer

javax.swing.JComponent

- javax.swing.JLabel
- - javax.swing.DefaultListCellRenderer

javax.swing.JLabel

- javax.swing.DefaultListCellRenderer

javax.swing.DefaultListCellRenderer

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

ListCellRenderer

<

Object

>

,

SwingConstants

**Direct Known Subclasses:** DefaultListCellRenderer.UIResource

,

MetalFileChooserUI.FileRenderer

,

MetalFileChooserUI.FilterComboBoxRenderer

```java
public class
DefaultListCellRenderer

extends
JLabel

implements
ListCellRenderer
<
Object
>,
Serializable
```

Renders an item in a list.

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,

isOpaque

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default list cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

**Since:** 1.2
**See Also:** Serialized Form

public class

DefaultListCellRenderer

extends

JLabel

implements

ListCellRenderer

<

Object

>,

Serializable

Renders an item in a list.

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,

isOpaque

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default list cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,

isOpaque

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default list cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

Nested Classes

Modifier and Type

Class

Description

static class

DefaultListCellRenderer.UIResource

A subclass of DefaultListCellRenderer that implements UIResource.

- Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

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

protected static

Border

noFocusBorder

No focus border

- Fields declared in class javax.swing.

JLabel

labelFor

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

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultListCellRenderer

()

Constructs a default renderer object for an item
in a list.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.

void

invalidate

()

Overridden for performance reasons.

boolean

isOpaque

()

Overridden for performance reasons.

void

repaint

()

Overridden for performance reasons.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.

void

repaint

​(

Rectangle

r)

Overridden for performance reasons.

void

revalidate

()

Overridden for performance reasons.

void

validate

()

Overridden for performance reasons.

- Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

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

- Methods declared in interface javax.swing.

ListCellRenderer

getListCellRendererComponent

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DefaultListCellRenderer.UIResource

A subclass of DefaultListCellRenderer that implements UIResource.

- Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

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

A subclass of DefaultListCellRenderer that implements UIResource.

Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

---

#### Nested classes/interfaces declared in class javax.swing. JLabel

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

protected static

Border

noFocusBorder

No focus border

- Fields declared in class javax.swing.

JLabel

labelFor

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

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

No focus border

Fields declared in class javax.swing.

JLabel

labelFor

---

#### Fields declared in class javax.swing. JLabel

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

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

DefaultListCellRenderer

()

Constructs a default renderer object for an item
in a list.

---

#### Constructor Summary

Constructs a default renderer object for an item
in a list.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.

void

invalidate

()

Overridden for performance reasons.

boolean

isOpaque

()

Overridden for performance reasons.

void

repaint

()

Overridden for performance reasons.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.

void

repaint

​(

Rectangle

r)

Overridden for performance reasons.

void

revalidate

()

Overridden for performance reasons.

void

validate

()

Overridden for performance reasons.

- Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

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

- Methods declared in interface javax.swing.

ListCellRenderer

getListCellRendererComponent

---

#### Method Summary

Overridden for performance reasons.

Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

,

updateUI

---

#### Methods declared in class javax.swing. JLabel

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

Methods declared in interface javax.swing.

ListCellRenderer

getListCellRendererComponent

---

#### Methods declared in interface javax.swing. ListCellRenderer

============ FIELD DETAIL ===========

- Field Detail

- noFocusBorder

```java
protected static
Border
noFocusBorder
```

No focus border

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultListCellRenderer

```java
public DefaultListCellRenderer()
```

Constructs a default renderer object for an item
in a list.

============ METHOD DETAIL ==========

- Method Detail

- isOpaque

```java
public boolean isOpaque()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** isOpaque

in class

JComponent
**Returns:** true

if the background is completely opaque
and differs from the JList's background;

false

otherwise
**Since:** 1.5
**See Also:** JComponent.setOpaque(boolean)

- validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

- invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

- repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

- revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

Field Detail

- noFocusBorder

```java
protected static
Border
noFocusBorder
```

No focus border

---

#### Field Detail

noFocusBorder

```java
protected static
Border
noFocusBorder
```

No focus border

---

#### noFocusBorder

protected static

Border

noFocusBorder

No focus border

Constructor Detail

- DefaultListCellRenderer

```java
public DefaultListCellRenderer()
```

Constructs a default renderer object for an item
in a list.

---

#### Constructor Detail

DefaultListCellRenderer

```java
public DefaultListCellRenderer()
```

Constructs a default renderer object for an item
in a list.

---

#### DefaultListCellRenderer

public DefaultListCellRenderer()

Constructs a default renderer object for an item
in a list.

Method Detail

- isOpaque

```java
public boolean isOpaque()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** isOpaque

in class

JComponent
**Returns:** true

if the background is completely opaque
and differs from the JList's background;

false

otherwise
**Since:** 1.5
**See Also:** JComponent.setOpaque(boolean)

- validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

- invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

- repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

- revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### Method Detail

isOpaque

```java
public boolean isOpaque()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** isOpaque

in class

JComponent
**Returns:** true

if the background is completely opaque
and differs from the JList's background;

false

otherwise
**Since:** 1.5
**See Also:** JComponent.setOpaque(boolean)

---

#### isOpaque

public boolean isOpaque()

Overridden for performance reasons.
See the

Implementation Note

for more information.

validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

---

#### validate

public void validate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

---

#### invalidate

public void invalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

---

#### repaint

public void repaint()

Overridden for performance reasons.
See the

Implementation Note

for more information.

revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

---

#### revalidate

public void revalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### repaint

public void repaint​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### repaint

public void repaint​(

Rectangle

r)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

---

