# Class JPasswordField

**Source:** `java.desktop\javax\swing\JPasswordField.html`

### Class Description

```java
@JavaBean
(
description
="Allows the editing of a line of text but doesn\'t show the characters.")
public class
JPasswordField

extends
JTextField
```

JPasswordField

is a lightweight component that allows
the editing of a single line of text where the view indicates
something was typed, but does not show the original characters.
You can find further information and examples in

How to Use Text Fields

,
a section in

The Java Tutorial.

JPasswordField

is intended
to be source-compatible with

java.awt.TextField

used with

echoChar

set. It is provided separately
to make it easier to safely change the UI for the

JTextField

without affecting password entries.

NOTE:

By default, JPasswordField disables input methods; otherwise, input
characters could be visible while they were composed using input methods.
If an application needs the input methods support, please use the
inherited method,

enableInputMethods(true)

.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

Scrollable

,

SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public JPasswordField()

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

---

#### public JPasswordField​(
String
text)

Constructs a new

JPasswordField

initialized
with the specified text. The document model is set to the
default, and the number of columns to 0.

**Parameters:**
- text

- the text to be displayed,

null

if none

---

#### public JPasswordField​(int columns)

Constructs a new empty

JPasswordField

with the specified
number of columns. A default model is created, and the initial string
is set to

null

.

**Parameters:**
- columns

- the number of columns >= 0

---

#### public JPasswordField​(
String
text,
int columns)

Constructs a new

JPasswordField

initialized with
the specified text and columns. The document model is set to
the default.

**Parameters:**
- text

- the text to be displayed,

null

if none
- columns

- the number of columns >= 0

---

#### public JPasswordField​(
Document
doc,

String
txt,
int columns)

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.
This is the constructor through which the other constructors feed.
The echo character is set to '*', but may be changed by the current
Look and Feel. If the document model is

null

, a default one will be created.

**Parameters:**
- doc

- the text storage to use
- txt

- the text to be displayed,

null

if none
- columns

- the number of columns to use to calculate
the preferred width >= 0; if columns is set to zero, the
preferred width will be whatever naturally results from
the component implementation

---

### Method Details

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Returns the name of the L&F class that renders this component.

**Overrides:**
- getUIClassID

in class

JTextField

**Returns:**
- the string "PasswordFieldUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Reloads the pluggable UI. The key used to fetch the
new interface is

getUIClassID()

. The type of
the UI is

TextUI

.

invalidate

is called after setting the UI.

**Overrides:**
- updateUI

in class

JTextComponent

**See Also:**
- JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

**Since:**
- 1.6

---

#### public char getEchoChar()

Returns the character to be used for echoing. The default is '*'.
The default may be different depending on the currently running Look
and Feel. For example, Metal/Ocean's default is a bullet character.

**Returns:**
- the echo character, 0 if unset

**See Also:**
- setEchoChar(char)

,

echoCharIsSet()

---

#### @BeanProperty
(
bound
=false,

visualUpdate
=true,

description
="character to display in place of the real characters")
public void setEchoChar​(char c)

Sets the echo character for this

JPasswordField

.
Note that this is largely a suggestion, since the
view that gets installed can use whatever graphic techniques
it desires to represent the field. Setting a value of 0 indicates
that you wish to see the text as it is typed, similar to
the behavior of a standard

JTextField

.

**Parameters:**
- c

- the echo character to display

**See Also:**
- echoCharIsSet()

,

getEchoChar()

---

#### public boolean echoCharIsSet()

Returns true if this

JPasswordField

has a character
set for echoing. A character is considered to be set if the echo
character is not 0.

**Returns:**
- true if a character is set for echoing

**See Also:**
- setEchoChar(char)

,

getEchoChar()

---

#### public void cut()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and removing the contents from
the model, is not acceptable for a password field.

**Overrides:**
- cut

in class

JTextComponent

**See Also:**
- Toolkit.getSystemClipboard()

,

Clipboard

---

#### public void copy()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and leaving the contents from
the model, is not acceptable for a password field.

**Overrides:**
- copy

in class

JTextComponent

**See Also:**
- Toolkit.getSystemClipboard()

,

Clipboard

---

#### @Deprecated

public
String
getText()

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

.

For security reasons, this method is deprecated. Use the

* getPassword

method instead.

**Overrides:**
- getText

in class

JTextComponent

**Returns:**
- the text

**See Also:**
- JTextComponent.setText(java.lang.String)

---

#### @Deprecated

public
String
getText​(int offs,
int len)
throws
BadLocationException

Fetches a portion of the text represented by the
component. Returns an empty string if length is 0.

For security reasons, this method is deprecated. Use the

getPassword

method instead.

**Overrides:**
- getText

in class

JTextComponent

**Parameters:**
- offs

- the offset >= 0
- len

- the length >= 0

