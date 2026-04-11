# Class TextArea

**Source:** `java.desktop\java\awt\TextArea.html`

### Class Description

```java
public class
TextArea

extends
TextComponent
```

A

TextArea

object is a multi-line region
that displays text. It can be set to allow editing or
to be read-only.

The following image shows the appearance of a text area:

This text area could be created by the following line of code:

```java
new TextArea("Hello", 5, 40);
```

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final int SCROLLBARS_BOTH

Create and display both vertical and horizontal scrollbars.

**See Also:**
- Constant Field Values

**Since:**
- 1.1

---

#### public static final int SCROLLBARS_VERTICAL_ONLY

Create and display vertical scrollbar only.

**See Also:**
- Constant Field Values

**Since:**
- 1.1

---

#### public static final int SCROLLBARS_HORIZONTAL_ONLY

Create and display horizontal scrollbar only.

**See Also:**
- Constant Field Values

**Since:**
- 1.1

---

#### public static final int SCROLLBARS_NONE

Do not create or display any scrollbars for the text area.

**See Also:**
- Constant Field Values

**Since:**
- 1.1

---

### Constructor Details

#### public TextArea()
throws
HeadlessException

Constructs a new text area with the empty string as text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public TextArea​(
String
text)
throws
HeadlessException

Constructs a new text area with the specified text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Parameters:**
- text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public TextArea​(int rows,
int columns)
throws
HeadlessException

Constructs a new text area with the specified number of
rows and columns and the empty string as text.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:**
- rows

- the number of rows
- columns

- the number of columns

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public TextArea​(
String
text,
int rows,
int columns)
throws
HeadlessException

Constructs a new text area with the specified text,
and with the specified number of rows and columns.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:**
- text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
- rows

- the number of rows
- columns

- the number of columns

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public TextArea​(
String
text,
int rows,
int columns,
int scrollbars)
throws
HeadlessException

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified. All

TextArea

constructors defer to
this one.

The

TextArea

class defines several constants
that can be supplied as values for the

scrollbars

argument:

- SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

.

Any other value for the

scrollbars

argument is invalid and will result in
this text area being created with scrollbar visibility equal to
the default value of

SCROLLBARS_BOTH

.

**Parameters:**
- text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
- rows

- the number of rows; if

rows

is less than

0

,

rows

is set to

0
- columns

- the number of columns; if

columns

is less than

0

,

columns

is set to

0
- scrollbars

- a constant that determines what
scrollbars are created to view the text area

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.1

---

### Method Details

#### public void addNotify()

Creates the

TextArea

's peer. The peer allows us to modify
the appearance of the

TextArea

without changing any of its
functionality.

**Overrides:**
- addNotify

in class

TextComponent

**See Also:**
- TextComponent.removeNotify()

---

#### public void insert​(
String
str,
int pos)

Inserts the specified text at the specified position
in this text area.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:**
- str

- the non-

null

text to insert
- pos

- the position at which to insert

**See Also:**
- TextComponent.setText(java.lang.String)

,

replaceRange(java.lang.String, int, int)

,

append(java.lang.String)

**Since:**
- 1.1

---

#### @Deprecated

public void insertText​(
String
str,
int pos)

Inserts the specified text at the specified position
in this text area.

**Parameters:**
- str

- the non-

null

text to insert
- pos

- the position at which to insert

---

#### public void append​(
String
str)

Appends the given text to the text area's current text.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:**
- str

- the non-

null

text to append

**See Also:**
- insert(java.lang.String, int)

**Since:**
- 1.1

---

#### @Deprecated

public void appendText​(
String
str)

Appends the given text to the text area's current text.

**Parameters:**
- str

- the text to append

---

#### public void replaceRange​(
String
str,
int start,
int end)

Replaces text between the indicated start and end positions
with the specified replacement text. The text at the end
position will not be replaced. The text at the start
position will be replaced (unless the start position is the
same as the end position).
The text position is zero-based. The inserted substring may be
of a different length than the text it replaces.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:**
- str

- the non-

null

text to use as
the replacement
- start

- the start position
- end

- the end position

**See Also:**
- insert(java.lang.String, int)

**Since:**
- 1.1

---

#### @Deprecated

public void replaceText​(
String
str,
int start,
int end)

Replaces a range of characters between
the indicated start and end positions
with the specified replacement text (the text at the end
position will not be replaced).

**Parameters:**
- str

- the non-

null

text to use as
the replacement
- start

- the start position
- end

- the end position

---

#### public int getRows()

Returns the number of rows in the text area.

**Returns:**
- the number of rows in the text area

**See Also:**
- setRows(int)

,

getColumns()

**Since:**
- 1.0

---

#### public void setRows​(int rows)

Sets the number of rows for this text area.

**Parameters:**
- rows

- the number of rows

**Throws:**
- IllegalArgumentException

- if the value
supplied for

rows

is less than

0

**See Also:**
- getRows()

,

setColumns(int)

**Since:**
- 1.1

---

#### public int getColumns()

Returns the number of columns in this text area.

**Returns:**
- the number of columns in the text area

**See Also:**
- setColumns(int)

,

getRows()

---

#### public void setColumns​(int columns)

Sets the number of columns for this text area.

**Parameters:**
- columns

- the number of columns

**Throws:**
- IllegalArgumentException

- if the value
supplied for

columns

is less than

0

**See Also:**
- getColumns()

,

setRows(int)

**Since:**
- 1.1

---

#### public int getScrollbarVisibility()

Returns an enumerated value that indicates which scroll bars
the text area uses.

The

TextArea

class defines four integer constants
that are used to specify which scroll bars are available.

TextArea

has one constructor that gives the
application discretion over scroll bars.

**Returns:**
- an integer that indicates which scroll bars are used

**See Also:**
- SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

,

TextArea(java.lang.String, int, int, int)

**Since:**
- 1.1

---

