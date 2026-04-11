# Class BasicSplitPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicSplitPaneUI.html`

### Class Description

```java
public class
BasicSplitPaneUI

extends
SplitPaneUI
```

A Basic L&F implementation of the SplitPaneUI.

**Direct Known Subclasses:** MetalSplitPaneUI

,

SynthSplitPaneUI

---

### Field Details

#### protected static final
String
NON_CONTINUOUS_DIVIDER

The divider used for non-continuous layout is added to the split pane
with this object.

**See Also:**
- Constant Field Values

---

#### protected static int KEYBOARD_DIVIDER_MOVE_OFFSET

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

---

#### protected
JSplitPane
splitPane

JSplitPane instance this instance is providing
the look and feel for.

---

#### protected
BasicSplitPaneUI.BasicHorizontalLayoutManager
layoutManager

LayoutManager that is created and placed into the split pane.

---

#### protected
BasicSplitPaneDivider
divider

Instance of the divider for this JSplitPane.

---

#### protected
PropertyChangeListener
propertyChangeListener

Instance of the PropertyChangeListener for this JSplitPane.

---

#### protected
FocusListener
focusListener

Instance of the FocusListener for this JSplitPane.

---

#### protected int dividerSize

The size of the divider while the dragging session is valid.

---

#### protected
Component
nonContinuousLayoutDivider

Instance for the shadow of the divider when non continuous layout
is being used.

---

#### protected boolean draggingHW

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

---

#### protected int beginDragDividerLocation

Location of the divider when the dragging session began.

---

#### @Deprecated

protected
KeyStroke
upKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
downKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
leftKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
rightKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
homeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
endKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
dividerResizeToggleKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
ActionListener
keyboardUpLeftListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
ActionListener
keyboardDownRightListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
ActionListener
keyboardHomeListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
ActionListener
keyboardEndListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
ActionListener
keyboardResizeToggleListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

### Constructor Details

#### public BasicSplitPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates a new instance of

BasicSplitPaneUI

.

**Parameters:**
- x

- a component

**Returns:**
- a new instance of

BasicSplitPaneUI

---

#### public void installUI​(
JComponent
c)

Installs the UI.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- the component where this UI delegate is being installed

**See Also:**
- ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### protected void installDefaults()

Installs the UI defaults.

---

#### protected void installListeners()

Installs the event listeners for the UI.

---

#### protected void installKeyboardActions()

Installs the keyboard actions for the UI.

---

#### public void uninstallUI​(
JComponent
c)

Uninstalls the UI.

**Overrides:**
- uninstallUI

in class

ComponentUI

**Parameters:**
- c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### protected void uninstallDefaults()

Uninstalls the UI defaults.

---

#### protected void uninstallListeners()

Uninstalls the event listeners for the UI.

---

#### protected void uninstallKeyboardActions()

Uninstalls the keyboard actions for the UI.

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

**Returns:**
- an instance of

PropertyChangeListener

---

#### protected
FocusListener
createFocusListener()

Creates a

FocusListener

for the

JSplitPane

UI.

**Returns:**
- an instance of

FocusListener

---

#### @Deprecated

protected
ActionListener
createKeyboardUpLeftListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:**
- an instance of

ActionListener

---

#### @Deprecated

protected
ActionListener
createKeyboardDownRightListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:**
- an instance of

ActionListener

---

#### @Deprecated

protected
ActionListener
createKeyboardHomeListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:**
- an instance of

ActionListener

---

#### @Deprecated

protected
ActionListener
createKeyboardEndListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:**
- an instance of

ActionListener

---

#### @Deprecated

protected
ActionListener
createKeyboardResizeToggleListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:**
- an instance of

ActionListener

---

#### public int getOrientation()

Returns the orientation for the

JSplitPane

.

**Returns:**
- the orientation

---

#### public void setOrientation​(int orientation)

Set the orientation for the

JSplitPane

.

**Parameters:**
- orientation

- the orientation

---

#### public boolean isContinuousLayout()

Determines whether the

JSplitPane

is set to use a continuous layout.

**Returns:**
- true

if a continuous layout is set

---

#### public void setContinuousLayout​(boolean b)

Turn continuous layout on/off.

**Parameters:**
- b

- if

true

the continuous layout turns on

---

#### public int getLastDragLocation()

Returns the last drag location of the

JSplitPane

.

**Returns:**
- the last drag location

---

#### public void setLastDragLocation​(int l)

Set the last drag location of the

JSplitPane

.

**Parameters:**
- l

- the drag location

---

#### public
BasicSplitPaneDivider
getDivider()

Returns the divider between the top Components.

**Returns:**
- the divider between the top Components

---

#### protected
Component
createDefaultNonContinuousLayoutDivider()

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

**Returns:**
- the default non continuous layout divider

---

#### protected void setNonContinuousLayoutDivider​(
Component
newDivider)

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session. It is recommended that the passed in component
be a heavy weight.

**Parameters:**
- newDivider

- the new divider

---

#### protected void setNonContinuousLayoutDivider​(
Component
newDivider,
boolean rememberSizes)

Sets the divider to use.

**Parameters:**
- newDivider

- the new divider
- rememberSizes

- if

true

the pane size is remembered

---

#### public
Component
getNonContinuousLayoutDivider()

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session.

**Returns:**
- the divider

---

#### public
JSplitPane
getSplitPane()

Returns the

JSplitPane

this instance is currently contained
in.

**Returns:**
- the instance of

JSplitPane

---

#### public
BasicSplitPaneDivider
createDefaultDivider()

Creates the default divider.

**Returns:**
- the default divider

---

#### public void resetToPreferredSizes​(
JSplitPane
jc)

Messaged to reset the preferred sizes.

**Specified by:**
- resetToPreferredSizes

in class

SplitPaneUI

**Parameters:**
- jc

- a

JSplitPane

---

#### public void setDividerLocation​(
JSplitPane
jc,
int location)

Sets the location of the divider to location.

**Specified by:**
- setDividerLocation

in class

SplitPaneUI

**Parameters:**
- jc

- a

JSplitPane
- location

- an integer specifying the location of the divider

---

#### public int getDividerLocation​(
JSplitPane
jc)

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

**Specified by:**
- getDividerLocation

in class

SplitPaneUI

**Parameters:**
- jc

- a

JSplitPane

**Returns:**
- an integer specifying the location of the divider

---

#### public int getMinimumDividerLocation​(
JSplitPane
jc)

Gets the minimum location of the divider.

**Specified by:**
- getMinimumDividerLocation

in class

SplitPaneUI

**Parameters:**
- jc

- a

JSplitPane

**Returns:**
- and integer specifying the minimum location of the divider

---

#### public int getMaximumDividerLocation​(
JSplitPane
jc)

Gets the maximum location of the divider.

**Specified by:**
- getMaximumDividerLocation

in class

SplitPaneUI

**Parameters:**
- jc

- a

JSplitPane

**Returns:**
- an integer specifying the maximum location of the divider

---

#### public void finishedPaintingChildren​(
JSplitPane
sp,