**Returns:**
- the text

**Throws:**
- BadLocationException

- if the offset or length are invalid

---

#### @BeanProperty
(
bound
=false)
public char[] getPassword()

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

. For stronger
security, it is recommended that the returned character array be
cleared after use by setting each character to zero.

**Returns:**
- the text

---

#### protected
String
paramString()

Returns a string representation of this

JPasswordField

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JTextField

**Returns:**
- a string representation of this

JPasswordField

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Returns the

AccessibleContext

associated with this

JPasswordField

. For password fields, the

AccessibleContext

takes the form of an

AccessibleJPasswordField

.
A new

AccessibleJPasswordField

instance is created
if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

JTextField

**Returns:**
- an

AccessibleJPasswordField

that serves as the

AccessibleContext

of this

JPasswordField

---

### Additional Sections

#### Class JPasswordField

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.text.JTextComponent
- - javax.swing.JTextField
- - javax.swing.JPasswordField

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.text.JTextComponent
- - javax.swing.JTextField
- - javax.swing.JPasswordField

java.awt.Container

- javax.swing.JComponent
- - javax.swing.text.JTextComponent
- - javax.swing.JTextField
- - javax.swing.JPasswordField

javax.swing.JComponent

- javax.swing.text.JTextComponent
- - javax.swing.JTextField
- - javax.swing.JPasswordField

javax.swing.text.JTextComponent

- javax.swing.JTextField
- - javax.swing.JPasswordField

javax.swing.JTextField

- javax.swing.JPasswordField

javax.swing.JPasswordField

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

Scrollable

,

SwingConstants

```java
@JavaBean
(
description
="Allows the editing of a line of text but doesn\'t show the characters.")
public class
JPasswordField

extends
JTextField
```

JPasswordField

is a lightweight component that allows
the editing of a single line of text where the view indicates
something was typed, but does not show the original characters.
You can find further information and examples in

How to Use Text Fields

,
a section in

The Java Tutorial.

JPasswordField

is intended
to be source-compatible with

java.awt.TextField

used with

echoChar

set. It is provided separately
to make it easier to safely change the UI for the

JTextField

without affecting password entries.

NOTE:

By default, JPasswordField disables input methods; otherwise, input
characters could be visible while they were composed using input methods.
If an application needs the input methods support, please use the
inherited method,

enableInputMethods(true)

.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**Since:** 1.2
**See Also:** Serialized Form

@JavaBean

(

description

="Allows the editing of a line of text but doesn\'t show the characters.")
public class

JPasswordField

extends

JTextField

JPasswordField

is a lightweight component that allows
the editing of a single line of text where the view indicates
something was typed, but does not show the original characters.
You can find further information and examples in

How to Use Text Fields

,
a section in

The Java Tutorial.

JPasswordField

is intended
to be source-compatible with

java.awt.TextField

used with

echoChar

set. It is provided separately
to make it easier to safely change the UI for the

JTextField

without affecting password entries.

NOTE:

By default, JPasswordField disables input methods; otherwise, input
characters could be visible while they were composed using input methods.
If an application needs the input methods support, please use the
inherited method,

enableInputMethods(true)

.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

JPasswordField

is intended
to be source-compatible with

java.awt.TextField

used with

echoChar

set. It is provided separately
to make it easier to safely change the UI for the

JTextField

without affecting password entries.

NOTE:

By default, JPasswordField disables input methods; otherwise, input
characters could be visible while they were composed using input methods.
If an application needs the input methods support, please use the
inherited method,

enableInputMethods(true)

.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

NOTE:

By default, JPasswordField disables input methods; otherwise, input
characters could be visible while they were composed using input methods.
If an application needs the input methods support, please use the
inherited method,

enableInputMethods(true)

.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

protected class

JPasswordField.AccessibleJPasswordField

This class implements accessibility support for the

JPasswordField

class.

- Nested classes/interfaces declared in class javax.swing.

JTextField

JTextField.AccessibleJTextField

- Nested classes/interfaces declared in class javax.swing.text.

JTextComponent

JTextComponent.AccessibleJTextComponent

,

JTextComponent.DropLocation

,

JTextComponent.KeyBinding

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

JTextField

notifyAction

- Fields declared in class javax.swing.text.

JTextComponent

DEFAULT_KEYMAP

,

FOCUS_ACCELERATOR_KEY

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

JPasswordField

()

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

JPasswordField

​(int columns)

Constructs a new empty

JPasswordField

with the specified
number of columns.

JPasswordField

​(

String

text)

Constructs a new

JPasswordField

initialized
with the specified text.

JPasswordField

​(

String

text,
int columns)

Constructs a new

JPasswordField

initialized with
the specified text and columns.

JPasswordField

​(

Document

doc,

String

txt,
int columns)

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

copy

()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.

void

cut

