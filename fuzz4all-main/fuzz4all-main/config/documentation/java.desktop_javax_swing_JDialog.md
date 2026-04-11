# Class JDialog

**Source:** `java.desktop\javax\swing\JDialog.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="JMenuBar",

description
="A toplevel window for creating dialog boxes.")
public class
JDialog

extends
Dialog

implements
WindowConstants
,
Accessible
,
RootPaneContainer
```

The main class for creating a dialog window. You can use this class
to create a custom dialog, or invoke the many class methods
in

JOptionPane

to create a variety of standard dialogs.
For information about creating dialogs, see

The Java Tutorial

section

How
to Make Dialogs

.

The

JDialog

component contains a

JRootPane

as its only child.
The

contentPane

should be the parent of any children of the

JDialog

.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a dialog as follows:

```java
dialog.add(child);
```

And the child will be added to the contentPane.
The

contentPane

is always non-

null

.
Attempting to set it to

null

generates an exception.
The default

contentPane

has a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JDialog

.

Please see the

JRootPane

documentation for a complete
description of the

contentPane

,

glassPane

,
and

layeredPane

components.

In a multi-screen environment, you can create a

JDialog

on a different screen device than its owner. See

Frame

for
more information.

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

RootPaneContainer

,

WindowConstants

---

### Field Details

#### protected
JRootPane
rootPane

**See Also:**
- getRootPane()

,

setRootPane(javax.swing.JRootPane)

---

#### protected boolean rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JDialog

is constructed.

**See Also:**
- isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### protected
AccessibleContext
accessibleContext

AccessibleContext

associated with this

JDialog

---

### Constructor Details

#### public JDialog()

Creates a modeless dialog without a title and without a specified

Frame

owner. A shared, hidden frame will be
set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Frame
owner)

Creates a modeless dialog with the specified

Frame

as its owner and an empty title. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:**
- owner

- the

Frame

from which the dialog is displayed

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Frame
owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Frame

as its owner. If

owner

is

null

,
a shared, hidden frame will be set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:**
- owner

- the

Frame

from which the dialog is displayed
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Frame
owner,

String
title)

Creates a modeless dialog with the specified title and
with the specified owner frame. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:**
- owner

- the

Frame

from which the dialog is displayed
- title

- the

String

to display in the dialog's
title bar

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Frame
owner,

String
title,
boolean modal)

Creates a dialog with the specified title, owner

Frame

and modality. If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:**
- owner

- the

Frame

from which the dialog is displayed
- title

- the

String

to display in the dialog's
title bar
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

otherwise the dialog is modeless

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.
If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:**
- owner

- the

Frame

from which the dialog is displayed
- title

- the

String

to display in the dialog's
title bar
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
- gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.4

---

#### public JDialog​(
Dialog
owner)

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner

**Throws:**
- HeadlessException

-

if GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Dialog
owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Dialog
owner,

String
title)

Creates a modeless dialog with the specified title and
with the specified owner dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
- title

- the

String

to display in the dialog's
title bar

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Dialog
owner,

String
title,
boolean modal)

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
- title

- the

String

to display in the dialog's
title bar
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### public JDialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
- title

- the

String

to display in the dialog's
title bar
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless
- gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.

**See Also:**
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.4

---

#### public JDialog​(
Window
owner)

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner

**Throws:**
- IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
- IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.6

---

#### public JDialog​(
Window
owner,

Dialog.ModalityType
modalityType)

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
- modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS

**Throws:**
- IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
- IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
- SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType

**See Also:**
- Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.6

---

#### public JDialog​(
Window
owner,

String
title)

Creates a modeless dialog with the specified title and owner

Window

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
- title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title

**Throws:**
- IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
- IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.6

---

#### public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)

Creates a dialog with the specified title, owner

Window

and
modality.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
- title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
- modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS

**Throws:**
- IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
- IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
- SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType

**See Also:**
- Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.6

---

#### public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:**
- owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
- title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
- modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
- gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed

**Throws:**
- IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
- IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
- SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType

**See Also:**
- Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

**Since:**
- 1.6

---

### Method Details

#### protected void dialogInit()

Called by the constructors to init the

JDialog

properly.

---

#### protected
JRootPane
createRootPane()

Called by the constructor methods to create the default

rootPane

.

**Returns:**
- a new

JRootPane

---

#### protected void processWindowEvent​(
WindowEvent
e)

Handles window events depending on the state of the

defaultCloseOperation

property.

**Overrides:**
- processWindowEvent

in class

Window

**Parameters:**
- e

- the window event

**See Also:**
- setDefaultCloseOperation(int)

---

#### @BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE"},

description
="The dialog\'s default close operation.")
public void setDefaultCloseOperation​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the dialog after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
dialog after invoking any registered

WindowListener

objects.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:**
- operation

- the operation which should be performed when the
user closes the dialog

**Throws:**
- IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values

**See Also:**
- Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

---

#### public int getDefaultCloseOperation()

Returns the operation which occurs when the user
initiates a "close" on this dialog.

**Returns:**
- an integer indicating the window-close operation

**See Also:**
- setDefaultCloseOperation(int)

---

#### @BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JDialog

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:**
- newHandler

- the new

TransferHandler

**See Also:**
- TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

**Since:**
- 1.6

---

#### public
TransferHandler
getTransferHandler()

Gets the

transferHandler

property.

**Returns:**
- the value of the

transferHandler

property

**See Also:**
- TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

**Since:**
- 1.6

---

#### public void update​(
Graphics
g)

Calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:**
- update

in class

Container

**Parameters:**
- g

- the

Graphics

context in which to paint

**See Also:**
- Component.update(Graphics)

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this dialog.")
public void setJMenuBar​(
JMenuBar
menu)

Sets the menubar for this dialog.

**Parameters:**
- menu

- the menubar being placed in the dialog

**See Also:**
- getJMenuBar()

---

#### public
JMenuBar
getJMenuBar()

Returns the menubar set on this dialog.

**Returns:**
- the menubar set on this dialog

**See Also:**
- setJMenuBar(javax.swing.JMenuBar)

---

#### protected boolean isRootPaneCheckingEnabled()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:**
- true if

add

and

setLayout

are forwarded; false otherwise

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### @BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:**
- enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JDialog

.

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

---

#### protected void addImpl​(
Component
comp,

Object
constraints,
int index)

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:**
- addImpl

in class

Container

**Parameters:**
- comp

- the component to be enhanced
- constraints

- the constraints to be respected
- index

- the index

**Throws:**
- IllegalArgumentException

- if

index

is invalid
- IllegalArgumentException

- if adding the container's parent
to itself
- IllegalArgumentException

- if adding a window to a container

**See Also:**
- setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### public void remove​(
Component
comp)

Removes the specified component from the container. If

comp

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JDialog

or

contentPane

.

**Overrides:**
- remove

in class

Container

**Parameters:**
- comp

- the component to be removed

**Throws:**
- NullPointerException

- if

comp

is null

**See Also:**
- Container.add(java.awt.Component)

,

RootPaneContainer

---

#### public void setLayout​(
LayoutManager
manager)

Sets the

LayoutManager

.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:**
- setLayout

in class

Container

**Parameters:**
- manager

- the

LayoutManager

**See Also:**
- setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this dialog.")
public
JRootPane
getRootPane()

Returns the

rootPane

object for this dialog.

**Specified by:**
- getRootPane

in interface

RootPaneContainer

**Returns:**
- this components single JRootPane child.

**See Also:**
- setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

---

#### protected void setRootPane​(
JRootPane
root)

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:**
- root

- the

rootPane

object for this dialog

**See Also:**
- getRootPane()

---

#### public
Container
getContentPane()

Returns the

contentPane

object for this dialog.

**Specified by:**
- getContentPane

in interface

RootPaneContainer

**Returns:**
- the

contentPane

property

**See Also:**
- setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the dialog where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:**
- setContentPane

in interface

RootPaneContainer

**Parameters:**
- contentPane

- the

contentPane

object for this dialog

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null

**See Also:**
- JRootPane

,

getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

---

#### public
JLayeredPane
getLayeredPane()

Returns the

layeredPane

object for this dialog.

**Specified by:**
- getLayeredPane

in interface

RootPaneContainer

**Returns:**
- the