Graphics
g)

Called when the specified split pane has finished painting
its children.

**Specified by:**
- finishedPaintingChildren

in class

SplitPaneUI

**Parameters:**
- sp

- a

JSplitPane
- g

- the

Graphics

context

---

#### public
Dimension
getPreferredSize​(
JComponent
jc)

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- jc

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object containing given component's preferred
size appropriate for the look and feel

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
getMinimumSize​(
JComponent
jc)

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- jc

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### public
Dimension
getMaximumSize​(
JComponent
jc)

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- jc

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### public
Insets
getInsets​(
JComponent
jc)

Returns the insets. The insets are returned from the border insets
of the current border.

**Parameters:**
- jc

- a component

**Returns:**
- the insets

---

#### protected void resetLayoutManager()

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

---

#### protected void startDragging()

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

---

#### protected void dragDividerTo​(int location)

Messaged during a dragging session to move the divider to the
passed in

location

. If

continuousLayout

is

true

the location is reset and the splitPane validated.

**Parameters:**
- location

- the location of divider

---

#### protected void finishDraggingTo​(int location)

Messaged to finish the dragging session. If not continuous display
the dividers

location

will be reset.

**Parameters:**
- location

- the location of divider

---

#### @Deprecated

protected int getDividerBorderSize()

As of Java 2 platform v1.3 this method is no longer used. Instead
you should set the border on the divider.

Returns the width of one side of the divider border.

**Returns:**
- the width of one side of the divider border

---

### Additional Sections

#### Class BasicSplitPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SplitPaneUI
- - javax.swing.plaf.basic.BasicSplitPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SplitPaneUI
- - javax.swing.plaf.basic.BasicSplitPaneUI

javax.swing.plaf.SplitPaneUI

- javax.swing.plaf.basic.BasicSplitPaneUI

javax.swing.plaf.basic.BasicSplitPaneUI

**Direct Known Subclasses:** MetalSplitPaneUI

,

SynthSplitPaneUI

```java
public class
BasicSplitPaneUI

extends
SplitPaneUI
```

A Basic L&F implementation of the SplitPaneUI.

public class

BasicSplitPaneUI

extends

SplitPaneUI

A Basic L&F implementation of the SplitPaneUI.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicSplitPaneUI.BasicHorizontalLayoutManager

LayoutManager for JSplitPanes that have an orientation of
HORIZONTAL_SPLIT.

class

BasicSplitPaneUI.BasicVerticalLayoutManager

LayoutManager used for JSplitPanes with an orientation of
VERTICAL_SPLIT.

class

BasicSplitPaneUI.FocusHandler

Implementation of the FocusListener that the JSplitPane UI uses.

class

BasicSplitPaneUI.KeyboardDownRightHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardEndHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardHomeHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardResizeToggleHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardUpLeftHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.PropertyHandler

Implementation of the PropertyChangeListener
that the JSplitPane UI uses.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

beginDragDividerLocation

Location of the divider when the dragging session began.

protected

BasicSplitPaneDivider

divider

Instance of the divider for this JSplitPane.

protected

KeyStroke

dividerResizeToggleKey

Deprecated.

As of Java 2 platform v1.3.

protected int

dividerSize

The size of the divider while the dragging session is valid.

protected

KeyStroke

downKey

Deprecated.

As of Java 2 platform v1.3.

protected boolean

draggingHW

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

protected

KeyStroke

endKey

Deprecated.

As of Java 2 platform v1.3.

protected

FocusListener

focusListener

Instance of the FocusListener for this JSplitPane.

protected

KeyStroke

homeKey

Deprecated.

As of Java 2 platform v1.3.

protected static int

KEYBOARD_DIVIDER_MOVE_OFFSET

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

protected

ActionListener

keyboardDownRightListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardEndListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardHomeListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardResizeToggleListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardUpLeftListener

Deprecated.

As of Java 2 platform v1.3.

protected

BasicSplitPaneUI.BasicHorizontalLayoutManager

layoutManager

LayoutManager that is created and placed into the split pane.

protected

KeyStroke

leftKey

Deprecated.

As of Java 2 platform v1.3.

protected static

String

NON_CONTINUOUS_DIVIDER

The divider used for non-continuous layout is added to the split pane
with this object.

protected

Component

nonContinuousLayoutDivider

Instance for the shadow of the divider when non continuous layout
is being used.

protected

PropertyChangeListener

propertyChangeListener

Instance of the PropertyChangeListener for this JSplitPane.

protected

KeyStroke

rightKey

Deprecated.

As of Java 2 platform v1.3.

protected

JSplitPane

splitPane

JSplitPane instance this instance is providing
the look and feel for.

protected

KeyStroke

upKey

Deprecated.

As of Java 2 platform v1.3.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicSplitPaneUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

BasicSplitPaneDivider

createDefaultDivider

()

Creates the default divider.

protected

Component

createDefaultNonContinuousLayoutDivider

()

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

protected

FocusListener

createFocusListener

()

Creates a

FocusListener

for the

JSplitPane

UI.

protected

ActionListener

createKeyboardDownRightListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardEndListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardHomeListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardResizeToggleListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardUpLeftListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

static

ComponentUI

createUI

​(

JComponent

x)

Creates a new instance of

BasicSplitPaneUI

.

protected void

dragDividerTo

​(int location)

Messaged during a dragging session to move the divider to the
passed in

location

.

protected void

finishDraggingTo

​(int location)

Messaged to finish the dragging session.

void

finishedPaintingChildren

​(

JSplitPane

sp,

Graphics

g)

Called when the specified split pane has finished painting
its children.

BasicSplitPaneDivider

getDivider

()

Returns the divider between the top Components.

protected int

getDividerBorderSize

()

Deprecated.

As of Java 2 platform v1.3, instead set the border on the
divider.

int

getDividerLocation

​(

JSplitPane

jc)

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

Insets

getInsets

​(

JComponent

jc)

Returns the insets.

int

getLastDragLocation

()

Returns the last drag location of the

JSplitPane

.

int

getMaximumDividerLocation

​(

JSplitPane

jc)

Gets the maximum location of the divider.

Dimension

getMaximumSize

​(

JComponent

jc)

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

int

getMinimumDividerLocation

​(

JSplitPane

jc)

Gets the minimum location of the divider.

Dimension

getMinimumSize

​(

JComponent

jc)

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

Component

getNonContinuousLayoutDivider

()

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout.

int

getOrientation

()

Returns the orientation for the

JSplitPane

.

Dimension

getPreferredSize

​(

JComponent

jc)

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

JSplitPane

getSplitPane

()

Returns the

JSplitPane

this instance is currently contained
in.

protected void

installDefaults

()

Installs the UI defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions for the UI.

protected void

installListeners

()

Installs the event listeners for the UI.

void

installUI

​(

JComponent

c)

Installs the UI.

boolean

isContinuousLayout

()

Determines whether the

JSplitPane

is set to use a continuous layout.

protected void