()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.

boolean

echoCharIsSet

()

Returns true if this

JPasswordField

has a character
set for echoing.

AccessibleContext

getAccessibleContext

()

Returns the

AccessibleContext

associated with this

JPasswordField

.

char

getEchoChar

()

Returns the character to be used for echoing.

char[]

getPassword

()

Returns the text contained in this

TextComponent

.

String

getText

()

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

String

getText

​(int offs,
int len)

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

protected

String

paramString

()

Returns a string representation of this

JPasswordField

.

void

setEchoChar

​(char c)

Sets the echo character for this

JPasswordField

.

void

updateUI

()

Reloads the pluggable UI.

- Methods declared in class javax.swing.

JTextField

actionPropertyChanged

,

addActionListener

,

configurePropertiesFromAction

,

createActionPropertyChangeListener

,

createDefaultModel

,

fireActionPerformed

,

getAction

,

getActionListeners

,

getActions

,

getColumns

,

getColumnWidth

,

getHorizontalAlignment

,

getHorizontalVisibility

,

getPreferredSize

,

getScrollOffset

,

isValidateRoot

,

postActionEvent

,

removeActionListener

,

scrollRectToVisible

,

setAction

,

setActionCommand

,

setColumns

,

setDocument

,

setFont

,

setHorizontalAlignment

,

setScrollOffset

- Methods declared in class javax.swing.text.

JTextComponent

addCaretListener

,

addKeymap

,

fireCaretUpdate

,

getCaret

,

getCaretColor

,

getCaretListeners

,

getCaretPosition

,

getDisabledTextColor

,

getDocument

,

getDragEnabled

,

getDropLocation

,

getDropMode

,

getFocusAccelerator

,

getHighlighter

,

getKeymap

,

getKeymap

,

getMargin

,

getNavigationFilter

,

getPreferredScrollableViewportSize

,

getPrintable

,

getScrollableBlockIncrement

,

getScrollableTracksViewportHeight

,

getScrollableTracksViewportWidth

,

getScrollableUnitIncrement

,

getSelectedText

,

getSelectedTextColor

,

getSelectionColor

,

getSelectionEnd

,

getSelectionStart

,

getToolTipText

,

getUI

,

isEditable

,

loadKeymap

,

modelToView

,

modelToView2D

,

moveCaretPosition

,

paste

,

print

,

print

,

print

,

read

,

removeCaretListener

,

removeKeymap

,

replaceSelection

,

restoreComposedText

,

saveComposedText

,

select

,

selectAll

,

setCaret

,

setCaretColor

,

setCaretPosition

,

setDisabledTextColor

,

setDragEnabled

,

setDropMode

,

setEditable

,

setFocusAccelerator

,

setHighlighter

,

setKeymap

,

setMargin

,

setNavigationFilter

,

setSelectedTextColor

,

setSelectionColor

,

setSelectionEnd

,

setSelectionStart

,

setText

,

setUI

,

viewToModel

,

viewToModel2D

,

write

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

Nested Classes

Modifier and Type

Class

Description

protected class

JPasswordField.AccessibleJPasswordField

This class implements accessibility support for the

JPasswordField

class.

- Nested classes/interfaces declared in class javax.swing.

JTextField

JTextField.AccessibleJTextField

- Nested classes/interfaces declared in class javax.swing.text.

JTextComponent

JTextComponent.AccessibleJTextComponent

,

JTextComponent.DropLocation

,

JTextComponent.KeyBinding

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

This class implements accessibility support for the

JPasswordField

class.

Nested classes/interfaces declared in class javax.swing.

JTextField

JTextField.AccessibleJTextField

---

#### Nested classes/interfaces declared in class javax.swing. JTextField

Nested classes/interfaces declared in class javax.swing.text.

JTextComponent

JTextComponent.AccessibleJTextComponent

,

JTextComponent.DropLocation

,

JTextComponent.KeyBinding

---

#### Nested classes/interfaces declared in class javax.swing.text. JTextComponent

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

JTextField

notifyAction

- Fields declared in class javax.swing.text.

JTextComponent

DEFAULT_KEYMAP

,

FOCUS_ACCELERATOR_KEY

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

Fields declared in class javax.swing.

JTextField

notifyAction

---

#### Fields declared in class javax.swing. JTextField

Fields declared in class javax.swing.text.

JTextComponent

DEFAULT_KEYMAP

,

FOCUS_ACCELERATOR_KEY

---

#### Fields declared in class javax.swing.text. JTextComponent

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

JPasswordField

()

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

JPasswordField

​(int columns)

Constructs a new empty

JPasswordField

with the specified
number of columns.

JPasswordField

​(

String

text)

Constructs a new

JPasswordField

initialized
with the specified text.

JPasswordField

​(

String

text,
int columns)

Constructs a new

JPasswordField