layeredPane

property

**See Also:**
- setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane which holds the various dialog layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:**
- setLayeredPane

in interface

RootPaneContainer

**Parameters:**
- layeredPane

- the new

layeredPane

property

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null

**See Also:**
- getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

---

#### public
Component
getGlassPane()

Returns the

glassPane

object for this dialog.

**Specified by:**
- getGlassPane

in interface

RootPaneContainer

**Returns:**
- the

glassPane

property

**See Also:**
- setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

---

#### @BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:**
- setGlassPane

in interface

RootPaneContainer

**Parameters:**
- glassPane

- the

glassPane

object for this dialog

**See Also:**
- getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

---

#### @BeanProperty
(
bound
=false)
public
Graphics
getGraphics()

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:**
- getGraphics

in class

Component

**Returns:**
- a graphics context for this component, or

null

if it has none

**See Also:**
- Component.paint(java.awt.Graphics)

**Since:**
- 1.6

---

#### public void repaint​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:**
- repaint

in class

Component

**Parameters:**
- time

- maximum time in milliseconds before update
- x

- the

x

coordinate
- y

- the

y

coordinate
- width

- the width
- height

- the height

**See Also:**
- RepaintManager

**Since:**
- 1.6

---

#### public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JDialog

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JDialog

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JDialog by doing the following:

```java
JDialog dialog = new JDialog();
dialog.setUndecorated(true);
dialog.getRootPane().setWindowDecorationStyle(JRootPane.PLAIN_DIALOG);
```

**Parameters:**
- defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations

**See Also:**
- LookAndFeel.getSupportsWindowDecorations()

**Since:**
- 1.4

---

#### public static boolean isDefaultLookAndFeelDecorated()

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:**
- true if look and feel should provide Window decorations.

**Since:**
- 1.4

---

#### protected
String
paramString()

Returns a string representation of this

JDialog

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

Dialog

**Returns:**
- a string representation of this

JDialog

.

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JDialog.
For JDialogs, the AccessibleContext takes the form of an
AccessibleJDialog.
A new AccessibleJDialog instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Dialog

**Returns:**
- an AccessibleJDialog that serves as the
AccessibleContext of this JDialog

---

### Additional Sections

#### Class JDialog

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Window
- - java.awt.Dialog
- - javax.swing.JDialog

java.awt.Component

- java.awt.Container
- - java.awt.Window
- - java.awt.Dialog
- - javax.swing.JDialog

java.awt.Container

- java.awt.Window
- - java.awt.Dialog
- - javax.swing.JDialog

java.awt.Window

- java.awt.Dialog
- - javax.swing.JDialog

java.awt.Dialog

- javax.swing.JDialog

javax.swing.JDialog

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

RootPaneContainer

,

WindowConstants

```java
@JavaBean
(
defaultProperty
="JMenuBar",

description
="A toplevel window for creating dialog boxes.")
public class
JDialog

extends
Dialog

implements
WindowConstants
,
Accessible
,
RootPaneContainer
```

The main class for creating a dialog window. You can use this class
to create a custom dialog, or invoke the many class methods
in

JOptionPane

to create a variety of standard dialogs.
For information about creating dialogs, see

The Java Tutorial

section

How
to Make Dialogs

.

The

JDialog

component contains a

JRootPane

as its only child.
The

contentPane

should be the parent of any children of the

JDialog

.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a dialog as follows:

```java
dialog.add(child);
```

And the child will be added to the contentPane.
The

contentPane

is always non-

null

.
Attempting to set it to

null

generates an exception.
The default

contentPane

has a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JDialog

.

Please see the

JRootPane

documentation for a complete
description of the

contentPane

,

glassPane

,
and

layeredPane

components.

In a multi-screen environment, you can create a

JDialog

on a different screen device than its owner. See

Frame

for
more information.

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
**See Also:** JOptionPane

,

JRootPane

,

RootPaneContainer

,

Serialized Form

@JavaBean

(

defaultProperty

="JMenuBar",

description

="A toplevel window for creating dialog boxes.")
public class

JDialog

extends

Dialog

implements

WindowConstants

,

Accessible

,

RootPaneContainer

The main class for creating a dialog window. You can use this class
to create a custom dialog, or invoke the many class methods
in

JOptionPane

to create a variety of standard dialogs.
For information about creating dialogs, see

The Java Tutorial

section

How
to Make Dialogs

.

The

JDialog

component contains a

JRootPane

as its only child.
The

contentPane

should be the parent of any children of the

JDialog

.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a dialog as follows:

```java
dialog.add(child);
```

And the child will be added to the contentPane.
The

contentPane

is always non-

null

.
Attempting to set it to

null

generates an exception.
The default

contentPane

has a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JDialog

.

Please see the

JRootPane

documentation for a complete
description of the

contentPane

,

glassPane

,
and

layeredPane

components.

In a multi-screen environment, you can create a

JDialog

on a different screen device than its owner. See

Frame

for
more information.

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

The

JDialog

component contains a

JRootPane

as its only child.
The

contentPane

should be the parent of any children of the

JDialog

.
As a convenience, the

add

,

remove

, and

setLayout

methods of this class are overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a dialog as follows:

```java
dialog.add(child);
```

And the child will be added to the contentPane.
The

contentPane

is always non-

null

.
Attempting to set it to

null

generates an exception.
The default

contentPane

has a

BorderLayout

manager set on it.
Refer to

RootPaneContainer

for details on adding, removing and setting the

LayoutManager

of a

JDialog

.

Please see the

JRootPane

documentation for a complete
description of the

contentPane

,

glassPane

,
and

layeredPane

components.

In a multi-screen environment, you can create a

JDialog

on a different screen device than its owner. See

Frame

for
more information.

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

dialog.add(child);

Please see the

JRootPane

documentation for a complete
description of the

contentPane

,

glassPane

,
and

layeredPane

components.

In a multi-screen environment, you can create a

JDialog

on a different screen device than its owner. See

Frame

for
more information.

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

In a multi-screen environment, you can create a

JDialog

on a different screen device than its owner. See

Frame

for
more information.

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

JDialog.AccessibleJDialog

This class implements accessibility support for the

JDialog

class.

- Nested classes/interfaces declared in class java.awt.

Dialog

Dialog.AccessibleAWTDialog

,

Dialog.ModalExclusionType

,

Dialog.ModalityType

- Nested classes/interfaces declared in class java.awt.

Window

Window.AccessibleAWTWindow

,

Window.Type

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

protected

AccessibleContext

accessibleContext

AccessibleContext

associated with this

JDialog

protected

JRootPane

rootPane

protected boolean

rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

- Fields declared in class java.awt.

Dialog

DEFAULT_MODALITY_TYPE

- Fields declared in class java.awt.

Component

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

WindowConstants

DISPOSE_ON_CLOSE

,

DO_NOTHING_ON_CLOSE

,

EXIT_ON_CLOSE

,

HIDE_ON_CLOSE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JDialog

()

Creates a modeless dialog without a title and without a specified

Frame

owner.

JDialog

​(

Dialog

owner)

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

JDialog