resetLayoutManager

()

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

void

resetToPreferredSizes

​(

JSplitPane

jc)

Messaged to reset the preferred sizes.

void

setContinuousLayout

​(boolean b)

Turn continuous layout on/off.

void

setDividerLocation

​(

JSplitPane

jc,
int location)

Sets the location of the divider to location.

void

setLastDragLocation

​(int l)

Set the last drag location of the

JSplitPane

.

protected void

setNonContinuousLayoutDivider

​(

Component

newDivider)

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout.

protected void

setNonContinuousLayoutDivider

​(

Component

newDivider,
boolean rememberSizes)

Sets the divider to use.

void

setOrientation

​(int orientation)

Set the orientation for the

JSplitPane

.

protected void

startDragging

()

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

protected void

uninstallDefaults

()

Uninstalls the UI defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions for the UI.

protected void

uninstallListeners

()

Uninstalls the event listeners for the UI.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

paint

,

update

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

toString

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

class

BasicSplitPaneUI.BasicHorizontalLayoutManager

LayoutManager for JSplitPanes that have an orientation of
HORIZONTAL_SPLIT.

class

BasicSplitPaneUI.BasicVerticalLayoutManager

LayoutManager used for JSplitPanes with an orientation of
VERTICAL_SPLIT.

class

BasicSplitPaneUI.FocusHandler

Implementation of the FocusListener that the JSplitPane UI uses.

class

BasicSplitPaneUI.KeyboardDownRightHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardEndHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardHomeHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardResizeToggleHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.KeyboardUpLeftHandler

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

class

BasicSplitPaneUI.PropertyHandler

Implementation of the PropertyChangeListener
that the JSplitPane UI uses.

---

#### Nested Class Summary

LayoutManager for JSplitPanes that have an orientation of
HORIZONTAL_SPLIT.

LayoutManager used for JSplitPanes with an orientation of
VERTICAL_SPLIT.

Implementation of the FocusListener that the JSplitPane UI uses.

Implementation of an ActionListener that the JSplitPane UI uses for
handling specific key presses.

Implementation of the PropertyChangeListener
that the JSplitPane UI uses.

Field Summary

Fields

Modifier and Type

Field

Description

protected int

beginDragDividerLocation

Location of the divider when the dragging session began.

protected

BasicSplitPaneDivider

divider

Instance of the divider for this JSplitPane.

protected

KeyStroke

dividerResizeToggleKey

Deprecated.

As of Java 2 platform v1.3.

protected int

dividerSize

The size of the divider while the dragging session is valid.

protected

KeyStroke

downKey

Deprecated.

As of Java 2 platform v1.3.

protected boolean

draggingHW

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

protected

KeyStroke

endKey

Deprecated.

As of Java 2 platform v1.3.

protected

FocusListener

focusListener

Instance of the FocusListener for this JSplitPane.

protected

KeyStroke

homeKey

Deprecated.

As of Java 2 platform v1.3.

protected static int

KEYBOARD_DIVIDER_MOVE_OFFSET

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

protected

ActionListener

keyboardDownRightListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardEndListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardHomeListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardResizeToggleListener

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

keyboardUpLeftListener

Deprecated.

As of Java 2 platform v1.3.

protected

BasicSplitPaneUI.BasicHorizontalLayoutManager

layoutManager

LayoutManager that is created and placed into the split pane.

protected

KeyStroke

leftKey

Deprecated.

As of Java 2 platform v1.3.

protected static

String

NON_CONTINUOUS_DIVIDER

The divider used for non-continuous layout is added to the split pane
with this object.

protected

Component

nonContinuousLayoutDivider

Instance for the shadow of the divider when non continuous layout
is being used.

protected

PropertyChangeListener

propertyChangeListener

Instance of the PropertyChangeListener for this JSplitPane.

protected

KeyStroke

rightKey

Deprecated.

As of Java 2 platform v1.3.

protected

JSplitPane

splitPane

JSplitPane instance this instance is providing
the look and feel for.

protected

KeyStroke

upKey

Deprecated.

As of Java 2 platform v1.3.

---

#### Field Summary

Location of the divider when the dragging session began.

Instance of the divider for this JSplitPane.

Deprecated.

As of Java 2 platform v1.3.

The size of the divider while the dragging session is valid.

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

Instance of the FocusListener for this JSplitPane.

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

LayoutManager that is created and placed into the split pane.

The divider used for non-continuous layout is added to the split pane
with this object.

Instance for the shadow of the divider when non continuous layout
is being used.

Instance of the PropertyChangeListener for this JSplitPane.

JSplitPane instance this instance is providing
the look and feel for.

Constructor Summary

Constructors

Constructor

Description

BasicSplitPaneUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

BasicSplitPaneDivider

createDefaultDivider

()

Creates the default divider.

protected

Component

createDefaultNonContinuousLayoutDivider

()

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

protected

FocusListener

createFocusListener

()

Creates a

FocusListener

for the

JSplitPane

UI.

protected

ActionListener

createKeyboardDownRightListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardEndListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardHomeListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardResizeToggleListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

ActionListener

createKeyboardUpLeftListener

()

Deprecated.

As of Java 2 platform v1.3.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

static

ComponentUI

createUI

​(

JComponent

x)

Creates a new instance of

BasicSplitPaneUI

.

protected void

dragDividerTo

​(int location)

Messaged during a dragging session to move the divider to the
passed in

location

.

protected void

finishDraggingTo

​(int location)

Messaged to finish the dragging session.

void

finishedPaintingChildren

​(

JSplitPane

sp,

Graphics

g)

Called when the specified split pane has finished painting
its children.

BasicSplitPaneDivider

getDivider

()

Returns the divider between the top Components.

protected int

getDividerBorderSize

()

Deprecated.

As of Java 2 platform v1.3, instead set the border on the
divider.

int

getDividerLocation

​(

JSplitPane

jc)

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

Insets

getInsets

​(

JComponent

jc)

Returns the insets.

int

getLastDragLocation

()

Returns the last drag location of the

JSplitPane

.

int

getMaximumDividerLocation

​(

JSplitPane

jc)

Gets the maximum location of the divider.

Dimension

getMaximumSize

​(

JComponent

jc)

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

int

getMinimumDividerLocation

​(

JSplitPane

jc)

Gets the minimum location of the divider.

Dimension

getMinimumSize

​(

JComponent

jc)

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

Component

getNonContinuousLayoutDivider

()

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout.

int

getOrientation

()

Returns the orientation for the

JSplitPane

.

Dimension

getPreferredSize

​(

JComponent

jc)

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

JSplitPane

getSplitPane

()

Returns the

JSplitPane

this instance is currently contained
in.

protected void

installDefaults

()

Installs the UI defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions for the UI.

protected void

installListeners

()

Installs the event listeners for the UI.

void

installUI

​(

JComponent

c)

Installs the UI.

boolean

isContinuousLayout

()

Determines whether the

JSplitPane

is set to use a continuous layout.

protected void

resetLayoutManager

