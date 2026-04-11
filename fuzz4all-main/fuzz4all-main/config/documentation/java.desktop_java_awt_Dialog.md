# Class Dialog

**Source:** `java.desktop\java\awt\Dialog.html`

### Class Description

```java
public class
Dialog

extends
Window
```

A Dialog is a top-level window with a title and a border
that is typically used to take some form of input from the user.

The size of the dialog includes any area designated for the
border. The dimensions of the border area can be obtained
using the

getInsets

method, however, since
these dimensions are platform-dependent, a valid insets
value cannot be obtained until the dialog is made displayable
by either calling

pack

or

show

.
Since the border area is included in the overall size of the
dialog, the border effectively obscures a portion of the dialog,
constraining the area available for rendering and/or displaying
subcomponents to the rectangle which has an upper-left corner
location of

(insets.left, insets.top)

, and has a size of

width - (insets.left + insets.right)

by

height - (insets.top + insets.bottom)

.

The default layout for a dialog is

BorderLayout

.

A dialog may have its native decorations (i.e. Frame & Titlebar) turned off
with

setUndecorated

. This can only be done while the dialog
is not

displayable

.

A dialog may have another window as its owner when it's constructed. When
the owner window of a visible dialog is minimized, the dialog will
automatically be hidden from the user. When the owner window is subsequently
restored, the dialog is made visible to the user again.

In a multi-screen environment, you can create a

Dialog

on a different screen device than its owner. See

Frame

for
more information.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

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
Dialog.ModalityType
DEFAULT_MODALITY_TYPE

Default modality type for modal dialogs. The default modality type is

APPLICATION_MODAL

. Calling the oldstyle

setModal(true)

is equal to

setModalityType(DEFAULT_MODALITY_TYPE)

.

**See Also:**
- Dialog.ModalityType

,

setModal(boolean)

**Since:**
- 1.6

---

### Constructor Details

#### public Dialog​(
Frame
owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

**Parameters:**
- owner

- the owner of the dialog or

null

if
this dialog has no owner

**Throws:**
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

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### public Dialog​(
Frame
owner,
boolean modal)

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

**Parameters:**
- owner

- the owner of the dialog or

null

if
this dialog has no owner
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

**Throws:**
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
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

---

#### public Dialog​(
Frame
owner,

String
title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

**Parameters:**
- owner

- the owner of the dialog or

null

if
this dialog has no owner
- title

- the title of the dialog or

null

if this dialog
has no title

**Throws:**
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

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### public Dialog​(
Frame
owner,

String
title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

**Parameters:**
- owner

- the owner of the dialog or

null

if
this dialog has no owner
- title

- the title of the dialog or

null

if this dialog
has no title
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

**Throws:**
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
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### public Dialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

**Parameters:**
- owner

- the owner of the dialog or

null

if this dialog
has no owner
- title

- the title of the dialog or

null

if this dialog
has no title
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

**Since:**
- 1.4

---

#### public Dialog​(
Dialog
owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

**Parameters:**
- owner

- the owner of the dialog or

null

if this
dialog has no owner

**Throws:**
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

**Since:**
- 1.2

---

#### public Dialog​(
Dialog
owner,

String
title)

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

**Parameters:**
- owner

- the owner of the dialog or

null

if this
has no owner
- title

- the title of the dialog or

null

if this dialog
has no title

**Throws:**
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

**Since:**
- 1.2

---

#### public Dialog​(
Dialog
owner,

String
title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

**Parameters:**
- owner

- the owner of the dialog or

null

if this
dialog has no owner
- title

- the title of the dialog or

null

if this
dialog has no title
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE

**Throws:**
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
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

**Since:**
- 1.2

---

#### public Dialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

**Parameters:**
- owner

- the owner of the dialog or

null

if this
dialog has no owner
- title

- the title of the dialog or

null

if this
dialog has no title
- modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

**Since:**
- 1.4

---

#### public Dialog​(
Window
owner)

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

**Parameters:**
- owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null

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

**Since:**
- 1.6

---

#### public Dialog​(
Window
owner,

String
title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

**Parameters:**
- owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
- title

- the title of the dialog or

null

if this dialog
has no title

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

**Since:**
- 1.6

---

#### public Dialog​(
Window
owner,

Dialog.ModalityType
modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

**Parameters:**
- owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType

**See Also:**
- Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

**Since:**
- 1.6

---

#### public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

**Parameters:**
- owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
- title

- the title of the dialog or

null

if this dialog
has no title
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType

**See Also:**
- Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

**Since:**
- 1.6

---

#### public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

**Parameters:**
- owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
- title

- the title of the dialog or

null

if this dialog
has no title
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

- if

gc

is not from a screen device
- HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
- SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType

**See Also:**
- Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

**Since:**
- 1.6

---

### Method Details

#### public void addNotify()

Makes this Dialog displayable by connecting it to
a native screen resource. Making a dialog displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:**
- addNotify

in class

Window

**See Also:**
- Component.isDisplayable()

,

Container.removeNotify()

---

#### public boolean isModal()

Indicates whether the dialog is modal.

This method is obsolete and is kept for backwards compatibility only.
Use

getModalityType()

instead.

**Returns:**
- true

if this dialog window is modal;

false

otherwise

**See Also:**
- DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

setModal(boolean)

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

---

#### public void setModal​(boolean modal)

Specifies whether this dialog should be modal.

This method is obsolete and is kept for backwards compatibility only.
Use

setModalityType()

instead.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:**
- modal

- specifies whether dialog blocks input to other windows
when shown; calling to

setModal(true)

is equivalent to

setModalityType(Dialog.DEFAULT_MODALITY_TYPE)

, and
calling to

setModal(false)

is equivalent to

setModalityType(Dialog.ModalityType.MODELESS)

**See Also:**
- DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

isModal()

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

**Since:**
- 1.1

---

#### public
Dialog.ModalityType
getModalityType()

Returns the modality type of this dialog.

**Returns:**
- modality type of this dialog

**See Also:**
- setModalityType(java.awt.Dialog.ModalityType)

**Since:**
- 1.6

---

#### public void setModalityType​(
Dialog.ModalityType
type)

Sets the modality type for this dialog. See

