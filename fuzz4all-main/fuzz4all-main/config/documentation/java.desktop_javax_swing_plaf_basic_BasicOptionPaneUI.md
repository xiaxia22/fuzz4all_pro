# Class BasicOptionPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicOptionPaneUI.html`

### Class Description

```java
public class
BasicOptionPaneUI

extends
OptionPaneUI
```

Provides the basic look and feel for a

JOptionPane

.

BasicMessagePaneUI

provides a means to place an icon,
message and buttons into a

Container

.
Generally, the layout will look like:

```java
------------------
| i | message |
| c | message |
| o | message |
| n | message |
------------------
| buttons |
|________________|
```

icon is an instance of

Icon

that is wrapped inside a

JLabel

. The message is an opaque object and is tested
for the following: if the message is a

Component

it is
added to the

Container

, if it is an

Icon

it is wrapped inside a

JLabel

and added to the

Container

otherwise it is wrapped inside a

JLabel

.

The above layout is used when the option pane's

ComponentOrientation

property is horizontal, left-to-right.
The layout will be adjusted appropriately for other orientations.

The

Container

, message, icon, and buttons are all
determined from abstract methods.

**Direct Known Subclasses:** SynthOptionPaneUI

---

### Field Details

#### public static final int MinimumWidth

The mininum width of

JOptionPane

.

**See Also:**
- Constant Field Values

---

#### public static final int MinimumHeight

The mininum height of

JOptionPane

.

**See Also:**
- Constant Field Values

---

#### protected
JOptionPane
optionPane

JOptionPane

that the receiver is providing the
look and feel for.

---

#### protected
Dimension
minimumSize

The size of

JOptionPane

.

---

#### protected
JComponent
inputComponent

JComponent provide for input if optionPane.getWantsInput() returns
true.

---

#### protected
Component
initialFocusComponent

Component to receive focus when messaged with selectInitialValue.

---

#### protected boolean hasCustomComponents

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

---

#### protected
PropertyChangeListener
propertyChangeListener

The instance of

PropertyChangeListener

.

---

### Constructor Details

#### public BasicOptionPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates a new

BasicOptionPaneUI

instance.

**Parameters:**
- x

- the component

**Returns:**
- a new

BasicOptionPaneUI

instance

---

#### public void installUI​(
JComponent
c)

Installs the receiver as the L&F for the passed in

JOptionPane

.

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

#### public void uninstallUI​(
JComponent
c)

Removes the receiver from the L&F controller of the passed in split
pane.

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

#### protected void installDefaults()

Installs default properties.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void installComponents()

Registers components.

---

#### protected void uninstallComponents()

Unregisters components.

---

#### protected
LayoutManager
createLayoutManager()

Returns a layout manager.

**Returns:**
- a layout manager

---

#### protected void installListeners()

Registers listeners.

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Returns an instance of

PropertyChangeListener

.

**Returns:**
- an instance of

PropertyChangeListener

---

#### protected void installKeyboardActions()

Registers keyboard actions.

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

#### public
Dimension
getMinimumOptionPaneSize()

Returns the minimum size the option pane should be. Primarily
provided for subclassers wishing to offer a different minimum size.

**Returns:**
- the minimum size of the option pane

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- c

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

#### protected
Container
createMessageArea()

Messaged from

installComponents

to create a

Container

containing the body of the message. The icon is the created
by calling

addIcon

.

**Returns:**
- a instance of

Container

---

#### protected void addMessageComponents​(
Container
container,

GridBagConstraints
cons,

Object
msg,
int maxll,
boolean internallyCreated)

Creates the appropriate object to represent

msg

and places it
into

container

. If

msg

is an instance of

Component

, it is added directly; if it is an

Icon

, a

JLabel

is created to represent it; otherwise, a

JLabel

is created for the string. If

msg

is an Object[], this method
will be recursively invoked for the children.

internallyCreated

is

true

if

msg

is an instance of

Component

and
was created internally by this method (this is used to correctly set

hasCustomComponents

only if

internallyCreated

is

false

).

**Parameters:**
- container

- a container
- cons

- an instance of

GridBagConstraints
- msg

- a message
- maxll

- a maximum length
- internallyCreated

-

true

if the component was internally created

---

#### protected
Object
getMessage()

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

**Returns:**
- the message to display

---

#### protected void addIcon​(
Container
top)

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

. This is messaged from

createMessageArea

.

**Parameters:**
- top

- a container

---

#### protected
Icon
getIcon()

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

**Returns:**
- the icon

---

#### protected
Icon
getIconForType​(int messageType)

Returns the icon to use for the passed in type.

**Parameters:**
- messageType

- a type of message

**Returns:**
- the icon to use for the passed in type

---

#### protected int getMaxCharactersPerLineCount()

Returns the maximum number of characters to place on a line.

**Returns:**
- the maximum number of characters to place on a line

---

#### protected void burstStringInto​(
Container
c,

String
d,
int maxll)

Recursively creates new

JLabel

instances to represent

d

.
Each

JLabel

instance is added to

c

.

**Parameters:**
- c

- a container
- d

- a text
- maxll

- a maximum length of a text

---

#### protected
Container
createSeparator()

Returns a separator.

**Returns:**
- a separator

---

#### protected
Container
createButtonArea()

Creates and returns a

Container

containing the buttons.
The buttons are created by calling