()

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

void

resetToPreferredSizes

​(

JSplitPane

jc)

Messaged to reset the preferred sizes.

void

setContinuousLayout

​(boolean b)

Turn continuous layout on/off.

void

setDividerLocation

​(

JSplitPane

jc,
int location)

Sets the location of the divider to location.

void

setLastDragLocation

​(int l)

Set the last drag location of the

JSplitPane

.

protected void

setNonContinuousLayoutDivider

​(

Component

newDivider)

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout.

protected void

setNonContinuousLayoutDivider

​(

Component

newDivider,
boolean rememberSizes)

Sets the divider to use.

void

setOrientation

​(int orientation)

Set the orientation for the

JSplitPane

.

protected void

startDragging

()

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

protected void

uninstallDefaults

()

Uninstalls the UI defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions for the UI.

protected void

uninstallListeners

()

Uninstalls the event listeners for the UI.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

paint

,

update

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Creates the default divider.

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

Creates a

FocusListener

for the

JSplitPane

UI.

Deprecated.

As of Java 2 platform v1.3.

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

Creates a new instance of

BasicSplitPaneUI

.

Messaged during a dragging session to move the divider to the
passed in

location

.

Messaged to finish the dragging session.

Called when the specified split pane has finished painting
its children.

Returns the divider between the top Components.

Deprecated.

As of Java 2 platform v1.3, instead set the border on the
divider.

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

Returns the insets.

Returns the last drag location of the

JSplitPane

.

Gets the maximum location of the divider.

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

Gets the minimum location of the divider.

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout.

Returns the orientation for the

JSplitPane

.

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

Returns the

JSplitPane

this instance is currently contained
in.

Installs the UI defaults.

Installs the keyboard actions for the UI.

Installs the event listeners for the UI.

Installs the UI.

Determines whether the

JSplitPane

is set to use a continuous layout.

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

Messaged to reset the preferred sizes.

Turn continuous layout on/off.

Sets the location of the divider to location.

Set the last drag location of the

JSplitPane

.

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout.

Sets the divider to use.

Set the orientation for the

JSplitPane

.

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

Uninstalls the UI defaults.

Uninstalls the keyboard actions for the UI.

Uninstalls the event listeners for the UI.

Uninstalls the UI.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

paint

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

toString

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

- NON_CONTINUOUS_DIVIDER

```java
protected static final
String
NON_CONTINUOUS_DIVIDER
```

The divider used for non-continuous layout is added to the split pane
with this object.

**See Also:** Constant Field Values

- KEYBOARD_DIVIDER_MOVE_OFFSET

```java
protected static int KEYBOARD_DIVIDER_MOVE_OFFSET
```

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

- splitPane

```java
protected
JSplitPane
splitPane
```

JSplitPane instance this instance is providing
the look and feel for.

- layoutManager

```java
protected
BasicSplitPaneUI.BasicHorizontalLayoutManager
layoutManager
```

LayoutManager that is created and placed into the split pane.

- divider

```java
protected
BasicSplitPaneDivider
divider
```

Instance of the divider for this JSplitPane.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Instance of the PropertyChangeListener for this JSplitPane.

- focusListener

```java
protected
FocusListener
focusListener
```

Instance of the FocusListener for this JSplitPane.

- dividerSize

```java
protected int dividerSize
```

The size of the divider while the dragging session is valid.

- nonContinuousLayoutDivider

```java
protected
Component
nonContinuousLayoutDivider
```

Instance for the shadow of the divider when non continuous layout
is being used.

- draggingHW

```java
protected boolean draggingHW
```

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

- beginDragDividerLocation

```java
protected int beginDragDividerLocation
```

Location of the divider when the dragging session began.

- upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- homeKey

```java
@Deprecated

protected
KeyStroke
homeKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- endKey

```java
@Deprecated

protected
KeyStroke
endKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- dividerResizeToggleKey

```java
@Deprecated

protected
KeyStroke
dividerResizeToggleKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardUpLeftListener

```java
@Deprecated

protected
ActionListener
keyboardUpLeftListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardDownRightListener

```java
@Deprecated

protected
ActionListener
keyboardDownRightListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardHomeListener

```java
@Deprecated

protected
ActionListener
keyboardHomeListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardEndListener

```java
@Deprecated

protected
ActionListener
keyboardEndListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardResizeToggleListener

```java
@Deprecated

protected
ActionListener
keyboardResizeToggleListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicSplitPaneUI

```java
public BasicSplitPaneUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new instance of

BasicSplitPaneUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicSplitPaneUI

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- installDefaults

```java
protected void installDefaults()
```

Installs the UI defaults.

- installListeners

```java
protected void installListeners()
```

Installs the event listeners for the UI.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions for the UI.

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the UI defaults.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the event listeners for the UI.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions for the UI.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

**Returns:** an instance of

PropertyChangeListener

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a

FocusListener

for the

JSplitPane

UI.

**Returns:** an instance of

FocusListener

- createKeyboardUpLeftListener

```java
@Deprecated

protected
ActionListener
createKeyboardUpLeftListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardDownRightListener

```java
@Deprecated

protected
ActionListener
createKeyboardDownRightListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardHomeListener

```java
@Deprecated

protected
ActionListener
createKeyboardHomeListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardEndListener

```java
@Deprecated

protected
ActionListener
createKeyboardEndListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardResizeToggleListener

```java
@Deprecated

protected
ActionListener
createKeyboardResizeToggleListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- getOrientation

```java
public int getOrientation()
```

Returns the orientation for the

JSplitPane

.

**Returns:** the orientation

- setOrientation

```java
public void setOrientation​(int orientation)
```

Set the orientation for the

JSplitPane

.

**Parameters:** orientation

- the orientation

- isContinuousLayout

```java
public boolean isContinuousLayout()
```

Determines whether the

JSplitPane

is set to use a continuous layout.

**Returns:** true

if a continuous layout is set

- setContinuousLayout

```java
public void setContinuousLayout​(boolean b)
```

Turn continuous layout on/off.

**Parameters:** b

- if

true

the continuous layout turns on

- getLastDragLocation

```java
public int getLastDragLocation()
```

Returns the last drag location of the

JSplitPane

.

**Returns:** the last drag location

- setLastDragLocation

```java
public void setLastDragLocation​(int l)
```

Set the last drag location of the

JSplitPane

.

**Parameters:** l

- the drag location

- getDivider

```java
public
BasicSplitPaneDivider
getDivider()
```

Returns the divider between the top Components.

**Returns:** the divider between the top Components

- createDefaultNonContinuousLayoutDivider

```java
protected
Component
createDefaultNonContinuousLayoutDivider()
```

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

**Returns:** the default non continuous layout divider

- setNonContinuousLayoutDivider

```java
protected void setNonContinuousLayoutDivider​(
Component
newDivider)
```

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session. It is recommended that the passed in component
be a heavy weight.

**Parameters:** newDivider

- the new divider

- setNonContinuousLayoutDivider