​(

Dialog

owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

JDialog

​(

Dialog

owner,

String

title)

Creates a modeless dialog with the specified title and
with the specified owner dialog.

JDialog

​(

Dialog

owner,

String

title,
boolean modal)

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

JDialog

​(

Dialog

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

JDialog

​(

Frame

owner)

Creates a modeless dialog with the specified

Frame

as its owner and an empty title.

JDialog

​(

Frame

owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Frame

as its owner.

JDialog

​(

Frame

owner,

String

title)

Creates a modeless dialog with the specified title and
with the specified owner frame.

JDialog

​(

Frame

owner,

String

title,
boolean modal)

Creates a dialog with the specified title, owner

Frame

and modality.

JDialog

​(

Frame

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.

JDialog

​(

Window

owner)

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

JDialog

​(

Window

owner,

Dialog.ModalityType

modalityType)

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

JDialog

​(

Window

owner,

String

title)

Creates a modeless dialog with the specified title and owner

Window

.

JDialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType)

Creates a dialog with the specified title, owner

Window

and
modality.

JDialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType,

GraphicsConfiguration

gc)

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

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

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified child

Component

.

protected

JRootPane

createRootPane

()

Called by the constructor methods to create the default

rootPane

.

protected void

dialogInit

()

Called by the constructors to init the

JDialog

properly.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JDialog.

Container

getContentPane

()

Returns the

contentPane

object for this dialog.

int

getDefaultCloseOperation

()

Returns the operation which occurs when the user
initiates a "close" on this dialog.

Component

getGlassPane

()

Returns the

glassPane

object for this dialog.

Graphics

getGraphics

()

Creates a graphics context for this component.

JMenuBar

getJMenuBar

()

Returns the menubar set on this dialog.

JLayeredPane

getLayeredPane

()

Returns the

layeredPane

object for this dialog.

JRootPane

getRootPane

()

Returns the

rootPane

object for this dialog.

TransferHandler

getTransferHandler

()

Gets the

transferHandler

property.

static boolean

isDefaultLookAndFeelDecorated

()

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel.

protected boolean

isRootPaneCheckingEnabled

()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

protected

String

paramString

()

Returns a string representation of this

JDialog

.

protected void

processWindowEvent

​(

WindowEvent

e)

Handles window events depending on the state of the

defaultCloseOperation

property.

void

remove

​(

Component

comp)

Removes the specified component from the container.

void

repaint

​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds.

void

setContentPane

​(

Container

contentPane)

Sets the

contentPane

property.

void

setDefaultCloseOperation

​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.

static void

setDefaultLookAndFeelDecorated

​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel.

void

setGlassPane

​(

Component

glassPane)

Sets the

glassPane

property.

void

setJMenuBar

​(

JMenuBar

menu)

Sets the menubar for this dialog.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

Sets the

layeredPane

property.

void

setLayout

​(

LayoutManager

manager)

Sets the

LayoutManager

.

protected void

setRootPane

​(

JRootPane

root)

Sets the

rootPane

property.

protected void

setRootPaneCheckingEnabled

​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

void

setTransferHandler

​(

TransferHandler

newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

void

update

​(

Graphics

g)

Calls

paint(g)

.

- Methods declared in class java.awt.

Dialog

addNotify

,

getModalityType

,

getTitle

,

hide

,

isModal

,

isResizable

,

isUndecorated

,

setModal

,

setModalityType

,

setResizable

,

setTitle

,

setUndecorated

,

setVisible

,

show

,

toBack

- Methods declared in class java.awt.

Window

addPropertyChangeListener

,

addPropertyChangeListener

,

addWindowFocusListener

,

addWindowListener

,

addWindowStateListener

,

applyResourceBundle

,

applyResourceBundle

,

createBufferStrategy

,

createBufferStrategy

,

dispose

,

getBackground

,

getBufferStrategy

,

getFocusableWindowState

,

getFocusCycleRootAncestor

,

getFocusOwner

,

getFocusTraversalKeys

,

getIconImages

,

getInputContext

,

getListeners

,

getLocale

,

getModalExclusionType

,

getMostRecentFocusOwner

,

getOpacity

,

getOwnedWindows

,

getOwner

,

getOwnerlessWindows

,

getShape

,

getToolkit

,

getType

,

getWarningString

,

getWindowFocusListeners

,

getWindowListeners

,

getWindows

,

getWindowStateListeners

,

isActive

,

isAlwaysOnTop

,

isAlwaysOnTopSupported

,

isAutoRequestFocus

,

isFocusableWindow

,

isFocusCycleRoot

,

isFocused

,

isLocationByPlatform

,

isOpaque

,

isShowing

,

isValidateRoot

,

pack

,

paint

,

postEvent

,

processEvent

,

processWindowFocusEvent

,

processWindowStateEvent

,

removeWindowFocusListener

,

removeWindowListener

,

removeWindowStateListener

,

reshape

,

setAlwaysOnTop

,

setAutoRequestFocus

,

setBackground

,

setBounds

,

setBounds

,

setCursor

,

setFocusableWindowState

,

setFocusCycleRoot

,

setIconImage

,

setIconImages

,

setLocation

,

setLocation

,

setLocationByPlatform

,

setLocationRelativeTo

,

setMinimumSize

,

setModalExclusionType

,

setOpacity

,

setShape

,

setSize

,

setSize

,

setType

,

toFront

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

getAlignmentX

,

getAlignmentY

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

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

,

insets

,

invalidate

,

isAncestorOf

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

print

,

printComponents

,

processContainerEvent

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

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

getSize

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

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

isDoubleBuffered

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

prepareImage

,

prepareImage

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

resize

,

resize

,

revalidate

,

setComponentOrientation

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setMaximumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

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

JDialog.AccessibleJDialog

This class implements accessibility support for the

JDialog

class.

- Nested classes/interfaces declared in class java.awt.

Dialog

Dialog.AccessibleAWTDialog

,

Dialog.ModalExclusionType

,

Dialog.ModalityType

- Nested classes/interfaces declared in class java.awt.

Window

Window.AccessibleAWTWindow

,

Window.Type

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

JDialog

class.

Nested classes/interfaces declared in class java.awt.

Dialog

Dialog.AccessibleAWTDialog

,

Dialog.ModalExclusionType

,

Dialog.ModalityType

---

#### Nested classes/interfaces declared in class java.awt. Dialog

Nested classes/interfaces declared in class java.awt.

Window

Window.AccessibleAWTWindow

,

Window.Type

---

#### Nested classes/interfaces declared in class java.awt. Window

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

protected

AccessibleContext

accessibleContext

AccessibleContext

associated with this

JDialog

protected

JRootPane

rootPane

protected boolean

rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

- Fields declared in class java.awt.

Dialog

DEFAULT_MODALITY_TYPE

- Fields declared in class java.awt.

Component

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

WindowConstants

DISPOSE_ON_CLOSE

,

DO_NOTHING_ON_CLOSE

,

EXIT_ON_CLOSE

,

HIDE_ON_CLOSE

---

#### Field Summary

AccessibleContext

associated with this

JDialog

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

.

Fields declared in class java.awt.

Dialog

DEFAULT_MODALITY_TYPE

---

#### Fields declared in class java.awt. Dialog

Fields declared in class java.awt.

Component

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

WindowConstants

DISPOSE_ON_CLOSE

,

DO_NOTHING_ON_CLOSE

,

EXIT_ON_CLOSE

,

HIDE_ON_CLOSE

---

#### Fields declared in interface javax.swing. WindowConstants

Constructor Summary

Constructors

Constructor

Description

JDialog

()

Creates a modeless dialog without a title and without a specified

Frame

owner.

JDialog

​(

Dialog

owner)

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

JDialog

​(

Dialog

owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

JDialog

​(

Dialog

owner,

String

title)

Creates a modeless dialog with the specified title and
with the specified owner dialog.

JDialog

​(

Dialog

owner,

String

title,
boolean modal)

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

JDialog

​(

Dialog

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

JDialog

​(

Frame

owner)

Creates a modeless dialog with the specified

Frame

as its owner and an empty title.

JDialog

​(

Frame

owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Frame

as its owner.

JDialog

​(

Frame

owner,

String

title)

Creates a modeless dialog with the specified title and
with the specified owner frame.

JDialog

​(

Frame

owner,

String

title,
boolean modal)

Creates a dialog with the specified title, owner

Frame

and modality.

JDialog

​(

Frame

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.

JDialog

​(

Window

owner)

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

JDialog

​(

Window

owner,

Dialog.ModalityType

modalityType)

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

JDialog

​(

Window

owner,

String

title)

Creates a modeless dialog with the specified title and owner

Window

.

JDialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType)

Creates a dialog with the specified title, owner

Window

and
modality.

JDialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType,

GraphicsConfiguration

gc)

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

---

#### Constructor Summary

Creates a modeless dialog without a title and without a specified

Frame

owner.

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

Creates a modeless dialog with the specified title and
with the specified owner dialog.

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

Creates a modeless dialog with the specified

Frame

as its owner and an empty title.

Creates a dialog with an empty title and the specified modality and

Frame

as its owner.

Creates a modeless dialog with the specified title and
with the specified owner frame.

Creates a dialog with the specified title, owner

Frame

and modality.

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

Creates a modeless dialog with the specified title and owner

Window

.

Creates a dialog with the specified title, owner

Window

and
modality.

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified child

Component

.

protected

JRootPane

createRootPane

()

Called by the constructor methods to create the default

rootPane

.

protected void

dialogInit

()

Called by the constructors to init the

JDialog

properly.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JDialog.

Container

getContentPane

()

Returns the

contentPane

object for this dialog.

int

getDefaultCloseOperation

()

Returns the operation which occurs when the user
initiates a "close" on this dialog.

Component

getGlassPane

()

Returns the

glassPane

object for this dialog.

Graphics

getGraphics

()

Creates a graphics context for this component.

JMenuBar

getJMenuBar

()

Returns the menubar set on this dialog.

JLayeredPane

getLayeredPane

()

Returns the

layeredPane

object for this dialog.

JRootPane

getRootPane

()

Returns the

rootPane

object for this dialog.

TransferHandler

getTransferHandler

()

Gets the

transferHandler

property.

static boolean

isDefaultLookAndFeelDecorated

()

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel.

protected boolean

isRootPaneCheckingEnabled

()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

protected

String

paramString

()

Returns a string representation of this

JDialog

.

protected void

processWindowEvent

​(

WindowEvent

e)

Handles window events depending on the state of the

defaultCloseOperation

property.

void

remove

​(

Component

comp)

Removes the specified component from the container.

void

repaint

​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds.

void

setContentPane

​(

Container

contentPane)

Sets the

contentPane

property.

void

setDefaultCloseOperation

​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.

static void

setDefaultLookAndFeelDecorated

​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel.

void

setGlassPane

​(

Component

glassPane)

Sets the

glassPane

property.

void

setJMenuBar

​(

JMenuBar

menu)

Sets the menubar for this dialog.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

Sets the

layeredPane

property.

void

setLayout

​(

LayoutManager

manager)

Sets the

LayoutManager

.

protected void

setRootPane

​(

JRootPane

root)

Sets the

rootPane

property.

protected void

setRootPaneCheckingEnabled

​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

void

setTransferHandler

​(

TransferHandler

newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

void

update

​(

Graphics

g)

Calls

paint(g)

.

- Methods declared in class java.awt.

Dialog

addNotify

,

getModalityType

,

getTitle

,

hide

,

isModal

,

isResizable

,

isUndecorated

,

setModal

,

setModalityType

,

setResizable

,

setTitle

,

setUndecorated

,

setVisible

,

show

,

toBack

- Methods declared in class java.awt.

Window

addPropertyChangeListener

,

addPropertyChangeListener

,

addWindowFocusListener

,

addWindowListener

,

addWindowStateListener

,

applyResourceBundle

,

applyResourceBundle

,

createBufferStrategy

,

createBufferStrategy

,

dispose

,

getBackground

,

getBufferStrategy

,

getFocusableWindowState

,

getFocusCycleRootAncestor

,

getFocusOwner

,

getFocusTraversalKeys

,

getIconImages

,

getInputContext

,

getListeners

,

getLocale

,

getModalExclusionType

,

getMostRecentFocusOwner

,

getOpacity

,

getOwnedWindows

,

getOwner

,

getOwnerlessWindows

,

getShape

,

getToolkit

,

getType

,

getWarningString

,

getWindowFocusListeners

,

getWindowListeners

,

getWindows

,

getWindowStateListeners

,

isActive

,

isAlwaysOnTop

,

isAlwaysOnTopSupported

,

isAutoRequestFocus

,

isFocusableWindow

,

isFocusCycleRoot

,

isFocused

,

isLocationByPlatform

,

isOpaque

,

isShowing

,

isValidateRoot

,

pack

,

paint

,

postEvent

,

processEvent

,

processWindowFocusEvent

,

processWindowStateEvent

,

removeWindowFocusListener

,

removeWindowListener

,

removeWindowStateListener

,

reshape

,

setAlwaysOnTop

,

setAutoRequestFocus

,

setBackground

,

setBounds

,

setBounds

,

setCursor

,

setFocusableWindowState

,

setFocusCycleRoot

,

setIconImage

,

setIconImages

,

setLocation

,

setLocation

,

setLocationByPlatform

,

setLocationRelativeTo

,

setMinimumSize

,

setModalExclusionType

,

setOpacity

,

setShape

,

setSize

,

setSize

,

setType

,

toFront

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

getAlignmentX

,

getAlignmentY

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

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

,

insets

,

invalidate

,

isAncestorOf

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

print

,

printComponents

,

processContainerEvent

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

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

getSize

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

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

isDoubleBuffered

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

prepareImage

,

prepareImage

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

resize

,

resize

,

revalidate

,

setComponentOrientation

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setMaximumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

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

Adds the specified child

Component

.

Called by the constructor methods to create the default

rootPane

.

Called by the constructors to init the

JDialog

properly.

Gets the AccessibleContext associated with this JDialog.

Returns the

contentPane

object for this dialog.

Returns the operation which occurs when the user
initiates a "close" on this dialog.

Returns the

glassPane

object for this dialog.

Creates a graphics context for this component.

Returns the menubar set on this dialog.

Returns the

layeredPane

object for this dialog.

Returns the

rootPane

object for this dialog.

Gets the

transferHandler

property.

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel.

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

Returns a string representation of this

JDialog

.

Handles window events depending on the state of the

defaultCloseOperation

property.

Removes the specified component from the container.

Repaints the specified rectangle of this component within

time

milliseconds.

Sets the

contentPane

property.

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel.

Sets the

glassPane

property.

Sets the menubar for this dialog.

Sets the

layeredPane

property.

Sets the

LayoutManager

.

Sets the

rootPane

property.

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component.

Calls

paint(g)

.

Methods declared in class java.awt.

Dialog

addNotify

,

getModalityType

,

getTitle

,

hide

,

isModal

,

isResizable

,

isUndecorated

,

setModal

,

setModalityType

,

setResizable

,

setTitle

,

setUndecorated

,

setVisible

,

show

,

toBack

---

#### Methods declared in class java.awt. Dialog

Methods declared in class java.awt.

Window

addPropertyChangeListener

,

addPropertyChangeListener

,

addWindowFocusListener

,

addWindowListener

,

addWindowStateListener

,

applyResourceBundle

,

applyResourceBundle

,

createBufferStrategy

,

createBufferStrategy

,

dispose

,

getBackground

,

getBufferStrategy

,

getFocusableWindowState

,

getFocusCycleRootAncestor

,

getFocusOwner

,

getFocusTraversalKeys

,

getIconImages

,

getInputContext

,

getListeners

,

getLocale

,

getModalExclusionType

,

getMostRecentFocusOwner

,

getOpacity

,

getOwnedWindows

,

getOwner

,

getOwnerlessWindows

,

getShape

,

getToolkit

,

getType

,

getWarningString

,

getWindowFocusListeners

,

getWindowListeners

,

getWindows

,

getWindowStateListeners

,

isActive

,

isAlwaysOnTop

,

isAlwaysOnTopSupported

,

isAutoRequestFocus

,

isFocusableWindow

,

isFocusCycleRoot

,

isFocused

,

isLocationByPlatform

,

isOpaque

,

isShowing

,

isValidateRoot

,

pack

,

paint

,

postEvent

,

processEvent

,

processWindowFocusEvent

,

processWindowStateEvent

,

removeWindowFocusListener

,

removeWindowListener

,

removeWindowStateListener

,

reshape

,

setAlwaysOnTop

,

setAutoRequestFocus

,

setBackground

,

setBounds

,

setBounds

,

setCursor

,

setFocusableWindowState

,

setFocusCycleRoot

,

setIconImage

,

setIconImages

,

setLocation

,

setLocation

,

setLocationByPlatform

,

setLocationRelativeTo

,

setMinimumSize

,

setModalExclusionType

,

setOpacity

,

setShape

,

setSize

,

setSize

,

setType

,

toFront

---

#### Methods declared in class java.awt. Window

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

getAlignmentX

,

getAlignmentY

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

getFocusTraversalPolicy

,

getInsets

,

getLayout

,

getMaximumSize

,

getMinimumSize

,

getMousePosition

,

getPreferredSize

,

insets

,

invalidate

,

isAncestorOf

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

print

,

printComponents

,

processContainerEvent

,

remove

,

removeAll

,

removeContainerListener

,

removeNotify

,

setComponentZOrder

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocation

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

getSize

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

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

isDoubleBuffered

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

prepareImage

,

prepareImage

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

resize

,

resize

,

revalidate

,

setComponentOrientation

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setMaximumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

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

- rootPane

```java
protected
JRootPane
rootPane
```

**See Also:** getRootPane()

,

setRootPane(javax.swing.JRootPane)

- rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JDialog

is constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

AccessibleContext

associated with this

JDialog

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JDialog

```java
public JDialog()
```

Creates a modeless dialog without a title and without a specified

Frame

owner. A shared, hidden frame will be
set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner)
```

Creates a modeless dialog with the specified

Frame

as its owner and an empty title. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,
boolean modal)
```

Creates a dialog with an empty title and the specified modality and

Frame

as its owner. If

owner

is

null

,
a shared, hidden frame will be set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,

String
title)
```

Creates a modeless dialog with the specified title and
with the specified owner frame. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,

String
title,
boolean modal)
```

Creates a dialog with the specified title, owner

Frame

and modality. If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

otherwise the dialog is modeless
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.
If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner)
```

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Throws:** HeadlessException

-

if GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,
boolean modal)
```

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,

String
title)
```

Creates a modeless dialog with the specified title and
with the specified owner dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,

String
title,
boolean modal)
```

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner)
```

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

Dialog.ModalityType
modalityType)
```

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

String
title)
```

Creates a modeless dialog with the specified title and owner

Window

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)
```