#### public
Dimension
getPreferredSize​(int rows,
int columns)

Determines the preferred size of a text area with the specified
number of rows and columns.

**Parameters:**
- rows

- the number of rows
- columns

- the number of columns

**Returns:**
- the preferred dimensions required to display
the text area with the specified
number of rows and columns

**See Also:**
- Component.getPreferredSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
preferredSize​(int rows,
int columns)

Determines the preferred size of the text area with the specified
number of rows and columns.

**Parameters:**
- rows

- the number of rows
- columns

- the number of columns

**Returns:**
- the preferred dimensions needed for the text area

---

#### public
Dimension
getPreferredSize()

Determines the preferred size of this text area.

**Overrides:**
- getPreferredSize

in class

Component

**Returns:**
- the preferred dimensions needed for this text area

**See Also:**
- Component.getPreferredSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
preferredSize()

Description copied from class:

Component

**Overrides:**
- preferredSize

in class

Component

**Returns:**
- the component's preferred size

---

#### public
Dimension
getMinimumSize​(int rows,
int columns)

Determines the minimum size of a text area with the specified
number of rows and columns.

**Parameters:**
- rows

- the number of rows
- columns

- the number of columns

**Returns:**
- the minimum dimensions required to display
the text area with the specified
number of rows and columns

**See Also:**
- Component.getMinimumSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
minimumSize​(int rows,
int columns)

Determines the minimum size of the text area with the specified
number of rows and columns.

**Parameters:**
- rows

- the number of rows
- columns

- the number of columns

**Returns:**
- the minimum size for the text area

---

#### public
Dimension
getMinimumSize()

Determines the minimum size of this text area.

**Overrides:**
- getMinimumSize

in class

Component

**Returns:**
- the preferred dimensions needed for this text area

**See Also:**
- Component.getPreferredSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
minimumSize()

Description copied from class:

Component

**Overrides:**
- minimumSize

in class

Component

**Returns:**
- the minimum size of this component

---

#### protected
String
paramString()

Returns a string representing the state of this

TextArea

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

TextComponent

**Returns:**
- the parameter string of this text area

---

#### public
AccessibleContext
getAccessibleContext()

Returns the

AccessibleContext

associated with
this

TextArea

. For text areas, the

AccessibleContext

takes the form of an

AccessibleAWTTextArea

.
A new

AccessibleAWTTextArea

instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

TextComponent

**Returns:**
- an

AccessibleAWTTextArea

that serves as the

AccessibleContext

of this

TextArea

**Since:**
- 1.3

---

### Additional Sections

#### Class TextArea

java.lang.Object

- java.awt.Component
- - java.awt.TextComponent
- - java.awt.TextArea

java.awt.Component

- java.awt.TextComponent
- - java.awt.TextArea

java.awt.TextComponent

- java.awt.TextArea

java.awt.TextArea

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
public class
TextArea