```java
protected void setNonContinuousLayoutDivider​(
Component
newDivider,
boolean rememberSizes)
```

Sets the divider to use.

**Parameters:** newDivider

- the new divider
**Parameters:** rememberSizes

- if

true

the pane size is remembered

- getNonContinuousLayoutDivider

```java
public
Component
getNonContinuousLayoutDivider()
```

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session.

**Returns:** the divider

- getSplitPane

```java
public
JSplitPane
getSplitPane()
```

Returns the

JSplitPane

this instance is currently contained
in.

**Returns:** the instance of

JSplitPane

- createDefaultDivider

```java
public
BasicSplitPaneDivider
createDefaultDivider()
```

Creates the default divider.

**Returns:** the default divider

- resetToPreferredSizes

```java
public void resetToPreferredSizes​(
JSplitPane
jc)
```

Messaged to reset the preferred sizes.

**Specified by:** resetToPreferredSizes

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane

- setDividerLocation

```java
public void setDividerLocation​(
JSplitPane
jc,
int location)
```

Sets the location of the divider to location.

**Specified by:** setDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Parameters:** location

- an integer specifying the location of the divider

- getDividerLocation

```java
public int getDividerLocation​(
JSplitPane
jc)
```

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

**Specified by:** getDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the location of the divider

- getMinimumDividerLocation

```java
public int getMinimumDividerLocation​(
JSplitPane
jc)
```

Gets the minimum location of the divider.

**Specified by:** getMinimumDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** and integer specifying the minimum location of the divider

- getMaximumDividerLocation

```java
public int getMaximumDividerLocation​(
JSplitPane
jc)
```

Gets the maximum location of the divider.

**Specified by:** getMaximumDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the maximum location of the divider

- finishedPaintingChildren

```java
public void finishedPaintingChildren​(
JSplitPane
sp,

Graphics
g)
```

Called when the specified split pane has finished painting
its children.

**Specified by:** finishedPaintingChildren

in class

SplitPaneUI
**Parameters:** sp

- a

JSplitPane
**Parameters:** g

- the

Graphics

context

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
jc)
```

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** jc

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
jc)
```

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** jc

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
jc)
```

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** jc

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- getInsets

```java
public
Insets
getInsets​(
JComponent
jc)
```

Returns the insets. The insets are returned from the border insets
of the current border.

**Parameters:** jc

- a component
**Returns:** the insets

- resetLayoutManager

```java
protected void resetLayoutManager()
```

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

- startDragging

```java
protected void startDragging()
```

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

- dragDividerTo

```java
protected void dragDividerTo​(int location)
```

Messaged during a dragging session to move the divider to the
passed in

location

. If

continuousLayout

is

true

the location is reset and the splitPane validated.

**Parameters:** location

- the location of divider

- finishDraggingTo

```java
protected void finishDraggingTo​(int location)
```

Messaged to finish the dragging session. If not continuous display
the dividers

location

will be reset.

**Parameters:** location

- the location of divider

- getDividerBorderSize

```java
@Deprecated

protected int getDividerBorderSize()
```

Deprecated.

As of Java 2 platform v1.3, instead set the border on the
divider.

As of Java 2 platform v1.3 this method is no longer used. Instead
you should set the border on the divider.

Returns the width of one side of the divider border.

**Returns:** the width of one side of the divider border

Field Detail

- NON_CONTINUOUS_DIVIDER

```java
protected static final
String
NON_CONTINUOUS_DIVIDER
```

The divider used for non-continuous layout is added to the split pane
with this object.

**See Also:** Constant Field Values

- KEYBOARD_DIVIDER_MOVE_OFFSET

```java
protected static int KEYBOARD_DIVIDER_MOVE_OFFSET
```

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

- splitPane

```java
protected
JSplitPane
splitPane
```

JSplitPane instance this instance is providing
the look and feel for.

- layoutManager

```java
protected
BasicSplitPaneUI.BasicHorizontalLayoutManager
layoutManager
```

LayoutManager that is created and placed into the split pane.

- divider

```java
protected
BasicSplitPaneDivider
divider
```

Instance of the divider for this JSplitPane.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Instance of the PropertyChangeListener for this JSplitPane.

- focusListener

```java
protected
FocusListener
focusListener
```

Instance of the FocusListener for this JSplitPane.

- dividerSize

```java
protected int dividerSize
```

The size of the divider while the dragging session is valid.

- nonContinuousLayoutDivider

```java
protected
Component
nonContinuousLayoutDivider
```

Instance for the shadow of the divider when non continuous layout
is being used.

- draggingHW

```java
protected boolean draggingHW
```

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

- beginDragDividerLocation

```java
protected int beginDragDividerLocation
```

Location of the divider when the dragging session began.

- upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- homeKey

```java
@Deprecated

protected
KeyStroke
homeKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- endKey

```java
@Deprecated

protected
KeyStroke
endKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- dividerResizeToggleKey

```java
@Deprecated

protected
KeyStroke
dividerResizeToggleKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardUpLeftListener

```java
@Deprecated

protected
ActionListener
keyboardUpLeftListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardDownRightListener

```java
@Deprecated

protected
ActionListener
keyboardDownRightListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardHomeListener

```java
@Deprecated

protected
ActionListener
keyboardHomeListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardEndListener

```java
@Deprecated

protected
ActionListener
keyboardEndListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- keyboardResizeToggleListener

```java
@Deprecated

protected
ActionListener
keyboardResizeToggleListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### Field Detail

NON_CONTINUOUS_DIVIDER

```java
protected static final
String
NON_CONTINUOUS_DIVIDER
```

The divider used for non-continuous layout is added to the split pane
with this object.

**See Also:** Constant Field Values

---

#### NON_CONTINUOUS_DIVIDER

protected static final

String

NON_CONTINUOUS_DIVIDER

The divider used for non-continuous layout is added to the split pane
with this object.

KEYBOARD_DIVIDER_MOVE_OFFSET

```java
protected static int KEYBOARD_DIVIDER_MOVE_OFFSET
```

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

---

#### KEYBOARD_DIVIDER_MOVE_OFFSET

protected static int KEYBOARD_DIVIDER_MOVE_OFFSET

How far (relative) the divider does move when it is moved around by
the cursor keys on the keyboard.

splitPane

```java
protected
JSplitPane
splitPane
```

JSplitPane instance this instance is providing
the look and feel for.

---

#### splitPane

protected

JSplitPane

splitPane

JSplitPane instance this instance is providing
the look and feel for.

layoutManager

```java
protected
BasicSplitPaneUI.BasicHorizontalLayoutManager
layoutManager
```

LayoutManager that is created and placed into the split pane.

---

#### layoutManager

protected

BasicSplitPaneUI.BasicHorizontalLayoutManager

layoutManager

LayoutManager that is created and placed into the split pane.

divider

```java
protected
BasicSplitPaneDivider
divider
```

Instance of the divider for this JSplitPane.

---

#### divider

protected

BasicSplitPaneDivider

divider

Instance of the divider for this JSplitPane.

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Instance of the PropertyChangeListener for this JSplitPane.

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

Instance of the PropertyChangeListener for this JSplitPane.

focusListener

```java
protected
FocusListener
focusListener
```

Instance of the FocusListener for this JSplitPane.

---

#### focusListener

protected

FocusListener

focusListener

Instance of the FocusListener for this JSplitPane.

dividerSize

```java
protected int dividerSize
```

The size of the divider while the dragging session is valid.

---

#### dividerSize

protected int dividerSize

The size of the divider while the dragging session is valid.

nonContinuousLayoutDivider

```java
protected
Component
nonContinuousLayoutDivider
```

Instance for the shadow of the divider when non continuous layout
is being used.

---

#### nonContinuousLayoutDivider

protected

Component

nonContinuousLayoutDivider

Instance for the shadow of the divider when non continuous layout
is being used.

draggingHW

```java
protected boolean draggingHW
```

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

---

#### draggingHW

protected boolean draggingHW

Set to true in startDragging if any of the children
(not including the nonContinuousLayoutDivider) are heavy weights.

beginDragDividerLocation

```java
protected int beginDragDividerLocation
```

Location of the divider when the dragging session began.

---

#### beginDragDividerLocation

protected int beginDragDividerLocation

Location of the divider when the dragging session began.

upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### upKey

@Deprecated

protected

KeyStroke

upKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### downKey

@Deprecated

protected

KeyStroke

downKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### leftKey

@Deprecated

protected

KeyStroke

leftKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### rightKey

@Deprecated

protected

KeyStroke

rightKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

homeKey

```java
@Deprecated