Creates a dialog with the specified title, owner

Window

and
modality.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

============ METHOD DETAIL ==========

- Method Detail

- dialogInit

```java
protected void dialogInit()
```

Called by the constructors to init the

JDialog

properly.

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor methods to create the default

rootPane

.

**Returns:** a new

JRootPane

- processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Handles window events depending on the state of the

defaultCloseOperation

property.

**Overrides:** processWindowEvent

in class

Window
**Parameters:** e

- the window event
**See Also:** setDefaultCloseOperation(int)

- setDefaultCloseOperation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE"},

description
="The dialog\'s default close operation.")
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the dialog after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
dialog after invoking any registered

WindowListener

objects.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:** operation

- the operation which should be performed when the
user closes the dialog
**Throws:** IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values
**See Also:** Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

- getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the operation which occurs when the user
initiates a "close" on this dialog.

**Returns:** an integer indicating the window-close operation
**See Also:** setDefaultCloseOperation(int)

- setTransferHandler

```java
@BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)
```

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JDialog

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:** newHandler

- the new

TransferHandler
**Since:** 1.6
**See Also:** TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

- getTransferHandler

```java
public
TransferHandler
getTransferHandler()
```

Gets the

transferHandler

property.

**Returns:** the value of the

transferHandler

property
**Since:** 1.6
**See Also:** TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