getButtons

.

**Returns:**
- a

Container

containing the buttons

---

#### protected void addButtonComponents​(
Container
container,

Object
[] buttons,
int initialIndex)

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

. This
differs from addMessageComponents in that it will recurse on

buttons

and that if button is not a Component
it will create an instance of JButton.

**Parameters:**
- container

- a container
- buttons

- an array of buttons
- initialIndex

- an initial index

---

#### protected
ActionListener
createButtonActionListener​(int buttonIndex)

Constructs a new instance of a

ButtonActionListener

.

**Parameters:**
- buttonIndex

- an index of the button

**Returns:**
- a new instance of a

ButtonActionListener

---

#### protected
Object
[] getButtons()

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for. If the

JOptionPane

has options
set, they will be provided, otherwise if the optionType is

YES_NO_OPTION

,

yesNoOptions

is returned, if the type is

YES_NO_CANCEL_OPTION

yesNoCancelOptions

is returned, otherwise

defaultButtons

are returned.

**Returns:**
- the buttons to display from the JOptionPane

---

#### protected boolean getSizeButtonsToSameWidth()

Returns

true

, basic L&F wants all the buttons to have the same
width.

**Returns:**
- true

if all the buttons should have the same width

---

#### protected int getInitialValueIndex()

Returns the initial index into the buttons to select. The index
is calculated from the initial value from the JOptionPane and
options of the JOptionPane or 0.

**Returns:**
- the initial index into the buttons to select

---

#### protected void resetInputValue()

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

---

#### public void selectInitialValue​(
JOptionPane
op)

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

**Specified by:**
- selectInitialValue

in class

OptionPaneUI

**Parameters:**
- op

- a

JOptionPane

---

#### public boolean containsCustomComponents​(
JOptionPane
op)

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

**Specified by:**
- containsCustomComponents

in class

OptionPaneUI

**Parameters:**
- op

- a

JOptionPane

**Returns:**
- true

if the given

JOptionPane

contains user
created

Component

s

---

### Additional Sections

#### Class BasicOptionPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.OptionPaneUI
- - javax.swing.plaf.basic.BasicOptionPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.OptionPaneUI
- - javax.swing.plaf.basic.BasicOptionPaneUI

javax.swing.plaf.OptionPaneUI

- javax.swing.plaf.basic.BasicOptionPaneUI

javax.swing.plaf.basic.BasicOptionPaneUI

**Direct Known Subclasses:** SynthOptionPaneUI

```java
public class
BasicOptionPaneUI

extends
OptionPaneUI
```

Provides the basic look and feel for a

JOptionPane

.

BasicMessagePaneUI

provides a means to place an icon,
message and buttons into a

Container

.
Generally, the layout will look like:

```java
------------------
| i | message |
| c | message |
| o | message |
| n | message |
------------------
| buttons |
|________________|
```

icon is an instance of

Icon

that is wrapped inside a

JLabel

. The message is an opaque object and is tested
for the following: if the message is a

Component

it is
added to the

Container

, if it is an

Icon

it is wrapped inside a

JLabel

and added to the

Container

otherwise it is wrapped inside a

JLabel

.

The above layout is used when the option pane's

ComponentOrientation

property is horizontal, left-to-right.
The layout will be adjusted appropriately for other orientations.

The

Container

, message, icon, and buttons are all
determined from abstract methods.

public class

BasicOptionPaneUI

extends

OptionPaneUI

Provides the basic look and feel for a

JOptionPane

.

BasicMessagePaneUI

provides a means to place an icon,
message and buttons into a

Container

.
Generally, the layout will look like:

```java
------------------
| i | message |
| c | message |
| o | message |
| n | message |
------------------
| buttons |
|________________|
```

icon is an instance of

Icon

that is wrapped inside a

JLabel

. The message is an opaque object and is tested
for the following: if the message is a

Component

it is
added to the

Container

, if it is an

Icon

it is wrapped inside a

JLabel

and added to the

Container

otherwise it is wrapped inside a

JLabel

.

The above layout is used when the option pane's

ComponentOrientation

property is horizontal, left-to-right.
The layout will be adjusted appropriately for other orientations.

The

Container

, message, icon, and buttons are all
determined from abstract methods.

------------------
| i | message |
| c | message |
| o | message |
| n | message |
------------------
| buttons |
|________________|

The above layout is used when the option pane's

ComponentOrientation

property is horizontal, left-to-right.
The layout will be adjusted appropriately for other orientations.

The

Container

, message, icon, and buttons are all
determined from abstract methods.

The

Container

, message, icon, and buttons are all
determined from abstract methods.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicOptionPaneUI.ButtonActionListener

This class should be treated as a "protected" inner class.

static class

BasicOptionPaneUI.ButtonAreaLayout

ButtonAreaLayout

behaves in a similar manner to

FlowLayout

.

class

BasicOptionPaneUI.PropertyChangeHandler

This class should be treated as a "protected" inner class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

hasCustomComponents

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

protected

Component

initialFocusComponent

Component to receive focus when messaged with selectInitialValue.

protected

JComponent

inputComponent

JComponent provide for input if optionPane.getWantsInput() returns
true.

static int

MinimumHeight

The mininum height of

JOptionPane

.

protected

Dimension

minimumSize

The size of

JOptionPane

.

static int

MinimumWidth