initialized with
the specified text and columns.

JPasswordField

​(

Document

doc,

String

txt,
int columns)

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.

---

#### Constructor Summary

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

Constructs a new empty

JPasswordField

with the specified
number of columns.

Constructs a new

JPasswordField

initialized
with the specified text.

Constructs a new

JPasswordField

initialized with
the specified text and columns.

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

copy

()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.

void

cut

()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.

boolean

echoCharIsSet

()

Returns true if this

JPasswordField

has a character
set for echoing.

AccessibleContext

getAccessibleContext

()

Returns the

AccessibleContext

associated with this

JPasswordField

.

char

getEchoChar

()

Returns the character to be used for echoing.

char[]

getPassword

()

Returns the text contained in this

TextComponent

.

String

getText

()

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

String

getText

​(int offs,
int len)

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

protected

String

paramString

()

Returns a string representation of this

JPasswordField

.

void

setEchoChar

​(char c)

Sets the echo character for this

JPasswordField

.

void

updateUI

()

Reloads the pluggable UI.

- Methods declared in class javax.swing.

JTextField

actionPropertyChanged

,

addActionListener

,

configurePropertiesFromAction

,

createActionPropertyChangeListener

,

createDefaultModel

,

fireActionPerformed

,

getAction

,

getActionListeners

,

getActions

,

getColumns

,

getColumnWidth

,

getHorizontalAlignment

,

getHorizontalVisibility

,

getPreferredSize

,

getScrollOffset

,

isValidateRoot

,

postActionEvent

,

removeActionListener

,

scrollRectToVisible

,

setAction

,

setActionCommand

,

setColumns

,

setDocument

,

setFont

,

setHorizontalAlignment

,

setScrollOffset

- Methods declared in class javax.swing.text.

JTextComponent

addCaretListener

,

addKeymap

,

fireCaretUpdate

,

getCaret

,

getCaretColor

,

getCaretListeners

,

getCaretPosition

,

getDisabledTextColor

,

getDocument

,

getDragEnabled

,

getDropLocation

,

getDropMode

,

getFocusAccelerator

,

getHighlighter

,

getKeymap

,

getKeymap

,

getMargin

,

getNavigationFilter

,

getPreferredScrollableViewportSize

,

getPrintable

,

getScrollableBlockIncrement

,

getScrollableTracksViewportHeight

,

getScrollableTracksViewportWidth

,

getScrollableUnitIncrement

,

getSelectedText

,

getSelectedTextColor

,

getSelectionColor

,

getSelectionEnd

,

getSelectionStart

,

getToolTipText

,

getUI

,

isEditable

,

loadKeymap

,

modelToView

,

modelToView2D

,

moveCaretPosition

,

paste

,

print

,

print

,

print

,

read

,

removeCaretListener

,

removeKeymap

,

replaceSelection

,

restoreComposedText

,

saveComposedText

,

select

,

selectAll

,

setCaret

,

setCaretColor

,

setCaretPosition

,

setDisabledTextColor

,

setDragEnabled

,

setDropMode

,

setEditable

,

setFocusAccelerator

,

setHighlighter

,

setKeymap

,

setMargin

,

setNavigationFilter

,

setSelectedTextColor

,

setSelectionColor

,

setSelectionEnd

,

setSelectionStart

,

setText

,

setUI

,

viewToModel

,

viewToModel2D

,

write

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

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.

Returns true if this

JPasswordField

has a character
set for echoing.

Returns the

AccessibleContext

associated with this

JPasswordField

.

Returns the character to be used for echoing.

Returns the text contained in this

TextComponent

.

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

Returns the name of the L&F class that renders this component.

Returns a string representation of this

JPasswordField

.

Sets the echo character for this

JPasswordField

.

Reloads the pluggable UI.

Methods declared in class javax.swing.

JTextField

actionPropertyChanged

,

addActionListener

,

configurePropertiesFromAction

,

createActionPropertyChangeListener

,

createDefaultModel

,

fireActionPerformed

,

getAction

,

getActionListeners

,

getActions

,

getColumns

,

getColumnWidth

,

getHorizontalAlignment

,

getHorizontalVisibility

,

getPreferredSize

,

getScrollOffset

,

isValidateRoot

,

postActionEvent

,

removeActionListener

,

scrollRectToVisible

,

setAction

,

setActionCommand

,

setColumns

,

setDocument

,

setFont

,

setHorizontalAlignment

,

setScrollOffset

---

#### Methods declared in class javax.swing. JTextField

Methods declared in class javax.swing.text.

JTextComponent

addCaretListener

,

addKeymap

,

fireCaretUpdate

,

getCaret

,

getCaretColor

,

getCaretListeners

,

getCaretPosition

,

getDisabledTextColor

,

getDocument

,

getDragEnabled

,

getDropLocation