ModalityType

for possible modality types.

If the given modality type is not supported,

MODELESS

is used. You may want to call

getModalityType()

after calling
this method to ensure that the modality type has been set.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:**
- type

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS

**Throws:**
- SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType

**See Also:**
- getModalityType()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

**Since:**
- 1.6

---

#### public
String
getTitle()

Gets the title of the dialog. The title is displayed in the
dialog's border.

**Returns:**
- the title of this dialog window. The title may be

null

.

**See Also:**
- setTitle(java.lang.String)

---

#### public void setTitle​(
String
title)

Sets the title of the Dialog.

**Parameters:**
- title

- the title displayed in the dialog's border;
a null value results in an empty title

**See Also:**
- getTitle()

---

#### public void setVisible​(boolean b)

Shows or hides this

Dialog

depending on the value of parameter

b

.

**Overrides:**
- setVisible

in class

Window

**Parameters:**
- b

- if

true

, makes the

Dialog

visible,
otherwise hides the

Dialog

.
If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If

false

, hides the

Dialog

and then causes

setVisible(true)

to return if it is currently blocked.

Notes for modal dialogs

.

- setVisible(true)

: If the dialog is not already
visible, this call will not return until the dialog is
hidden by calling

setVisible(false)

or

dispose

.

setVisible(false)

: Hides the dialog and then
returns on

setVisible(true)

if it is currently blocked.

It is OK to call this method from the event dispatching
thread because the toolkit ensures that other events are
not blocked while this method is blocked.

**See Also:**
- Window.setVisible(boolean)

,

Window.dispose()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

---

#### @Deprecated

public void show()

Makes the

Dialog

visible. If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If the dialog is already visible, this will bring the dialog
to the front.

If the dialog is modal and is not already visible, this call
will not return until the dialog is hidden by calling hide or
dispose. It is permissible to show modal dialogs from the event
dispatching thread because the toolkit will ensure that another
event pump runs while the one which invoked this method is blocked.

**Overrides:**
- show

in class

Window

**See Also:**
- Component.hide()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

,

Window.setVisible(boolean)

---

#### @Deprecated

public void hide()

Hides the Dialog and then causes

show

to return if it is currently
blocked.

**Overrides:**
- hide

in class

Window

**See Also:**
- Window.show()

,

Window.dispose()

,

Window.setVisible(boolean)

---

#### public void toBack()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

**Overrides:**
- toBack

in class

Window

**See Also:**
- Window.toBack()

---

#### public boolean isResizable()

Indicates whether this dialog is resizable by the user.
By default, all dialogs are initially resizable.

**Returns:**
- true

if the user can resize the dialog;

false

otherwise.

**See Also:**
- setResizable(boolean)

---

#### public void setResizable​(boolean resizable)

Sets whether this dialog is resizable by the user.

**Parameters:**
- resizable

-

true

if the user can
resize this dialog;

false

otherwise.

**See Also:**
- isResizable()

---

#### public void setUndecorated​(boolean undecorated)

Disables or enables decorations for this dialog.

This method can only be called while the dialog is not displayable. To
make this dialog decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:**
- undecorated

-

true

if no dialog decorations are to be
enabled;

false

if dialog decorations are to be enabled

**Throws:**
- IllegalComponentStateException

- if the dialog is displayable
- IllegalComponentStateException

- if

undecorated

is

false

, and this dialog does not have the default shape
- IllegalComponentStateException

- if

undecorated

is

false

, and this dialog opacity is less than

1.0f
- IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this dialog background
color is less than

1.0f

**See Also:**
- isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

**Since:**
- 1.4

---

#### public boolean isUndecorated()

Indicates whether this dialog is undecorated.
By default, all dialogs are initially decorated.

**Returns:**
- true

if dialog is undecorated;

false

otherwise.

**See Also:**
- setUndecorated(boolean)

**Since:**
- 1.4

---

#### protected
String
paramString()

Returns a string representing the state of this dialog. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

Container

**Returns:**
- the parameter string of this dialog window.

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this Dialog.
For dialogs, the AccessibleContext takes the form of an
AccessibleAWTDialog.
A new AccessibleAWTDialog instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Window

**Returns:**
- an AccessibleAWTDialog that serves as the
AccessibleContext of this Dialog

**Since:**
- 1.3

---

### Additional Sections

#### Class Dialog

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Window
- - java.awt.Dialog

java.awt.Component

- java.awt.Container
- - java.awt.Window
- - java.awt.Dialog

java.awt.Container

- java.awt.Window
- - java.awt.Dialog

java.awt.Window

- java.awt.Dialog

java.awt.Dialog

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

**Direct Known Subclasses:** FileDialog

,

JDialog

```java
public class
Dialog

extends
Window
```

A Dialog is a top-level window with a title and a border
that is typically used to take some form of input from the user.

The size of the dialog includes any area designated for the
border. The dimensions of the border area can be obtained
using the

getInsets

method, however, since
these dimensions are platform-dependent, a valid insets
value cannot be obtained until the dialog is made displayable
by either calling

pack

or

show

.
Since the border area is included in the overall size of the
dialog, the border effectively obscures a portion of the dialog,
constraining the area available for rendering and/or displaying
subcomponents to the rectangle which has an upper-left corner
location of

(insets.left, insets.top)

, and has a size of

width - (insets.left + insets.right)

by

height - (insets.top + insets.bottom)

.

The default layout for a dialog is

BorderLayout

.

A dialog may have its native decorations (i.e. Frame & Titlebar) turned off
with

setUndecorated

. This can only be done while the dialog
is not

displayable

.

A dialog may have another window as its owner when it's constructed. When
the owner window of a visible dialog is minimized, the dialog will
automatically be hidden from the user. When the owner window is subsequently
restored, the dialog is made visible to the user again.

In a multi-screen environment, you can create a

Dialog

on a different screen device than its owner. See

Frame

for
more information.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

**Since:** 1.0
**See Also:** WindowEvent

,

Window.addWindowListener(java.awt.event.WindowListener)

,

Serialized Form

public class

Dialog

extends

Window

A Dialog is a top-level window with a title and a border
that is typically used to take some form of input from the user.

