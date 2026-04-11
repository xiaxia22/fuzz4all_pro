# Class FileDialog

**Source:** `java.desktop\java\awt\FileDialog.html`

### Class Description

```java
public class
FileDialog

extends
Dialog
```

The

FileDialog

class displays a dialog window
from which the user can select a file.

Since it is a modal dialog, when the application calls
its

show

method to display the dialog,
it blocks the rest of the application until the user has
chosen a file.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final int LOAD

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

**See Also:**
- Constant Field Values

---

#### public static final int SAVE

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public FileDialog​(
Frame
parent)

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:**
- parent

- the owner of the dialog

**Since:**
- 1.1

---

#### public FileDialog​(
Frame
parent,

String
title)

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:**
- parent

- the owner of the dialog
- title

- the title of the dialog

---

#### public FileDialog​(
Frame
parent,

String
title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:**
- parent

- the owner of the dialog
- title

- the title of the dialog
- mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE

**Throws:**
- IllegalArgumentException

- if an illegal file
dialog mode is supplied

**See Also:**
- LOAD

,

SAVE

---

#### public FileDialog​(
Dialog
parent)

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:**
- parent

- the owner of the dialog

**Throws:**
- IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
- IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.5

---

#### public FileDialog​(
Dialog
parent,

String
title)

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:**
- parent

- the owner of the dialog
- title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown

**Throws:**
- IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
- IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.5

---

#### public FileDialog​(
Dialog
parent,

String
title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:**
- parent

- the owner of the dialog
- title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown
- mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE

**Throws:**
- IllegalArgumentException

- if an illegal
file dialog mode is supplied;
- IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
- IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

LOAD

,

SAVE

**Since:**
- 1.5

---

### Method Details

#### public void setTitle​(
String
title)

Sets the title of the Dialog.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Overrides:**
- setTitle

in class

Dialog

**Parameters:**
- title

- the title displayed in the dialog's border;
a null value results in an empty title

**See Also:**
- Dialog.getTitle()

---

#### public void addNotify()

Creates the file dialog's peer. The peer allows us to change the look
of the file dialog without changing its functionality.

**Overrides:**
- addNotify

in class

Dialog

**See Also:**
- Component.isDisplayable()

,

Container.removeNotify()

---

#### public int getMode()

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

**Returns:**
- the mode of this file dialog window, either

FileDialog.LOAD

or

FileDialog.SAVE

**See Also:**
- LOAD

,

SAVE

,

setMode(int)

---

#### public void setMode​(int mode)

Sets the mode of the file dialog. If

mode

is not
a legal value, an exception will be thrown and

mode

will not be set.

**Parameters:**
- mode

- the mode for this file dialog, either

FileDialog.LOAD

or

FileDialog.SAVE

**Throws:**
- IllegalArgumentException

- if an illegal file
dialog mode is supplied

**See Also:**
- LOAD

,

SAVE

,

getMode()

**Since:**
- 1.1

---

#### public
String
getDirectory()

Gets the directory of this file dialog.

**Returns:**
- the (potentially

null

or invalid)
directory of this

FileDialog

**See Also:**
- setDirectory(java.lang.String)

---

#### public void setDirectory​(
String
dir)

Sets the directory of this file dialog window to be the
specified directory. Specifying a

null

or an
invalid directory implies an implementation-defined default.
This default will not be realized, however, until the user
has selected a file. Until this point,

getDirectory()

will return the value passed into this method.

Specifying "" as the directory is exactly equivalent to
specifying

null

as the directory.

**Parameters:**
- dir

- the specified directory

**See Also:**
- getDirectory()

---

#### public
String
getFile()

Gets the selected file of this file dialog. If the user
selected

CANCEL

, the returned file is

null

.

**Returns:**
- the currently selected file of this file dialog window,
or

null

if none is selected

**See Also:**
- setFile(java.lang.String)

---

#### public
File
[] getFiles()

Returns files that the user selects.

If the user cancels the file dialog,
then the method returns an empty array.