extends
TextComponent
```

A

TextArea

object is a multi-line region
that displays text. It can be set to allow editing or
to be read-only.

The following image shows the appearance of a text area:

This text area could be created by the following line of code:

```java
new TextArea("Hello", 5, 40);
```

**Since:** 1.0
**See Also:** Serialized Form

public class

TextArea

extends

TextComponent

A

TextArea

object is a multi-line region
that displays text. It can be set to allow editing or
to be read-only.

The following image shows the appearance of a text area:

This text area could be created by the following line of code:

```java
new TextArea("Hello", 5, 40);
```

The following image shows the appearance of a text area:

This text area could be created by the following line of code:

```java
new TextArea("Hello", 5, 40);
```

This text area could be created by the following line of code:

```java
new TextArea("Hello", 5, 40);
```

new TextArea("Hello", 5, 40);

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

TextArea.AccessibleAWTTextArea

This class implements accessibility support for the

TextArea

class.

- Nested classes/interfaces declared in class java.awt.

TextComponent

TextComponent.AccessibleAWTTextComponent

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

SCROLLBARS_BOTH

Create and display both vertical and horizontal scrollbars.

static int

SCROLLBARS_HORIZONTAL_ONLY

Create and display horizontal scrollbar only.

static int

SCROLLBARS_NONE

Do not create or display any scrollbars for the text area.

static int

SCROLLBARS_VERTICAL_ONLY

Create and display vertical scrollbar only.

- Fields declared in class java.awt.

TextComponent

textListener

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

TextArea

()

Constructs a new text area with the empty string as text.

TextArea

​(int rows,
int columns)

Constructs a new text area with the specified number of
rows and columns and the empty string as text.

TextArea

​(

String

text)

Constructs a new text area with the specified text.

TextArea

​(

String

text,
int rows,
int columns)

Constructs a new text area with the specified text,
and with the specified number of rows and columns.

TextArea

​(

String

text,
int rows,
int columns,
int scrollbars)

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified.

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

Creates the

TextArea

's peer.

void

append

​(

String

str)

Appends the given text to the text area's current text.

void

appendText

​(

String

str)

Deprecated.

As of JDK version 1.1,
replaced by

append(String)

.

AccessibleContext

getAccessibleContext

()

Returns the

AccessibleContext

associated with
this

TextArea

.

int

getColumns

()

Returns the number of columns in this text area.

Dimension

getMinimumSize

()

Determines the minimum size of this text area.

Dimension

getMinimumSize

​(int rows,
int columns)

Determines the minimum size of a text area with the specified
number of rows and columns.

Dimension

getPreferredSize

()

Determines the preferred size of this text area.

Dimension

getPreferredSize

​(int rows,
int columns)

Determines the preferred size of a text area with the specified
number of rows and columns.

int

getRows

()

Returns the number of rows in the text area.

int

getScrollbarVisibility

()

Returns an enumerated value that indicates which scroll bars
the text area uses.

void

insert

​(

String

str,
int pos)

Inserts the specified text at the specified position
in this text area.

void

insertText

​(

String

str,
int pos)

Deprecated.

As of JDK version 1.1,
replaced by

insert(String, int)

.

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Dimension

minimumSize

​(int rows,
int columns)

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int, int)

.

protected

String

paramString

()

Returns a string representing the state of this

TextArea

.

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Dimension

preferredSize

​(int rows,
int columns)

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int, int)

.

void

replaceRange

​(

String

str,
int start,
int end)

Replaces text between the indicated start and end positions
with the specified replacement text.

void

replaceText

​(

String

str,
int start,
int end)

Deprecated.

As of JDK version 1.1,
replaced by

replaceRange(String, int, int)

.

void

setColumns

​(int columns)

Sets the number of columns for this text area.

void

setRows

​(int rows)

Sets the number of rows for this text area.

- Methods declared in class java.awt.

TextComponent

addTextListener

,

enableInputMethods

,

getBackground

,

getCaretPosition

,

getListeners

,

getSelectedText

,

getSelectionEnd

,

getSelectionStart

,

getText

,

getTextListeners

,

isEditable

,

processEvent

,

processTextEvent

,

removeNotify

,

removeTextListener

,

select

,

selectAll

,

setBackground

,

setCaretPosition

,

setEditable

,

setSelectionEnd

,

setSelectionStart

,

setText

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

,

enable

,

enableEvents

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

getAlignmentX

,

getAlignmentY

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

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

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

getToolkit

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

hide

,

imageUpdate

,

inside

,

invalidate

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

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

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

paint

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

print

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

reshape

,

resize

,

resize

,

revalidate

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

TextArea.AccessibleAWTTextArea

This class implements accessibility support for the

TextArea

class.

- Nested classes/interfaces declared in class java.awt.

TextComponent

TextComponent.AccessibleAWTTextComponent

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

TextArea

class.

Nested classes/interfaces declared in class java.awt.

TextComponent

TextComponent.AccessibleAWTTextComponent

---

#### Nested classes/interfaces declared in class java.awt. TextComponent

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

SCROLLBARS_BOTH

Create and display both vertical and horizontal scrollbars.

static int

SCROLLBARS_HORIZONTAL_ONLY

Create and display horizontal scrollbar only.

static int

SCROLLBARS_NONE

Do not create or display any scrollbars for the text area.

static int

SCROLLBARS_VERTICAL_ONLY

Create and display vertical scrollbar only.

- Fields declared in class java.awt.

TextComponent

textListener

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

Create and display both vertical and horizontal scrollbars.

Create and display horizontal scrollbar only.

Do not create or display any scrollbars for the text area.

Create and display vertical scrollbar only.

Fields declared in class java.awt.

TextComponent

textListener

---

#### Fields declared in class java.awt. TextComponent

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

TextArea

()

Constructs a new text area with the empty string as text.

TextArea

​(int rows,
int columns)

Constructs a new text area with the specified number of
rows and columns and the empty string as text.

TextArea

​(

String

text)

Constructs a new text area with the specified text.

TextArea

​(

String

text,
int rows,
int columns)

Constructs a new text area with the specified text,
and with the specified number of rows and columns.

TextArea

​(

String

text,
int rows,
int columns,
int scrollbars)

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified.

---

#### Constructor Summary

Constructs a new text area with the empty string as text.

Constructs a new text area with the specified number of
rows and columns and the empty string as text.

Constructs a new text area with the specified text.

Constructs a new text area with the specified text,
and with the specified number of rows and columns.

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified.

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

Creates the

TextArea

's peer.

void

append

​(

String

str)

Appends the given text to the text area's current text.

void

appendText

​(

String

str)

Deprecated.

As of JDK version 1.1,
replaced by

append(String)

.

AccessibleContext

getAccessibleContext

()

Returns the

AccessibleContext

associated with
this

TextArea

.

int

getColumns

()

Returns the number of columns in this text area.

Dimension

getMinimumSize

()

Determines the minimum size of this text area.

Dimension

getMinimumSize

​(int rows,
int columns)

Determines the minimum size of a text area with the specified
number of rows and columns.

Dimension

getPreferredSize

()

Determines the preferred size of this text area.

Dimension

getPreferredSize

​(int rows,
int columns)

Determines the preferred size of a text area with the specified
number of rows and columns.

int

getRows

()

Returns the number of rows in the text area.

int

getScrollbarVisibility

()

Returns an enumerated value that indicates which scroll bars
the text area uses.

void

insert

​(

String

str,
int pos)

Inserts the specified text at the specified position
in this text area.

void

insertText

​(

String

str,
int pos)

Deprecated.

As of JDK version 1.1,
replaced by

insert(String, int)

.

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Dimension

minimumSize

​(int rows,
int columns)

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int, int)

.

protected

String

paramString

()

Returns a string representing the state of this

TextArea

.

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Dimension

preferredSize

​(int rows,
int columns)

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int, int)

.

void

replaceRange

​(

String

str,
int start,
int end)

Replaces text between the indicated start and end positions
with the specified replacement text.

void

replaceText

​(

String

str,
int start,
int end)

Deprecated.

As of JDK version 1.1,
replaced by

replaceRange(String, int, int)

.

void

setColumns

​(int columns)

Sets the number of columns for this text area.

void

setRows

​(int rows)

Sets the number of rows for this text area.

- Methods declared in class java.awt.

TextComponent

addTextListener

,

enableInputMethods

,

getBackground

,

getCaretPosition

,

getListeners

,

getSelectedText

,

getSelectionEnd

,

getSelectionStart

,

getText

,

getTextListeners

,

isEditable

,

processEvent

,

processTextEvent

,

removeNotify

,

removeTextListener

,

select

,

selectAll

,

setBackground

,

setCaretPosition

,

setEditable

,

setSelectionEnd

,

setSelectionStart

,

setText

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

,

enable

,

enableEvents

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

getAlignmentX

,

getAlignmentY

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

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

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

getToolkit

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

hide

,

imageUpdate

,

inside

,

invalidate

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

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

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

paint

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

print

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

reshape

,

resize

,

resize

,

revalidate

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

Creates the

TextArea

's peer.

Appends the given text to the text area's current text.

Deprecated.

As of JDK version 1.1,
replaced by

append(String)

.

Returns the

AccessibleContext

associated with
this

TextArea

.

Returns the number of columns in this text area.

Determines the minimum size of this text area.

Determines the minimum size of a text area with the specified
number of rows and columns.

Determines the preferred size of this text area.

Determines the preferred size of a text area with the specified
number of rows and columns.

Returns the number of rows in the text area.

Returns an enumerated value that indicates which scroll bars
the text area uses.

Inserts the specified text at the specified position
in this text area.

Deprecated.

As of JDK version 1.1,
replaced by

insert(String, int)

.

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int, int)

.

Returns a string representing the state of this

TextArea

.

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int, int)

.

Replaces text between the indicated start and end positions
with the specified replacement text.

Deprecated.

As of JDK version 1.1,
replaced by

replaceRange(String, int, int)

.

Sets the number of columns for this text area.

Sets the number of rows for this text area.

Methods declared in class java.awt.

TextComponent

addTextListener

,

enableInputMethods

,

getBackground

,

getCaretPosition

,

getListeners

,

getSelectedText

,

getSelectionEnd

,

getSelectionStart

,

getText

,

getTextListeners

,

isEditable

,

processEvent

,

processTextEvent

,

removeNotify

,

removeTextListener

,

select

,

selectAll

,

setBackground

,

setCaretPosition

,

setEditable

,

setSelectionEnd

,

setSelectionStart

,

setText

---

#### Methods declared in class java.awt. TextComponent

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

,

enable

,

enableEvents

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

getAlignmentX

,

getAlignmentY

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

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

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

getToolkit

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

hide

,

imageUpdate

,

inside

,

invalidate

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

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

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

paint

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

print

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

reshape

,

resize

,

resize

,

revalidate

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

- SCROLLBARS_BOTH

```java
public static final int SCROLLBARS_BOTH
```

Create and display both vertical and horizontal scrollbars.

**Since:** 1.1
**See Also:** Constant Field Values

- SCROLLBARS_VERTICAL_ONLY

```java
public static final int SCROLLBARS_VERTICAL_ONLY
```

Create and display vertical scrollbar only.

**Since:** 1.1
**See Also:** Constant Field Values

- SCROLLBARS_HORIZONTAL_ONLY

```java
public static final int SCROLLBARS_HORIZONTAL_ONLY
```

Create and display horizontal scrollbar only.

**Since:** 1.1
**See Also:** Constant Field Values

- SCROLLBARS_NONE

```java
public static final int SCROLLBARS_NONE
```

Do not create or display any scrollbars for the text area.

**Since:** 1.1
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TextArea

```java
public TextArea()
throws
HeadlessException
```

Constructs a new text area with the empty string as text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(
String
text)
throws
HeadlessException
```