The size of the dialog includes any area designated for the
border. The dimensions of the border area can be obtained
using the

getInsets

method, however, since
these dimensions are platform-dependent, a valid insets
value cannot be obtained until the dialog is made displayable
by either calling

pack

or

show

.
Since the border area is included in the overall size of the
dialog, the border effectively obscures a portion of the dialog,
constraining the area available for rendering and/or displaying
subcomponents to the rectangle which has an upper-left corner
location of

(insets.left, insets.top)

, and has a size of

width - (insets.left + insets.right)

by

height - (insets.top + insets.bottom)

.

The default layout for a dialog is

BorderLayout

.

A dialog may have its native decorations (i.e. Frame & Titlebar) turned off
with

setUndecorated

. This can only be done while the dialog
is not

displayable

.

A dialog may have another window as its owner when it's constructed. When
the owner window of a visible dialog is minimized, the dialog will
automatically be hidden from the user. When the owner window is subsequently
restored, the dialog is made visible to the user again.

In a multi-screen environment, you can create a

Dialog

on a different screen device than its owner. See

Frame

for
more information.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

The default layout for a dialog is

BorderLayout

.

A dialog may have its native decorations (i.e. Frame & Titlebar) turned off
with

setUndecorated

. This can only be done while the dialog
is not

displayable

.

A dialog may have another window as its owner when it's constructed. When
the owner window of a visible dialog is minimized, the dialog will
automatically be hidden from the user. When the owner window is subsequently
restored, the dialog is made visible to the user again.

In a multi-screen environment, you can create a

Dialog

on a different screen device than its owner. See

Frame

for
more information.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

A dialog may have its native decorations (i.e. Frame & Titlebar) turned off
with

setUndecorated

. This can only be done while the dialog
is not

displayable

.

A dialog may have another window as its owner when it's constructed. When
the owner window of a visible dialog is minimized, the dialog will
automatically be hidden from the user. When the owner window is subsequently
restored, the dialog is made visible to the user again.

In a multi-screen environment, you can create a

Dialog

on a different screen device than its owner. See

Frame

for
more information.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

A dialog may have another window as its owner when it's constructed. When
the owner window of a visible dialog is minimized, the dialog will
automatically be hidden from the user. When the owner window is subsequently
restored, the dialog is made visible to the user again.

In a multi-screen environment, you can create a

Dialog

on a different screen device than its owner. See

Frame

for
more information.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

In a multi-screen environment, you can create a

Dialog

on a different screen device than its owner. See

Frame

for
more information.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

A dialog can be either modeless (the default) or modal. A modal
dialog is one which blocks input to some other top-level windows
in the application, except for any windows created with the dialog
as their owner. See

AWT Modality

specification for details.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

Dialogs are capable of generating the following

WindowEvents

:

WindowOpened

,

WindowClosing

,

WindowClosed

,

WindowActivated

,

WindowDeactivated

,

WindowGainedFocus

,

WindowLostFocus

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Dialog.AccessibleAWTDialog

This class implements accessibility support for the

Dialog

class.

static class

Dialog.ModalExclusionType

Any top-level window can be marked not to be blocked by modal
dialogs.

static class

Dialog.ModalityType

Modal dialogs block all input to some top-level windows.

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

static

Dialog.ModalityType

DEFAULT_MODALITY_TYPE

Default modality type for modal dialogs.

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

Dialog