**Returns:**
- files that the user selects or an empty array
if the user cancels the file dialog.

**See Also:**
- setFile(String)

,

getFile()

**Since:**
- 1.7

---

#### public void setFile​(
String
file)

Sets the selected file for this file dialog window to be the
specified file. This file becomes the default file if it is set
before the file dialog window is first shown.

When the dialog is shown, the specified file is selected. The kind of
selection depends on the file existence, the dialog type, and the native
platform. E.g., the file could be highlighted in the file list, or a
file name editbox could be populated with the file name.

This method accepts either a full file path, or a file name with an
extension if used together with the

setDirectory

method.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

**Parameters:**
- file

- the file being set

**See Also:**
- getFile()

,

getFiles()

---

#### public void setMultipleMode​(boolean enable)

Enables or disables multiple file selection for the file dialog.

**Parameters:**
- enable

- if

true

, multiple file selection is enabled;

false

- disabled.

**See Also:**
- isMultipleMode()

**Since:**
- 1.7

---

#### public boolean isMultipleMode()

Returns whether the file dialog allows the multiple file selection.

**Returns:**
- true

if the file dialog allows the multiple
file selection;

false

otherwise.

**See Also:**
- setMultipleMode(boolean)

**Since:**
- 1.7

---

#### public
FilenameFilter
getFilenameFilter()

Determines this file dialog's filename filter. A filename filter
allows the user to specify which files appear in the file dialog
window. Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Returns:**
- this file dialog's filename filter

**See Also:**
- FilenameFilter

,

setFilenameFilter(java.io.FilenameFilter)

---

#### public void setFilenameFilter​(
FilenameFilter
filter)

Sets the filename filter for this file dialog window to the
specified filter.
Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Parameters:**
- filter

- the specified filter

**See Also:**
- FilenameFilter

,

getFilenameFilter()

---

#### protected
String
paramString()

Returns a string representing the state of this

FileDialog

window. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

Dialog

**Returns:**
- the parameter string of this file dialog window

---

### Additional Sections

#### Class FileDialog

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - java.awt.Window
- - java.awt.Dialog
- - java.awt.FileDialog

java.awt.Component

- java.awt.Container
- - java.awt.Window
- - java.awt.Dialog
- - java.awt.FileDialog

java.awt.Container

- java.awt.Window
- - java.awt.Dialog
- - java.awt.FileDialog

java.awt.Window

- java.awt.Dialog
- - java.awt.FileDialog

java.awt.Dialog

- java.awt.FileDialog

java.awt.FileDialog

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
public class
FileDialog