- update

```java
public void update​(
Graphics
g)
```

Calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** Component.update(Graphics)

- setJMenuBar

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this dialog.")
public void setJMenuBar​(
JMenuBar
menu)
```

Sets the menubar for this dialog.

**Parameters:** menu

- the menubar being placed in the dialog
**See Also:** getJMenuBar()

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the menubar set on this dialog.

**Returns:** the menubar set on this dialog
**See Also:** setJMenuBar(javax.swing.JMenuBar)

- isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:** true if

add

and

setLayout

are forwarded; false otherwise
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- setRootPaneCheckingEnabled

```java
@BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)
```

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:** enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JDialog

.
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be respected
**Parameters:** index

- the index
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from the container. If

comp

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JDialog

or

contentPane

.

**Overrides:** remove

in class

Container
**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is null
**See Also:** Container.add(java.awt.Component)

,

RootPaneContainer

- setLayout

```java
public void setLayout​(
LayoutManager
manager)
```

Sets the

LayoutManager

.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:** setLayout

in class

Container
**Parameters:** manager

- the

LayoutManager
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- getRootPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this dialog.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this dialog.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** this components single JRootPane child.
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:** root

- the

rootPane

object for this dialog
**See Also:** getRootPane()

- getContentPane

```java
public
Container
getContentPane()
```

Returns the

contentPane

object for this dialog.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the

contentPane

property
**See Also:** setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

- setContentPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the dialog where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the

contentPane

object for this dialog
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** JRootPane

,

getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the

layeredPane

object for this dialog.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the

layeredPane

property
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

- setLayeredPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane which holds the various dialog layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the new

layeredPane

property
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Returns the

glassPane

object for this dialog.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the

glassPane

property
**See Also:** setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

- setGlassPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)
```

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the

glassPane

object for this dialog
**See Also:** getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

- getGraphics

```java
@BeanProperty
(
bound
=false)
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:** getGraphics

in class

Component
**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.6
**See Also:** Component.paint(java.awt.Graphics)

- repaint

```java
public void repaint​(long time,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:** repaint

in class

Component
**Parameters:** time

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.6
**See Also:** RepaintManager

- setDefaultLookAndFeelDecorated

```java
public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)
```

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JDialog

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JDialog

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JDialog by doing the following:

```java
JDialog dialog = new JDialog();
dialog.setUndecorated(true);
dialog.getRootPane().setWindowDecorationStyle(JRootPane.PLAIN_DIALOG);
```

**Parameters:** defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations
**Since:** 1.4
**See Also:** LookAndFeel.getSupportsWindowDecorations()

- isDefaultLookAndFeelDecorated

```java
public static boolean isDefaultLookAndFeelDecorated()
```

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:** true if look and feel should provide Window decorations.
**Since:** 1.4

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JDialog

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

Dialog
**Returns:** a string representation of this

JDialog

.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JDialog.
For JDialogs, the AccessibleContext takes the form of an
AccessibleJDialog.
A new AccessibleJDialog instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Dialog
**Returns:** an AccessibleJDialog that serves as the
AccessibleContext of this JDialog

Field Detail

- rootPane

```java
protected
JRootPane
rootPane
```

**See Also:** getRootPane()

,

setRootPane(javax.swing.JRootPane)

- rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JDialog

is constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

AccessibleContext

associated with this

JDialog

---

#### Field Detail

rootPane

```java
protected
JRootPane
rootPane
```

**See Also:** getRootPane()

,

setRootPane(javax.swing.JRootPane)

---

#### rootPane

protected

JRootPane

rootPane

rootPaneCheckingEnabled

```java
protected boolean rootPaneCheckingEnabled
```

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JDialog

is constructed.

**See Also:** isRootPaneCheckingEnabled()

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### rootPaneCheckingEnabled

protected boolean rootPaneCheckingEnabled

If true then calls to

add

and

setLayout

will be forwarded to the

contentPane

. This is initially
false, but is set to true when the

JDialog

is constructed.

accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

AccessibleContext

associated with this

JDialog

---

#### accessibleContext

protected

AccessibleContext

accessibleContext

AccessibleContext

associated with this

JDialog

Constructor Detail

- JDialog

```java
public JDialog()
```

Creates a modeless dialog without a title and without a specified

Frame

owner. A shared, hidden frame will be
set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner)
```

Creates a modeless dialog with the specified

Frame

as its owner and an empty title. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,
boolean modal)
```

Creates a dialog with an empty title and the specified modality and

Frame

as its owner. If

owner

is

null

,
a shared, hidden frame will be set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,

String
title)
```

Creates a modeless dialog with the specified title and
with the specified owner frame. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,

String
title,
boolean modal)
```

Creates a dialog with the specified title, owner

Frame

and modality. If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

otherwise the dialog is modeless
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.
If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner)
```

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Throws:** HeadlessException

-

if GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,
boolean modal)
```

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,

String
title)
```

Creates a modeless dialog with the specified title and
with the specified owner dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,

String
title,
boolean modal)
```

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner)
```

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

Dialog.ModalityType
modalityType)
```

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

String
title)
```

Creates a modeless dialog with the specified title and owner

Window

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)
```

Creates a dialog with the specified title, owner

Window

and
modality.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

- JDialog