​(

Dialog

owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

Dialog

​(

Dialog

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

Dialog

​(

Dialog

owner,

String

title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

Dialog

​(

Dialog

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

Dialog

​(

Frame

owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

Dialog

​(

Frame

owner,
boolean modal)

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

Dialog

​(

Frame

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

Dialog

​(

Frame

owner,

String

title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

Dialog

​(

Frame

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

Dialog

​(

Window

owner)

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

Dialog

​(

Window

owner,

Dialog.ModalityType

modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

Dialog

​(

Window

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

Dialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

Dialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

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

addNotify

()

Makes this Dialog displayable by connecting it to
a native screen resource.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Dialog.

Dialog.ModalityType

getModalityType

()

Returns the modality type of this dialog.

String

getTitle

()

Gets the title of the dialog.

void

hide

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

boolean

isModal

()

Indicates whether the dialog is modal.

boolean

isResizable

()

Indicates whether this dialog is resizable by the user.

boolean

isUndecorated

()

Indicates whether this dialog is undecorated.

protected

String

paramString

()

Returns a string representing the state of this dialog.

void

setModal

​(boolean modal)

Specifies whether this dialog should be modal.

void

setModalityType

​(

Dialog.ModalityType

type)

Sets the modality type for this dialog.

void

setResizable

​(boolean resizable)

Sets whether this dialog is resizable by the user.

void

setTitle

​(

String

title)

Sets the title of the Dialog.

void

setUndecorated

​(boolean undecorated)

Disables or enables decorations for this dialog.

void

setVisible

​(boolean b)

Shows or hides this

Dialog

depending on the value of parameter

b

.

void

show

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

void

toBack

()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

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

processWindowEvent

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

addImpl

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

setLayout

,

transferFocusDownCycle

,

update

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

getGraphics

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

Dialog.AccessibleAWTDialog

This class implements accessibility support for the

Dialog

class.

static class

Dialog.ModalExclusionType

Any top-level window can be marked not to be blocked by modal
dialogs.

static class

Dialog.ModalityType

Modal dialogs block all input to some top-level windows.

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

Dialog

class.

Any top-level window can be marked not to be blocked by modal
dialogs.

Modal dialogs block all input to some top-level windows.

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

static

Dialog.ModalityType

DEFAULT_MODALITY_TYPE

Default modality type for modal dialogs.

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

Default modality type for modal dialogs.

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

Dialog

​(

Dialog

owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

Dialog

​(

Dialog

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

Dialog

​(

Dialog

owner,

String

title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

Dialog

​(

Dialog

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

Dialog

​(

Frame

owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

Dialog

​(

Frame

owner,
boolean modal)

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

Dialog

​(

Frame

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

Dialog

​(

Frame

owner,

String

title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

Dialog

​(

Frame

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

Dialog

​(

Window

owner)

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

Dialog

​(

Window

owner,

Dialog.ModalityType

modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

Dialog

​(

Window

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

Dialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

Dialog

​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

---

#### Constructor Summary

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addNotify

()

Makes this Dialog displayable by connecting it to
a native screen resource.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Dialog.

Dialog.ModalityType

getModalityType

()

Returns the modality type of this dialog.

String

getTitle

()

Gets the title of the dialog.

void

hide

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

boolean

isModal

()

Indicates whether the dialog is modal.

boolean

isResizable

()

Indicates whether this dialog is resizable by the user.

boolean

isUndecorated

()

Indicates whether this dialog is undecorated.

protected

String

paramString

()

Returns a string representing the state of this dialog.

void

setModal

​(boolean modal)

Specifies whether this dialog should be modal.

void

setModalityType

​(

Dialog.ModalityType

type)

Sets the modality type for this dialog.

void

setResizable

​(boolean resizable)

Sets whether this dialog is resizable by the user.

void

setTitle

​(

String

title)

Sets the title of the Dialog.

void

setUndecorated

​(boolean undecorated)

Disables or enables decorations for this dialog.

void

setVisible

​(boolean b)

Shows or hides this

Dialog

depending on the value of parameter

b

.

void

show

()

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

void

toBack

()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

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

processWindowEvent

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

addImpl

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

setLayout

,

transferFocusDownCycle

,

update

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

getGraphics

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

Makes this Dialog displayable by connecting it to
a native screen resource.

Gets the AccessibleContext associated with this Dialog.

Returns the modality type of this dialog.

Gets the title of the dialog.

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Indicates whether the dialog is modal.

Indicates whether this dialog is resizable by the user.

Indicates whether this dialog is undecorated.

Returns a string representing the state of this dialog.

Specifies whether this dialog should be modal.

Sets the modality type for this dialog.

Sets whether this dialog is resizable by the user.

Sets the title of the Dialog.

Disables or enables decorations for this dialog.

Shows or hides this

Dialog

depending on the value of parameter

b

.

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

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

processWindowEvent

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

addImpl

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

setLayout

,

transferFocusDownCycle

,

update

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

getGraphics

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

- DEFAULT_MODALITY_TYPE

```java
public static final
Dialog.ModalityType
DEFAULT_MODALITY_TYPE
```

Default modality type for modal dialogs. The default modality type is

APPLICATION_MODAL

. Calling the oldstyle

setModal(true)

is equal to

setModalityType(DEFAULT_MODALITY_TYPE)

.

**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Dialog

```java
public Dialog​(
Frame
owner)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
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
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Frame
owner,
boolean modal)
```

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Frame
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Frame
owner,

String
title,
boolean modal)
```

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog or

null

if this dialog
has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Dialog
owner)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
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
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Dialog
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

**Parameters:** owner

- the owner of the dialog or

null

if this
has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Dialog
owner,

String
title,
boolean modal)
```

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this
dialog has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**Since:** 1.2
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this
dialog has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Window
owner)
```

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
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

- Dialog

```java
public Dialog​(
Window
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- Dialog

```java
public Dialog​(
Window
owner,

Dialog.ModalityType
modalityType)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

- Dialog

```java
public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

- Dialog

```java
public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

============ METHOD DETAIL ==========

- Method Detail

- addNotify

```java
public void addNotify()
```

Makes this Dialog displayable by connecting it to
a native screen resource. Making a dialog displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Window
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- isModal

```java
public boolean isModal()
```

Indicates whether the dialog is modal.

This method is obsolete and is kept for backwards compatibility only.
Use

getModalityType()

instead.

**Returns:** true

if this dialog window is modal;

false

otherwise
**See Also:** DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

setModal(boolean)

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

- setModal

```java
public void setModal​(boolean modal)
```

Specifies whether this dialog should be modal.

This method is obsolete and is kept for backwards compatibility only.
Use

setModalityType()

instead.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:** modal

- specifies whether dialog blocks input to other windows
when shown; calling to

setModal(true)

is equivalent to

setModalityType(Dialog.DEFAULT_MODALITY_TYPE)

, and
calling to

setModal(false)

is equivalent to

setModalityType(Dialog.ModalityType.MODELESS)
**Since:** 1.1
**See Also:** DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

isModal()

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

- getModalityType

```java
public
Dialog.ModalityType
getModalityType()
```

Returns the modality type of this dialog.

**Returns:** modality type of this dialog
**Since:** 1.6
**See Also:** setModalityType(java.awt.Dialog.ModalityType)

- setModalityType

```java
public void setModalityType​(
Dialog.ModalityType
type)
```

Sets the modality type for this dialog. See

ModalityType

for possible modality types.

If the given modality type is not supported,

MODELESS

is used. You may want to call

getModalityType()

after calling
this method to ensure that the modality type has been set.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:** type

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** getModalityType()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

- getTitle

```java
public
String
getTitle()
```

Gets the title of the dialog. The title is displayed in the
dialog's border.

**Returns:** the title of this dialog window. The title may be

null

.
**See Also:** setTitle(java.lang.String)

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the Dialog.

**Parameters:** title

- the title displayed in the dialog's border;
a null value results in an empty title
**See Also:** getTitle()

- setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this

Dialog

depending on the value of parameter

b

.

**Overrides:** setVisible

in class

Window
**Parameters:** b

- if

true

, makes the

Dialog

visible,
otherwise hides the

Dialog

.
If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If

false

, hides the

Dialog

and then causes

setVisible(true)

to return if it is currently blocked.

Notes for modal dialogs

.

- setVisible(true)

: If the dialog is not already
visible, this call will not return until the dialog is
hidden by calling

setVisible(false)

or

dispose

.

setVisible(false)

: Hides the dialog and then
returns on

setVisible(true)

if it is currently blocked.

It is OK to call this method from the event dispatching
thread because the toolkit ensures that other events are
not blocked while this method is blocked.
**See Also:** Window.setVisible(boolean)

,

Window.dispose()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

- show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Makes the

Dialog

visible. If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If the dialog is already visible, this will bring the dialog
to the front.

If the dialog is modal and is not already visible, this call
will not return until the dialog is hidden by calling hide or
dispose. It is permissible to show modal dialogs from the event
dispatching thread because the toolkit will ensure that another
event pump runs while the one which invoked this method is blocked.

**Overrides:** show

in class

Window
**See Also:** Component.hide()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

,

Window.setVisible(boolean)

- hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Hides the Dialog and then causes

show

to return if it is currently
blocked.

**Overrides:** hide

in class

Window
**See Also:** Window.show()

,

Window.dispose()

,

Window.setVisible(boolean)

- toBack

```java
public void toBack()
```

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

**Overrides:** toBack

in class

Window
**See Also:** Window.toBack()

- isResizable

```java
public boolean isResizable()
```

Indicates whether this dialog is resizable by the user.
By default, all dialogs are initially resizable.

**Returns:** true

if the user can resize the dialog;

false

otherwise.
**See Also:** setResizable(boolean)

- setResizable

```java
public void setResizable​(boolean resizable)
```

Sets whether this dialog is resizable by the user.

**Parameters:** resizable

-

true

if the user can
resize this dialog;

false

otherwise.
**See Also:** isResizable()

- setUndecorated

```java
public void setUndecorated​(boolean undecorated)
```

Disables or enables decorations for this dialog.

This method can only be called while the dialog is not displayable. To
make this dialog decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:** undecorated

-

true

if no dialog decorations are to be
enabled;

false

if dialog decorations are to be enabled
**Throws:** IllegalComponentStateException

- if the dialog is displayable
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this dialog does not have the default shape
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this dialog opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this dialog background
color is less than

1.0f
**Since:** 1.4
**See Also:** isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

- isUndecorated

```java
public boolean isUndecorated()
```

Indicates whether this dialog is undecorated.
By default, all dialogs are initially decorated.

**Returns:** true

if dialog is undecorated;

false

otherwise.
**Since:** 1.4
**See Also:** setUndecorated(boolean)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this dialog. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this dialog window.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Dialog.
For dialogs, the AccessibleContext takes the form of an
AccessibleAWTDialog.
A new AccessibleAWTDialog instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Window
**Returns:** an AccessibleAWTDialog that serves as the
AccessibleContext of this Dialog
**Since:** 1.3

Field Detail

- DEFAULT_MODALITY_TYPE

```java
public static final
Dialog.ModalityType
DEFAULT_MODALITY_TYPE
```

Default modality type for modal dialogs. The default modality type is

APPLICATION_MODAL

. Calling the oldstyle

setModal(true)

is equal to

setModalityType(DEFAULT_MODALITY_TYPE)

.

**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

---

#### Field Detail

DEFAULT_MODALITY_TYPE

```java
public static final
Dialog.ModalityType
DEFAULT_MODALITY_TYPE
```

Default modality type for modal dialogs. The default modality type is

APPLICATION_MODAL

. Calling the oldstyle

setModal(true)

is equal to

setModalityType(DEFAULT_MODALITY_TYPE)

.

**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

---

#### DEFAULT_MODALITY_TYPE

public static final

Dialog.ModalityType

DEFAULT_MODALITY_TYPE

Default modality type for modal dialogs. The default modality type is

APPLICATION_MODAL

. Calling the oldstyle

setModal(true)

is equal to

setModalityType(DEFAULT_MODALITY_TYPE)

.

Constructor Detail

- Dialog

```java
public Dialog​(
Frame
owner)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
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
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Frame
owner,
boolean modal)
```

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Frame
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Frame
owner,

String
title,
boolean modal)
```

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog or

null

if this dialog
has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Dialog
owner)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
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
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Dialog
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

**Parameters:** owner

- the owner of the dialog or

null

if this
has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Dialog
owner,

String
title,
boolean modal)
```

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this
dialog has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**Since:** 1.2
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

- Dialog

```java
public Dialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this
dialog has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

- Dialog

```java
public Dialog​(
Window
owner)
```

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
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

- Dialog

```java
public Dialog​(
Window
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- Dialog

```java
public Dialog​(
Window
owner,

Dialog.ModalityType
modalityType)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

- Dialog

```java
public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

- Dialog

```java
public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

---

#### Constructor Detail

Dialog

```java
public Dialog​(
Frame
owner)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
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
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### Dialog

public Dialog​(

Frame

owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and an empty title.

Dialog

```java
public Dialog​(
Frame
owner,
boolean modal)
```

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

---

#### Dialog

public Dialog​(

Frame

owner,
boolean modal)

Constructs an initially invisible

Dialog

with the specified
owner

Frame

and modality and an empty title.

Dialog

```java
public Dialog​(
Frame
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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
**See Also:** GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### Dialog

public Dialog​(

Frame

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Frame

and title.

Dialog

```java
public Dialog​(
Frame
owner,

String
title,
boolean modal)
```

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

**Parameters:** owner

- the owner of the dialog or

null

if
this dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### Dialog

public Dialog​(

Frame

owner,

String

title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Frame

, title and modality.

Dialog

```java
public Dialog​(
Frame
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog or

null

if this dialog
has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### Dialog

public Dialog​(

Frame

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the specified owner

Frame

, title, modality, and

GraphicsConfiguration

.

Dialog

```java
public Dialog​(
Dialog
owner)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
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
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Dialog

public Dialog​(

Dialog

owner)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Dialog

and an empty title.

Dialog

```java
public Dialog​(
Dialog
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

**Parameters:** owner

- the owner of the dialog or

null

if this
has no owner
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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
**Since:** 1.2
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Dialog

public Dialog​(

Dialog

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with the specified owner

Dialog

and title.

Dialog

```java
public Dialog​(
Dialog
owner,

String
title,
boolean modal)
```

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this
dialog has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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
**Since:** 1.2
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

---

#### Dialog

public Dialog​(

Dialog

owner,

String

title,
boolean modal)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, and modality.

Dialog

```java
public Dialog​(
Dialog
owner,

String
title,
boolean modal,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog or

null

if this
dialog has no owner
**Parameters:** title

- the title of the dialog or

null

if this
dialog has no title
**Parameters:** modal

- specifies whether dialog blocks user input to other top-level
windows when shown. If

false

, the dialog is

MODELESS

;
if

true

, the modality type property is set to

DEFAULT_MODALITY_TYPE
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** Dialog.ModalityType

,

Dialog.ModalityType.MODELESS

,

DEFAULT_MODALITY_TYPE

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Component.setSize(int, int)

,

Component.setVisible(boolean)

---

#### Dialog

public Dialog​(

Dialog

owner,

String

title,
boolean modal,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the
specified owner

Dialog

, title, modality and

GraphicsConfiguration

.

Dialog

```java
public Dialog​(
Window
owner)
```

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
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

---

#### Dialog

public Dialog​(

Window

owner)

Constructs an initially invisible, modeless

Dialog

with the
specified owner

Window

and an empty title.

Dialog

```java
public Dialog​(
Window
owner,

String
title)
```

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

---

#### Dialog

public Dialog​(

Window

owner,

String

title)

Constructs an initially invisible, modeless

Dialog

with
the specified owner

Window

and title.

Dialog

```java
public Dialog​(
Window
owner,

Dialog.ModalityType
modalityType)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

---

#### Dialog

public Dialog​(

Window

owner,

Dialog.ModalityType

modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

and modality and an empty title.

Dialog

```java
public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

---

#### Dialog

public Dialog​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title and modality.

Dialog

```java
public Dialog​(
Window
owner,

String
title,

Dialog.ModalityType
modalityType,

GraphicsConfiguration
gc)
```

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

**Parameters:** owner

- the owner of the dialog. The owner must be an instance of

Dialog

,

Frame

, any
of their descendants or

null
**Parameters:** title

- the title of the dialog or

null

if this dialog
has no title
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

- if

gc

is not from a screen device
**Throws:** HeadlessException

- when

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** Dialog.ModalityType

,

setModal(boolean)

,

setModalityType(java.awt.Dialog.ModalityType)

,

GraphicsEnvironment.isHeadless()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

---

#### Dialog

public Dialog​(

Window

owner,

String

title,

Dialog.ModalityType

modalityType,

GraphicsConfiguration

gc)

Constructs an initially invisible

Dialog

with the
specified owner

Window

, title, modality and

GraphicsConfiguration

.

Method Detail

- addNotify

```java
public void addNotify()
```

Makes this Dialog displayable by connecting it to
a native screen resource. Making a dialog displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Window
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- isModal

```java
public boolean isModal()
```

Indicates whether the dialog is modal.

This method is obsolete and is kept for backwards compatibility only.
Use

getModalityType()

instead.

**Returns:** true

if this dialog window is modal;

false

otherwise
**See Also:** DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

setModal(boolean)

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

- setModal

```java
public void setModal​(boolean modal)
```

Specifies whether this dialog should be modal.

This method is obsolete and is kept for backwards compatibility only.
Use

setModalityType()

instead.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:** modal

- specifies whether dialog blocks input to other windows
when shown; calling to

setModal(true)

is equivalent to

setModalityType(Dialog.DEFAULT_MODALITY_TYPE)

, and
calling to

setModal(false)

is equivalent to

setModalityType(Dialog.ModalityType.MODELESS)
**Since:** 1.1
**See Also:** DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

isModal()

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

- getModalityType

```java
public
Dialog.ModalityType
getModalityType()
```

Returns the modality type of this dialog.

**Returns:** modality type of this dialog
**Since:** 1.6
**See Also:** setModalityType(java.awt.Dialog.ModalityType)

- setModalityType

```java
public void setModalityType​(
Dialog.ModalityType
type)
```

Sets the modality type for this dialog. See

ModalityType

for possible modality types.

If the given modality type is not supported,

MODELESS

is used. You may want to call

getModalityType()

after calling
this method to ensure that the modality type has been set.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:** type

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** getModalityType()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

- getTitle

```java
public
String
getTitle()
```

Gets the title of the dialog. The title is displayed in the
dialog's border.

**Returns:** the title of this dialog window. The title may be

null

.
**See Also:** setTitle(java.lang.String)

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the Dialog.

**Parameters:** title

- the title displayed in the dialog's border;
a null value results in an empty title
**See Also:** getTitle()

- setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this

Dialog

depending on the value of parameter

b

.

**Overrides:** setVisible

in class

Window
**Parameters:** b

- if

true

, makes the

Dialog

visible,
otherwise hides the

Dialog

.
If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If

false

, hides the

Dialog

and then causes

setVisible(true)

to return if it is currently blocked.

Notes for modal dialogs

.

- setVisible(true)

: If the dialog is not already
visible, this call will not return until the dialog is
hidden by calling

setVisible(false)

or

dispose

.

setVisible(false)

: Hides the dialog and then
returns on

setVisible(true)

if it is currently blocked.

It is OK to call this method from the event dispatching
thread because the toolkit ensures that other events are
not blocked while this method is blocked.
**See Also:** Window.setVisible(boolean)

,

Window.dispose()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

- show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Makes the

Dialog

visible. If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If the dialog is already visible, this will bring the dialog
to the front.

If the dialog is modal and is not already visible, this call
will not return until the dialog is hidden by calling hide or
dispose. It is permissible to show modal dialogs from the event
dispatching thread because the toolkit will ensure that another
event pump runs while the one which invoked this method is blocked.

**Overrides:** show

in class

Window
**See Also:** Component.hide()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

,

Window.setVisible(boolean)

- hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Hides the Dialog and then causes

show

to return if it is currently
blocked.

**Overrides:** hide

in class

Window
**See Also:** Window.show()

,

Window.dispose()

,

Window.setVisible(boolean)

- toBack

```java
public void toBack()
```

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

**Overrides:** toBack

in class

Window
**See Also:** Window.toBack()

- isResizable

```java
public boolean isResizable()
```

Indicates whether this dialog is resizable by the user.
By default, all dialogs are initially resizable.

**Returns:** true

if the user can resize the dialog;

false

otherwise.
**See Also:** setResizable(boolean)

- setResizable

```java
public void setResizable​(boolean resizable)
```

Sets whether this dialog is resizable by the user.

**Parameters:** resizable

-

true

if the user can
resize this dialog;

false

otherwise.
**See Also:** isResizable()

- setUndecorated

```java
public void setUndecorated​(boolean undecorated)
```

Disables or enables decorations for this dialog.

This method can only be called while the dialog is not displayable. To
make this dialog decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:** undecorated

-

true

if no dialog decorations are to be
enabled;

false

if dialog decorations are to be enabled
**Throws:** IllegalComponentStateException

- if the dialog is displayable
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this dialog does not have the default shape
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this dialog opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this dialog background
color is less than

1.0f
**Since:** 1.4
**See Also:** isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

- isUndecorated

```java
public boolean isUndecorated()
```

Indicates whether this dialog is undecorated.
By default, all dialogs are initially decorated.

**Returns:** true

if dialog is undecorated;

false

otherwise.
**Since:** 1.4
**See Also:** setUndecorated(boolean)

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this dialog. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this dialog window.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Dialog.
For dialogs, the AccessibleContext takes the form of an
AccessibleAWTDialog.
A new AccessibleAWTDialog instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Window
**Returns:** an AccessibleAWTDialog that serves as the
AccessibleContext of this Dialog
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Makes this Dialog displayable by connecting it to
a native screen resource. Making a dialog displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Window
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

---

#### addNotify

public void addNotify()

Makes this Dialog displayable by connecting it to
a native screen resource. Making a dialog displayable will
cause any of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

isModal

```java
public boolean isModal()
```

Indicates whether the dialog is modal.

This method is obsolete and is kept for backwards compatibility only.
Use

getModalityType()

instead.

**Returns:** true

if this dialog window is modal;

false

otherwise
**See Also:** DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

setModal(boolean)

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

---

#### isModal

public boolean isModal()

Indicates whether the dialog is modal.

This method is obsolete and is kept for backwards compatibility only.
Use

getModalityType()

instead.

This method is obsolete and is kept for backwards compatibility only.
Use

getModalityType()

instead.

setModal

```java
public void setModal​(boolean modal)
```

Specifies whether this dialog should be modal.

This method is obsolete and is kept for backwards compatibility only.
Use

setModalityType()

instead.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:** modal

- specifies whether dialog blocks input to other windows
when shown; calling to

setModal(true)

is equivalent to

setModalityType(Dialog.DEFAULT_MODALITY_TYPE)

, and
calling to

setModal(false)

is equivalent to

setModalityType(Dialog.ModalityType.MODELESS)
**Since:** 1.1
**See Also:** DEFAULT_MODALITY_TYPE

,

Dialog.ModalityType.MODELESS

,

isModal()

,

getModalityType()

,

setModalityType(java.awt.Dialog.ModalityType)

---

#### setModal

public void setModal​(boolean modal)

Specifies whether this dialog should be modal.

This method is obsolete and is kept for backwards compatibility only.
Use

setModalityType()

instead.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

This method is obsolete and is kept for backwards compatibility only.
Use

setModalityType()

instead.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

getModalityType

```java
public
Dialog.ModalityType
getModalityType()
```

Returns the modality type of this dialog.

**Returns:** modality type of this dialog
**Since:** 1.6
**See Also:** setModalityType(java.awt.Dialog.ModalityType)

---

#### getModalityType

public

Dialog.ModalityType

getModalityType()

Returns the modality type of this dialog.

setModalityType

```java
public void setModalityType​(
Dialog.ModalityType
type)
```

Sets the modality type for this dialog. See

ModalityType

for possible modality types.

If the given modality type is not supported,

MODELESS

is used. You may want to call

getModalityType()

after calling
this method to ensure that the modality type has been set.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

**Parameters:** type

- specifies whether dialog blocks input to other
windows when shown.

null

value and unsupported modality
types are equivalent to

MODELESS
**Throws:** SecurityException

- if the calling thread does not have permission
to create modal dialogs with the given

modalityType
**Since:** 1.6
**See Also:** getModalityType()

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

---

#### setModalityType

public void setModalityType​(

Dialog.ModalityType

type)

Sets the modality type for this dialog. See

ModalityType

for possible modality types.

If the given modality type is not supported,

MODELESS

is used. You may want to call

getModalityType()

after calling
this method to ensure that the modality type has been set.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

If the given modality type is not supported,

MODELESS

is used. You may want to call

getModalityType()

after calling
this method to ensure that the modality type has been set.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

Note: changing modality of the visible dialog may have no effect
until it is hidden and then shown again.

getTitle

```java
public
String
getTitle()
```

Gets the title of the dialog. The title is displayed in the
dialog's border.

**Returns:** the title of this dialog window. The title may be

null

.
**See Also:** setTitle(java.lang.String)

---

#### getTitle

public

String

getTitle()

Gets the title of the dialog. The title is displayed in the
dialog's border.

setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the Dialog.

**Parameters:** title

- the title displayed in the dialog's border;
a null value results in an empty title
**See Also:** getTitle()

---

#### setTitle

public void setTitle​(

String

title)

Sets the title of the Dialog.

setVisible

```java
public void setVisible​(boolean b)
```

Shows or hides this

Dialog

depending on the value of parameter

b

.

**Overrides:** setVisible

in class

Window
**Parameters:** b

- if

true

, makes the

Dialog

visible,
otherwise hides the

Dialog

.
If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If

false

, hides the

Dialog

and then causes

setVisible(true)

to return if it is currently blocked.

Notes for modal dialogs

.

- setVisible(true)

: If the dialog is not already
visible, this call will not return until the dialog is
hidden by calling

setVisible(false)

or

dispose

.

setVisible(false)

: Hides the dialog and then
returns on

setVisible(true)

if it is currently blocked.

It is OK to call this method from the event dispatching
thread because the toolkit ensures that other events are
not blocked while this method is blocked.
**See Also:** Window.setVisible(boolean)

,

Window.dispose()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

---

#### setVisible

public void setVisible​(boolean b)

Shows or hides this

Dialog

depending on the value of parameter

b

.

Notes for modal dialogs

.

- setVisible(true)

: If the dialog is not already
visible, this call will not return until the dialog is
hidden by calling

setVisible(false)

or

dispose

.

setVisible(false)

: Hides the dialog and then
returns on

setVisible(true)

if it is currently blocked.

It is OK to call this method from the event dispatching
thread because the toolkit ensures that other events are
not blocked while this method is blocked.

setVisible(true)

: If the dialog is not already
visible, this call will not return until the dialog is
hidden by calling

setVisible(false)

or

dispose

.

setVisible(false)

: Hides the dialog and then
returns on

setVisible(true)

if it is currently blocked.

It is OK to call this method from the event dispatching
thread because the toolkit ensures that other events are
not blocked while this method is blocked.

show

```java
@Deprecated

public void show()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Makes the

Dialog

visible. If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If the dialog is already visible, this will bring the dialog
to the front.

If the dialog is modal and is not already visible, this call
will not return until the dialog is hidden by calling hide or
dispose. It is permissible to show modal dialogs from the event
dispatching thread because the toolkit will ensure that another
event pump runs while the one which invoked this method is blocked.

**Overrides:** show

in class

Window
**See Also:** Component.hide()

,

Component.isDisplayable()

,

Component.validate()

,

isModal()

,

Window.setVisible(boolean)

---

#### show

@Deprecated

public void show()

Makes the

Dialog

visible. If the dialog and/or its owner
are not yet displayable, both are made displayable. The
dialog will be validated prior to being made visible.
If the dialog is already visible, this will bring the dialog
to the front.

If the dialog is modal and is not already visible, this call
will not return until the dialog is hidden by calling hide or
dispose. It is permissible to show modal dialogs from the event
dispatching thread because the toolkit will ensure that another
event pump runs while the one which invoked this method is blocked.

If the dialog is modal and is not already visible, this call
will not return until the dialog is hidden by calling hide or
dispose. It is permissible to show modal dialogs from the event
dispatching thread because the toolkit will ensure that another
event pump runs while the one which invoked this method is blocked.

hide

```java
@Deprecated

public void hide()
```

Deprecated.

As of JDK version 1.5, replaced by

setVisible(boolean)

.

Hides the Dialog and then causes

show

to return if it is currently
blocked.

**Overrides:** hide

in class

Window
**See Also:** Window.show()

,

Window.dispose()

,

Window.setVisible(boolean)

---

#### hide

@Deprecated

public void hide()

Hides the Dialog and then causes

show

to return if it is currently
blocked.

toBack

```java
public void toBack()
```

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

**Overrides:** toBack

in class

Window
**See Also:** Window.toBack()

---

#### toBack

public void toBack()

If this Window is visible, sends this Window to the back and may cause
it to lose focus or activation if it is the focused or active Window.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

Places this Window at the bottom of the stacking order and shows it
behind any other Windows in this VM. No action will take place is this
Window is not visible. Some platforms do not allow Windows which are
owned by other Windows to appear below their owners. Every attempt will
be made to move this Window as low as possible in the stacking order;
however, developers should not assume that this method will move this
Window below all other windows in every situation.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

Because of variations in native windowing systems, no guarantees about
changes to the focused and active Windows can be made. Developers must
never assume that this Window is no longer the focused or active Window
until this Window receives a WINDOW_LOST_FOCUS or WINDOW_DEACTIVATED
event. On platforms where the top-most window is the focused window,
this method will

probably

cause this Window to lose focus. In
that case, the next highest, focusable Window in this VM will receive
focus. On platforms where the stacking order does not typically affect
the focused window, this method will

probably

leave the focused
and active Windows unchanged.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

If this dialog is modal and blocks some windows, then all of them are
also sent to the back to keep them below the blocking dialog.

isResizable

```java
public boolean isResizable()
```

Indicates whether this dialog is resizable by the user.
By default, all dialogs are initially resizable.

**Returns:** true

if the user can resize the dialog;

false

otherwise.
**See Also:** setResizable(boolean)

---

#### isResizable

public boolean isResizable()

Indicates whether this dialog is resizable by the user.
By default, all dialogs are initially resizable.

setResizable

```java
public void setResizable​(boolean resizable)
```

Sets whether this dialog is resizable by the user.

**Parameters:** resizable

-

true

if the user can
resize this dialog;

false

otherwise.
**See Also:** isResizable()

---

#### setResizable

public void setResizable​(boolean resizable)

Sets whether this dialog is resizable by the user.

setUndecorated

```java
public void setUndecorated​(boolean undecorated)
```

Disables or enables decorations for this dialog.

This method can only be called while the dialog is not displayable. To
make this dialog decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

**Parameters:** undecorated

-

true

if no dialog decorations are to be
enabled;

false

if dialog decorations are to be enabled
**Throws:** IllegalComponentStateException

- if the dialog is displayable
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this dialog does not have the default shape
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and this dialog opacity is less than

1.0f
**Throws:** IllegalComponentStateException

- if

undecorated

is

false

, and the alpha value of this dialog background
color is less than

1.0f
**Since:** 1.4
**See Also:** isUndecorated()

,

Component.isDisplayable()

,

Window.getShape()

,

Window.getOpacity()

,

Window.getBackground()

---

#### setUndecorated

public void setUndecorated​(boolean undecorated)

Disables or enables decorations for this dialog.

This method can only be called while the dialog is not displayable. To
make this dialog decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

This method can only be called while the dialog is not displayable. To
make this dialog decorated, it must be opaque and have the default shape,
otherwise the

IllegalComponentStateException

will be thrown.
Refer to

Window.setShape(java.awt.Shape)

,

Window.setOpacity(float)

and

Window.setBackground(java.awt.Color)

for details

isUndecorated

```java
public boolean isUndecorated()
```

Indicates whether this dialog is undecorated.
By default, all dialogs are initially decorated.

**Returns:** true

if dialog is undecorated;

false

otherwise.
**Since:** 1.4
**See Also:** setUndecorated(boolean)

---

#### isUndecorated

public boolean isUndecorated()

Indicates whether this dialog is undecorated.
By default, all dialogs are initially decorated.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this dialog. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Container
**Returns:** the parameter string of this dialog window.

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this dialog. This
method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this Dialog.
For dialogs, the AccessibleContext takes the form of an
AccessibleAWTDialog.
A new AccessibleAWTDialog instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Window
**Returns:** an AccessibleAWTDialog that serves as the
AccessibleContext of this Dialog
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this Dialog.
For dialogs, the AccessibleContext takes the form of an
AccessibleAWTDialog.
A new AccessibleAWTDialog instance is created if necessary.

---