,

getDropMode

,

getFocusAccelerator

,

getHighlighter

,

getKeymap

,

getKeymap

,

getMargin

,

getNavigationFilter

,

getPreferredScrollableViewportSize

,

getPrintable

,

getScrollableBlockIncrement

,

getScrollableTracksViewportHeight

,

getScrollableTracksViewportWidth

,

getScrollableUnitIncrement

,

getSelectedText

,

getSelectedTextColor

,

getSelectionColor

,

getSelectionEnd

,

getSelectionStart

,

getToolTipText

,

getUI

,

isEditable

,

loadKeymap

,

modelToView

,

modelToView2D

,

moveCaretPosition

,

paste

,

print

,

print

,

print

,

read

,

removeCaretListener

,

removeKeymap

,

replaceSelection

,

restoreComposedText

,

saveComposedText

,

select

,

selectAll

,

setCaret

,

setCaretColor

,

setCaretPosition

,

setDisabledTextColor

,

setDragEnabled

,

setDropMode

,

setEditable

,

setFocusAccelerator

,

setHighlighter

,

setKeymap

,

setMargin

,

setNavigationFilter

,

setSelectedTextColor

,

setSelectionColor

,

setSelectionEnd

,

setSelectionStart

,

setText

,

setUI

,

viewToModel

,

viewToModel2D

,

write

---

#### Methods declared in class javax.swing.text. JTextComponent

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

- JPasswordField

```java
public JPasswordField()
```

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

- JPasswordField

```java
public JPasswordField​(
String
text)
```

Constructs a new

JPasswordField

initialized
with the specified text. The document model is set to the
default, and the number of columns to 0.

**Parameters:** text

- the text to be displayed,

null

if none

- JPasswordField

```java
public JPasswordField​(int columns)
```

Constructs a new empty

JPasswordField

with the specified
number of columns. A default model is created, and the initial string
is set to

null

.

**Parameters:** columns

- the number of columns >= 0

- JPasswordField

```java
public JPasswordField​(
String
text,
int columns)
```

Constructs a new

JPasswordField

initialized with
the specified text and columns. The document model is set to
the default.

**Parameters:** text

- the text to be displayed,

null

if none
**Parameters:** columns

- the number of columns >= 0

- JPasswordField

```java
public JPasswordField​(
Document
doc,

String
txt,
int columns)
```

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.
This is the constructor through which the other constructors feed.
The echo character is set to '*', but may be changed by the current
Look and Feel. If the document model is

null

, a default one will be created.

**Parameters:** doc

- the text storage to use
**Parameters:** txt

- the text to be displayed,

null

if none
**Parameters:** columns

- the number of columns to use to calculate
the preferred width >= 0; if columns is set to zero, the
preferred width will be whatever naturally results from
the component implementation

============ METHOD DETAIL ==========

- Method Detail

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JTextField
**Returns:** the string "PasswordFieldUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Reloads the pluggable UI. The key used to fetch the
new interface is

getUIClassID()

. The type of
the UI is

TextUI

.

invalidate

is called after setting the UI.

**Overrides:** updateUI

in class

JTextComponent
**Since:** 1.6
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

- getEchoChar

```java
public char getEchoChar()
```

Returns the character to be used for echoing. The default is '*'.
The default may be different depending on the currently running Look
and Feel. For example, Metal/Ocean's default is a bullet character.

**Returns:** the echo character, 0 if unset
**See Also:** setEchoChar(char)

,

echoCharIsSet()

- setEchoChar

```java
@BeanProperty
(
bound
=false,

visualUpdate
=true,

description
="character to display in place of the real characters")
public void setEchoChar​(char c)
```

Sets the echo character for this

JPasswordField

.
Note that this is largely a suggestion, since the
view that gets installed can use whatever graphic techniques
it desires to represent the field. Setting a value of 0 indicates
that you wish to see the text as it is typed, similar to
the behavior of a standard

JTextField

.

**Parameters:** c

- the echo character to display
**See Also:** echoCharIsSet()

,

getEchoChar()

- echoCharIsSet

```java
public boolean echoCharIsSet()
```

Returns true if this

JPasswordField

has a character
set for echoing. A character is considered to be set if the echo
character is not 0.

**Returns:** true if a character is set for echoing
**See Also:** setEchoChar(char)

,

getEchoChar()

- cut

```java
public void cut()
```

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and removing the contents from
the model, is not acceptable for a password field.

**Overrides:** cut

in class

JTextComponent
**See Also:** Toolkit.getSystemClipboard()

,

Clipboard

- copy

```java
public void copy()
```

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and leaving the contents from
the model, is not acceptable for a password field.

**Overrides:** copy

in class

JTextComponent
**See Also:** Toolkit.getSystemClipboard()

,

Clipboard

- getText

```java
@Deprecated

public
String
getText()
```

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