extends
Dialog
```

The

FileDialog

class displays a dialog window
from which the user can select a file.

Since it is a modal dialog, when the application calls
its

show

method to display the dialog,
it blocks the rest of the application until the user has
chosen a file.

**Since:** 1.0
**See Also:** Window.show()

,

Serialized Form

public class

FileDialog

extends

Dialog

The

FileDialog

class displays a dialog window
from which the user can select a file.

Since it is a modal dialog, when the application calls
its

show

method to display the dialog,
it blocks the rest of the application until the user has
chosen a file.

Since it is a modal dialog, when the application calls
its

show

method to display the dialog,
it blocks the rest of the application until the user has
chosen a file.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

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

static int

LOAD

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

static int

SAVE

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

- Fields declared in class java.awt.

Dialog

DEFAULT_MODALITY_TYPE

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

FileDialog

​(

Dialog

parent)

Creates a file dialog for loading a file.

FileDialog

​(

Dialog

parent,

String

title)

Creates a file dialog window with the specified title for loading
a file.

FileDialog

​(

Dialog

parent,

String

title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

FileDialog

​(

Frame

parent)

Creates a file dialog for loading a file.

FileDialog

​(

Frame

parent,

String

title)

Creates a file dialog window with the specified title for loading
a file.

FileDialog

​(

Frame

parent,

String

title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addNotify

()

Creates the file dialog's peer.

String

getDirectory

()

Gets the directory of this file dialog.

String

getFile

()

Gets the selected file of this file dialog.

FilenameFilter

getFilenameFilter

()

Determines this file dialog's filename filter.

File

[]

getFiles

()

Returns files that the user selects.

int

getMode

()

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

boolean

isMultipleMode

()

Returns whether the file dialog allows the multiple file selection.

protected

String

paramString

()

Returns a string representing the state of this

FileDialog

window.

void

setDirectory

​(

String

dir)

Sets the directory of this file dialog window to be the
specified directory.

void

setFile

​(

String

file)

Sets the selected file for this file dialog window to be the
specified file.

void

setFilenameFilter

​(

FilenameFilter

filter)

Sets the filename filter for this file dialog window to the
specified filter.

void

setMode

​(int mode)

Sets the mode of the file dialog.

void

setMultipleMode

​(boolean enable)

Enables or disables multiple file selection for the file dialog.

void

setTitle

​(

String

title)

Sets the title of the Dialog.

- Methods declared in class java.awt.

Dialog

getAccessibleContext

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

static int

LOAD

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

static int

SAVE

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

- Fields declared in class java.awt.

Dialog

DEFAULT_MODALITY_TYPE

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

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

Fields declared in class java.awt.

Dialog

DEFAULT_MODALITY_TYPE

---

#### Fields declared in class java.awt. Dialog

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

FileDialog

​(

Dialog

parent)

Creates a file dialog for loading a file.

FileDialog

​(

Dialog

parent,

String

title)

Creates a file dialog window with the specified title for loading
a file.

FileDialog

​(

Dialog

parent,

String

title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

FileDialog

​(

Frame

parent)

Creates a file dialog for loading a file.

FileDialog

​(

Frame

parent,

String

title)

Creates a file dialog window with the specified title for loading
a file.

FileDialog

​(

Frame

parent,

String

title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

---

#### Constructor Summary

Creates a file dialog for loading a file.

Creates a file dialog window with the specified title for loading
a file.

Creates a file dialog window with the specified title for loading
or saving a file.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addNotify

()

Creates the file dialog's peer.

String

getDirectory

()

Gets the directory of this file dialog.

String

getFile

()

Gets the selected file of this file dialog.

FilenameFilter

getFilenameFilter

()

Determines this file dialog's filename filter.

File

[]

getFiles

()

Returns files that the user selects.

int

getMode

()

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

boolean

isMultipleMode

()

Returns whether the file dialog allows the multiple file selection.

protected

String

paramString

()

Returns a string representing the state of this

FileDialog

window.

void

setDirectory

​(

String

dir)

Sets the directory of this file dialog window to be the
specified directory.

void

setFile

​(

String

file)

Sets the selected file for this file dialog window to be the
specified file.

void

setFilenameFilter

​(

FilenameFilter

filter)

Sets the filename filter for this file dialog window to the
specified filter.

void

setMode

​(int mode)

Sets the mode of the file dialog.

void

setMultipleMode

​(boolean enable)

Enables or disables multiple file selection for the file dialog.

void

setTitle

​(

String

title)

Sets the title of the Dialog.

- Methods declared in class java.awt.

Dialog

getAccessibleContext

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

Creates the file dialog's peer.

Gets the directory of this file dialog.

Gets the selected file of this file dialog.

Determines this file dialog's filename filter.

Returns files that the user selects.

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

Returns whether the file dialog allows the multiple file selection.

Returns a string representing the state of this

FileDialog

window.

Sets the directory of this file dialog window to be the
specified directory.

Sets the selected file for this file dialog window to be the
specified file.

Sets the filename filter for this file dialog window to the
specified filter.

Sets the mode of the file dialog.

Enables or disables multiple file selection for the file dialog.

Sets the title of the Dialog.

Methods declared in class java.awt.

Dialog

getAccessibleContext

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

- LOAD

```java
public static final int LOAD
```

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

**See Also:** Constant Field Values

- SAVE

```java
public static final int SAVE
```

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FileDialog

```java
public FileDialog​(
Frame
parent)
```

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Since:** 1.1

- FileDialog

```java
public FileDialog​(
Frame
parent,

String
title)
```

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog

- FileDialog

```java
public FileDialog​(
Frame
parent,

String
title,
int mode)
```

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog
**Parameters:** mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal file
dialog mode is supplied
**See Also:** LOAD

,

SAVE

- FileDialog

```java
public FileDialog​(
Dialog
parent)
```

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

- FileDialog

```java
public FileDialog​(
Dialog
parent,

String
title)
```

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

- FileDialog

```java
public FileDialog​(
Dialog
parent,

String
title,
int mode)
```

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown
**Parameters:** mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal
file dialog mode is supplied;
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

,

LOAD

,

SAVE

============ METHOD DETAIL ==========

- Method Detail

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the Dialog.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Overrides:** setTitle

in class

Dialog
**Parameters:** title

- the title displayed in the dialog's border;
a null value results in an empty title
**See Also:** Dialog.getTitle()

- addNotify

```java
public void addNotify()
```

Creates the file dialog's peer. The peer allows us to change the look
of the file dialog without changing its functionality.

**Overrides:** addNotify

in class

Dialog
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- getMode

```java
public int getMode()
```

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

**Returns:** the mode of this file dialog window, either

FileDialog.LOAD

or

FileDialog.SAVE
**See Also:** LOAD

,

SAVE

,

setMode(int)

- setMode

```java
public void setMode​(int mode)
```

Sets the mode of the file dialog. If

mode

is not
a legal value, an exception will be thrown and

mode

will not be set.

**Parameters:** mode

- the mode for this file dialog, either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal file
dialog mode is supplied
**Since:** 1.1
**See Also:** LOAD

,

SAVE

,

getMode()

- getDirectory

```java
public
String
getDirectory()
```

Gets the directory of this file dialog.

**Returns:** the (potentially

null

or invalid)
directory of this

FileDialog
**See Also:** setDirectory(java.lang.String)

- setDirectory

```java
public void setDirectory​(
String
dir)
```

Sets the directory of this file dialog window to be the
specified directory. Specifying a

null

or an
invalid directory implies an implementation-defined default.
This default will not be realized, however, until the user
has selected a file. Until this point,

getDirectory()

will return the value passed into this method.

Specifying "" as the directory is exactly equivalent to
specifying

null

as the directory.

**Parameters:** dir

- the specified directory
**See Also:** getDirectory()

- getFile

```java
public
String
getFile()
```

Gets the selected file of this file dialog. If the user
selected

CANCEL

, the returned file is

null

.

**Returns:** the currently selected file of this file dialog window,
or

null

if none is selected
**See Also:** setFile(java.lang.String)

- getFiles

```java
public
File
[] getFiles()
```

Returns files that the user selects.

If the user cancels the file dialog,
then the method returns an empty array.

**Returns:** files that the user selects or an empty array
if the user cancels the file dialog.
**Since:** 1.7
**See Also:** setFile(String)

,

getFile()

- setFile

```java
public void setFile​(
String
file)
```

Sets the selected file for this file dialog window to be the
specified file. This file becomes the default file if it is set
before the file dialog window is first shown.

When the dialog is shown, the specified file is selected. The kind of
selection depends on the file existence, the dialog type, and the native
platform. E.g., the file could be highlighted in the file list, or a
file name editbox could be populated with the file name.

This method accepts either a full file path, or a file name with an
extension if used together with the

setDirectory

method.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

**Parameters:** file

- the file being set
**See Also:** getFile()

,

getFiles()

- setMultipleMode

```java
public void setMultipleMode​(boolean enable)
```

Enables or disables multiple file selection for the file dialog.

**Parameters:** enable

- if

true

, multiple file selection is enabled;

false

- disabled.
**Since:** 1.7
**See Also:** isMultipleMode()

- isMultipleMode

```java
public boolean isMultipleMode()
```

Returns whether the file dialog allows the multiple file selection.

**Returns:** true

if the file dialog allows the multiple
file selection;

false

otherwise.
**Since:** 1.7
**See Also:** setMultipleMode(boolean)

- getFilenameFilter

```java
public
FilenameFilter
getFilenameFilter()
```

Determines this file dialog's filename filter. A filename filter
allows the user to specify which files appear in the file dialog
window. Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Returns:** this file dialog's filename filter
**See Also:** FilenameFilter

,

setFilenameFilter(java.io.FilenameFilter)

- setFilenameFilter

```java
public void setFilenameFilter​(
FilenameFilter
filter)
```

Sets the filename filter for this file dialog window to the
specified filter.
Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Parameters:** filter

- the specified filter
**See Also:** FilenameFilter

,

getFilenameFilter()

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

FileDialog

window. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Dialog
**Returns:** the parameter string of this file dialog window

Field Detail

- LOAD

```java
public static final int LOAD
```

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

**See Also:** Constant Field Values

- SAVE

```java
public static final int SAVE
```

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

**See Also:** Constant Field Values

---

#### Field Detail

LOAD

```java
public static final int LOAD
```

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

**See Also:** Constant Field Values

---

#### LOAD

public static final int LOAD

This constant value indicates that the purpose of the file
dialog window is to locate a file from which to read.

SAVE

```java
public static final int SAVE
```

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

**See Also:** Constant Field Values

---

#### SAVE

public static final int SAVE

This constant value indicates that the purpose of the file
dialog window is to locate a file to which to write.

Constructor Detail

- FileDialog

```java
public FileDialog​(
Frame
parent)
```

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Since:** 1.1

- FileDialog

```java
public FileDialog​(
Frame
parent,

String
title)
```

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog

- FileDialog

```java
public FileDialog​(
Frame
parent,

String
title,
int mode)
```

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog
**Parameters:** mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal file
dialog mode is supplied
**See Also:** LOAD

,

SAVE

- FileDialog

```java
public FileDialog​(
Dialog
parent)
```

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

- FileDialog

```java
public FileDialog​(
Dialog
parent,

String
title)
```

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

- FileDialog

```java
public FileDialog​(
Dialog
parent,

String
title,
int mode)
```

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown
**Parameters:** mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal
file dialog mode is supplied;
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

,

LOAD

,

SAVE

---

#### Constructor Detail

FileDialog

```java
public FileDialog​(
Frame
parent)
```

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Since:** 1.1

---

#### FileDialog

public FileDialog​(

Frame

parent)

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

FileDialog

```java
public FileDialog​(
Frame
parent,

String
title)
```

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog

---

#### FileDialog

public FileDialog​(

Frame

parent,

String

title)

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

FileDialog

```java
public FileDialog​(
Frame
parent,

String
title,
int mode)
```

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog
**Parameters:** mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal file
dialog mode is supplied
**See Also:** LOAD

,

SAVE

---

#### FileDialog

public FileDialog​(

Frame

parent,

String

title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

FileDialog

```java
public FileDialog​(
Dialog
parent)
```

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

---

#### FileDialog

public FileDialog​(

Dialog

parent)

Creates a file dialog for loading a file. The title of the
file dialog is initially empty. This is a convenience method for

FileDialog(parent, "", LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

FileDialog

```java
public FileDialog​(
Dialog
parent,

String
title)
```

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

---

#### FileDialog

public FileDialog​(

Dialog

parent,

String

title)

Creates a file dialog window with the specified title for loading
a file. The files shown are those in the current directory.
This is a convenience method for

FileDialog(parent, title, LOAD)

.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

FileDialog

```java
public FileDialog​(
Dialog
parent,

String
title,
int mode)
```

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Parameters:** parent

- the owner of the dialog
**Parameters:** title

- the title of the dialog; a

null

value
will be accepted without causing a

NullPointerException

to be thrown
**Parameters:** mode

- the mode of the dialog; either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal
file dialog mode is supplied;
**Throws:** IllegalArgumentException

- if the

parent

's

GraphicsConfiguration

is not from a screen device;
**Throws:** IllegalArgumentException

- if

parent

is

null

; this exception is always thrown when

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.5
**See Also:** GraphicsEnvironment.isHeadless()

,

LOAD

,

SAVE

---

#### FileDialog

public FileDialog​(

Dialog

parent,

String

title,
int mode)

Creates a file dialog window with the specified title for loading
or saving a file.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

If the value of

mode

is

LOAD

, then the
file dialog is finding a file to read, and the files shown are those
in the current directory. If the value of

mode

is

SAVE

, the file dialog is finding
a place to write a file.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Method Detail

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the Dialog.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Overrides:** setTitle

in class

Dialog
**Parameters:** title

- the title displayed in the dialog's border;
a null value results in an empty title
**See Also:** Dialog.getTitle()

- addNotify

```java
public void addNotify()
```

Creates the file dialog's peer. The peer allows us to change the look
of the file dialog without changing its functionality.

**Overrides:** addNotify

in class

Dialog
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

- getMode

```java
public int getMode()
```

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

**Returns:** the mode of this file dialog window, either

FileDialog.LOAD

or

FileDialog.SAVE
**See Also:** LOAD

,

SAVE

,

setMode(int)

- setMode

```java
public void setMode​(int mode)
```

Sets the mode of the file dialog. If

mode

is not
a legal value, an exception will be thrown and

mode

will not be set.

**Parameters:** mode

- the mode for this file dialog, either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal file
dialog mode is supplied
**Since:** 1.1
**See Also:** LOAD

,

SAVE

,

getMode()

- getDirectory

```java
public
String
getDirectory()
```

Gets the directory of this file dialog.

**Returns:** the (potentially

null

or invalid)
directory of this

FileDialog
**See Also:** setDirectory(java.lang.String)

- setDirectory

```java
public void setDirectory​(
String
dir)
```

Sets the directory of this file dialog window to be the
specified directory. Specifying a

null

or an
invalid directory implies an implementation-defined default.
This default will not be realized, however, until the user
has selected a file. Until this point,

getDirectory()

will return the value passed into this method.

Specifying "" as the directory is exactly equivalent to
specifying

null

as the directory.

**Parameters:** dir

- the specified directory
**See Also:** getDirectory()

- getFile

```java
public
String
getFile()
```

Gets the selected file of this file dialog. If the user
selected

CANCEL

, the returned file is

null

.

**Returns:** the currently selected file of this file dialog window,
or

null

if none is selected
**See Also:** setFile(java.lang.String)

- getFiles

```java
public
File
[] getFiles()
```

Returns files that the user selects.

If the user cancels the file dialog,
then the method returns an empty array.

**Returns:** files that the user selects or an empty array
if the user cancels the file dialog.
**Since:** 1.7
**See Also:** setFile(String)

,

getFile()

- setFile

```java
public void setFile​(
String
file)
```

Sets the selected file for this file dialog window to be the
specified file. This file becomes the default file if it is set
before the file dialog window is first shown.

When the dialog is shown, the specified file is selected. The kind of
selection depends on the file existence, the dialog type, and the native
platform. E.g., the file could be highlighted in the file list, or a
file name editbox could be populated with the file name.

This method accepts either a full file path, or a file name with an
extension if used together with the

setDirectory

method.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

**Parameters:** file

- the file being set
**See Also:** getFile()

,

getFiles()

- setMultipleMode

```java
public void setMultipleMode​(boolean enable)
```

Enables or disables multiple file selection for the file dialog.

**Parameters:** enable

- if

true

, multiple file selection is enabled;

false

- disabled.
**Since:** 1.7
**See Also:** isMultipleMode()

- isMultipleMode

```java
public boolean isMultipleMode()
```

Returns whether the file dialog allows the multiple file selection.

**Returns:** true

if the file dialog allows the multiple
file selection;

false

otherwise.
**Since:** 1.7
**See Also:** setMultipleMode(boolean)

- getFilenameFilter

```java
public
FilenameFilter
getFilenameFilter()
```

Determines this file dialog's filename filter. A filename filter
allows the user to specify which files appear in the file dialog
window. Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Returns:** this file dialog's filename filter
**See Also:** FilenameFilter

,

setFilenameFilter(java.io.FilenameFilter)

- setFilenameFilter

```java
public void setFilenameFilter​(
FilenameFilter
filter)
```

Sets the filename filter for this file dialog window to the
specified filter.
Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Parameters:** filter

- the specified filter
**See Also:** FilenameFilter

,

getFilenameFilter()

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

FileDialog

window. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Dialog
**Returns:** the parameter string of this file dialog window

---

#### Method Detail

setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the Dialog.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

**Overrides:** setTitle

in class

Dialog
**Parameters:** title

- the title displayed in the dialog's border;
a null value results in an empty title
**See Also:** Dialog.getTitle()

---

#### setTitle

public void setTitle​(

String

title)

Sets the title of the Dialog.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

Note:

Some platforms may not support
showing the user-specified title in a file dialog.
In this situation, either no title will be displayed in the file dialog's
title bar or, on some systems, the file dialog's title bar will not be
displayed.

addNotify

```java
public void addNotify()
```

Creates the file dialog's peer. The peer allows us to change the look
of the file dialog without changing its functionality.

**Overrides:** addNotify

in class

Dialog
**See Also:** Component.isDisplayable()

,

Container.removeNotify()

---

#### addNotify

public void addNotify()

Creates the file dialog's peer. The peer allows us to change the look
of the file dialog without changing its functionality.

getMode

```java
public int getMode()
```

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

**Returns:** the mode of this file dialog window, either

FileDialog.LOAD

or

FileDialog.SAVE
**See Also:** LOAD

,

SAVE

,

setMode(int)

---

#### getMode

public int getMode()

Indicates whether this file dialog box is for loading from a file
or for saving to a file.

setMode

```java
public void setMode​(int mode)
```

Sets the mode of the file dialog. If

mode

is not
a legal value, an exception will be thrown and

mode

will not be set.

**Parameters:** mode

- the mode for this file dialog, either

FileDialog.LOAD

or

FileDialog.SAVE
**Throws:** IllegalArgumentException

- if an illegal file
dialog mode is supplied
**Since:** 1.1
**See Also:** LOAD

,

SAVE

,

getMode()

---

#### setMode

public void setMode​(int mode)

Sets the mode of the file dialog. If

mode

is not
a legal value, an exception will be thrown and

mode

will not be set.

getDirectory

```java
public
String
getDirectory()
```

Gets the directory of this file dialog.

**Returns:** the (potentially

null

or invalid)
directory of this

FileDialog
**See Also:** setDirectory(java.lang.String)

---

#### getDirectory

public

String

getDirectory()

Gets the directory of this file dialog.

setDirectory

```java
public void setDirectory​(
String
dir)
```

Sets the directory of this file dialog window to be the
specified directory. Specifying a

null

or an
invalid directory implies an implementation-defined default.
This default will not be realized, however, until the user
has selected a file. Until this point,

getDirectory()

will return the value passed into this method.

Specifying "" as the directory is exactly equivalent to
specifying

null

as the directory.

**Parameters:** dir

- the specified directory
**See Also:** getDirectory()

---

#### setDirectory

public void setDirectory​(

String

dir)

Sets the directory of this file dialog window to be the
specified directory. Specifying a

null

or an
invalid directory implies an implementation-defined default.
This default will not be realized, however, until the user
has selected a file. Until this point,

getDirectory()

will return the value passed into this method.

Specifying "" as the directory is exactly equivalent to
specifying

null

as the directory.

Specifying "" as the directory is exactly equivalent to
specifying

null

as the directory.

getFile

```java
public
String
getFile()
```

Gets the selected file of this file dialog. If the user
selected

CANCEL

, the returned file is

null

.

**Returns:** the currently selected file of this file dialog window,
or

null

if none is selected
**See Also:** setFile(java.lang.String)

---

#### getFile

public

String

getFile()

Gets the selected file of this file dialog. If the user
selected

CANCEL

, the returned file is

null

.

getFiles

```java
public
File
[] getFiles()
```

Returns files that the user selects.

If the user cancels the file dialog,
then the method returns an empty array.

**Returns:** files that the user selects or an empty array
if the user cancels the file dialog.
**Since:** 1.7
**See Also:** setFile(String)

,

getFile()

---

#### getFiles

public

File

[] getFiles()

Returns files that the user selects.

If the user cancels the file dialog,
then the method returns an empty array.

If the user cancels the file dialog,
then the method returns an empty array.

setFile

```java
public void setFile​(
String
file)
```

Sets the selected file for this file dialog window to be the
specified file. This file becomes the default file if it is set
before the file dialog window is first shown.

When the dialog is shown, the specified file is selected. The kind of
selection depends on the file existence, the dialog type, and the native
platform. E.g., the file could be highlighted in the file list, or a
file name editbox could be populated with the file name.

This method accepts either a full file path, or a file name with an
extension if used together with the

setDirectory

method.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

**Parameters:** file

- the file being set
**See Also:** getFile()

,

getFiles()

---

#### setFile

public void setFile​(

String

file)

Sets the selected file for this file dialog window to be the
specified file. This file becomes the default file if it is set
before the file dialog window is first shown.

When the dialog is shown, the specified file is selected. The kind of
selection depends on the file existence, the dialog type, and the native
platform. E.g., the file could be highlighted in the file list, or a
file name editbox could be populated with the file name.

This method accepts either a full file path, or a file name with an
extension if used together with the

setDirectory

method.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

When the dialog is shown, the specified file is selected. The kind of
selection depends on the file existence, the dialog type, and the native
platform. E.g., the file could be highlighted in the file list, or a
file name editbox could be populated with the file name.

This method accepts either a full file path, or a file name with an
extension if used together with the

setDirectory

method.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

This method accepts either a full file path, or a file name with an
extension if used together with the

setDirectory

method.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

Specifying "" as the file is exactly equivalent to specifying

null

as the file.

setMultipleMode

```java
public void setMultipleMode​(boolean enable)
```

Enables or disables multiple file selection for the file dialog.

**Parameters:** enable

- if

true

, multiple file selection is enabled;

false

- disabled.
**Since:** 1.7
**See Also:** isMultipleMode()

---

#### setMultipleMode

public void setMultipleMode​(boolean enable)

Enables or disables multiple file selection for the file dialog.

isMultipleMode

```java
public boolean isMultipleMode()
```

Returns whether the file dialog allows the multiple file selection.

**Returns:** true

if the file dialog allows the multiple
file selection;

false

otherwise.
**Since:** 1.7
**See Also:** setMultipleMode(boolean)

---

#### isMultipleMode

public boolean isMultipleMode()

Returns whether the file dialog allows the multiple file selection.

getFilenameFilter

```java
public
FilenameFilter
getFilenameFilter()
```

Determines this file dialog's filename filter. A filename filter
allows the user to specify which files appear in the file dialog
window. Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Returns:** this file dialog's filename filter
**See Also:** FilenameFilter

,

setFilenameFilter(java.io.FilenameFilter)

---

#### getFilenameFilter

public

FilenameFilter

getFilenameFilter()

Determines this file dialog's filename filter. A filename filter
allows the user to specify which files appear in the file dialog
window. Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

setFilenameFilter

```java
public void setFilenameFilter​(
FilenameFilter
filter)
```

Sets the filename filter for this file dialog window to the
specified filter.
Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

**Parameters:** filter

- the specified filter
**See Also:** FilenameFilter

,

getFilenameFilter()

---

#### setFilenameFilter

public void setFilenameFilter​(

FilenameFilter

filter)

Sets the filename filter for this file dialog window to the
specified filter.
Filename filters do not function in Sun's reference
implementation for Microsoft Windows.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

FileDialog

window. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Dialog
**Returns:** the parameter string of this file dialog window

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this

FileDialog

window. This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

---