protected
KeyStroke
homeKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### homeKey

@Deprecated

protected

KeyStroke

homeKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

endKey

```java
@Deprecated

protected
KeyStroke
endKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### endKey

@Deprecated

protected

KeyStroke

endKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

dividerResizeToggleKey

```java
@Deprecated

protected
KeyStroke
dividerResizeToggleKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### dividerResizeToggleKey

@Deprecated

protected

KeyStroke

dividerResizeToggleKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

keyboardUpLeftListener

```java
@Deprecated

protected
ActionListener
keyboardUpLeftListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### keyboardUpLeftListener

@Deprecated

protected

ActionListener

keyboardUpLeftListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

keyboardDownRightListener

```java
@Deprecated

protected
ActionListener
keyboardDownRightListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### keyboardDownRightListener

@Deprecated

protected

ActionListener

keyboardDownRightListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

keyboardHomeListener

```java
@Deprecated

protected
ActionListener
keyboardHomeListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### keyboardHomeListener

@Deprecated

protected

ActionListener

keyboardHomeListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

keyboardEndListener

```java
@Deprecated

protected
ActionListener
keyboardEndListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### keyboardEndListener

@Deprecated

protected

ActionListener

keyboardEndListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

keyboardResizeToggleListener

```java
@Deprecated

protected
ActionListener
keyboardResizeToggleListener
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### keyboardResizeToggleListener

@Deprecated

protected

ActionListener

keyboardResizeToggleListener

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

Constructor Detail

- BasicSplitPaneUI

```java
public BasicSplitPaneUI()
```

---

#### Constructor Detail

BasicSplitPaneUI

```java
public BasicSplitPaneUI()
```

---

#### BasicSplitPaneUI

public BasicSplitPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new instance of

BasicSplitPaneUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicSplitPaneUI

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- installDefaults

```java
protected void installDefaults()
```

Installs the UI defaults.

- installListeners

```java
protected void installListeners()
```

Installs the event listeners for the UI.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions for the UI.

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the UI defaults.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the event listeners for the UI.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions for the UI.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

**Returns:** an instance of

PropertyChangeListener

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a

FocusListener

for the

JSplitPane

UI.

**Returns:** an instance of

FocusListener

- createKeyboardUpLeftListener

```java
@Deprecated

protected
ActionListener
createKeyboardUpLeftListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardDownRightListener

```java
@Deprecated

protected
ActionListener
createKeyboardDownRightListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardHomeListener

```java
@Deprecated

protected
ActionListener
createKeyboardHomeListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardEndListener

```java
@Deprecated

protected
ActionListener
createKeyboardEndListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- createKeyboardResizeToggleListener

```java
@Deprecated

protected
ActionListener
createKeyboardResizeToggleListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

- getOrientation

```java
public int getOrientation()
```

Returns the orientation for the

JSplitPane

.

**Returns:** the orientation

- setOrientation

```java
public void setOrientation​(int orientation)
```

Set the orientation for the

JSplitPane

.

**Parameters:** orientation

- the orientation

- isContinuousLayout

```java
public boolean isContinuousLayout()
```

Determines whether the

JSplitPane

is set to use a continuous layout.

**Returns:** true

if a continuous layout is set

- setContinuousLayout

```java
public void setContinuousLayout​(boolean b)
```

Turn continuous layout on/off.

**Parameters:** b

- if

true

the continuous layout turns on

- getLastDragLocation

```java
public int getLastDragLocation()
```

Returns the last drag location of the

JSplitPane

.

**Returns:** the last drag location

- setLastDragLocation

```java
public void setLastDragLocation​(int l)
```

Set the last drag location of the

JSplitPane

.

**Parameters:** l

- the drag location

- getDivider

```java
public
BasicSplitPaneDivider
getDivider()
```

Returns the divider between the top Components.

**Returns:** the divider between the top Components

- createDefaultNonContinuousLayoutDivider

```java
protected
Component
createDefaultNonContinuousLayoutDivider()
```

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

**Returns:** the default non continuous layout divider

- setNonContinuousLayoutDivider

```java
protected void setNonContinuousLayoutDivider​(
Component
newDivider)
```

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session. It is recommended that the passed in component
be a heavy weight.

**Parameters:** newDivider

- the new divider

- setNonContinuousLayoutDivider

```java
protected void setNonContinuousLayoutDivider​(
Component
newDivider,
boolean rememberSizes)
```

Sets the divider to use.

**Parameters:** newDivider

- the new divider
**Parameters:** rememberSizes

- if

true

the pane size is remembered

- getNonContinuousLayoutDivider

```java
public
Component
getNonContinuousLayoutDivider()
```

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session.

**Returns:** the divider

- getSplitPane

```java
public
JSplitPane
getSplitPane()
```

Returns the

JSplitPane

this instance is currently contained
in.

**Returns:** the instance of

JSplitPane

- createDefaultDivider

```java
public
BasicSplitPaneDivider
createDefaultDivider()
```

Creates the default divider.

**Returns:** the default divider

- resetToPreferredSizes

```java
public void resetToPreferredSizes​(
JSplitPane
jc)
```

Messaged to reset the preferred sizes.

**Specified by:** resetToPreferredSizes

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane

- setDividerLocation

```java
public void setDividerLocation​(
JSplitPane
jc,
int location)
```

Sets the location of the divider to location.

**Specified by:** setDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Parameters:** location

- an integer specifying the location of the divider