.

For security reasons, this method is deprecated. Use the

* getPassword

method instead.

**Overrides:** getText

in class

JTextComponent
**Returns:** the text
**See Also:** JTextComponent.setText(java.lang.String)

- getText

```java
@Deprecated

public
String
getText​(int offs,
int len)
throws
BadLocationException
```

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

Fetches a portion of the text represented by the
component. Returns an empty string if length is 0.

For security reasons, this method is deprecated. Use the

getPassword

method instead.

**Overrides:** getText

in class

JTextComponent
**Parameters:** offs

- the offset >= 0
**Parameters:** len

- the length >= 0
**Returns:** the text
**Throws:** BadLocationException

- if the offset or length are invalid

- getPassword

```java
@BeanProperty
(
bound
=false)
public char[] getPassword()
```

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

. For stronger
security, it is recommended that the returned character array be
cleared after use by setting each character to zero.

**Returns:** the text

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JPasswordField

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JTextField
**Returns:** a string representation of this

JPasswordField

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with this

JPasswordField

. For password fields, the

AccessibleContext

takes the form of an

AccessibleJPasswordField

.
A new

AccessibleJPasswordField

instance is created
if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JTextField
**Returns:** an

AccessibleJPasswordField

that serves as the

AccessibleContext

of this

JPasswordField

Constructor Detail

- JPasswordField

```java
public JPasswordField()
```

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

- JPasswordField

```java
public JPasswordField​(
String
text)
```

Constructs a new

JPasswordField

initialized
with the specified text. The document model is set to the
default, and the number of columns to 0.

**Parameters:** text

- the text to be displayed,

null

if none

- JPasswordField

```java
public JPasswordField​(int columns)
```

Constructs a new empty

JPasswordField

with the specified
number of columns. A default model is created, and the initial string
is set to

null

.

**Parameters:** columns

- the number of columns >= 0

- JPasswordField

```java
public JPasswordField​(
String
text,
int columns)
```

Constructs a new

JPasswordField

initialized with
the specified text and columns. The document model is set to
the default.

**Parameters:** text

- the text to be displayed,

null

if none
**Parameters:** columns

- the number of columns >= 0

- JPasswordField

```java
public JPasswordField​(
Document
doc,

String
txt,
int columns)
```

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.
This is the constructor through which the other constructors feed.
The echo character is set to '*', but may be changed by the current
Look and Feel. If the document model is

null

, a default one will be created.

**Parameters:** doc

- the text storage to use
**Parameters:** txt

- the text to be displayed,

null

if none
**Parameters:** columns

- the number of columns to use to calculate
the preferred width >= 0; if columns is set to zero, the
preferred width will be whatever naturally results from
the component implementation

---

#### Constructor Detail

JPasswordField

```java
public JPasswordField()
```

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

---

#### JPasswordField

public JPasswordField()

Constructs a new

JPasswordField

,
with a default document,

null

starting
text string, and 0 column width.

JPasswordField

```java
public JPasswordField​(
String
text)
```

Constructs a new

JPasswordField

initialized
with the specified text. The document model is set to the
default, and the number of columns to 0.

**Parameters:** text

- the text to be displayed,

null

if none

---

#### JPasswordField

public JPasswordField​(

String

text)

Constructs a new

JPasswordField

initialized
with the specified text. The document model is set to the
default, and the number of columns to 0.

JPasswordField

```java
public JPasswordField​(int columns)
```

Constructs a new empty

JPasswordField

with the specified
number of columns. A default model is created, and the initial string
is set to

null

.

**Parameters:** columns

- the number of columns >= 0

---

#### JPasswordField

public JPasswordField​(int columns)

Constructs a new empty

JPasswordField

with the specified
number of columns. A default model is created, and the initial string
is set to

null

.

JPasswordField

```java
public JPasswordField​(
String
text,
int columns)
```

Constructs a new

JPasswordField

initialized with
the specified text and columns. The document model is set to
the default.

**Parameters:** text

- the text to be displayed,

null

if none
**Parameters:** columns

- the number of columns >= 0

---

#### JPasswordField

public JPasswordField​(

String

text,
int columns)

Constructs a new

JPasswordField

initialized with
the specified text and columns. The document model is set to
the default.

JPasswordField

```java
public JPasswordField​(
Document
doc,

String
txt,
int columns)
```

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.
This is the constructor through which the other constructors feed.
The echo character is set to '*', but may be changed by the current
Look and Feel. If the document model is

null

, a default one will be created.

**Parameters:** doc

- the text storage to use
**Parameters:** txt

- the text to be displayed,

null

if none
**Parameters:** columns

- the number of columns to use to calculate
the preferred width >= 0; if columns is set to zero, the
preferred width will be whatever naturally results from
the component implementation

---

#### JPasswordField