```java
public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### Constructor Detail

JDialog

```java
public JDialog()
```

Creates a modeless dialog without a title and without a specified

Frame

owner. A shared, hidden frame will be
set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog()

Creates a modeless dialog without a title and without a specified

Frame

owner. A shared, hidden frame will be
set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

JDialog

```java
public JDialog​(
Frame
owner)
```

Creates a modeless dialog with the specified

Frame

as its owner and an empty title. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Frame

owner)

Creates a modeless dialog with the specified

Frame

as its owner and an empty title. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

JDialog

```java
public JDialog​(
Frame
owner,
boolean modal)
```

Creates a dialog with an empty title and the specified modality and

Frame

as its owner. If

owner

is

null

,
a shared, hidden frame will be set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Frame

owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Frame

as its owner. If

owner

is

null

,
a shared, hidden frame will be set as the owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

JDialog

```java
public JDialog​(
Frame
owner,

String
title)
```

Creates a modeless dialog with the specified title and
with the specified owner frame. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Frame

owner,

String

title)

Creates a modeless dialog with the specified title and
with the specified owner frame. If

owner

is

null

, a shared, hidden frame will be set as the
owner of the dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

JDialog

```java
public JDialog​(
Frame
owner,

String
title,
boolean modal)
```

Creates a dialog with the specified title, owner

Frame

and modality. If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

otherwise the dialog is modeless
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Frame

owner,

String

title,
boolean modal)

Creates a dialog with the specified title, owner

Frame

and modality. If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

JDialog

```java
public JDialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.
If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

**Parameters:** owner

- the

Frame

from which the dialog is displayed
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Frame

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Creates a dialog with the specified title,
owner

Frame

, modality and

GraphicsConfiguration

.
If

owner

is

null

,
a shared, hidden frame will be set as the owner of this dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

NOTE: This constructor does not allow you to create an unowned

JDialog

. To create an unowned

JDialog

you must use either the

JDialog(Window)

or

JDialog(Dialog)

constructor with an argument of

null

.

JDialog

```java
public JDialog​(
Dialog
owner)
```

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Throws:** HeadlessException

-

if GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Dialog

owner)

Creates a modeless dialog with the specified

Dialog

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Dialog
owner,
boolean modal)
```

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless.
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Dialog

owner,
boolean modal)

Creates a dialog with an empty title and the specified modality and

Dialog

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Dialog
owner,

String
title)
```

Creates a modeless dialog with the specified title and
with the specified owner dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Dialog

owner,

String

title)

Creates a modeless dialog with the specified title and
with the specified owner dialog.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Dialog
owner,

String
title,
boolean modal)
```

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Dialog

owner,

String

title,
boolean modal)

Creates a dialog with the specified title, modality
and the specified owner

Dialog

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the owner

Dialog

from which the dialog is displayed
or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

, otherwise the dialog is modeless
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true

.
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

Dialog.DEFAULT_MODALITY_TYPE

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Dialog

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Creates a dialog with the specified title, owner

Dialog

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Window
owner)
```

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Window

owner)

Creates a modeless dialog with the specified

Window

as its owner and an empty title.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Window
owner,

Dialog.ModalityType
modalityType)
```

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Window

owner,

Dialog.ModalityType

modalityType)

Creates a dialog with an empty title and the specified modality and

Window

as its owner.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Window
owner,

String
title)
```

Creates a modeless dialog with the specified title and owner

Window

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Window

owner,

String

title)

Creates a modeless dialog with the specified title and owner

Window

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)
```

Creates a dialog with the specified title, owner

Window

and
modality.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType)

Creates a dialog with the specified title, owner

Window

and
modality.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

JDialog

```java
public JDialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)
```

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

**Parameters:** owner

- the

Window

from which the dialog is displayed or

null

if this dialog has no owner
**Parameters:** title

- the

String

to display in the dialog's
title bar or

null

if the dialog has no title
**Parameters:** modalityType

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Parameters:** gc

- the

GraphicsConfiguration

of the target screen device;
if

null

, the default system

GraphicsConfiguration

is assumed
**Throws:** IllegalArgumentException

- if the

owner

is not an instance of

Dialog

or

Frame
**Throws:** IllegalArgumentException

- if the

owner

's

GraphicsConfiguration

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission to create modal dialogs
with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

Dialog.setModal(boolean)

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

JComponent.getDefaultLocale()

---

#### JDialog

public JDialog​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType,

GraphicsConfiguration

gc)

Creates a dialog with the specified title, owner

Window

,
modality and

GraphicsConfiguration

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

NOTE: Any popup components (

JComboBox

,

JPopupMenu

,

JMenuBar

)
created within a modal dialog will be forced to be lightweight.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

This constructor sets the component's locale property to the value
returned by

JComponent.getDefaultLocale

.

Method Detail

- dialogInit

```java
protected void dialogInit()
```

Called by the constructors to init the

JDialog

properly.

- createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor methods to create the default

rootPane

.

**Returns:** a new

JRootPane

- processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Handles window events depending on the state of the

defaultCloseOperation

property.

**Overrides:** processWindowEvent

in class

Window
**Parameters:** e

- the window event
**See Also:** setDefaultCloseOperation(int)

- setDefaultCloseOperation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE"},

description
="The dialog\'s default close operation.")
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the dialog after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
dialog after invoking any registered

WindowListener

objects.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:** operation

- the operation which should be performed when the
user closes the dialog
**Throws:** IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values
**See Also:** Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

- getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the operation which occurs when the user
initiates a "close" on this dialog.

**Returns:** an integer indicating the window-close operation
**See Also:** setDefaultCloseOperation(int)

- setTransferHandler

```java
@BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)
```

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JDialog

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:** newHandler

- the new

TransferHandler
**Since:** 1.6
**See Also:** TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

- getTransferHandler

```java
public
TransferHandler
getTransferHandler()
```

Gets the

transferHandler

property.

**Returns:** the value of the

transferHandler

property
**Since:** 1.6
**See Also:** TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

- update

```java
public void update​(
Graphics
g)
```

Calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** Component.update(Graphics)

- setJMenuBar

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this dialog.")
public void setJMenuBar​(
JMenuBar
menu)
```

Sets the menubar for this dialog.

**Parameters:** menu

- the menubar being placed in the dialog
**See Also:** getJMenuBar()

- getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the menubar set on this dialog.

**Returns:** the menubar set on this dialog
**See Also:** setJMenuBar(javax.swing.JMenuBar)

- isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:** true if

add

and

setLayout

are forwarded; false otherwise
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- setRootPaneCheckingEnabled

```java
@BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)
```

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:** enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JDialog

.
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be respected
**Parameters:** index

- the index
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from the container. If

comp

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JDialog

or

contentPane

.

**Overrides:** remove

in class

Container
**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is null
**See Also:** Container.add(java.awt.Component)

,

RootPaneContainer

- setLayout

```java
public void setLayout​(
LayoutManager
manager)
```

Sets the

LayoutManager

.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:** setLayout

in class

Container
**Parameters:** manager

- the

LayoutManager
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

- getRootPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this dialog.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this dialog.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** this components single JRootPane child.
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

- setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:** root

- the

rootPane

object for this dialog
**See Also:** getRootPane()

- getContentPane

```java
public
Container
getContentPane()
```

Returns the

contentPane

object for this dialog.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the

contentPane

property
**See Also:** setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

- setContentPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the dialog where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the

contentPane

object for this dialog
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** JRootPane

,

getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

- getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the

layeredPane

object for this dialog.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the

layeredPane

property
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

- setLayeredPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane which holds the various dialog layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the new

layeredPane

property
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

- getGlassPane

```java
public
Component
getGlassPane()
```

Returns the

glassPane

object for this dialog.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the

glassPane

property
**See Also:** setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

- setGlassPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)
```

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the

glassPane

object for this dialog
**See Also:** getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

- getGraphics

```java
@BeanProperty
(
bound
=false)
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:** getGraphics

in class

Component
**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.6
**See Also:** Component.paint(java.awt.Graphics)

- repaint