The mininum width of

JOptionPane

.

protected

JOptionPane

optionPane

JOptionPane

that the receiver is providing the
look and feel for.

protected

PropertyChangeListener

propertyChangeListener

The instance of

PropertyChangeListener

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicOptionPaneUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addButtonComponents

​(

Container

container,

Object

[] buttons,
int initialIndex)

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

.

protected void

addIcon

​(

Container

top)

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

.

protected void

addMessageComponents

​(

Container

container,

GridBagConstraints

cons,

Object

msg,
int maxll,
boolean internallyCreated)

Creates the appropriate object to represent

msg

and places it
into

container

.

protected void

burstStringInto

​(

Container

c,

String

d,
int maxll)

Recursively creates new

JLabel

instances to represent

d

.

boolean

containsCustomComponents

​(

JOptionPane

op)

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

protected

ActionListener

createButtonActionListener

​(int buttonIndex)

Constructs a new instance of a

ButtonActionListener

.

protected

Container

createButtonArea

()

Creates and returns a

Container

containing the buttons.

protected

LayoutManager

createLayoutManager

()

Returns a layout manager.

protected

Container

createMessageArea

()

Messaged from

installComponents

to create a

Container

containing the body of the message.

protected

PropertyChangeListener

createPropertyChangeListener

()

Returns an instance of

PropertyChangeListener

.

protected

Container

createSeparator

()

Returns a separator.

static

ComponentUI

createUI

​(

JComponent

x)

Creates a new

BasicOptionPaneUI

instance.

protected

Object

[]

getButtons

()

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for.

protected

Icon

getIcon

()

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

protected

Icon

getIconForType

​(int messageType)

Returns the icon to use for the passed in type.

protected int

getInitialValueIndex

()

Returns the initial index into the buttons to select.

protected int

getMaxCharactersPerLineCount

()

Returns the maximum number of characters to place on a line.

protected

Object

getMessage

()

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

Dimension

getMinimumOptionPaneSize

()

Returns the minimum size the option pane should be.

Dimension

getPreferredSize

​(

JComponent

c)

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

protected boolean

getSizeButtonsToSameWidth

()

Returns

true

, basic L&F wants all the buttons to have the same
width.

protected void

installComponents

()

Registers components.

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

void

installUI

​(

JComponent

c)

Installs the receiver as the L&F for the passed in

JOptionPane

.

protected void

resetInputValue

()

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

void

selectInitialValue

​(

JOptionPane

op)

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

protected void

uninstallComponents

()

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

void

uninstallUI

​(

JComponent

c)

Removes the receiver from the L&F controller of the passed in split
pane.

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

getMaximumSize

,

getMinimumSize

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

BasicOptionPaneUI.ButtonActionListener

This class should be treated as a "protected" inner class.

static class

BasicOptionPaneUI.ButtonAreaLayout

ButtonAreaLayout

behaves in a similar manner to

FlowLayout

.

class

BasicOptionPaneUI.PropertyChangeHandler

This class should be treated as a "protected" inner class.

---

#### Nested Class Summary

This class should be treated as a "protected" inner class.

ButtonAreaLayout

behaves in a similar manner to

FlowLayout

.

Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

hasCustomComponents

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

protected

Component

initialFocusComponent

Component to receive focus when messaged with selectInitialValue.

protected

JComponent

inputComponent

JComponent provide for input if optionPane.getWantsInput() returns
true.

static int

MinimumHeight

The mininum height of

JOptionPane

.

protected

Dimension

minimumSize

The size of

JOptionPane

.

static int

MinimumWidth

The mininum width of

JOptionPane

.

protected

JOptionPane

optionPane

JOptionPane

that the receiver is providing the
look and feel for.

protected

PropertyChangeListener

propertyChangeListener

The instance of

PropertyChangeListener

.

---

#### Field Summary

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

Component to receive focus when messaged with selectInitialValue.

JComponent provide for input if optionPane.getWantsInput() returns
true.

The mininum height of

JOptionPane

.

The size of

JOptionPane

.

The mininum width of

JOptionPane

.

JOptionPane

that the receiver is providing the
look and feel for.

The instance of

PropertyChangeListener

.

Constructor Summary

Constructors

Constructor

Description

BasicOptionPaneUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addButtonComponents

​(

Container

container,

Object

[] buttons,
int initialIndex)

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

.

protected void

addIcon

​(

Container

top)

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

.

protected void

addMessageComponents

​(

Container

container,

GridBagConstraints

cons,

Object

msg,
int maxll,
boolean internallyCreated)

Creates the appropriate object to represent

msg

and places it
into

container

.

protected void

burstStringInto

​(

Container

c,

String

d,
int maxll)

Recursively creates new

JLabel

instances to represent

d

.

boolean

containsCustomComponents

​(

JOptionPane

op)

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

protected

ActionListener

createButtonActionListener

​(int buttonIndex)

Constructs a new instance of a

ButtonActionListener

.

protected

Container

createButtonArea

()

Creates and returns a

Container

containing the buttons.

protected

LayoutManager

createLayoutManager

()

Returns a layout manager.

protected

Container

createMessageArea

()

Messaged from

installComponents

to create a

Container

containing the body of the message.

protected

PropertyChangeListener

createPropertyChangeListener

()

Returns an instance of

PropertyChangeListener

.

protected

Container