- getDividerLocation

```java
public int getDividerLocation​(
JSplitPane
jc)
```

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

**Specified by:** getDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the location of the divider

- getMinimumDividerLocation

```java
public int getMinimumDividerLocation​(
JSplitPane
jc)
```

Gets the minimum location of the divider.

**Specified by:** getMinimumDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** and integer specifying the minimum location of the divider

- getMaximumDividerLocation

```java
public int getMaximumDividerLocation​(
JSplitPane
jc)
```

Gets the maximum location of the divider.

**Specified by:** getMaximumDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the maximum location of the divider

- finishedPaintingChildren

```java
public void finishedPaintingChildren​(
JSplitPane
sp,

Graphics
g)
```

Called when the specified split pane has finished painting
its children.

**Specified by:** finishedPaintingChildren

in class

SplitPaneUI
**Parameters:** sp

- a

JSplitPane
**Parameters:** g

- the

Graphics

context

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
jc)
```

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** jc

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
jc)
```

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** jc

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
jc)
```

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** jc

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- getInsets

```java
public
Insets
getInsets​(
JComponent
jc)
```

Returns the insets. The insets are returned from the border insets
of the current border.

**Parameters:** jc

- a component
**Returns:** the insets

- resetLayoutManager

```java
protected void resetLayoutManager()
```

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

- startDragging

```java
protected void startDragging()
```

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

- dragDividerTo

```java
protected void dragDividerTo​(int location)
```

Messaged during a dragging session to move the divider to the
passed in

location

. If

continuousLayout

is

true

the location is reset and the splitPane validated.

**Parameters:** location

- the location of divider

- finishDraggingTo

```java
protected void finishDraggingTo​(int location)
```

Messaged to finish the dragging session. If not continuous display
the dividers

location

will be reset.

**Parameters:** location

- the location of divider

- getDividerBorderSize

```java
@Deprecated

protected int getDividerBorderSize()
```

Deprecated.

As of Java 2 platform v1.3, instead set the border on the
divider.

As of Java 2 platform v1.3 this method is no longer used. Instead
you should set the border on the divider.

Returns the width of one side of the divider border.

**Returns:** the width of one side of the divider border

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new instance of

BasicSplitPaneUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicSplitPaneUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Creates a new instance of

BasicSplitPaneUI

.

installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### installUI

public void installUI​(

JComponent

c)

Installs the UI.

installDefaults

```java
protected void installDefaults()
```

Installs the UI defaults.

---

#### installDefaults

protected void installDefaults()

Installs the UI defaults.

installListeners

```java
protected void installListeners()
```

Installs the event listeners for the UI.

---

#### installListeners

protected void installListeners()

Installs the event listeners for the UI.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions for the UI.

---

#### installKeyboardActions

protected void installKeyboardActions()

Installs the keyboard actions for the UI.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Uninstalls the UI.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the UI defaults.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls the UI defaults.

uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the event listeners for the UI.

---

#### uninstallListeners

protected void uninstallListeners()

Uninstalls the event listeners for the UI.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions for the UI.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Uninstalls the keyboard actions for the UI.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

**Returns:** an instance of

PropertyChangeListener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates a

PropertyChangeListener

for the

JSplitPane

UI.

createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a

FocusListener

for the

JSplitPane

UI.

**Returns:** an instance of

FocusListener

---

#### createFocusListener

protected

FocusListener

createFocusListener()

Creates a

FocusListener

for the

JSplitPane

UI.

createKeyboardUpLeftListener

```java
@Deprecated

protected
ActionListener
createKeyboardUpLeftListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

---

#### createKeyboardUpLeftListener

@Deprecated

protected

ActionListener

createKeyboardUpLeftListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

createKeyboardDownRightListener

```java
@Deprecated

protected
ActionListener
createKeyboardDownRightListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

---

#### createKeyboardDownRightListener

@Deprecated

protected

ActionListener

createKeyboardDownRightListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

createKeyboardHomeListener

```java
@Deprecated

protected
ActionListener
createKeyboardHomeListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

---

#### createKeyboardHomeListener

@Deprecated

protected

ActionListener

createKeyboardHomeListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

createKeyboardEndListener

```java
@Deprecated

protected
ActionListener
createKeyboardEndListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

---

#### createKeyboardEndListener

@Deprecated

protected

ActionListener

createKeyboardEndListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

createKeyboardResizeToggleListener

```java
@Deprecated

protected
ActionListener
createKeyboardResizeToggleListener()
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

**Returns:** an instance of

ActionListener

---

#### createKeyboardResizeToggleListener

@Deprecated

protected

ActionListener

createKeyboardResizeToggleListener()

As of Java 2 platform v1.3 this method is no longer used.
Subclassers previously using this method should instead create
an

Action

wrapping the

ActionListener

, and register
that

Action

by overriding

installKeyboardActions

and placing the

Action

in the

SplitPane's ActionMap

.
Please refer to the key bindings specification for further details.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

Creates an

ActionListener

for the

JSplitPane

UI that
listens for specific key presses.

getOrientation

```java
public int getOrientation()
```

Returns the orientation for the

JSplitPane

.

**Returns:** the orientation

---

#### getOrientation

public int getOrientation()

Returns the orientation for the

JSplitPane

.

setOrientation

```java
public void setOrientation​(int orientation)
```

Set the orientation for the

JSplitPane

.

**Parameters:** orientation

- the orientation

---

#### setOrientation

public void setOrientation​(int orientation)

Set the orientation for the

JSplitPane

.

isContinuousLayout

```java
public boolean isContinuousLayout()
```

Determines whether the

JSplitPane

is set to use a continuous layout.

**Returns:** true

if a continuous layout is set

---

#### isContinuousLayout

public boolean isContinuousLayout()

Determines whether the

JSplitPane

is set to use a continuous layout.

setContinuousLayout

```java
public void setContinuousLayout​(boolean b)
```

Turn continuous layout on/off.

**Parameters:** b

- if

true

the continuous layout turns on

---

#### setContinuousLayout

public void setContinuousLayout​(boolean b)

Turn continuous layout on/off.

getLastDragLocation

```java
public int getLastDragLocation()
```

Returns the last drag location of the

JSplitPane

.

**Returns:** the last drag location

---

#### getLastDragLocation

public int getLastDragLocation()

Returns the last drag location of the

JSplitPane

.

setLastDragLocation

```java
public void setLastDragLocation​(int l)
```

Set the last drag location of the

JSplitPane

.

**Parameters:** l

- the drag location

---

#### setLastDragLocation

public void setLastDragLocation​(int l)

Set the last drag location of the

JSplitPane

.

getDivider

```java
public
BasicSplitPaneDivider
getDivider()
```

Returns the divider between the top Components.

**Returns:** the divider between the top Components

---

#### getDivider

public

BasicSplitPaneDivider

getDivider()

Returns the divider between the top Components.

createDefaultNonContinuousLayoutDivider

```java
protected
Component
createDefaultNonContinuousLayoutDivider()
```

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