```java
public void repaint​(long time,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:** repaint

in class

Component
**Parameters:** time

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.6
**See Also:** RepaintManager

- setDefaultLookAndFeelDecorated

```java
public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)
```

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JDialog

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JDialog

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JDialog by doing the following:

```java
JDialog dialog = new JDialog();
dialog.setUndecorated(true);
dialog.getRootPane().setWindowDecorationStyle(JRootPane.PLAIN_DIALOG);
```

**Parameters:** defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations
**Since:** 1.4
**See Also:** LookAndFeel.getSupportsWindowDecorations()

- isDefaultLookAndFeelDecorated

```java
public static boolean isDefaultLookAndFeelDecorated()
```

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:** true if look and feel should provide Window decorations.
**Since:** 1.4

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JDialog

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

Dialog
**Returns:** a string representation of this

JDialog

.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JDialog.
For JDialogs, the AccessibleContext takes the form of an
AccessibleJDialog.
A new AccessibleJDialog instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Dialog
**Returns:** an AccessibleJDialog that serves as the
AccessibleContext of this JDialog

---

#### Method Detail

dialogInit

```java
protected void dialogInit()
```

Called by the constructors to init the

JDialog

properly.

---

#### dialogInit

protected void dialogInit()

Called by the constructors to init the

JDialog

properly.

createRootPane

```java
protected
JRootPane
createRootPane()
```

Called by the constructor methods to create the default

rootPane

.

**Returns:** a new

JRootPane

---

#### createRootPane

protected

JRootPane

createRootPane()

Called by the constructor methods to create the default

rootPane

.

processWindowEvent

```java
protected void processWindowEvent​(
WindowEvent
e)
```

Handles window events depending on the state of the

defaultCloseOperation

property.

**Overrides:** processWindowEvent

in class

Window
**Parameters:** e

- the window event
**See Also:** setDefaultCloseOperation(int)

---

#### processWindowEvent

protected void processWindowEvent​(

WindowEvent

e)

Handles window events depending on the state of the

defaultCloseOperation

property.

setDefaultCloseOperation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE"},

description
="The dialog\'s default close operation.")
public void setDefaultCloseOperation​(int operation)
```

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the dialog after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
dialog after invoking any registered

WindowListener

objects.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

**Parameters:** operation

- the operation which should be performed when the
user closes the dialog
**Throws:** IllegalArgumentException

- if defaultCloseOperation value
isn't one of the above valid values
**See Also:** Window.addWindowListener(java.awt.event.WindowListener)

,

getDefaultCloseOperation()

,

WindowConstants

---

#### setDefaultCloseOperation

@BeanProperty

(

preferred

=true,

enumerationValues

={"WindowConstants.DO_NOTHING_ON_CLOSE","WindowConstants.HIDE_ON_CLOSE","WindowConstants.DISPOSE_ON_CLOSE"},

description

="The dialog\'s default close operation.")
public void setDefaultCloseOperation​(int operation)

Sets the operation that will happen by default when
the user initiates a "close" on this dialog.
You must specify one of the following choices:

- DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the dialog after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
dialog after invoking any registered

WindowListener

objects.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

DO_NOTHING_ON_CLOSE

(defined in

WindowConstants

):
Don't do anything; require the
program to handle the operation in the

windowClosing

method of a registered

WindowListener

object.

HIDE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide the dialog after
invoking any registered

WindowListener

objects.

DISPOSE_ON_CLOSE

(defined in

WindowConstants

):
Automatically hide and dispose the
dialog after invoking any registered

WindowListener

objects.

The value is set to

HIDE_ON_CLOSE

by default. Changes
to the value of this property cause the firing of a property
change event, with property name "defaultCloseOperation".

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

Note

: When the last displayable window within the
Java virtual machine (VM) is disposed of, the VM may
terminate. See

AWT Threading Issues

for more information.

getDefaultCloseOperation

```java
public int getDefaultCloseOperation()
```

Returns the operation which occurs when the user
initiates a "close" on this dialog.

**Returns:** an integer indicating the window-close operation
**See Also:** setDefaultCloseOperation(int)

---

#### getDefaultCloseOperation

public int getDefaultCloseOperation()

Returns the operation which occurs when the user
initiates a "close" on this dialog.

setTransferHandler

```java
@BeanProperty
(
hidden
=true,

description
="Mechanism for transfer of data into the component")
public void setTransferHandler​(
TransferHandler
newHandler)
```

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JDialog

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Parameters:** newHandler

- the new

TransferHandler
**Since:** 1.6
**See Also:** TransferHandler

,

getTransferHandler()

,

Component.setDropTarget(java.awt.dnd.DropTarget)

---

#### setTransferHandler

@BeanProperty

(

hidden

=true,

description

="Mechanism for transfer of data into the component")
public void setTransferHandler​(

TransferHandler

newHandler)

Sets the

transferHandler

property, which is a mechanism to
support transfer of data into this component. Use

null

if the component does not support data transfer operations.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JDialog

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

If the system property

suppressSwingDropSupport

is

false

(the default) and the current drop target on this component is either

null

or not a user-set drop target, this method will change the
drop target as follows: If

newHandler

is

null

it will
clear the drop target. If not

null

it will install a new

DropTarget

.

Note: When used with

JDialog

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

Note: When used with

JDialog

,

TransferHandler

only
provides data import capability, as the data export related methods
are currently typed to

JComponent

.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

Please see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

getTransferHandler

```java
public
TransferHandler
getTransferHandler()
```

Gets the

transferHandler

property.

**Returns:** the value of the

transferHandler

property
**Since:** 1.6
**See Also:** TransferHandler

,

setTransferHandler(javax.swing.TransferHandler)

---

#### getTransferHandler

public

TransferHandler

getTransferHandler()

Gets the

transferHandler

property.

update

```java
public void update​(
Graphics
g)
```

Calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

**Overrides:** update

in class

Container
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** Component.update(Graphics)

---

#### update

public void update​(

Graphics

g)

Calls

paint(g)

. This method was overridden to
prevent an unnecessary call to clear the background.