public JPasswordField​(

Document

doc,

String

txt,
int columns)

Constructs a new

JPasswordField

that uses the
given text storage model and the given number of columns.
This is the constructor through which the other constructors feed.
The echo character is set to '*', but may be changed by the current
Look and Feel. If the document model is

null

, a default one will be created.

Method Detail

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JTextField
**Returns:** the string "PasswordFieldUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Reloads the pluggable UI. The key used to fetch the
new interface is

getUIClassID()

. The type of
the UI is

TextUI

.

invalidate

is called after setting the UI.

**Overrides:** updateUI

in class

JTextComponent
**Since:** 1.6
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

- getEchoChar

```java
public char getEchoChar()
```

Returns the character to be used for echoing. The default is '*'.
The default may be different depending on the currently running Look
and Feel. For example, Metal/Ocean's default is a bullet character.

**Returns:** the echo character, 0 if unset
**See Also:** setEchoChar(char)

,

echoCharIsSet()

- setEchoChar

```java
@BeanProperty
(
bound
=false,

visualUpdate
=true,

description
="character to display in place of the real characters")
public void setEchoChar​(char c)
```

Sets the echo character for this

JPasswordField

.
Note that this is largely a suggestion, since the
view that gets installed can use whatever graphic techniques
it desires to represent the field. Setting a value of 0 indicates
that you wish to see the text as it is typed, similar to
the behavior of a standard

JTextField

.

**Parameters:** c

- the echo character to display
**See Also:** echoCharIsSet()

,

getEchoChar()

- echoCharIsSet

```java
public boolean echoCharIsSet()
```

Returns true if this

JPasswordField

has a character
set for echoing. A character is considered to be set if the echo
character is not 0.

**Returns:** true if a character is set for echoing
**See Also:** setEchoChar(char)

,

getEchoChar()

- cut

```java
public void cut()
```

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and removing the contents from
the model, is not acceptable for a password field.

**Overrides:** cut

in class

JTextComponent
**See Also:** Toolkit.getSystemClipboard()

,

Clipboard

- copy

```java
public void copy()
```

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and leaving the contents from
the model, is not acceptable for a password field.

**Overrides:** copy

in class

JTextComponent
**See Also:** Toolkit.getSystemClipboard()

,

Clipboard

- getText

```java
@Deprecated

public
String
getText()
```

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

.

For security reasons, this method is deprecated. Use the

* getPassword

method instead.

**Overrides:** getText

in class

JTextComponent
**Returns:** the text
**See Also:** JTextComponent.setText(java.lang.String)

- getText

```java
@Deprecated

public
String
getText​(int offs,
int len)
throws
BadLocationException
```

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

Fetches a portion of the text represented by the
component. Returns an empty string if length is 0.

For security reasons, this method is deprecated. Use the

getPassword

method instead.

**Overrides:** getText

in class

JTextComponent
**Parameters:** offs

- the offset >= 0
**Parameters:** len

- the length >= 0
**Returns:** the text
**Throws:** BadLocationException

- if the offset or length are invalid

- getPassword

```java
@BeanProperty
(
bound
=false)
public char[] getPassword()
```

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

. For stronger
security, it is recommended that the returned character array be
cleared after use by setting each character to zero.

**Returns:** the text

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JPasswordField

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JTextField
**Returns:** a string representation of this

JPasswordField

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with this

JPasswordField

. For password fields, the

AccessibleContext

takes the form of an

AccessibleJPasswordField

.
A new

AccessibleJPasswordField

instance is created
if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JTextField
**Returns:** an

AccessibleJPasswordField

that serves as the

AccessibleContext

of this

JPasswordField

---

#### Method Detail

getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JTextField
**Returns:** the string "PasswordFieldUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false)
public

String

getUIClassID()

Returns the name of the L&F class that renders this component.

updateUI

```java
public void updateUI()
```

Reloads the pluggable UI. The key used to fetch the
new interface is

getUIClassID()

. The type of
the UI is

TextUI

.

invalidate

is called after setting the UI.

**Overrides:** updateUI

in class

JTextComponent
**Since:** 1.6
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

---

#### updateUI

public void updateUI()

Reloads the pluggable UI. The key used to fetch the
new interface is

getUIClassID()

. The type of
the UI is

TextUI

.

invalidate

is called after setting the UI.

getEchoChar

```java
public char getEchoChar()
```

Returns the character to be used for echoing. The default is '*'.
The default may be different depending on the currently running Look
and Feel. For example, Metal/Ocean's default is a bullet character.

**Returns:** the echo character, 0 if unset
**See Also:** setEchoChar(char)

,

echoCharIsSet()

---

#### getEchoChar

public char getEchoChar()

Returns the character to be used for echoing. The default is '*'.
The default may be different depending on the currently running Look
and Feel. For example, Metal/Ocean's default is a bullet character.