Constructs a new text area with the specified text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(int rows,
int columns)
throws
HeadlessException
```

Constructs a new text area with the specified number of
rows and columns and the empty string as text.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(
String
text,
int rows,
int columns)
throws
HeadlessException
```

Constructs a new text area with the specified text,
and with the specified number of rows and columns.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(
String
text,
int rows,
int columns,
int scrollbars)
throws
HeadlessException
```

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified. All

TextArea

constructors defer to
this one.

The

TextArea

class defines several constants
that can be supplied as values for the

scrollbars

argument:

- SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

.

Any other value for the

scrollbars

argument is invalid and will result in
this text area being created with scrollbar visibility equal to
the default value of

SCROLLBARS_BOTH

.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Parameters:** rows

- the number of rows; if

rows

is less than

0

,

rows

is set to

0
**Parameters:** columns

- the number of columns; if

columns

is less than

0

,

columns

is set to

0
**Parameters:** scrollbars

- a constant that determines what
scrollbars are created to view the text area
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- addNotify

```java
public void addNotify()
```

Creates the

TextArea

's peer. The peer allows us to modify
the appearance of the

TextArea

without changing any of its
functionality.

**Overrides:** addNotify

in class

TextComponent
**See Also:** TextComponent.removeNotify()

- insert

```java
public void insert​(
String
str,
int pos)
```

Inserts the specified text at the specified position
in this text area.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to insert
**Parameters:** pos

- the position at which to insert
**Since:** 1.1
**See Also:** TextComponent.setText(java.lang.String)

,

replaceRange(java.lang.String, int, int)

,

append(java.lang.String)

- insertText

```java
@Deprecated

public void insertText​(
String
str,
int pos)
```

Deprecated.

As of JDK version 1.1,
replaced by

insert(String, int)

.

Inserts the specified text at the specified position
in this text area.

**Parameters:** str

- the non-

null

text to insert
**Parameters:** pos

- the position at which to insert

- append

```java
public void append​(
String
str)
```

Appends the given text to the text area's current text.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to append
**Since:** 1.1
**See Also:** insert(java.lang.String, int)

- appendText

```java
@Deprecated

public void appendText​(
String
str)
```

Deprecated.

As of JDK version 1.1,
replaced by

append(String)

.

Appends the given text to the text area's current text.

**Parameters:** str

- the text to append

- replaceRange

```java
public void replaceRange​(
String
str,
int start,
int end)
```

Replaces text between the indicated start and end positions
with the specified replacement text. The text at the end
position will not be replaced. The text at the start
position will be replaced (unless the start position is the
same as the end position).
The text position is zero-based. The inserted substring may be
of a different length than the text it replaces.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to use as
the replacement
**Parameters:** start

- the start position
**Parameters:** end

- the end position
**Since:** 1.1
**See Also:** insert(java.lang.String, int)

- replaceText

```java
@Deprecated