createSeparator

()

Returns a separator.

static

ComponentUI

createUI

​(

JComponent

x)

Creates a new

BasicOptionPaneUI

instance.

protected

Object

[]

getButtons

()

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for.

protected

Icon

getIcon

()

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

protected

Icon

getIconForType

​(int messageType)

Returns the icon to use for the passed in type.

protected int

getInitialValueIndex

()

Returns the initial index into the buttons to select.

protected int

getMaxCharactersPerLineCount

()

Returns the maximum number of characters to place on a line.

protected

Object

getMessage

()

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

Dimension

getMinimumOptionPaneSize

()

Returns the minimum size the option pane should be.

Dimension

getPreferredSize

​(

JComponent

c)

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

protected boolean

getSizeButtonsToSameWidth

()

Returns

true

, basic L&F wants all the buttons to have the same
width.

protected void

installComponents

()

Registers components.

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

void

installUI

​(

JComponent

c)

Installs the receiver as the L&F for the passed in

JOptionPane

.

protected void

resetInputValue

()

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

void

selectInitialValue

​(

JOptionPane

op)

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

protected void

uninstallComponents

()

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

void

uninstallUI

​(

JComponent

c)

Removes the receiver from the L&F controller of the passed in split
pane.

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

getMaximumSize

,

getMinimumSize

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

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

.

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

.

Creates the appropriate object to represent

msg

and places it
into

container

.

Recursively creates new

JLabel

instances to represent

d

.

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

Constructs a new instance of a

ButtonActionListener

.

Creates and returns a

Container

containing the buttons.

Returns a layout manager.

Messaged from

installComponents

to create a

Container

containing the body of the message.

Returns an instance of

PropertyChangeListener

.

Returns a separator.

Creates a new

BasicOptionPaneUI

instance.

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for.

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

Returns the icon to use for the passed in type.

Returns the initial index into the buttons to select.

Returns the maximum number of characters to place on a line.

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

Returns the minimum size the option pane should be.

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

Returns

true

, basic L&F wants all the buttons to have the same
width.

Registers components.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Installs the receiver as the L&F for the passed in

JOptionPane

.

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

Unregisters components.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

Removes the receiver from the L&F controller of the passed in split
pane.

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

getMaximumSize

,

getMinimumSize

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

- MinimumWidth

```java
public static final int MinimumWidth
```

The mininum width of

JOptionPane

.

**See Also:** Constant Field Values

- MinimumHeight

```java
public static final int MinimumHeight
```

The mininum height of

JOptionPane

.

**See Also:** Constant Field Values

- optionPane

```java
protected
JOptionPane
optionPane
```

JOptionPane

that the receiver is providing the
look and feel for.

- minimumSize

```java
protected
Dimension
minimumSize
```

The size of

JOptionPane

.

- inputComponent

```java
protected
JComponent
inputComponent
```

JComponent provide for input if optionPane.getWantsInput() returns
true.

- initialFocusComponent

```java
protected
Component
initialFocusComponent
```

Component to receive focus when messaged with selectInitialValue.

- hasCustomComponents

```java
protected boolean hasCustomComponents
```

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of

PropertyChangeListener

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicOptionPaneUI

```java
public BasicOptionPaneUI()
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

Creates a new

BasicOptionPaneUI

instance.

**Parameters:** x

- the component
**Returns:** a new

BasicOptionPaneUI

instance

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the receiver as the L&F for the passed in

JOptionPane

.

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

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Removes the receiver from the L&F controller of the passed in split
pane.

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

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- installComponents

```java
protected void installComponents()
```

Registers components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Returns a layout manager.

**Returns:** a layout manager

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- getMinimumOptionPaneSize

```java
public
Dimension
getMinimumOptionPaneSize()
```

Returns the minimum size the option pane should be. Primarily
provided for subclassers wishing to offer a different minimum size.

**Returns:** the minimum size of the option pane

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

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

- createMessageArea

```java
protected
Container
createMessageArea()
```

Messaged from

installComponents

to create a

Container

containing the body of the message. The icon is the created
by calling

addIcon

.

**Returns:** a instance of

Container

- addMessageComponents

```java
protected void addMessageComponents​(
Container
container,

GridBagConstraints
cons,

Object
msg,
int maxll,
boolean internallyCreated)
```

Creates the appropriate object to represent

msg

and places it
into

container

. If

msg

is an instance of

Component

, it is added directly; if it is an

Icon

, a

JLabel

is created to represent it; otherwise, a

JLabel

is created for the string. If

msg

is an Object[], this method
will be recursively invoked for the children.

internallyCreated

is

true

if

msg

is an instance of

Component

and
was created internally by this method (this is used to correctly set

hasCustomComponents

only if

internallyCreated

is

false

).

**Parameters:** container

- a container
**Parameters:** cons

- an instance of

GridBagConstraints
**Parameters:** msg

- a message
**Parameters:** maxll

- a maximum length
**Parameters:** internallyCreated

-

true

if the component was internally created

- getMessage

```java
protected
Object
getMessage()
```

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

**Returns:** the message to display

- addIcon

```java
protected void addIcon​(
Container
top)
```

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

. This is messaged from

createMessageArea

.

**Parameters:** top

- a container

- getIcon

```java
protected
Icon
getIcon()
```

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

**Returns:** the icon

- getIconForType

```java
protected
Icon
getIconForType​(int messageType)
```

Returns the icon to use for the passed in type.

**Parameters:** messageType

- a type of message
**Returns:** the icon to use for the passed in type

- getMaxCharactersPerLineCount

```java
protected int getMaxCharactersPerLineCount()
```

Returns the maximum number of characters to place on a line.

**Returns:** the maximum number of characters to place on a line

- burstStringInto

```java
protected void burstStringInto​(
Container
c,

String
d,
int maxll)
```

Recursively creates new

JLabel

instances to represent

d

.
Each

JLabel

instance is added to

c

.

**Parameters:** c

- a container
**Parameters:** d

- a text
**Parameters:** maxll

- a maximum length of a text

- createSeparator

```java
protected
Container
createSeparator()
```

Returns a separator.

**Returns:** a separator

- createButtonArea

```java
protected
Container
createButtonArea()
```

Creates and returns a

Container

containing the buttons.
The buttons are created by calling

getButtons

.

**Returns:** a

Container

containing the buttons

- addButtonComponents

```java
protected void addButtonComponents​(
Container
container,

Object
[] buttons,
int initialIndex)
```

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

. This
differs from addMessageComponents in that it will recurse on

buttons

and that if button is not a Component
it will create an instance of JButton.

**Parameters:** container

- a container
**Parameters:** buttons

- an array of buttons
**Parameters:** initialIndex

- an initial index

- createButtonActionListener

```java
protected
ActionListener
createButtonActionListener​(int buttonIndex)
```

Constructs a new instance of a

ButtonActionListener

.

**Parameters:** buttonIndex

- an index of the button
**Returns:** a new instance of a

ButtonActionListener

- getButtons

```java
protected
Object
[] getButtons()
```

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for. If the

JOptionPane

has options
set, they will be provided, otherwise if the optionType is

YES_NO_OPTION

,

yesNoOptions

is returned, if the type is

YES_NO_CANCEL_OPTION

yesNoCancelOptions

is returned, otherwise

defaultButtons

are returned.

**Returns:** the buttons to display from the JOptionPane

- getSizeButtonsToSameWidth

```java
protected boolean getSizeButtonsToSameWidth()
```

Returns

true

, basic L&F wants all the buttons to have the same
width.

**Returns:** true

if all the buttons should have the same width

- getInitialValueIndex

```java
protected int getInitialValueIndex()
```

Returns the initial index into the buttons to select. The index
is calculated from the initial value from the JOptionPane and
options of the JOptionPane or 0.

**Returns:** the initial index into the buttons to select

- resetInputValue

```java
protected void resetInputValue()
```

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

- selectInitialValue

```java
public void selectInitialValue​(
JOptionPane
op)
```

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

**Specified by:** selectInitialValue

in class

OptionPaneUI
**Parameters:** op

- a

JOptionPane

- containsCustomComponents

```java
public boolean containsCustomComponents​(
JOptionPane
op)
```

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

**Specified by:** containsCustomComponents

in class

OptionPaneUI
**Parameters:** op

- a

JOptionPane
**Returns:** true

if the given

JOptionPane

contains user
created

Component

s

Field Detail

- MinimumWidth

```java
public static final int MinimumWidth
```

The mininum width of

JOptionPane

.

**See Also:** Constant Field Values

- MinimumHeight

```java
public static final int MinimumHeight
```

The mininum height of

JOptionPane

.

**See Also:** Constant Field Values

- optionPane

```java
protected
JOptionPane
optionPane
```

JOptionPane

that the receiver is providing the
look and feel for.

- minimumSize

```java
protected
Dimension
minimumSize
```

The size of

JOptionPane

.

- inputComponent

```java
protected
JComponent
inputComponent
```

JComponent provide for input if optionPane.getWantsInput() returns
true.

- initialFocusComponent

```java
protected
Component
initialFocusComponent
```

Component to receive focus when messaged with selectInitialValue.

- hasCustomComponents

```java
protected boolean hasCustomComponents
```

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of

PropertyChangeListener

.

---

#### Field Detail

MinimumWidth

```java
public static final int MinimumWidth
```

The mininum width of

JOptionPane

.

**See Also:** Constant Field Values

---

#### MinimumWidth

public static final int MinimumWidth

The mininum width of

JOptionPane

.

MinimumHeight

```java
public static final int MinimumHeight
```

The mininum height of

JOptionPane

.

**See Also:** Constant Field Values

---

#### MinimumHeight

public static final int MinimumHeight

The mininum height of

JOptionPane

.

optionPane

```java
protected
JOptionPane
optionPane
```

JOptionPane

that the receiver is providing the
look and feel for.

---

#### optionPane

protected

JOptionPane

optionPane

JOptionPane

that the receiver is providing the
look and feel for.

minimumSize

```java
protected
Dimension
minimumSize
```

The size of

JOptionPane

.

---

#### minimumSize

protected

Dimension

minimumSize

The size of

JOptionPane

.

inputComponent

```java
protected
JComponent
inputComponent
```

JComponent provide for input if optionPane.getWantsInput() returns
true.

---

#### inputComponent

protected

JComponent

inputComponent

JComponent provide for input if optionPane.getWantsInput() returns
true.

initialFocusComponent

```java
protected
Component
initialFocusComponent
```

Component to receive focus when messaged with selectInitialValue.

---

#### initialFocusComponent

protected

Component

initialFocusComponent

Component to receive focus when messaged with selectInitialValue.

hasCustomComponents

```java
protected boolean hasCustomComponents
```

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

---

#### hasCustomComponents

protected boolean hasCustomComponents

This is set to true in validateComponent if a Component is contained
in either the message or the buttons.

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of

PropertyChangeListener

.

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

The instance of

PropertyChangeListener

.

Constructor Detail

- BasicOptionPaneUI

```java
public BasicOptionPaneUI()
```

---

#### Constructor Detail

BasicOptionPaneUI

```java
public BasicOptionPaneUI()
```

---

#### BasicOptionPaneUI

public BasicOptionPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new

BasicOptionPaneUI

instance.

**Parameters:** x

- the component
**Returns:** a new

BasicOptionPaneUI

instance

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the receiver as the L&F for the passed in

JOptionPane

.

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

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Removes the receiver from the L&F controller of the passed in split
pane.

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

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- installComponents

```java
protected void installComponents()
```

Registers components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Returns a layout manager.

**Returns:** a layout manager

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- getMinimumOptionPaneSize

```java
public
Dimension
getMinimumOptionPaneSize()
```

Returns the minimum size the option pane should be. Primarily
provided for subclassers wishing to offer a different minimum size.

**Returns:** the minimum size of the option pane

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

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

- createMessageArea

```java
protected
Container
createMessageArea()
```

Messaged from

installComponents

to create a

Container

containing the body of the message. The icon is the created
by calling

addIcon

.

**Returns:** a instance of

Container

- addMessageComponents

```java
protected void addMessageComponents​(
Container
container,

GridBagConstraints
cons,

Object
msg,
int maxll,
boolean internallyCreated)
```

Creates the appropriate object to represent

msg

and places it
into

container

. If

msg

is an instance of

Component

, it is added directly; if it is an

Icon

, a

JLabel

is created to represent it; otherwise, a

JLabel

is created for the string. If

msg

is an Object[], this method
will be recursively invoked for the children.

internallyCreated

is

true

if

msg

is an instance of

Component

and
was created internally by this method (this is used to correctly set

hasCustomComponents

only if

internallyCreated

is

false

).

**Parameters:** container

- a container
**Parameters:** cons

- an instance of

GridBagConstraints
**Parameters:** msg

- a message
**Parameters:** maxll

- a maximum length
**Parameters:** internallyCreated

-

true

if the component was internally created

- getMessage

```java
protected
Object
getMessage()
```

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

**Returns:** the message to display

- addIcon

```java
protected void addIcon​(
Container
top)
```

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

. This is messaged from

createMessageArea

.

**Parameters:** top

- a container

- getIcon

```java
protected
Icon
getIcon()
```

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

**Returns:** the icon

- getIconForType

```java
protected
Icon
getIconForType​(int messageType)
```

Returns the icon to use for the passed in type.

**Parameters:** messageType

- a type of message
**Returns:** the icon to use for the passed in type

- getMaxCharactersPerLineCount

```java
protected int getMaxCharactersPerLineCount()
```

Returns the maximum number of characters to place on a line.

**Returns:** the maximum number of characters to place on a line

- burstStringInto

```java
protected void burstStringInto​(
Container
c,

String
d,
int maxll)
```

Recursively creates new

JLabel

instances to represent

d

.
Each

JLabel

instance is added to

c

.

**Parameters:** c

- a container
**Parameters:** d

- a text
**Parameters:** maxll

- a maximum length of a text

- createSeparator

```java
protected
Container
createSeparator()
```

Returns a separator.

**Returns:** a separator

- createButtonArea

```java
protected
Container
createButtonArea()
```

Creates and returns a

Container

containing the buttons.
The buttons are created by calling

getButtons

.

**Returns:** a

Container

containing the buttons

- addButtonComponents

```java
protected void addButtonComponents​(
Container
container,

Object
[] buttons,
int initialIndex)
```

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

. This
differs from addMessageComponents in that it will recurse on

buttons

and that if button is not a Component
it will create an instance of JButton.

**Parameters:** container

- a container
**Parameters:** buttons

- an array of buttons
**Parameters:** initialIndex

- an initial index

- createButtonActionListener

```java
protected
ActionListener
createButtonActionListener​(int buttonIndex)
```

Constructs a new instance of a

ButtonActionListener

.

**Parameters:** buttonIndex

- an index of the button
**Returns:** a new instance of a

ButtonActionListener

- getButtons

```java
protected
Object
[] getButtons()
```

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for. If the

JOptionPane

has options
set, they will be provided, otherwise if the optionType is

YES_NO_OPTION

,

yesNoOptions

is returned, if the type is

YES_NO_CANCEL_OPTION

yesNoCancelOptions

is returned, otherwise

defaultButtons

are returned.

**Returns:** the buttons to display from the JOptionPane

- getSizeButtonsToSameWidth

```java
protected boolean getSizeButtonsToSameWidth()
```

Returns

true

, basic L&F wants all the buttons to have the same
width.

**Returns:** true

if all the buttons should have the same width

- getInitialValueIndex

```java
protected int getInitialValueIndex()
```

Returns the initial index into the buttons to select. The index
is calculated from the initial value from the JOptionPane and
options of the JOptionPane or 0.

**Returns:** the initial index into the buttons to select

- resetInputValue

```java
protected void resetInputValue()
```

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

- selectInitialValue

```java
public void selectInitialValue​(
JOptionPane
op)
```

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

**Specified by:** selectInitialValue

in class

OptionPaneUI
**Parameters:** op

- a

JOptionPane

- containsCustomComponents

```java
public boolean containsCustomComponents​(
JOptionPane
op)
```

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

**Specified by:** containsCustomComponents

in class

OptionPaneUI
**Parameters:** op

- a

JOptionPane
**Returns:** true

if the given

JOptionPane

contains user
created

Component

s

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

Creates a new

BasicOptionPaneUI

instance.

**Parameters:** x

- the component
**Returns:** a new

BasicOptionPaneUI

instance

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Creates a new

BasicOptionPaneUI

instance.

installUI

```java
public void installUI​(
JComponent
c)
```

Installs the receiver as the L&F for the passed in

JOptionPane

.

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

Installs the receiver as the L&F for the passed in

JOptionPane

.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Removes the receiver from the L&F controller of the passed in split
pane.

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

Removes the receiver from the L&F controller of the passed in split
pane.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

installComponents

```java
protected void installComponents()
```

Registers components.

---

#### installComponents

protected void installComponents()

Registers components.

uninstallComponents

```java
protected void uninstallComponents()
```

Unregisters components.

---

#### uninstallComponents

protected void uninstallComponents()

Unregisters components.

createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Returns a layout manager.

**Returns:** a layout manager

---

#### createLayoutManager

protected

LayoutManager

createLayoutManager()

Returns a layout manager.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Returns an instance of

PropertyChangeListener

.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Registers keyboard actions.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

getMinimumOptionPaneSize

```java
public
Dimension
getMinimumOptionPaneSize()
```

Returns the minimum size the option pane should be. Primarily
provided for subclassers wishing to offer a different minimum size.

**Returns:** the minimum size of the option pane

---

#### getMinimumOptionPaneSize

public

Dimension

getMinimumOptionPaneSize()

Returns the minimum size the option pane should be. Primarily
provided for subclassers wishing to offer a different minimum size.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

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

c)

If

c

is the

JOptionPane

the receiver
is contained in, the preferred
size that is returned is the maximum of the preferred size of
the

LayoutManager

for the

JOptionPane

, and

getMinimumOptionPaneSize

.

createMessageArea

```java
protected
Container
createMessageArea()
```

Messaged from

installComponents

to create a

Container

containing the body of the message. The icon is the created
by calling

addIcon

.

**Returns:** a instance of

Container

---

#### createMessageArea

protected

Container

createMessageArea()

Messaged from

installComponents

to create a

Container

containing the body of the message. The icon is the created
by calling

addIcon

.

addMessageComponents

```java
protected void addMessageComponents​(
Container
container,

GridBagConstraints
cons,

Object
msg,
int maxll,
boolean internallyCreated)
```

Creates the appropriate object to represent

msg

and places it
into

container

. If

msg

is an instance of

Component

, it is added directly; if it is an

Icon

, a

JLabel

is created to represent it; otherwise, a

JLabel

is created for the string. If

msg

is an Object[], this method
will be recursively invoked for the children.

internallyCreated

is

true

if

msg

is an instance of

Component

and
was created internally by this method (this is used to correctly set

hasCustomComponents

only if

internallyCreated

is

false

).

**Parameters:** container

- a container
**Parameters:** cons

- an instance of

GridBagConstraints
**Parameters:** msg

- a message
**Parameters:** maxll

- a maximum length
**Parameters:** internallyCreated

-

true

if the component was internally created

---

#### addMessageComponents

protected void addMessageComponents​(

Container

container,

GridBagConstraints

cons,

Object

msg,
int maxll,
boolean internallyCreated)

Creates the appropriate object to represent

msg

and places it
into

container

. If

msg

is an instance of

Component

, it is added directly; if it is an

Icon

, a

JLabel

is created to represent it; otherwise, a

JLabel

is created for the string. If

msg

is an Object[], this method
will be recursively invoked for the children.

internallyCreated

is

true

if

msg

is an instance of

Component

and
was created internally by this method (this is used to correctly set

hasCustomComponents

only if

internallyCreated

is

false

).

getMessage

```java
protected
Object
getMessage()
```

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

**Returns:** the message to display

---

#### getMessage

protected

Object

getMessage()

Returns the message to display from the

JOptionPane

the receiver is
providing the look and feel for.

addIcon

```java
protected void addIcon​(
Container
top)
```

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

. This is messaged from

createMessageArea

.

**Parameters:** top

- a container

---

#### addIcon

protected void addIcon​(

Container

top)

Creates and adds a JLabel representing the icon returned from

getIcon

to

top

. This is messaged from

createMessageArea

.

getIcon

```java
protected
Icon
getIcon()
```

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

**Returns:** the icon

---

#### getIcon

protected

Icon

getIcon()

Returns the icon from the

JOptionPane

the receiver is providing
the look and feel for, or the default icon as returned from

getDefaultIcon

.

getIconForType

```java
protected
Icon
getIconForType​(int messageType)
```

Returns the icon to use for the passed in type.

**Parameters:** messageType

- a type of message
**Returns:** the icon to use for the passed in type

---

#### getIconForType

protected

Icon

getIconForType​(int messageType)

Returns the icon to use for the passed in type.

getMaxCharactersPerLineCount

```java
protected int getMaxCharactersPerLineCount()
```

Returns the maximum number of characters to place on a line.

**Returns:** the maximum number of characters to place on a line

---

#### getMaxCharactersPerLineCount

protected int getMaxCharactersPerLineCount()

Returns the maximum number of characters to place on a line.

burstStringInto

```java
protected void burstStringInto​(
Container
c,

String
d,
int maxll)
```

Recursively creates new

JLabel

instances to represent

d

.
Each

JLabel

instance is added to

c

.

**Parameters:** c

- a container
**Parameters:** d

- a text
**Parameters:** maxll

- a maximum length of a text

---

#### burstStringInto

protected void burstStringInto​(

Container

c,

String

d,
int maxll)

Recursively creates new

JLabel

instances to represent

d

.
Each

JLabel

instance is added to

c

.

createSeparator

```java
protected
Container
createSeparator()
```

Returns a separator.

**Returns:** a separator

---

#### createSeparator

protected

Container

createSeparator()

Returns a separator.

createButtonArea

```java
protected
Container
createButtonArea()
```

Creates and returns a

Container

containing the buttons.
The buttons are created by calling

getButtons

.

**Returns:** a

Container

containing the buttons

---

#### createButtonArea

protected

Container

createButtonArea()

Creates and returns a

Container

containing the buttons.
The buttons are created by calling

getButtons

.

addButtonComponents

```java
protected void addButtonComponents​(
Container
container,

Object
[] buttons,
int initialIndex)
```

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

. This
differs from addMessageComponents in that it will recurse on

buttons

and that if button is not a Component
it will create an instance of JButton.

**Parameters:** container

- a container
**Parameters:** buttons

- an array of buttons
**Parameters:** initialIndex

- an initial index

---

#### addButtonComponents

protected void addButtonComponents​(

Container

container,

Object

[] buttons,
int initialIndex)

Creates the appropriate object to represent each of the objects in

buttons

and adds it to

container

. This
differs from addMessageComponents in that it will recurse on

buttons

and that if button is not a Component
it will create an instance of JButton.

createButtonActionListener

```java
protected
ActionListener
createButtonActionListener​(int buttonIndex)
```

Constructs a new instance of a

ButtonActionListener

.

**Parameters:** buttonIndex

- an index of the button
**Returns:** a new instance of a

ButtonActionListener

---

#### createButtonActionListener

protected

ActionListener

createButtonActionListener​(int buttonIndex)

Constructs a new instance of a

ButtonActionListener

.

getButtons

```java
protected
Object
[] getButtons()
```

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for. If the

JOptionPane

has options
set, they will be provided, otherwise if the optionType is

YES_NO_OPTION

,

yesNoOptions

is returned, if the type is

YES_NO_CANCEL_OPTION

yesNoCancelOptions

is returned, otherwise

defaultButtons

are returned.

**Returns:** the buttons to display from the JOptionPane

---

#### getButtons

protected

Object

[] getButtons()

Returns the buttons to display from the

JOptionPane

the receiver is
providing the look and feel for. If the

JOptionPane

has options
set, they will be provided, otherwise if the optionType is

YES_NO_OPTION

,

yesNoOptions

is returned, if the type is

YES_NO_CANCEL_OPTION

yesNoCancelOptions

is returned, otherwise

defaultButtons

are returned.

getSizeButtonsToSameWidth

```java
protected boolean getSizeButtonsToSameWidth()
```

Returns

true

, basic L&F wants all the buttons to have the same
width.

**Returns:** true

if all the buttons should have the same width

---

#### getSizeButtonsToSameWidth

protected boolean getSizeButtonsToSameWidth()

Returns

true

, basic L&F wants all the buttons to have the same
width.

getInitialValueIndex

```java
protected int getInitialValueIndex()
```

Returns the initial index into the buttons to select. The index
is calculated from the initial value from the JOptionPane and
options of the JOptionPane or 0.

**Returns:** the initial index into the buttons to select

---

#### getInitialValueIndex

protected int getInitialValueIndex()

Returns the initial index into the buttons to select. The index
is calculated from the initial value from the JOptionPane and
options of the JOptionPane or 0.

resetInputValue

```java
protected void resetInputValue()
```

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

---

#### resetInputValue

protected void resetInputValue()

Sets the input value in the option pane the receiver is providing
the look and feel for based on the value in the inputComponent.

selectInitialValue

```java
public void selectInitialValue​(
JOptionPane
op)
```

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

**Specified by:** selectInitialValue

in class

OptionPaneUI
**Parameters:** op

- a

JOptionPane

---

#### selectInitialValue

public void selectInitialValue​(

JOptionPane

op)

If inputComponent is non-null, the focus is requested on that,
otherwise request focus on the default value

containsCustomComponents

```java
public boolean containsCustomComponents​(
JOptionPane
op)
```

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

**Specified by:** containsCustomComponents

in class

OptionPaneUI
**Parameters:** op

- a

JOptionPane
**Returns:** true

if the given

JOptionPane

contains user
created

Component

s

---

#### containsCustomComponents

public boolean containsCustomComponents​(

JOptionPane

op)

Returns true if in the last call to validateComponent the message
or buttons contained a subclass of Component.

---