**Returns:** the default non continuous layout divider

---

#### createDefaultNonContinuousLayoutDivider

protected

Component

createDefaultNonContinuousLayoutDivider()

Returns the default non continuous layout divider, which is an
instance of

Canvas

that fills in the background with dark gray.

setNonContinuousLayoutDivider

```java
protected void setNonContinuousLayoutDivider​(
Component
newDivider)
```

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session. It is recommended that the passed in component
be a heavy weight.

**Parameters:** newDivider

- the new divider

---

#### setNonContinuousLayoutDivider

protected void setNonContinuousLayoutDivider​(

Component

newDivider)

Sets the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session. It is recommended that the passed in component
be a heavy weight.

setNonContinuousLayoutDivider

```java
protected void setNonContinuousLayoutDivider​(
Component
newDivider,
boolean rememberSizes)
```

Sets the divider to use.

**Parameters:** newDivider

- the new divider
**Parameters:** rememberSizes

- if

true

the pane size is remembered

---

#### setNonContinuousLayoutDivider

protected void setNonContinuousLayoutDivider​(

Component

newDivider,
boolean rememberSizes)

Sets the divider to use.

getNonContinuousLayoutDivider

```java
public
Component
getNonContinuousLayoutDivider()
```

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session.

**Returns:** the divider

---

#### getNonContinuousLayoutDivider

public

Component

getNonContinuousLayoutDivider()

Returns the divider to use when the

JSplitPane

is configured to
not continuously layout. This divider will only be used during a
dragging session.

getSplitPane

```java
public
JSplitPane
getSplitPane()
```

Returns the

JSplitPane

this instance is currently contained
in.

**Returns:** the instance of

JSplitPane

---

#### getSplitPane

public

JSplitPane

getSplitPane()

Returns the

JSplitPane

this instance is currently contained
in.

createDefaultDivider

```java
public
BasicSplitPaneDivider
createDefaultDivider()
```

Creates the default divider.

**Returns:** the default divider

---

#### createDefaultDivider

public

BasicSplitPaneDivider

createDefaultDivider()

Creates the default divider.

resetToPreferredSizes

```java
public void resetToPreferredSizes​(
JSplitPane
jc)
```

Messaged to reset the preferred sizes.

**Specified by:** resetToPreferredSizes

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane

---

#### resetToPreferredSizes

public void resetToPreferredSizes​(

JSplitPane

jc)

Messaged to reset the preferred sizes.

setDividerLocation

```java
public void setDividerLocation​(
JSplitPane
jc,
int location)
```

Sets the location of the divider to location.

**Specified by:** setDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Parameters:** location

- an integer specifying the location of the divider

---

#### setDividerLocation

public void setDividerLocation​(

JSplitPane

jc,
int location)

Sets the location of the divider to location.

getDividerLocation

```java
public int getDividerLocation​(
JSplitPane
jc)
```

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

**Specified by:** getDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the location of the divider

---

#### getDividerLocation

public int getDividerLocation​(

JSplitPane

jc)

Returns the location of the divider, which may differ from what
the splitpane thinks the location of the divider is.

getMinimumDividerLocation

```java
public int getMinimumDividerLocation​(
JSplitPane
jc)
```

Gets the minimum location of the divider.

**Specified by:** getMinimumDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** and integer specifying the minimum location of the divider

---

#### getMinimumDividerLocation

public int getMinimumDividerLocation​(

JSplitPane

jc)

Gets the minimum location of the divider.

getMaximumDividerLocation

```java
public int getMaximumDividerLocation​(
JSplitPane
jc)
```

Gets the maximum location of the divider.

**Specified by:** getMaximumDividerLocation

in class

SplitPaneUI
**Parameters:** jc

- a

JSplitPane
**Returns:** an integer specifying the maximum location of the divider

---

#### getMaximumDividerLocation

public int getMaximumDividerLocation​(

JSplitPane

jc)

Gets the maximum location of the divider.

finishedPaintingChildren

```java
public void finishedPaintingChildren​(
JSplitPane
sp,

Graphics
g)
```

Called when the specified split pane has finished painting
its children.

**Specified by:** finishedPaintingChildren

in class

SplitPaneUI
**Parameters:** sp

- a

JSplitPane
**Parameters:** g

- the

Graphics

context

---

#### finishedPaintingChildren

public void finishedPaintingChildren​(

JSplitPane

sp,

Graphics

g)

Called when the specified split pane has finished painting
its children.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
jc)
```

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** jc

- the component whose preferred size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object containing given component's preferred
size appropriate for the look and feel
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

jc)

Returns the preferred size for the passed in component,
This is passed off to the current layout manager.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
jc)
```

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** jc

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

JComponent

jc)

Returns the minimum size for the passed in component,
This is passed off to the current layout manager.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
jc)
```

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** jc

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

jc)

Returns the maximum size for the passed in component,
This is passed off to the current layout manager.

getInsets

```java
public
Insets
getInsets​(
JComponent
jc)
```

Returns the insets. The insets are returned from the border insets
of the current border.

**Parameters:** jc

- a component
**Returns:** the insets

---

#### getInsets

public

Insets

getInsets​(

JComponent

jc)

Returns the insets. The insets are returned from the border insets
of the current border.

resetLayoutManager

```java
protected void resetLayoutManager()
```

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

---

#### resetLayoutManager

protected void resetLayoutManager()

Resets the layout manager based on orientation and messages it
with invalidateLayout to pull in appropriate Components.

startDragging

```java
protected void startDragging()
```

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

---

#### startDragging

protected void startDragging()

Should be messaged before the dragging session starts, resets
lastDragLocation and dividerSize.

dragDividerTo

```java
protected void dragDividerTo​(int location)
```

Messaged during a dragging session to move the divider to the
passed in

location

. If

continuousLayout

is

true

the location is reset and the splitPane validated.

**Parameters:** location

- the location of divider

---

#### dragDividerTo

protected void dragDividerTo​(int location)

Messaged during a dragging session to move the divider to the
passed in

location

. If

continuousLayout

is

true

the location is reset and the splitPane validated.

finishDraggingTo

```java
protected void finishDraggingTo​(int location)
```

Messaged to finish the dragging session. If not continuous display
the dividers

location

will be reset.

**Parameters:** location

- the location of divider

---

#### finishDraggingTo

protected void finishDraggingTo​(int location)

Messaged to finish the dragging session. If not continuous display
the dividers

location

will be reset.

getDividerBorderSize

```java
@Deprecated

protected int getDividerBorderSize()
```

Deprecated.

As of Java 2 platform v1.3, instead set the border on the
divider.

As of Java 2 platform v1.3 this method is no longer used. Instead
you should set the border on the divider.

Returns the width of one side of the divider border.

**Returns:** the width of one side of the divider border

---

#### getDividerBorderSize

@Deprecated

protected int getDividerBorderSize()

As of Java 2 platform v1.3 this method is no longer used. Instead
you should set the border on the divider.

Returns the width of one side of the divider border.

Returns the width of one side of the divider border.

---