public void replaceText​(
String
str,
int start,
int end)
```

Deprecated.

As of JDK version 1.1,
replaced by

replaceRange(String, int, int)

.

Replaces a range of characters between
the indicated start and end positions
with the specified replacement text (the text at the end
position will not be replaced).

**Parameters:** str

- the non-

null

text to use as
the replacement
**Parameters:** start

- the start position
**Parameters:** end

- the end position

- getRows

```java
public int getRows()
```

Returns the number of rows in the text area.

**Returns:** the number of rows in the text area
**Since:** 1.0
**See Also:** setRows(int)

,

getColumns()

- setRows

```java
public void setRows​(int rows)
```

Sets the number of rows for this text area.

**Parameters:** rows

- the number of rows
**Throws:** IllegalArgumentException

- if the value
supplied for

rows

is less than

0
**Since:** 1.1
**See Also:** getRows()

,

setColumns(int)

- getColumns

```java
public int getColumns()
```

Returns the number of columns in this text area.

**Returns:** the number of columns in the text area
**See Also:** setColumns(int)

,

getRows()

- setColumns

```java
public void setColumns​(int columns)
```

Sets the number of columns for this text area.

**Parameters:** columns

- the number of columns
**Throws:** IllegalArgumentException

- if the value
supplied for

columns

is less than

0
**Since:** 1.1
**See Also:** getColumns()

,

setRows(int)

- getScrollbarVisibility

```java
public int getScrollbarVisibility()
```

Returns an enumerated value that indicates which scroll bars
the text area uses.

The

TextArea

class defines four integer constants
that are used to specify which scroll bars are available.

TextArea

has one constructor that gives the
application discretion over scroll bars.

**Returns:** an integer that indicates which scroll bars are used
**Since:** 1.1
**See Also:** SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

,

TextArea(java.lang.String, int, int, int)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(int rows,
int columns)
```

Determines the preferred size of a text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the preferred dimensions required to display
the text area with the specified
number of rows and columns
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize​(int rows,
int columns)
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int, int)

.

Determines the preferred size of the text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the preferred dimensions needed for the text area

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Determines the preferred size of this text area.

**Overrides:** getPreferredSize

in class

Component
**Returns:** the preferred dimensions needed for this text area
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

- getMinimumSize

```java
public
Dimension
getMinimumSize​(int rows,
int columns)
```

Determines the minimum size of a text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the minimum dimensions required to display
the text area with the specified
number of rows and columns
**Since:** 1.1
**See Also:** Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize​(int rows,
int columns)
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int, int)

.

Determines the minimum size of the text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the minimum size for the text area

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Determines the minimum size of this text area.

**Overrides:** getMinimumSize

in class

Component
**Returns:** the preferred dimensions needed for this text area
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

TextArea

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

TextComponent
**Returns:** the parameter string of this text area

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with
this

TextArea

. For text areas, the

AccessibleContext

takes the form of an

AccessibleAWTTextArea

.
A new

AccessibleAWTTextArea

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

TextComponent
**Returns:** an

AccessibleAWTTextArea

that serves as the

AccessibleContext

of this

TextArea
**Since:** 1.3

Field Detail

- SCROLLBARS_BOTH

```java
public static final int SCROLLBARS_BOTH
```

Create and display both vertical and horizontal scrollbars.

**Since:** 1.1
**See Also:** Constant Field Values

- SCROLLBARS_VERTICAL_ONLY

```java
public static final int SCROLLBARS_VERTICAL_ONLY
```

Create and display vertical scrollbar only.

**Since:** 1.1
**See Also:** Constant Field Values

- SCROLLBARS_HORIZONTAL_ONLY

```java
public static final int SCROLLBARS_HORIZONTAL_ONLY
```

Create and display horizontal scrollbar only.

**Since:** 1.1
**See Also:** Constant Field Values

- SCROLLBARS_NONE

```java
public static final int SCROLLBARS_NONE
```

Do not create or display any scrollbars for the text area.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### Field Detail

SCROLLBARS_BOTH

```java
public static final int SCROLLBARS_BOTH
```

Create and display both vertical and horizontal scrollbars.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### SCROLLBARS_BOTH

public static final int SCROLLBARS_BOTH

Create and display both vertical and horizontal scrollbars.

SCROLLBARS_VERTICAL_ONLY

```java
public static final int SCROLLBARS_VERTICAL_ONLY
```

Create and display vertical scrollbar only.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### SCROLLBARS_VERTICAL_ONLY

public static final int SCROLLBARS_VERTICAL_ONLY

Create and display vertical scrollbar only.

SCROLLBARS_HORIZONTAL_ONLY

```java
public static final int SCROLLBARS_HORIZONTAL_ONLY
```

Create and display horizontal scrollbar only.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### SCROLLBARS_HORIZONTAL_ONLY

public static final int SCROLLBARS_HORIZONTAL_ONLY

Create and display horizontal scrollbar only.

SCROLLBARS_NONE

```java
public static final int SCROLLBARS_NONE
```

Do not create or display any scrollbars for the text area.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### SCROLLBARS_NONE

public static final int SCROLLBARS_NONE

Do not create or display any scrollbars for the text area.

Constructor Detail

- TextArea

```java
public TextArea()
throws
HeadlessException
```

Constructs a new text area with the empty string as text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(
String
text)
throws
HeadlessException
```

Constructs a new text area with the specified text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(int rows,
int columns)
throws
HeadlessException
```