setJMenuBar

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The menubar for accessing pulldown menus from this dialog.")
public void setJMenuBar​(
JMenuBar
menu)
```

Sets the menubar for this dialog.

**Parameters:** menu

- the menubar being placed in the dialog
**See Also:** getJMenuBar()

---

#### setJMenuBar

@BeanProperty

(

bound

=false,

hidden

=true,

description

="The menubar for accessing pulldown menus from this dialog.")
public void setJMenuBar​(

JMenuBar

menu)

Sets the menubar for this dialog.

getJMenuBar

```java
public
JMenuBar
getJMenuBar()
```

Returns the menubar set on this dialog.

**Returns:** the menubar set on this dialog
**See Also:** setJMenuBar(javax.swing.JMenuBar)

---

#### getJMenuBar

public

JMenuBar

getJMenuBar()

Returns the menubar set on this dialog.

isRootPaneCheckingEnabled

```java
protected boolean isRootPaneCheckingEnabled()
```

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Returns:** true if

add

and

setLayout

are forwarded; false otherwise
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### isRootPaneCheckingEnabled

protected boolean isRootPaneCheckingEnabled()

Returns whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

setRootPaneCheckingEnabled

```java
@BeanProperty
(
hidden
=true,

description
="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)
```

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

**Parameters:** enabled

- true if

add

and

setLayout

are forwarded, false if they should operate directly on the

JDialog

.
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

setLayout(java.awt.LayoutManager)

,

isRootPaneCheckingEnabled()

,

RootPaneContainer

---

#### setRootPaneCheckingEnabled

@BeanProperty

(

hidden

=true,

description

="Whether the add and setLayout methods are forwarded")
protected void setRootPaneCheckingEnabled​(boolean enabled)

Sets whether calls to

add

and

setLayout

are forwarded to the

contentPane

.

addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be respected
**Parameters:** index

- the index
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### addImpl

protected void addImpl​(

Component

comp,

Object

constraints,
int index)

Adds the specified child

Component

.
This method is overridden to conditionally forward calls to the

contentPane

.
By default, children are added to the

contentPane

instead
of the frame, refer to

RootPaneContainer

for
details.

remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from the container. If

comp

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JDialog

or

contentPane

.

**Overrides:** remove

in class

Container
**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is null
**See Also:** Container.add(java.awt.Component)

,

RootPaneContainer

---

#### remove

public void remove​(

Component

comp)

Removes the specified component from the container. If

comp

is not the

rootPane

, this will forward
the call to the

contentPane

. This will do nothing if

comp

is not a child of the

JDialog

or

contentPane

.

setLayout

```java
public void setLayout​(
LayoutManager
manager)
```

Sets the

LayoutManager

.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

**Overrides:** setLayout

in class

Container
**Parameters:** manager

- the

LayoutManager
**See Also:** setRootPaneCheckingEnabled(boolean)

,

RootPaneContainer

---

#### setLayout

public void setLayout​(

LayoutManager

manager)

Sets the

LayoutManager

.
Overridden to conditionally forward the call to the

contentPane

.
Refer to

RootPaneContainer

for
more information.

getRootPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="the RootPane object for this dialog.")
public
JRootPane
getRootPane()
```

Returns the

rootPane

object for this dialog.

**Specified by:** getRootPane

in interface

RootPaneContainer
**Returns:** this components single JRootPane child.
**See Also:** setRootPane(javax.swing.JRootPane)

,

RootPaneContainer.getRootPane()

---

#### getRootPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="the RootPane object for this dialog.")
public

JRootPane

getRootPane()

Returns the

rootPane

object for this dialog.

setRootPane

```java
protected void setRootPane​(
JRootPane
root)
```

Sets the

rootPane

property.
This method is called by the constructor.

**Parameters:** root

- the

rootPane

object for this dialog
**See Also:** getRootPane()

---

#### setRootPane

protected void setRootPane​(

JRootPane

root)

Sets the

rootPane

property.
This method is called by the constructor.

getContentPane

```java
public
Container
getContentPane()
```

Returns the

contentPane

object for this dialog.

**Specified by:** getContentPane

in interface

RootPaneContainer
**Returns:** the

contentPane

property
**See Also:** setContentPane(java.awt.Container)

,

RootPaneContainer.getContentPane()

---

#### getContentPane

public

Container

getContentPane()

Returns the

contentPane

object for this dialog.

setContentPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The client area of the dialog where child components are normally inserted.")
public void setContentPane​(
Container
contentPane)
```

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

**Specified by:** setContentPane

in interface

RootPaneContainer
**Parameters:** contentPane

- the

contentPane

object for this dialog
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is

null
**See Also:** JRootPane

,

getContentPane()

,

RootPaneContainer.setContentPane(java.awt.Container)

---

#### setContentPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="The client area of the dialog where child components are normally inserted.")
public void setContentPane​(

Container

contentPane)

Sets the

contentPane

property.
This method is called by the constructor.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

Swing's painting architecture requires an opaque

JComponent

in the containment hierarchy. This is typically provided by the
content pane. If you replace the content pane it is recommended you
replace it with an opaque

JComponent

.

getLayeredPane

```java
public
JLayeredPane
getLayeredPane()
```

Returns the

layeredPane

object for this dialog.

**Specified by:** getLayeredPane

in interface

RootPaneContainer
**Returns:** the

layeredPane

property
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

,

RootPaneContainer.getLayeredPane()

---

#### getLayeredPane

public

JLayeredPane

getLayeredPane()

Returns the

layeredPane

object for this dialog.

setLayeredPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="The pane which holds the various dialog layers.")
public void setLayeredPane​(
JLayeredPane
layeredPane)
```

Sets the

layeredPane

property.
This method is called by the constructor.

**Specified by:** setLayeredPane

in interface

RootPaneContainer
**Parameters:** layeredPane

- the new

layeredPane

property
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
**See Also:** getLayeredPane()

,

RootPaneContainer.setLayeredPane(javax.swing.JLayeredPane)

---

#### setLayeredPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="The pane which holds the various dialog layers.")
public void setLayeredPane​(

JLayeredPane

layeredPane)

Sets the

layeredPane

property.
This method is called by the constructor.

getGlassPane

```java
public
Component
getGlassPane()
```

Returns the

glassPane

object for this dialog.

**Specified by:** getGlassPane

in interface

RootPaneContainer
**Returns:** the

glassPane

property
**See Also:** setGlassPane(java.awt.Component)

,

RootPaneContainer.getGlassPane()

---

#### getGlassPane

public

Component

getGlassPane()

Returns the

glassPane

object for this dialog.

setGlassPane

```java
@BeanProperty
(
bound
=false,

hidden
=true,

description
="A transparent pane used for menu rendering.")
public void setGlassPane​(
Component
glassPane)
```

Sets the

glassPane

property.
This method is called by the constructor.

**Specified by:** setGlassPane

in interface

RootPaneContainer
**Parameters:** glassPane

- the

glassPane

object for this dialog
**See Also:** getGlassPane()

,

RootPaneContainer.setGlassPane(java.awt.Component)

---

#### setGlassPane

@BeanProperty

(

bound

=false,

hidden

=true,

description

="A transparent pane used for menu rendering.")
public void setGlassPane​(

Component

glassPane)

Sets the

glassPane

property.
This method is called by the constructor.

getGraphics

```java
@BeanProperty
(
bound
=false)
public
Graphics
getGraphics()
```

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

**Overrides:** getGraphics

in class

Component
**Returns:** a graphics context for this component, or

null

if it has none
**Since:** 1.6
**See Also:** Component.paint(java.awt.Graphics)

---

#### getGraphics

@BeanProperty

(

bound

=false)
public

Graphics

getGraphics()

Creates a graphics context for this component. This method will
return

null

if this component is currently not
displayable.

repaint

```java
public void repaint​(long time,
int x,
int y,
int width,
int height)
```

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

**Overrides:** repaint

in class

Component
**Parameters:** time

- maximum time in milliseconds before update
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** width

- the width
**Parameters:** height

- the height
**Since:** 1.6
**See Also:** RepaintManager

---

#### repaint

public void repaint​(long time,
int x,
int y,
int width,
int height)

Repaints the specified rectangle of this component within

time

milliseconds. Refer to

RepaintManager

for details on how the repaint is handled.

setDefaultLookAndFeelDecorated

```java
public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)
```

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JDialog

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JDialog

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JDialog by doing the following:

```java
JDialog dialog = new JDialog();
dialog.setUndecorated(true);
dialog.getRootPane().setWindowDecorationStyle(JRootPane.PLAIN_DIALOG);
```

**Parameters:** defaultLookAndFeelDecorated

- A hint as to whether or not current
look and feel should provide window decorations
**Since:** 1.4
**See Also:** LookAndFeel.getSupportsWindowDecorations()

---

#### setDefaultLookAndFeelDecorated

public static void setDefaultLookAndFeelDecorated​(boolean defaultLookAndFeelDecorated)

Provides a hint as to whether or not newly created

JDialog

s
should have their Window decorations (such as borders, widgets to
close the window, title...) provided by the current look
and feel. If

defaultLookAndFeelDecorated

is true,
the current

LookAndFeel

supports providing window
decorations, and the current window manager supports undecorated
windows, then newly created

JDialog

s will have their
Window decorations provided by the current

LookAndFeel

.
Otherwise, newly created

JDialog

s will have their
Window decorations provided by the current window manager.

You can get the same effect on a single JDialog by doing the following:

```java
JDialog dialog = new JDialog();
dialog.setUndecorated(true);
dialog.getRootPane().setWindowDecorationStyle(JRootPane.PLAIN_DIALOG);
```

You can get the same effect on a single JDialog by doing the following:

```java
JDialog dialog = new JDialog();
dialog.setUndecorated(true);
dialog.getRootPane().setWindowDecorationStyle(JRootPane.PLAIN_DIALOG);
```

JDialog dialog = new JDialog();
dialog.setUndecorated(true);
dialog.getRootPane().setWindowDecorationStyle(JRootPane.PLAIN_DIALOG);

isDefaultLookAndFeelDecorated

```java
public static boolean isDefaultLookAndFeelDecorated()
```

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

**Returns:** true if look and feel should provide Window decorations.
**Since:** 1.4

---

#### isDefaultLookAndFeelDecorated

public static boolean isDefaultLookAndFeelDecorated()

Returns true if newly created

JDialog

s should have their
Window decorations provided by the current look and feel. This is only
a hint, as certain look and feels may not support this feature.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JDialog

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

Dialog
**Returns:** a string representation of this

JDialog

.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JDialog

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JDialog.
For JDialogs, the AccessibleContext takes the form of an
AccessibleJDialog.
A new AccessibleJDialog instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Dialog
**Returns:** an AccessibleJDialog that serves as the
AccessibleContext of this JDialog

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JDialog.
For JDialogs, the AccessibleContext takes the form of an
AccessibleJDialog.
A new AccessibleJDialog instance is created if necessary.

---