setEchoChar

```java
@BeanProperty
(
bound
=false,

visualUpdate
=true,

description
="character to display in place of the real characters")
public void setEchoChar​(char c)
```

Sets the echo character for this

JPasswordField

.
Note that this is largely a suggestion, since the
view that gets installed can use whatever graphic techniques
it desires to represent the field. Setting a value of 0 indicates
that you wish to see the text as it is typed, similar to
the behavior of a standard

JTextField

.

**Parameters:** c

- the echo character to display
**See Also:** echoCharIsSet()

,

getEchoChar()

---

#### setEchoChar

@BeanProperty

(

bound

=false,

visualUpdate

=true,

description

="character to display in place of the real characters")
public void setEchoChar​(char c)

Sets the echo character for this

JPasswordField

.
Note that this is largely a suggestion, since the
view that gets installed can use whatever graphic techniques
it desires to represent the field. Setting a value of 0 indicates
that you wish to see the text as it is typed, similar to
the behavior of a standard

JTextField

.

echoCharIsSet

```java
public boolean echoCharIsSet()
```

Returns true if this

JPasswordField

has a character
set for echoing. A character is considered to be set if the echo
character is not 0.

**Returns:** true if a character is set for echoing
**See Also:** setEchoChar(char)

,

getEchoChar()

---

#### echoCharIsSet

public boolean echoCharIsSet()

Returns true if this

JPasswordField

has a character
set for echoing. A character is considered to be set if the echo
character is not 0.

cut

```java
public void cut()
```

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and removing the contents from
the model, is not acceptable for a password field.

**Overrides:** cut

in class

JTextComponent
**See Also:** Toolkit.getSystemClipboard()

,

Clipboard

---

#### cut

public void cut()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and removing the contents from
the model, is not acceptable for a password field.

copy

```java
public void copy()
```

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and leaving the contents from
the model, is not acceptable for a password field.

**Overrides:** copy

in class

JTextComponent
**See Also:** Toolkit.getSystemClipboard()

,

Clipboard

---

#### copy

public void copy()

Invokes

provideErrorFeedback

on the current
look and feel, which typically initiates an error beep.
The normal behavior of transferring the
currently selected range in the associated text model
to the system clipboard, and leaving the contents from
the model, is not acceptable for a password field.

getText

```java
@Deprecated

public
String
getText()
```

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

.

For security reasons, this method is deprecated. Use the

* getPassword

method instead.

**Overrides:** getText

in class

JTextComponent
**Returns:** the text
**See Also:** JTextComponent.setText(java.lang.String)

---

#### getText

@Deprecated

public

String

getText()

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

.

For security reasons, this method is deprecated. Use the

* getPassword

method instead.

For security reasons, this method is deprecated. Use the

* getPassword

method instead.

getText

```java
@Deprecated

public
String
getText​(int offs,
int len)
throws
BadLocationException
```

Deprecated.

As of Java 2 platform v1.2,
replaced by

getPassword

.

Fetches a portion of the text represented by the
component. Returns an empty string if length is 0.

For security reasons, this method is deprecated. Use the

getPassword

method instead.

**Overrides:** getText

in class

JTextComponent
**Parameters:** offs

- the offset >= 0
**Parameters:** len

- the length >= 0
**Returns:** the text
**Throws:** BadLocationException

- if the offset or length are invalid

---

#### getText

@Deprecated

public

String

getText​(int offs,
int len)
throws

BadLocationException

Fetches a portion of the text represented by the
component. Returns an empty string if length is 0.

For security reasons, this method is deprecated. Use the

getPassword

method instead.

For security reasons, this method is deprecated. Use the

getPassword

method instead.

getPassword

```java
@BeanProperty
(
bound
=false)
public char[] getPassword()
```

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

. For stronger
security, it is recommended that the returned character array be
cleared after use by setting each character to zero.

**Returns:** the text

---

#### getPassword

@BeanProperty

(

bound

=false)
public char[] getPassword()

Returns the text contained in this

TextComponent

.
If the underlying document is

null

, will give a

NullPointerException

. For stronger
security, it is recommended that the returned character array be
cleared after use by setting each character to zero.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JPasswordField

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JTextField
**Returns:** a string representation of this

JPasswordField

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JPasswordField

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with this

JPasswordField

. For password fields, the

AccessibleContext

takes the form of an

AccessibleJPasswordField

.
A new

AccessibleJPasswordField

instance is created
if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JTextField
**Returns:** an

AccessibleJPasswordField

that serves as the

AccessibleContext

of this

JPasswordField

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Returns the

AccessibleContext

associated with this

JPasswordField

. For password fields, the

AccessibleContext

takes the form of an

AccessibleJPasswordField

.
A new

AccessibleJPasswordField

instance is created
if necessary.

---