Constructs a new text area with the specified number of
rows and columns and the empty string as text.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(
String
text,
int rows,
int columns)
throws
HeadlessException
```

Constructs a new text area with the specified text,
and with the specified number of rows and columns.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

- TextArea

```java
public TextArea​(
String
text,
int rows,
int columns,
int scrollbars)
throws
HeadlessException
```

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified. All

TextArea

constructors defer to
this one.

The

TextArea

class defines several constants
that can be supplied as values for the

scrollbars

argument:

- SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

.

Any other value for the

scrollbars

argument is invalid and will result in
this text area being created with scrollbar visibility equal to
the default value of

SCROLLBARS_BOTH

.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Parameters:** rows

- the number of rows; if

rows

is less than

0

,

rows

is set to

0
**Parameters:** columns

- the number of columns; if

columns

is less than

0

,

columns

is set to

0
**Parameters:** scrollbars

- a constant that determines what
scrollbars are created to view the text area
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

TextArea

```java
public TextArea()
throws
HeadlessException
```

Constructs a new text area with the empty string as text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### TextArea

public TextArea()
throws

HeadlessException

Constructs a new text area with the empty string as text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

TextArea

```java
public TextArea​(
String
text)
throws
HeadlessException
```

Constructs a new text area with the specified text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### TextArea

public TextArea​(

String

text)
throws

HeadlessException

Constructs a new text area with the specified text.
This text area is created with scrollbar visibility equal to

SCROLLBARS_BOTH

, so both vertical and horizontal
scrollbars will be visible for this text area.

TextArea

```java
public TextArea​(int rows,
int columns)
throws
HeadlessException
```

Constructs a new text area with the specified number of
rows and columns and the empty string as text.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### TextArea

public TextArea​(int rows,
int columns)
throws

HeadlessException

Constructs a new text area with the specified number of
rows and columns and the empty string as text.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

TextArea

```java
public TextArea​(
String
text,
int rows,
int columns)
throws
HeadlessException
```

Constructs a new text area with the specified text,
and with the specified number of rows and columns.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### TextArea

public TextArea​(

String

text,
int rows,
int columns)
throws

HeadlessException

Constructs a new text area with the specified text,
and with the specified number of rows and columns.
A column is an approximate average character
width that is platform-dependent. The text area is created with
scrollbar visibility equal to

SCROLLBARS_BOTH

, so both
vertical and horizontal scrollbars will be visible for this
text area.

TextArea

```java
public TextArea​(
String
text,
int rows,
int columns,
int scrollbars)
throws
HeadlessException
```

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified. All

TextArea

constructors defer to
this one.

The

TextArea

class defines several constants
that can be supplied as values for the

scrollbars

argument:

- SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

.

Any other value for the

scrollbars

argument is invalid and will result in
this text area being created with scrollbar visibility equal to
the default value of

SCROLLBARS_BOTH

.

**Parameters:** text

- the text to be displayed; if

text

is

null

, the empty
string

""

will be displayed
**Parameters:** rows

- the number of rows; if

rows

is less than

0

,

rows

is set to

0
**Parameters:** columns

- the number of columns; if

columns

is less than

0

,

columns

is set to

0
**Parameters:** scrollbars

- a constant that determines what
scrollbars are created to view the text area
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

---

#### TextArea

public TextArea​(

String

text,
int rows,
int columns,
int scrollbars)
throws

HeadlessException

Constructs a new text area with the specified text,
and with the rows, columns, and scroll bar visibility
as specified. All

TextArea

constructors defer to
this one.

The

TextArea

class defines several constants
that can be supplied as values for the

scrollbars

argument:

- SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

.

Any other value for the

scrollbars

argument is invalid and will result in
this text area being created with scrollbar visibility equal to
the default value of

SCROLLBARS_BOTH

.

The

TextArea

class defines several constants
that can be supplied as values for the

scrollbars

argument:

- SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

.

Any other value for the

scrollbars

argument is invalid and will result in
this text area being created with scrollbar visibility equal to
the default value of

SCROLLBARS_BOTH

.

SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

.

Method Detail

- addNotify

```java
public void addNotify()
```

Creates the

TextArea

's peer. The peer allows us to modify
the appearance of the

TextArea

without changing any of its
functionality.

**Overrides:** addNotify

in class

TextComponent
**See Also:** TextComponent.removeNotify()

- insert

```java
public void insert​(
String
str,
int pos)
```

Inserts the specified text at the specified position
in this text area.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to insert
**Parameters:** pos

- the position at which to insert
**Since:** 1.1
**See Also:** TextComponent.setText(java.lang.String)

,

replaceRange(java.lang.String, int, int)

,

append(java.lang.String)

- insertText

```java
@Deprecated

public void insertText​(
String
str,
int pos)
```

Deprecated.

As of JDK version 1.1,
replaced by

insert(String, int)

.

Inserts the specified text at the specified position
in this text area.

**Parameters:** str

- the non-

null

text to insert
**Parameters:** pos

- the position at which to insert

- append

```java
public void append​(
String
str)
```

Appends the given text to the text area's current text.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to append
**Since:** 1.1
**See Also:** insert(java.lang.String, int)

- appendText

```java
@Deprecated

public void appendText​(
String
str)
```

Deprecated.

As of JDK version 1.1,
replaced by

append(String)

.

Appends the given text to the text area's current text.

**Parameters:** str

- the text to append

- replaceRange

```java
public void replaceRange​(
String
str,
int start,
int end)
```

Replaces text between the indicated start and end positions
with the specified replacement text. The text at the end
position will not be replaced. The text at the start
position will be replaced (unless the start position is the
same as the end position).
The text position is zero-based. The inserted substring may be
of a different length than the text it replaces.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to use as
the replacement
**Parameters:** start

- the start position
**Parameters:** end

- the end position
**Since:** 1.1
**See Also:** insert(java.lang.String, int)

- replaceText

```java
@Deprecated

public void replaceText​(
String
str,
int start,
int end)
```

Deprecated.

As of JDK version 1.1,
replaced by

replaceRange(String, int, int)

.

Replaces a range of characters between
the indicated start and end positions
with the specified replacement text (the text at the end
position will not be replaced).

**Parameters:** str

- the non-

null

text to use as
the replacement
**Parameters:** start

- the start position
**Parameters:** end

- the end position

- getRows

```java
public int getRows()
```

Returns the number of rows in the text area.

**Returns:** the number of rows in the text area
**Since:** 1.0
**See Also:** setRows(int)

,

getColumns()

- setRows

```java
public void setRows​(int rows)
```

Sets the number of rows for this text area.

**Parameters:** rows

- the number of rows
**Throws:** IllegalArgumentException

- if the value
supplied for

rows

is less than

0
**Since:** 1.1
**See Also:** getRows()

,

setColumns(int)

- getColumns

```java
public int getColumns()
```

Returns the number of columns in this text area.

**Returns:** the number of columns in the text area
**See Also:** setColumns(int)

,

getRows()

- setColumns

```java
public void setColumns​(int columns)
```

Sets the number of columns for this text area.

**Parameters:** columns

- the number of columns
**Throws:** IllegalArgumentException

- if the value
supplied for

columns

is less than

0
**Since:** 1.1
**See Also:** getColumns()

,

setRows(int)

- getScrollbarVisibility

```java
public int getScrollbarVisibility()
```

Returns an enumerated value that indicates which scroll bars
the text area uses.

The

TextArea

class defines four integer constants
that are used to specify which scroll bars are available.

TextArea

has one constructor that gives the
application discretion over scroll bars.

**Returns:** an integer that indicates which scroll bars are used
**Since:** 1.1
**See Also:** SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

,

TextArea(java.lang.String, int, int, int)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(int rows,
int columns)
```

Determines the preferred size of a text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the preferred dimensions required to display
the text area with the specified
number of rows and columns
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize​(int rows,
int columns)
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int, int)

.

Determines the preferred size of the text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the preferred dimensions needed for the text area

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Determines the preferred size of this text area.

**Overrides:** getPreferredSize

in class

Component
**Returns:** the preferred dimensions needed for this text area
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

- getMinimumSize

```java
public
Dimension
getMinimumSize​(int rows,
int columns)
```

Determines the minimum size of a text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the minimum dimensions required to display
the text area with the specified
number of rows and columns
**Since:** 1.1
**See Also:** Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize​(int rows,
int columns)
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int, int)

.

Determines the minimum size of the text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the minimum size for the text area

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Determines the minimum size of this text area.

**Overrides:** getMinimumSize

in class

Component
**Returns:** the preferred dimensions needed for this text area
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

TextArea

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

TextComponent
**Returns:** the parameter string of this text area

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with
this

TextArea

. For text areas, the

AccessibleContext

takes the form of an

AccessibleAWTTextArea

.
A new

AccessibleAWTTextArea

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

TextComponent
**Returns:** an

AccessibleAWTTextArea

that serves as the

AccessibleContext

of this

TextArea
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Creates the

TextArea

's peer. The peer allows us to modify
the appearance of the

TextArea

without changing any of its
functionality.

**Overrides:** addNotify

in class

TextComponent
**See Also:** TextComponent.removeNotify()

---

#### addNotify

public void addNotify()

Creates the

TextArea

's peer. The peer allows us to modify
the appearance of the

TextArea

without changing any of its
functionality.

insert

```java
public void insert​(
String
str,
int pos)
```

Inserts the specified text at the specified position
in this text area.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to insert
**Parameters:** pos

- the position at which to insert
**Since:** 1.1
**See Also:** TextComponent.setText(java.lang.String)

,

replaceRange(java.lang.String, int, int)

,

append(java.lang.String)

---

#### insert

public void insert​(

String

str,
int pos)

Inserts the specified text at the specified position
in this text area.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

insertText

```java
@Deprecated

public void insertText​(
String
str,
int pos)
```

Deprecated.

As of JDK version 1.1,
replaced by

insert(String, int)

.

Inserts the specified text at the specified position
in this text area.

**Parameters:** str

- the non-

null

text to insert
**Parameters:** pos

- the position at which to insert

---

#### insertText

@Deprecated

public void insertText​(

String

str,
int pos)

Inserts the specified text at the specified position
in this text area.

append

```java
public void append​(
String
str)
```

Appends the given text to the text area's current text.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to append
**Since:** 1.1
**See Also:** insert(java.lang.String, int)

---

#### append

public void append​(

String

str)

Appends the given text to the text area's current text.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

appendText

```java
@Deprecated

public void appendText​(
String
str)
```

Deprecated.

As of JDK version 1.1,
replaced by

append(String)

.

Appends the given text to the text area's current text.

**Parameters:** str

- the text to append

---

#### appendText

@Deprecated

public void appendText​(

String

str)

Appends the given text to the text area's current text.

replaceRange

```java
public void replaceRange​(
String
str,
int start,
int end)
```

Replaces text between the indicated start and end positions
with the specified replacement text. The text at the end
position will not be replaced. The text at the start
position will be replaced (unless the start position is the
same as the end position).
The text position is zero-based. The inserted substring may be
of a different length than the text it replaces.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

**Parameters:** str

- the non-

null

text to use as
the replacement
**Parameters:** start

- the start position
**Parameters:** end

- the end position
**Since:** 1.1
**See Also:** insert(java.lang.String, int)

---

#### replaceRange

public void replaceRange​(

String

str,
int start,
int end)

Replaces text between the indicated start and end positions
with the specified replacement text. The text at the end
position will not be replaced. The text at the start
position will be replaced (unless the start position is the
same as the end position).
The text position is zero-based. The inserted substring may be
of a different length than the text it replaces.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

Note that passing

null

or inconsistent
parameters is invalid and will result in unspecified
behavior.

replaceText

```java
@Deprecated

public void replaceText​(
String
str,
int start,
int end)
```

Deprecated.

As of JDK version 1.1,
replaced by

replaceRange(String, int, int)

.

Replaces a range of characters between
the indicated start and end positions
with the specified replacement text (the text at the end
position will not be replaced).

**Parameters:** str

- the non-

null

text to use as
the replacement
**Parameters:** start

- the start position
**Parameters:** end

- the end position

---

#### replaceText

@Deprecated

public void replaceText​(

String

str,
int start,
int end)

Replaces a range of characters between
the indicated start and end positions
with the specified replacement text (the text at the end
position will not be replaced).

getRows

```java
public int getRows()
```

Returns the number of rows in the text area.

**Returns:** the number of rows in the text area
**Since:** 1.0
**See Also:** setRows(int)

,

getColumns()

---

#### getRows

public int getRows()

Returns the number of rows in the text area.

setRows

```java
public void setRows​(int rows)
```

Sets the number of rows for this text area.

**Parameters:** rows

- the number of rows
**Throws:** IllegalArgumentException

- if the value
supplied for

rows

is less than

0
**Since:** 1.1
**See Also:** getRows()

,

setColumns(int)

---

#### setRows

public void setRows​(int rows)

Sets the number of rows for this text area.

getColumns

```java
public int getColumns()
```

Returns the number of columns in this text area.

**Returns:** the number of columns in the text area
**See Also:** setColumns(int)

,

getRows()

---

#### getColumns

public int getColumns()

Returns the number of columns in this text area.

setColumns

```java
public void setColumns​(int columns)
```

Sets the number of columns for this text area.

**Parameters:** columns

- the number of columns
**Throws:** IllegalArgumentException

- if the value
supplied for

columns

is less than

0
**Since:** 1.1
**See Also:** getColumns()

,

setRows(int)

---

#### setColumns

public void setColumns​(int columns)

Sets the number of columns for this text area.

getScrollbarVisibility

```java
public int getScrollbarVisibility()
```

Returns an enumerated value that indicates which scroll bars
the text area uses.

The

TextArea

class defines four integer constants
that are used to specify which scroll bars are available.

TextArea

has one constructor that gives the
application discretion over scroll bars.

**Returns:** an integer that indicates which scroll bars are used
**Since:** 1.1
**See Also:** SCROLLBARS_BOTH

,

SCROLLBARS_VERTICAL_ONLY

,

SCROLLBARS_HORIZONTAL_ONLY

,

SCROLLBARS_NONE

,

TextArea(java.lang.String, int, int, int)

---

#### getScrollbarVisibility

public int getScrollbarVisibility()

Returns an enumerated value that indicates which scroll bars
the text area uses.

The

TextArea

class defines four integer constants
that are used to specify which scroll bars are available.

TextArea

has one constructor that gives the
application discretion over scroll bars.

The

TextArea

class defines four integer constants
that are used to specify which scroll bars are available.

TextArea

has one constructor that gives the
application discretion over scroll bars.

getPreferredSize

```java
public
Dimension
getPreferredSize​(int rows,
int columns)
```

Determines the preferred size of a text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the preferred dimensions required to display
the text area with the specified
number of rows and columns
**Since:** 1.1
**See Also:** Component.getPreferredSize()

---

#### getPreferredSize

public

Dimension

getPreferredSize​(int rows,
int columns)

Determines the preferred size of a text area with the specified
number of rows and columns.

preferredSize

```java
@Deprecated

public
Dimension
preferredSize​(int rows,
int columns)
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int, int)

.

Determines the preferred size of the text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the preferred dimensions needed for the text area

---

#### preferredSize

@Deprecated

public

Dimension

preferredSize​(int rows,
int columns)

Determines the preferred size of the text area with the specified
number of rows and columns.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Determines the preferred size of this text area.

**Overrides:** getPreferredSize

in class

Component
**Returns:** the preferred dimensions needed for this text area
**Since:** 1.1
**See Also:** Component.getPreferredSize()

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Determines the preferred size of this text area.

preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

---

#### preferredSize

@Deprecated

public

Dimension

preferredSize()

Description copied from class:

Component

Returns the component's preferred size.

getMinimumSize

```java
public
Dimension
getMinimumSize​(int rows,
int columns)
```

Determines the minimum size of a text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the minimum dimensions required to display
the text area with the specified
number of rows and columns
**Since:** 1.1
**See Also:** Component.getMinimumSize()

---

#### getMinimumSize

public

Dimension

getMinimumSize​(int rows,
int columns)

Determines the minimum size of a text area with the specified
number of rows and columns.

minimumSize

```java
@Deprecated

public
Dimension
minimumSize​(int rows,
int columns)
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int, int)

.

Determines the minimum size of the text area with the specified
number of rows and columns.

**Parameters:** rows

- the number of rows
**Parameters:** columns

- the number of columns
**Returns:** the minimum size for the text area

---

#### minimumSize

@Deprecated

public

Dimension

minimumSize​(int rows,
int columns)

Determines the minimum size of the text area with the specified
number of rows and columns.

getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Determines the minimum size of this text area.

**Overrides:** getMinimumSize

in class

Component
**Returns:** the preferred dimensions needed for this text area
**Since:** 1.1
**See Also:** Component.getPreferredSize()

---

#### getMinimumSize

public

Dimension

getMinimumSize()

Determines the minimum size of this text area.

minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

---

#### minimumSize

@Deprecated

public

Dimension

minimumSize()

Description copied from class:

Component

Returns the minimum size of this component.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

TextArea

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

TextComponent
**Returns:** the parameter string of this text area

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this

TextArea

.
This method is intended to be used only for debugging purposes, and the
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

Returns the

AccessibleContext

associated with
this

TextArea

. For text areas, the

AccessibleContext

takes the form of an

AccessibleAWTTextArea

.
A new

AccessibleAWTTextArea

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

TextComponent
**Returns:** an

AccessibleAWTTextArea

that serves as the

AccessibleContext

of this

TextArea
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Returns the

AccessibleContext

associated with
this

TextArea

. For text areas, the

AccessibleContext

takes the form of an

AccessibleAWTTextArea

.
A new

AccessibleAWTTextArea

instance is created if necessary.

---

