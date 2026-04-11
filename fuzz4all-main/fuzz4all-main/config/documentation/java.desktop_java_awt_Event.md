# Class Event

**Source:** `java.desktop\java\awt\Event.html`

### Class Description

```java
@Deprecated
(
since
="9")
public class
Event

extends
Object

implements
Serializable
```

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Event

is a platform-independent class that
encapsulates events from the platform's Graphical User
Interface in the Java 1.0 event model. In Java 1.1
and later versions, the

Event

class is maintained
only for backwards compatibility. The information in this
class description is provided to assist programmers in
converting Java 1.0 programs to the new event model.

In the Java 1.0 event model, an event contains an

id

field
that indicates what type of event it is and which other

Event

variables are relevant for the event.

For keyboard events,

key

contains a value indicating which key was activated, and

modifiers

contains the
modifiers for that event. For the KEY_PRESS and KEY_RELEASE
event ids, the value of

key

is the unicode
character code for the key. For KEY_ACTION and
KEY_ACTION_RELEASE, the value of

key

is
one of the defined action-key identifiers in the

Event

class (

PGUP

,

PGDN

,

F1

,

F2

, etc).

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int SHIFT_MASK

This flag indicates that the Shift key was down when the event
occurred.

**See Also:**
- Constant Field Values

---

#### public static final int CTRL_MASK

This flag indicates that the Control key was down when the event
occurred.

**See Also:**
- Constant Field Values

---

#### public static final int META_MASK

This flag indicates that the Meta key was down when the event
occurred. For mouse events, this flag indicates that the right
button was pressed or released.

**See Also:**
- Constant Field Values

---

#### public static final int ALT_MASK

This flag indicates that the Alt key was down when
the event occurred. For mouse events, this flag indicates that the
middle mouse button was pressed or released.

**See Also:**
- Constant Field Values

---

#### public static final int HOME

The Home key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int END

The End key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int PGUP

The Page Up key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int PGDN

The Page Down key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int UP

The Up Arrow key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int DOWN

The Down Arrow key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int LEFT

The Left Arrow key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int RIGHT

The Right Arrow key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F1

The F1 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F2

The F2 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F3

The F3 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F4

The F4 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F5

The F5 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F6

The F6 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F7

The F7 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F8

The F8 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F9

The F9 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F10

The F10 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F11

The F11 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int F12

The F12 function key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int PRINT_SCREEN

The Print Screen key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_LOCK

The Scroll Lock key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int CAPS_LOCK

The Caps Lock key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int NUM_LOCK

The Num Lock key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int PAUSE

The Pause key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int INSERT

The Insert key, a non-ASCII action key.

**See Also:**
- Constant Field Values

---

#### public static final int ENTER

The Enter key.

**See Also:**
- Constant Field Values

---

#### public static final int BACK_SPACE

The BackSpace key.

**See Also:**
- Constant Field Values

---

#### public static final int TAB

The Tab key.

**See Also:**
- Constant Field Values

---

#### public static final int ESCAPE

The Escape key.

**See Also:**
- Constant Field Values

---

#### public static final int DELETE

The Delete key.

**See Also:**
- Constant Field Values

---

#### public static final int WINDOW_DESTROY

The user has asked the window manager to kill the window.

**See Also:**
- Constant Field Values

---

#### public static final int WINDOW_EXPOSE

The user has asked the window manager to expose the window.

**See Also:**
- Constant Field Values

---

#### public static final int WINDOW_ICONIFY

The user has asked the window manager to iconify the window.

**See Also:**
- Constant Field Values

---

#### public static final int WINDOW_DEICONIFY

The user has asked the window manager to de-iconify the window.

**See Also:**
- Constant Field Values

---

#### public static final int WINDOW_MOVED

The user has asked the window manager to move the window.

**See Also:**
- Constant Field Values

---

#### public static final int KEY_PRESS

The user has pressed a normal key.

**See Also:**
- Constant Field Values

---

#### public static final int KEY_RELEASE

The user has released a normal key.

**See Also:**
- Constant Field Values

---

#### public static final int KEY_ACTION

The user has pressed a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:**
- Constant Field Values

---

#### public static final int KEY_ACTION_RELEASE

The user has released a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:**
- Constant Field Values

---

#### public static final int MOUSE_DOWN

The user has pressed the mouse button. The

ALT_MASK

flag indicates that the middle button has been pressed.
The

META_MASK

flag indicates that the
right button has been pressed.

**See Also:**
- ALT_MASK

,

META_MASK

,

Constant Field Values

---

#### public static final int MOUSE_UP

The user has released the mouse button. The

ALT_MASK

flag indicates that the middle button has been released.
The

META_MASK

flag indicates that the
right button has been released.

**See Also:**
- ALT_MASK

,

META_MASK

,

Constant Field Values

---

#### public static final int MOUSE_MOVE

The mouse has moved with no button pressed.

**See Also:**
- Constant Field Values

---

#### public static final int MOUSE_ENTER

The mouse has entered a component.

**See Also:**
- Constant Field Values

---

#### public static final int MOUSE_EXIT

The mouse has exited a component.

**See Also:**
- Constant Field Values

---

#### public static final int MOUSE_DRAG

The user has moved the mouse with a button pressed. The

ALT_MASK

flag indicates that the middle
button is being pressed. The

META_MASK

flag indicates
that the right button is being pressed.

**See Also:**
- ALT_MASK

,

META_MASK

,

Constant Field Values

---

#### public static final int SCROLL_LINE_UP

The user has activated the

line up

area of a scroll bar.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_LINE_DOWN

The user has activated the

line down

area of a scroll bar.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_PAGE_UP

The user has activated the

page up

area of a scroll bar.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_PAGE_DOWN

The user has activated the

page down

area of a scroll bar.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_ABSOLUTE

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_BEGIN

The scroll begin event.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_END

The scroll end event.

**See Also:**
- Constant Field Values

---

#### public static final int LIST_SELECT

An item in a list has been selected.

**See Also:**
- Constant Field Values

---

#### public static final int LIST_DESELECT

An item in a list has been deselected.

**See Also:**
- Constant Field Values

---

#### public static final int ACTION_EVENT

This event indicates that the user wants some action to occur.

**See Also:**
- Constant Field Values

---

#### public static final int LOAD_FILE

A file loading event.

**See Also:**
- Constant Field Values

---

#### public static final int SAVE_FILE

A file saving event.

**See Also:**
- Constant Field Values

---

#### public static final int GOT_FOCUS

A component gained the focus.

**See Also:**
- Constant Field Values

---

#### public static final int LOST_FOCUS

A component lost the focus.

**See Also:**
- Constant Field Values

---

#### public
Object
target

The target component. This indicates the component over which the
event occurred or with which the event is associated.
This object has been replaced by AWTEvent.getSource()

**See Also:**
- EventObject.getSource()

---

#### public long when

The time stamp.
Replaced by InputEvent.getWhen().

**See Also:**
- InputEvent.getWhen()

---

#### public int id

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.
This has been replaced by AWTEvent.getID()

**See Also:**
- AWTEvent.getID()

---

#### public int x

The

x

coordinate of the event.
Replaced by MouseEvent.getX()

**See Also:**
- MouseEvent.getX()

---

#### public int y

The

y

coordinate of the event.
Replaced by MouseEvent.getY()

**See Also:**
- MouseEvent.getY()

---

#### public int key

The key code of the key that was pressed in a keyboard event.
This has been replaced by KeyEvent.getKeyCode()

**See Also:**
- KeyEvent.getKeyCode()

---

#### public int modifiers

The state of the modifier keys.
This is replaced with InputEvent.getModifiers()
In java 1.1 MouseEvent and KeyEvent are subclasses
of InputEvent.

**See Also:**
- InputEvent.getModifiers()

---

#### public int clickCount

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks. For other events, its value is

0

.
This field has been replaced by MouseEvent.getClickCount().

**See Also:**
- MouseEvent.getClickCount()

---

#### public
Object
arg

An arbitrary argument of the event. The value of this field
depends on the type of event.

arg

has been replaced by event specific property.

---

#### public
Event
evt

The next event. This field is set when putting events into a
linked list.
This has been replaced by EventQueue.

**See Also:**
- EventQueue

---

### Constructor Details

#### public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers,

Object
arg)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and
argument.

**Parameters:**
- target

- the target component.
- when

- the time stamp.
- id

- the event type.
- x

- the

x

coordinate.
- y

- the

y

coordinate.
- key

- the key pressed in a keyboard event.
- modifiers

- the state of the modifier keys.
- arg

- the specified argument.

---

#### public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

, with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and an
argument set to

null

.

**Parameters:**
- target

- the target component.
- when

- the time stamp.
- id

- the event type.
- x

- the

x

coordinate.
- y

- the

y

coordinate.
- key

- the key pressed in a keyboard event.
- modifiers

- the state of the modifier keys.

---

#### public Event​(
Object
target,
int id,

Object
arg)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified
target component, event type, and argument.

**Parameters:**
- target

- the target component.
- id

- the event type.
- arg

- the specified argument.

---

### Method Details

#### public void translate​(int dx,
int dy)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Translates this event so that its

x

and

y

coordinates are increased by

dx

and

dy

,
respectively.

This method translates an event relative to the given component.
This involves, at a minimum, translating the coordinates into the
local coordinate system of the given component. It may also involve
translating a region in the case of an expose event.

**Parameters:**
- dx

- the distance to translate the

x

coordinate.
- dy

- the distance to translate the

y

coordinate.

---

#### public boolean shiftDown()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Shift key is down.

**Returns:**
- true

if the key is down;

false

otherwise.

**See Also:**
- modifiers

,

controlDown()

,

metaDown()

---

#### public boolean controlDown()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Control key is down.

**Returns:**
- true

if the key is down;

false

otherwise.

**See Also:**
- modifiers

,

shiftDown()

,

metaDown()

---

#### public boolean metaDown()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Meta key is down.

**Returns:**
- true

if the key is down;

false

otherwise.

**See Also:**
- modifiers

,

shiftDown()

,

controlDown()

---

#### protected
String
paramString()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a string representing the state of this

Event

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:**
- the parameter string of this event

---

#### public
String
toString()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a representation of this event's values as a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string that represents the event and the values
of its member fields.

**See Also:**
- paramString()

**Since:**
- 1.1

---

### Additional Sections

#### Class Event

java.lang.Object

- java.awt.Event

java.awt.Event

**All Implemented Interfaces:** Serializable

```java
@Deprecated
(
since
="9")
public class
Event

extends
Object

implements
Serializable
```

Deprecated.

It is recommended that

AWTEvent

and its subclasses be
used instead

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Event

is a platform-independent class that
encapsulates events from the platform's Graphical User
Interface in the Java 1.0 event model. In Java 1.1
and later versions, the

Event

class is maintained
only for backwards compatibility. The information in this
class description is provided to assist programmers in
converting Java 1.0 programs to the new event model.

In the Java 1.0 event model, an event contains an

id

field
that indicates what type of event it is and which other

Event

variables are relevant for the event.

For keyboard events,

key

contains a value indicating which key was activated, and

modifiers

contains the
modifiers for that event. For the KEY_PRESS and KEY_RELEASE
event ids, the value of

key

is the unicode
character code for the key. For KEY_ACTION and
KEY_ACTION_RELEASE, the value of

key

is
one of the defined action-key identifiers in the

Event

class (

PGUP

,

PGDN

,

F1

,

F2

, etc).

**Since:** 1.0
**See Also:** Serialized Form

@Deprecated

(

since

="9")
public class

Event

extends

Object

implements

Serializable

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Event

is a platform-independent class that
encapsulates events from the platform's Graphical User
Interface in the Java 1.0 event model. In Java 1.1
and later versions, the

Event

class is maintained
only for backwards compatibility. The information in this
class description is provided to assist programmers in
converting Java 1.0 programs to the new event model.

In the Java 1.0 event model, an event contains an

id

field
that indicates what type of event it is and which other

Event

variables are relevant for the event.

For keyboard events,

key

contains a value indicating which key was activated, and

modifiers

contains the
modifiers for that event. For the KEY_PRESS and KEY_RELEASE
event ids, the value of

key

is the unicode
character code for the key. For KEY_ACTION and
KEY_ACTION_RELEASE, the value of

key

is
one of the defined action-key identifiers in the

Event

class (

PGUP

,

PGDN

,

F1

,

F2

, etc).

Event

is a platform-independent class that
encapsulates events from the platform's Graphical User
Interface in the Java 1.0 event model. In Java 1.1
and later versions, the

Event

class is maintained
only for backwards compatibility. The information in this
class description is provided to assist programmers in
converting Java 1.0 programs to the new event model.

In the Java 1.0 event model, an event contains an

id

field
that indicates what type of event it is and which other

Event

variables are relevant for the event.

For keyboard events,

key

contains a value indicating which key was activated, and

modifiers

contains the
modifiers for that event. For the KEY_PRESS and KEY_RELEASE
event ids, the value of

key

is the unicode
character code for the key. For KEY_ACTION and
KEY_ACTION_RELEASE, the value of

key

is
one of the defined action-key identifiers in the

Event

class (

PGUP

,

PGDN

,

F1

,

F2

, etc).

In the Java 1.0 event model, an event contains an

id

field
that indicates what type of event it is and which other

Event

variables are relevant for the event.

For keyboard events,

key

contains a value indicating which key was activated, and

modifiers

contains the
modifiers for that event. For the KEY_PRESS and KEY_RELEASE
event ids, the value of

key

is the unicode
character code for the key. For KEY_ACTION and
KEY_ACTION_RELEASE, the value of

key

is
one of the defined action-key identifiers in the

Event

class (

PGUP

,

PGDN

,

F1

,

F2

, etc).

For keyboard events,

key

contains a value indicating which key was activated, and

modifiers

contains the
modifiers for that event. For the KEY_PRESS and KEY_RELEASE
event ids, the value of

key

is the unicode
character code for the key. For KEY_ACTION and
KEY_ACTION_RELEASE, the value of

key

is
one of the defined action-key identifiers in the

Event

class (

PGUP

,

PGDN

,

F1

,

F2

, etc).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTION_EVENT

Deprecated.

This event indicates that the user wants some action to occur.

static int

ALT_MASK

Deprecated.

This flag indicates that the Alt key was down when
the event occurred.

Object

arg

Deprecated.

An arbitrary argument of the event.

static int

BACK_SPACE

Deprecated.

The BackSpace key.

static int

CAPS_LOCK

Deprecated.

The Caps Lock key, a non-ASCII action key.

int

clickCount

Deprecated.

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks.

static int

CTRL_MASK

Deprecated.

This flag indicates that the Control key was down when the event
occurred.

static int

DELETE

Deprecated.

The Delete key.

static int

DOWN

Deprecated.

The Down Arrow key, a non-ASCII action key.

static int

END

Deprecated.

The End key, a non-ASCII action key.

static int

ENTER

Deprecated.

The Enter key.

static int

ESCAPE

Deprecated.

The Escape key.

Event

evt

Deprecated.

The next event.

static int

F1

Deprecated.

The F1 function key, a non-ASCII action key.

static int

F10

Deprecated.

The F10 function key, a non-ASCII action key.

static int

F11

Deprecated.

The F11 function key, a non-ASCII action key.

static int

F12

Deprecated.

The F12 function key, a non-ASCII action key.

static int

F2

Deprecated.

The F2 function key, a non-ASCII action key.

static int

F3

Deprecated.

The F3 function key, a non-ASCII action key.

static int

F4

Deprecated.

The F4 function key, a non-ASCII action key.

static int

F5

Deprecated.

The F5 function key, a non-ASCII action key.

static int

F6

Deprecated.

The F6 function key, a non-ASCII action key.

static int

F7

Deprecated.

The F7 function key, a non-ASCII action key.

static int

F8

Deprecated.

The F8 function key, a non-ASCII action key.

static int

F9

Deprecated.

The F9 function key, a non-ASCII action key.

static int

GOT_FOCUS

Deprecated.

A component gained the focus.

static int

HOME

Deprecated.

The Home key, a non-ASCII action key.

int

id

Deprecated.

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.

static int

INSERT

Deprecated.

The Insert key, a non-ASCII action key.

int

key

Deprecated.

The key code of the key that was pressed in a keyboard event.

static int

KEY_ACTION

Deprecated.

The user has pressed a non-ASCII

action

key.

static int

KEY_ACTION_RELEASE

Deprecated.

The user has released a non-ASCII

action

key.

static int

KEY_PRESS

Deprecated.

The user has pressed a normal key.

static int

KEY_RELEASE

Deprecated.

The user has released a normal key.

static int

LEFT

Deprecated.

The Left Arrow key, a non-ASCII action key.

static int

LIST_DESELECT

Deprecated.

An item in a list has been deselected.

static int

LIST_SELECT

Deprecated.

An item in a list has been selected.

static int

LOAD_FILE

Deprecated.

A file loading event.

static int

LOST_FOCUS

Deprecated.

A component lost the focus.

static int

META_MASK

Deprecated.

This flag indicates that the Meta key was down when the event
occurred.

int

modifiers

Deprecated.

The state of the modifier keys.

static int

MOUSE_DOWN

Deprecated.

The user has pressed the mouse button.

static int

MOUSE_DRAG

Deprecated.

The user has moved the mouse with a button pressed.

static int

MOUSE_ENTER

Deprecated.

The mouse has entered a component.

static int

MOUSE_EXIT

Deprecated.

The mouse has exited a component.

static int

MOUSE_MOVE

Deprecated.

The mouse has moved with no button pressed.

static int

MOUSE_UP

Deprecated.

The user has released the mouse button.

static int

NUM_LOCK

Deprecated.

The Num Lock key, a non-ASCII action key.

static int

PAUSE

Deprecated.

The Pause key, a non-ASCII action key.

static int

PGDN

Deprecated.

The Page Down key, a non-ASCII action key.

static int

PGUP

Deprecated.

The Page Up key, a non-ASCII action key.

static int

PRINT_SCREEN

Deprecated.

The Print Screen key, a non-ASCII action key.

static int

RIGHT

Deprecated.

The Right Arrow key, a non-ASCII action key.

static int

SAVE_FILE

Deprecated.

A file saving event.

static int

SCROLL_ABSOLUTE

Deprecated.

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

static int

SCROLL_BEGIN

Deprecated.

The scroll begin event.

static int

SCROLL_END

Deprecated.

The scroll end event.

static int

SCROLL_LINE_DOWN

Deprecated.

The user has activated the

line down

area of a scroll bar.

static int

SCROLL_LINE_UP

Deprecated.

The user has activated the

line up

area of a scroll bar.

static int

SCROLL_LOCK

Deprecated.

The Scroll Lock key, a non-ASCII action key.

static int

SCROLL_PAGE_DOWN

Deprecated.

The user has activated the

page down

area of a scroll bar.

static int

SCROLL_PAGE_UP

Deprecated.

The user has activated the

page up

area of a scroll bar.

static int

SHIFT_MASK

Deprecated.

This flag indicates that the Shift key was down when the event
occurred.

static int

TAB

Deprecated.

The Tab key.

Object

target

Deprecated.

The target component.

static int

UP

Deprecated.

The Up Arrow key, a non-ASCII action key.

long

when

Deprecated.

The time stamp.

static int

WINDOW_DEICONIFY

Deprecated.

The user has asked the window manager to de-iconify the window.

static int

WINDOW_DESTROY

Deprecated.

The user has asked the window manager to kill the window.

static int

WINDOW_EXPOSE

Deprecated.

The user has asked the window manager to expose the window.

static int

WINDOW_ICONIFY

Deprecated.

The user has asked the window manager to iconify the window.

static int

WINDOW_MOVED

Deprecated.

The user has asked the window manager to move the window.

int

x

Deprecated.

The

x

coordinate of the event.

int

y

Deprecated.

The

y

coordinate of the event.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Event

​(

Object

target,
int id,

Object

arg)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

Event

​(

Object

target,
long when,
int id,
int x,
int y,
int key,
int modifiers)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

Event

​(

Object

target,
long when,
int id,
int x,
int y,
int key,
int modifiers,

Object

arg)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

controlDown

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

boolean

metaDown

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

protected

String

paramString

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

boolean

shiftDown

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

String

toString

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

void

translate

​(int dx,
int dy)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTION_EVENT

Deprecated.

This event indicates that the user wants some action to occur.

static int

ALT_MASK

Deprecated.

This flag indicates that the Alt key was down when
the event occurred.

Object

arg

Deprecated.

An arbitrary argument of the event.

static int

BACK_SPACE

Deprecated.

The BackSpace key.

static int

CAPS_LOCK

Deprecated.

The Caps Lock key, a non-ASCII action key.

int

clickCount

Deprecated.

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks.

static int

CTRL_MASK

Deprecated.

This flag indicates that the Control key was down when the event
occurred.

static int

DELETE

Deprecated.

The Delete key.

static int

DOWN

Deprecated.

The Down Arrow key, a non-ASCII action key.

static int

END

Deprecated.

The End key, a non-ASCII action key.

static int

ENTER

Deprecated.

The Enter key.

static int

ESCAPE

Deprecated.

The Escape key.

Event

evt

Deprecated.

The next event.

static int

F1

Deprecated.

The F1 function key, a non-ASCII action key.

static int

F10

Deprecated.

The F10 function key, a non-ASCII action key.

static int

F11

Deprecated.

The F11 function key, a non-ASCII action key.

static int

F12

Deprecated.

The F12 function key, a non-ASCII action key.

static int

F2

Deprecated.

The F2 function key, a non-ASCII action key.

static int

F3

Deprecated.

The F3 function key, a non-ASCII action key.

static int

F4

Deprecated.

The F4 function key, a non-ASCII action key.

static int

F5

Deprecated.

The F5 function key, a non-ASCII action key.

static int

F6

Deprecated.

The F6 function key, a non-ASCII action key.

static int

F7

Deprecated.

The F7 function key, a non-ASCII action key.

static int

F8

Deprecated.

The F8 function key, a non-ASCII action key.

static int

F9

Deprecated.

The F9 function key, a non-ASCII action key.

static int

GOT_FOCUS

Deprecated.

A component gained the focus.

static int

HOME

Deprecated.

The Home key, a non-ASCII action key.

int

id

Deprecated.

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.

static int

INSERT

Deprecated.

The Insert key, a non-ASCII action key.

int

key

Deprecated.

The key code of the key that was pressed in a keyboard event.

static int

KEY_ACTION

Deprecated.

The user has pressed a non-ASCII

action

key.

static int

KEY_ACTION_RELEASE

Deprecated.

The user has released a non-ASCII

action

key.

static int

KEY_PRESS

Deprecated.

The user has pressed a normal key.

static int

KEY_RELEASE

Deprecated.

The user has released a normal key.

static int

LEFT

Deprecated.

The Left Arrow key, a non-ASCII action key.

static int

LIST_DESELECT

Deprecated.

An item in a list has been deselected.

static int

LIST_SELECT

Deprecated.

An item in a list has been selected.

static int

LOAD_FILE

Deprecated.

A file loading event.

static int

LOST_FOCUS

Deprecated.

A component lost the focus.

static int

META_MASK

Deprecated.

This flag indicates that the Meta key was down when the event
occurred.

int

modifiers

Deprecated.

The state of the modifier keys.

static int

MOUSE_DOWN

Deprecated.

The user has pressed the mouse button.

static int

MOUSE_DRAG

Deprecated.

The user has moved the mouse with a button pressed.

static int

MOUSE_ENTER

Deprecated.

The mouse has entered a component.

static int

MOUSE_EXIT

Deprecated.

The mouse has exited a component.

static int

MOUSE_MOVE

Deprecated.

The mouse has moved with no button pressed.

static int

MOUSE_UP

Deprecated.

The user has released the mouse button.

static int

NUM_LOCK

Deprecated.

The Num Lock key, a non-ASCII action key.

static int

PAUSE

Deprecated.

The Pause key, a non-ASCII action key.

static int

PGDN

Deprecated.

The Page Down key, a non-ASCII action key.

static int

PGUP

Deprecated.

The Page Up key, a non-ASCII action key.

static int

PRINT_SCREEN

Deprecated.

The Print Screen key, a non-ASCII action key.

static int

RIGHT

Deprecated.

The Right Arrow key, a non-ASCII action key.

static int

SAVE_FILE

Deprecated.

A file saving event.

static int

SCROLL_ABSOLUTE

Deprecated.

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

static int

SCROLL_BEGIN

Deprecated.

The scroll begin event.

static int

SCROLL_END

Deprecated.

The scroll end event.

static int

SCROLL_LINE_DOWN

Deprecated.

The user has activated the

line down

area of a scroll bar.

static int

SCROLL_LINE_UP

Deprecated.

The user has activated the

line up

area of a scroll bar.

static int

SCROLL_LOCK

Deprecated.

The Scroll Lock key, a non-ASCII action key.

static int

SCROLL_PAGE_DOWN

Deprecated.

The user has activated the

page down

area of a scroll bar.

static int

SCROLL_PAGE_UP

Deprecated.

The user has activated the

page up

area of a scroll bar.

static int

SHIFT_MASK

Deprecated.

This flag indicates that the Shift key was down when the event
occurred.

static int

TAB

Deprecated.

The Tab key.

Object

target

Deprecated.

The target component.

static int

UP

Deprecated.

The Up Arrow key, a non-ASCII action key.

long

when

Deprecated.

The time stamp.

static int

WINDOW_DEICONIFY

Deprecated.

The user has asked the window manager to de-iconify the window.

static int

WINDOW_DESTROY

Deprecated.

The user has asked the window manager to kill the window.

static int

WINDOW_EXPOSE

Deprecated.

The user has asked the window manager to expose the window.

static int

WINDOW_ICONIFY

Deprecated.

The user has asked the window manager to iconify the window.

static int

WINDOW_MOVED

Deprecated.

The user has asked the window manager to move the window.

int

x

Deprecated.

The

x

coordinate of the event.

int

y

Deprecated.

The

y

coordinate of the event.

---

#### Field Summary

Deprecated.

This event indicates that the user wants some action to occur.

This flag indicates that the Alt key was down when
the event occurred.

An arbitrary argument of the event.

The BackSpace key.

The Caps Lock key, a non-ASCII action key.

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks.

This flag indicates that the Control key was down when the event
occurred.

The Delete key.

The Down Arrow key, a non-ASCII action key.

The End key, a non-ASCII action key.

The Enter key.

The Escape key.

The next event.

The F1 function key, a non-ASCII action key.

The F10 function key, a non-ASCII action key.

The F11 function key, a non-ASCII action key.

The F12 function key, a non-ASCII action key.

The F2 function key, a non-ASCII action key.

The F3 function key, a non-ASCII action key.

The F4 function key, a non-ASCII action key.

The F5 function key, a non-ASCII action key.

The F6 function key, a non-ASCII action key.

The F7 function key, a non-ASCII action key.

The F8 function key, a non-ASCII action key.

The F9 function key, a non-ASCII action key.

A component gained the focus.

The Home key, a non-ASCII action key.

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.

The Insert key, a non-ASCII action key.

The key code of the key that was pressed in a keyboard event.

The user has pressed a non-ASCII

action

key.

The user has released a non-ASCII

action

key.

The user has pressed a normal key.

The user has released a normal key.

The Left Arrow key, a non-ASCII action key.

An item in a list has been deselected.

An item in a list has been selected.

A file loading event.

A component lost the focus.

This flag indicates that the Meta key was down when the event
occurred.

The state of the modifier keys.

The user has pressed the mouse button.

The user has moved the mouse with a button pressed.

The mouse has entered a component.

The mouse has exited a component.

The mouse has moved with no button pressed.

The user has released the mouse button.

The Num Lock key, a non-ASCII action key.

The Pause key, a non-ASCII action key.

The Page Down key, a non-ASCII action key.

The Page Up key, a non-ASCII action key.

The Print Screen key, a non-ASCII action key.

The Right Arrow key, a non-ASCII action key.

A file saving event.

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

The scroll begin event.

The scroll end event.

The user has activated the

line down

area of a scroll bar.

The user has activated the

line up

area of a scroll bar.

The Scroll Lock key, a non-ASCII action key.

The user has activated the

page down

area of a scroll bar.

The user has activated the

page up

area of a scroll bar.

This flag indicates that the Shift key was down when the event
occurred.

The Tab key.

The target component.

The Up Arrow key, a non-ASCII action key.

The time stamp.

The user has asked the window manager to de-iconify the window.

The user has asked the window manager to kill the window.

The user has asked the window manager to expose the window.

The user has asked the window manager to iconify the window.

The user has asked the window manager to move the window.

The

x

coordinate of the event.

The

y

coordinate of the event.

Constructor Summary

Constructors

Constructor

Description

Event

​(

Object

target,
int id,

Object

arg)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

Event

​(

Object

target,
long when,
int id,
int x,
int y,
int key,
int modifiers)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

Event

​(

Object

target,
long when,
int id,
int x,
int y,
int key,
int modifiers,

Object

arg)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

---

#### Constructor Summary

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

controlDown

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

boolean

metaDown

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

protected

String

paramString

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

boolean

shiftDown

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

String

toString

()

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

void

translate

​(int dx,
int dy)

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

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

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility.

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

- SHIFT_MASK

```java
public static final int SHIFT_MASK
```

Deprecated.

This flag indicates that the Shift key was down when the event
occurred.

**See Also:** Constant Field Values

- CTRL_MASK

```java
public static final int CTRL_MASK
```

Deprecated.

This flag indicates that the Control key was down when the event
occurred.

**See Also:** Constant Field Values

- META_MASK

```java
public static final int META_MASK
```

Deprecated.

This flag indicates that the Meta key was down when the event
occurred. For mouse events, this flag indicates that the right
button was pressed or released.

**See Also:** Constant Field Values

- ALT_MASK

```java
public static final int ALT_MASK
```

Deprecated.

This flag indicates that the Alt key was down when
the event occurred. For mouse events, this flag indicates that the
middle mouse button was pressed or released.

**See Also:** Constant Field Values

- HOME

```java
public static final int HOME
```

Deprecated.

The Home key, a non-ASCII action key.

**See Also:** Constant Field Values

- END

```java
public static final int END
```

Deprecated.

The End key, a non-ASCII action key.

**See Also:** Constant Field Values

- PGUP

```java
public static final int PGUP
```

Deprecated.

The Page Up key, a non-ASCII action key.

**See Also:** Constant Field Values

- PGDN

```java
public static final int PGDN
```

Deprecated.

The Page Down key, a non-ASCII action key.

**See Also:** Constant Field Values

- UP

```java
public static final int UP
```

Deprecated.

The Up Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- DOWN

```java
public static final int DOWN
```

Deprecated.

The Down Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- LEFT

```java
public static final int LEFT
```

Deprecated.

The Left Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- RIGHT

```java
public static final int RIGHT
```

Deprecated.

The Right Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- F1

```java
public static final int F1
```

Deprecated.

The F1 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F2

```java
public static final int F2
```

Deprecated.

The F2 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F3

```java
public static final int F3
```

Deprecated.

The F3 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F4

```java
public static final int F4
```

Deprecated.

The F4 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F5

```java
public static final int F5
```

Deprecated.

The F5 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F6

```java
public static final int F6
```

Deprecated.

The F6 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F7

```java
public static final int F7
```

Deprecated.

The F7 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F8

```java
public static final int F8
```

Deprecated.

The F8 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F9

```java
public static final int F9
```

Deprecated.

The F9 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F10

```java
public static final int F10
```

Deprecated.

The F10 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F11

```java
public static final int F11
```

Deprecated.

The F11 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F12

```java
public static final int F12
```

Deprecated.

The F12 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- PRINT_SCREEN

```java
public static final int PRINT_SCREEN
```

Deprecated.

The Print Screen key, a non-ASCII action key.

**See Also:** Constant Field Values

- SCROLL_LOCK

```java
public static final int SCROLL_LOCK
```

Deprecated.

The Scroll Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

- CAPS_LOCK

```java
public static final int CAPS_LOCK
```

Deprecated.

The Caps Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

- NUM_LOCK

```java
public static final int NUM_LOCK
```

Deprecated.

The Num Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

- PAUSE

```java
public static final int PAUSE
```

Deprecated.

The Pause key, a non-ASCII action key.

**See Also:** Constant Field Values

- INSERT

```java
public static final int INSERT
```

Deprecated.

The Insert key, a non-ASCII action key.

**See Also:** Constant Field Values

- ENTER

```java
public static final int ENTER
```

Deprecated.

The Enter key.

**See Also:** Constant Field Values

- BACK_SPACE

```java
public static final int BACK_SPACE
```

Deprecated.

The BackSpace key.

**See Also:** Constant Field Values

- TAB

```java
public static final int TAB
```

Deprecated.

The Tab key.

**See Also:** Constant Field Values

- ESCAPE

```java
public static final int ESCAPE
```

Deprecated.

The Escape key.

**See Also:** Constant Field Values

- DELETE

```java
public static final int DELETE
```

Deprecated.

The Delete key.

**See Also:** Constant Field Values

- WINDOW_DESTROY

```java
public static final int WINDOW_DESTROY
```

Deprecated.

The user has asked the window manager to kill the window.

**See Also:** Constant Field Values

- WINDOW_EXPOSE

```java
public static final int WINDOW_EXPOSE
```

Deprecated.

The user has asked the window manager to expose the window.

**See Also:** Constant Field Values

- WINDOW_ICONIFY

```java
public static final int WINDOW_ICONIFY
```

Deprecated.

The user has asked the window manager to iconify the window.

**See Also:** Constant Field Values

- WINDOW_DEICONIFY

```java
public static final int WINDOW_DEICONIFY
```

Deprecated.

The user has asked the window manager to de-iconify the window.

**See Also:** Constant Field Values

- WINDOW_MOVED

```java
public static final int WINDOW_MOVED
```

Deprecated.

The user has asked the window manager to move the window.

**See Also:** Constant Field Values

- KEY_PRESS

```java
public static final int KEY_PRESS
```

Deprecated.

The user has pressed a normal key.

**See Also:** Constant Field Values

- KEY_RELEASE

```java
public static final int KEY_RELEASE
```

Deprecated.

The user has released a normal key.

**See Also:** Constant Field Values

- KEY_ACTION

```java
public static final int KEY_ACTION
```

Deprecated.

The user has pressed a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:** Constant Field Values

- KEY_ACTION_RELEASE

```java
public static final int KEY_ACTION_RELEASE
```

Deprecated.

The user has released a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:** Constant Field Values

- MOUSE_DOWN

```java
public static final int MOUSE_DOWN
```

Deprecated.

The user has pressed the mouse button. The

ALT_MASK

flag indicates that the middle button has been pressed.
The

META_MASK

flag indicates that the
right button has been pressed.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

- MOUSE_UP

```java
public static final int MOUSE_UP
```

Deprecated.

The user has released the mouse button. The

ALT_MASK

flag indicates that the middle button has been released.
The

META_MASK

flag indicates that the
right button has been released.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

- MOUSE_MOVE

```java
public static final int MOUSE_MOVE
```

Deprecated.

The mouse has moved with no button pressed.

**See Also:** Constant Field Values

- MOUSE_ENTER

```java
public static final int MOUSE_ENTER
```

Deprecated.

The mouse has entered a component.

**See Also:** Constant Field Values

- MOUSE_EXIT

```java
public static final int MOUSE_EXIT
```

Deprecated.

The mouse has exited a component.

**See Also:** Constant Field Values

- MOUSE_DRAG

```java
public static final int MOUSE_DRAG
```

Deprecated.

The user has moved the mouse with a button pressed. The

ALT_MASK

flag indicates that the middle
button is being pressed. The

META_MASK

flag indicates
that the right button is being pressed.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

- SCROLL_LINE_UP

```java
public static final int SCROLL_LINE_UP
```

Deprecated.

The user has activated the

line up

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_LINE_DOWN

```java
public static final int SCROLL_LINE_DOWN
```

Deprecated.

The user has activated the

line down

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_PAGE_UP

```java
public static final int SCROLL_PAGE_UP
```

Deprecated.

The user has activated the

page up

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_PAGE_DOWN

```java
public static final int SCROLL_PAGE_DOWN
```

Deprecated.

The user has activated the

page down

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_ABSOLUTE

```java
public static final int SCROLL_ABSOLUTE
```

Deprecated.

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

**See Also:** Constant Field Values

- SCROLL_BEGIN

```java
public static final int SCROLL_BEGIN
```

Deprecated.

The scroll begin event.

**See Also:** Constant Field Values

- SCROLL_END

```java
public static final int SCROLL_END
```

Deprecated.

The scroll end event.

**See Also:** Constant Field Values

- LIST_SELECT

```java
public static final int LIST_SELECT
```

Deprecated.

An item in a list has been selected.

**See Also:** Constant Field Values

- LIST_DESELECT

```java
public static final int LIST_DESELECT
```

Deprecated.

An item in a list has been deselected.

**See Also:** Constant Field Values

- ACTION_EVENT

```java
public static final int ACTION_EVENT
```

Deprecated.

This event indicates that the user wants some action to occur.

**See Also:** Constant Field Values

- LOAD_FILE

```java
public static final int LOAD_FILE
```

Deprecated.

A file loading event.

**See Also:** Constant Field Values

- SAVE_FILE

```java
public static final int SAVE_FILE
```

Deprecated.

A file saving event.

**See Also:** Constant Field Values

- GOT_FOCUS

```java
public static final int GOT_FOCUS
```

Deprecated.

A component gained the focus.

**See Also:** Constant Field Values

- LOST_FOCUS

```java
public static final int LOST_FOCUS
```

Deprecated.

A component lost the focus.

**See Also:** Constant Field Values

- target

```java
public
Object
target
```

Deprecated.

The target component. This indicates the component over which the
event occurred or with which the event is associated.
This object has been replaced by AWTEvent.getSource()

**See Also:** EventObject.getSource()

- when

```java
public long when
```

Deprecated.

The time stamp.
Replaced by InputEvent.getWhen().

**See Also:** InputEvent.getWhen()

- id

```java
public int id
```

Deprecated.

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.
This has been replaced by AWTEvent.getID()

**See Also:** AWTEvent.getID()

- x

```java
public int x
```

Deprecated.

The

x

coordinate of the event.
Replaced by MouseEvent.getX()

**See Also:** MouseEvent.getX()

- y

```java
public int y
```

Deprecated.

The

y

coordinate of the event.
Replaced by MouseEvent.getY()

**See Also:** MouseEvent.getY()

- key

```java
public int key
```

Deprecated.

The key code of the key that was pressed in a keyboard event.
This has been replaced by KeyEvent.getKeyCode()

**See Also:** KeyEvent.getKeyCode()

- modifiers

```java
public int modifiers
```

Deprecated.

The state of the modifier keys.
This is replaced with InputEvent.getModifiers()
In java 1.1 MouseEvent and KeyEvent are subclasses
of InputEvent.

**See Also:** InputEvent.getModifiers()

- clickCount

```java
public int clickCount
```

Deprecated.

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks. For other events, its value is

0

.
This field has been replaced by MouseEvent.getClickCount().

**See Also:** MouseEvent.getClickCount()

- arg

```java
public
Object
arg
```

Deprecated.

An arbitrary argument of the event. The value of this field
depends on the type of event.

arg

has been replaced by event specific property.

- evt

```java
public
Event
evt
```

Deprecated.

The next event. This field is set when putting events into a
linked list.
This has been replaced by EventQueue.

**See Also:** EventQueue

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Event

```java
public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers,

Object
arg)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and
argument.

**Parameters:** target

- the target component.
**Parameters:** when

- the time stamp.
**Parameters:** id

- the event type.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** key

- the key pressed in a keyboard event.
**Parameters:** modifiers

- the state of the modifier keys.
**Parameters:** arg

- the specified argument.

- Event

```java
public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

, with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and an
argument set to

null

.

**Parameters:** target

- the target component.
**Parameters:** when

- the time stamp.
**Parameters:** id

- the event type.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** key

- the key pressed in a keyboard event.
**Parameters:** modifiers

- the state of the modifier keys.

- Event

```java
public Event​(
Object
target,
int id,

Object
arg)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified
target component, event type, and argument.

**Parameters:** target

- the target component.
**Parameters:** id

- the event type.
**Parameters:** arg

- the specified argument.

============ METHOD DETAIL ==========

- Method Detail

- translate

```java
public void translate​(int dx,
int dy)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Translates this event so that its

x

and

y

coordinates are increased by

dx

and

dy

,
respectively.

This method translates an event relative to the given component.
This involves, at a minimum, translating the coordinates into the
local coordinate system of the given component. It may also involve
translating a region in the case of an expose event.

**Parameters:** dx

- the distance to translate the

x

coordinate.
**Parameters:** dy

- the distance to translate the

y

coordinate.

- shiftDown

```java
public boolean shiftDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Shift key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

controlDown()

,

metaDown()

- controlDown

```java
public boolean controlDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Control key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

shiftDown()

,

metaDown()

- metaDown

```java
public boolean metaDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Meta key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

shiftDown()

,

controlDown()

- paramString

```java
protected
String
paramString()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a string representing the state of this

Event

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:** the parameter string of this event

- toString

```java
public
String
toString()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a representation of this event's values as a string.

**Overrides:** toString

in class

Object
**Returns:** a string that represents the event and the values
of its member fields.
**Since:** 1.1
**See Also:** paramString()

Field Detail

- SHIFT_MASK

```java
public static final int SHIFT_MASK
```

Deprecated.

This flag indicates that the Shift key was down when the event
occurred.

**See Also:** Constant Field Values

- CTRL_MASK

```java
public static final int CTRL_MASK
```

Deprecated.

This flag indicates that the Control key was down when the event
occurred.

**See Also:** Constant Field Values

- META_MASK

```java
public static final int META_MASK
```

Deprecated.

This flag indicates that the Meta key was down when the event
occurred. For mouse events, this flag indicates that the right
button was pressed or released.

**See Also:** Constant Field Values

- ALT_MASK

```java
public static final int ALT_MASK
```

Deprecated.

This flag indicates that the Alt key was down when
the event occurred. For mouse events, this flag indicates that the
middle mouse button was pressed or released.

**See Also:** Constant Field Values

- HOME

```java
public static final int HOME
```

Deprecated.

The Home key, a non-ASCII action key.

**See Also:** Constant Field Values

- END

```java
public static final int END
```

Deprecated.

The End key, a non-ASCII action key.

**See Also:** Constant Field Values

- PGUP

```java
public static final int PGUP
```

Deprecated.

The Page Up key, a non-ASCII action key.

**See Also:** Constant Field Values

- PGDN

```java
public static final int PGDN
```

Deprecated.

The Page Down key, a non-ASCII action key.

**See Also:** Constant Field Values

- UP

```java
public static final int UP
```

Deprecated.

The Up Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- DOWN

```java
public static final int DOWN
```

Deprecated.

The Down Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- LEFT

```java
public static final int LEFT
```

Deprecated.

The Left Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- RIGHT

```java
public static final int RIGHT
```

Deprecated.

The Right Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

- F1

```java
public static final int F1
```

Deprecated.

The F1 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F2

```java
public static final int F2
```

Deprecated.

The F2 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F3

```java
public static final int F3
```

Deprecated.

The F3 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F4

```java
public static final int F4
```

Deprecated.

The F4 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F5

```java
public static final int F5
```

Deprecated.

The F5 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F6

```java
public static final int F6
```

Deprecated.

The F6 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F7

```java
public static final int F7
```

Deprecated.

The F7 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F8

```java
public static final int F8
```

Deprecated.

The F8 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F9

```java
public static final int F9
```

Deprecated.

The F9 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F10

```java
public static final int F10
```

Deprecated.

The F10 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F11

```java
public static final int F11
```

Deprecated.

The F11 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- F12

```java
public static final int F12
```

Deprecated.

The F12 function key, a non-ASCII action key.

**See Also:** Constant Field Values

- PRINT_SCREEN

```java
public static final int PRINT_SCREEN
```

Deprecated.

The Print Screen key, a non-ASCII action key.

**See Also:** Constant Field Values

- SCROLL_LOCK

```java
public static final int SCROLL_LOCK
```

Deprecated.

The Scroll Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

- CAPS_LOCK

```java
public static final int CAPS_LOCK
```

Deprecated.

The Caps Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

- NUM_LOCK

```java
public static final int NUM_LOCK
```

Deprecated.

The Num Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

- PAUSE

```java
public static final int PAUSE
```

Deprecated.

The Pause key, a non-ASCII action key.

**See Also:** Constant Field Values

- INSERT

```java
public static final int INSERT
```

Deprecated.

The Insert key, a non-ASCII action key.

**See Also:** Constant Field Values

- ENTER

```java
public static final int ENTER
```

Deprecated.

The Enter key.

**See Also:** Constant Field Values

- BACK_SPACE

```java
public static final int BACK_SPACE
```

Deprecated.

The BackSpace key.

**See Also:** Constant Field Values

- TAB

```java
public static final int TAB
```

Deprecated.

The Tab key.

**See Also:** Constant Field Values

- ESCAPE

```java
public static final int ESCAPE
```

Deprecated.

The Escape key.

**See Also:** Constant Field Values

- DELETE

```java
public static final int DELETE
```

Deprecated.

The Delete key.

**See Also:** Constant Field Values

- WINDOW_DESTROY

```java
public static final int WINDOW_DESTROY
```

Deprecated.

The user has asked the window manager to kill the window.

**See Also:** Constant Field Values

- WINDOW_EXPOSE

```java
public static final int WINDOW_EXPOSE
```

Deprecated.

The user has asked the window manager to expose the window.

**See Also:** Constant Field Values

- WINDOW_ICONIFY

```java
public static final int WINDOW_ICONIFY
```

Deprecated.

The user has asked the window manager to iconify the window.

**See Also:** Constant Field Values

- WINDOW_DEICONIFY

```java
public static final int WINDOW_DEICONIFY
```

Deprecated.

The user has asked the window manager to de-iconify the window.

**See Also:** Constant Field Values

- WINDOW_MOVED

```java
public static final int WINDOW_MOVED
```

Deprecated.

The user has asked the window manager to move the window.

**See Also:** Constant Field Values

- KEY_PRESS

```java
public static final int KEY_PRESS
```

Deprecated.

The user has pressed a normal key.

**See Also:** Constant Field Values

- KEY_RELEASE

```java
public static final int KEY_RELEASE
```

Deprecated.

The user has released a normal key.

**See Also:** Constant Field Values

- KEY_ACTION

```java
public static final int KEY_ACTION
```

Deprecated.

The user has pressed a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:** Constant Field Values

- KEY_ACTION_RELEASE

```java
public static final int KEY_ACTION_RELEASE
```

Deprecated.

The user has released a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:** Constant Field Values

- MOUSE_DOWN

```java
public static final int MOUSE_DOWN
```

Deprecated.

The user has pressed the mouse button. The

ALT_MASK

flag indicates that the middle button has been pressed.
The

META_MASK

flag indicates that the
right button has been pressed.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

- MOUSE_UP

```java
public static final int MOUSE_UP
```

Deprecated.

The user has released the mouse button. The

ALT_MASK

flag indicates that the middle button has been released.
The

META_MASK

flag indicates that the
right button has been released.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

- MOUSE_MOVE

```java
public static final int MOUSE_MOVE
```

Deprecated.

The mouse has moved with no button pressed.

**See Also:** Constant Field Values

- MOUSE_ENTER

```java
public static final int MOUSE_ENTER
```

Deprecated.

The mouse has entered a component.

**See Also:** Constant Field Values

- MOUSE_EXIT

```java
public static final int MOUSE_EXIT
```

Deprecated.

The mouse has exited a component.

**See Also:** Constant Field Values

- MOUSE_DRAG

```java
public static final int MOUSE_DRAG
```

Deprecated.

The user has moved the mouse with a button pressed. The

ALT_MASK

flag indicates that the middle
button is being pressed. The

META_MASK

flag indicates
that the right button is being pressed.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

- SCROLL_LINE_UP

```java
public static final int SCROLL_LINE_UP
```

Deprecated.

The user has activated the

line up

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_LINE_DOWN

```java
public static final int SCROLL_LINE_DOWN
```

Deprecated.

The user has activated the

line down

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_PAGE_UP

```java
public static final int SCROLL_PAGE_UP
```

Deprecated.

The user has activated the

page up

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_PAGE_DOWN

```java
public static final int SCROLL_PAGE_DOWN
```

Deprecated.

The user has activated the

page down

area of a scroll bar.

**See Also:** Constant Field Values

- SCROLL_ABSOLUTE

```java
public static final int SCROLL_ABSOLUTE
```

Deprecated.

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

**See Also:** Constant Field Values

- SCROLL_BEGIN

```java
public static final int SCROLL_BEGIN
```

Deprecated.

The scroll begin event.

**See Also:** Constant Field Values

- SCROLL_END

```java
public static final int SCROLL_END
```

Deprecated.

The scroll end event.

**See Also:** Constant Field Values

- LIST_SELECT

```java
public static final int LIST_SELECT
```

Deprecated.

An item in a list has been selected.

**See Also:** Constant Field Values

- LIST_DESELECT

```java
public static final int LIST_DESELECT
```

Deprecated.

An item in a list has been deselected.

**See Also:** Constant Field Values

- ACTION_EVENT

```java
public static final int ACTION_EVENT
```

Deprecated.

This event indicates that the user wants some action to occur.

**See Also:** Constant Field Values

- LOAD_FILE

```java
public static final int LOAD_FILE
```

Deprecated.

A file loading event.

**See Also:** Constant Field Values

- SAVE_FILE

```java
public static final int SAVE_FILE
```

Deprecated.

A file saving event.

**See Also:** Constant Field Values

- GOT_FOCUS

```java
public static final int GOT_FOCUS
```

Deprecated.

A component gained the focus.

**See Also:** Constant Field Values

- LOST_FOCUS

```java
public static final int LOST_FOCUS
```

Deprecated.

A component lost the focus.

**See Also:** Constant Field Values

- target

```java
public
Object
target
```

Deprecated.

The target component. This indicates the component over which the
event occurred or with which the event is associated.
This object has been replaced by AWTEvent.getSource()

**See Also:** EventObject.getSource()

- when

```java
public long when
```

Deprecated.

The time stamp.
Replaced by InputEvent.getWhen().

**See Also:** InputEvent.getWhen()

- id

```java
public int id
```

Deprecated.

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.
This has been replaced by AWTEvent.getID()

**See Also:** AWTEvent.getID()

- x

```java
public int x
```

Deprecated.

The

x

coordinate of the event.
Replaced by MouseEvent.getX()

**See Also:** MouseEvent.getX()

- y

```java
public int y
```

Deprecated.

The

y

coordinate of the event.
Replaced by MouseEvent.getY()

**See Also:** MouseEvent.getY()

- key

```java
public int key
```

Deprecated.

The key code of the key that was pressed in a keyboard event.
This has been replaced by KeyEvent.getKeyCode()

**See Also:** KeyEvent.getKeyCode()

- modifiers

```java
public int modifiers
```

Deprecated.

The state of the modifier keys.
This is replaced with InputEvent.getModifiers()
In java 1.1 MouseEvent and KeyEvent are subclasses
of InputEvent.

**See Also:** InputEvent.getModifiers()

- clickCount

```java
public int clickCount
```

Deprecated.

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks. For other events, its value is

0

.
This field has been replaced by MouseEvent.getClickCount().

**See Also:** MouseEvent.getClickCount()

- arg

```java
public
Object
arg
```

Deprecated.

An arbitrary argument of the event. The value of this field
depends on the type of event.

arg

has been replaced by event specific property.

- evt

```java
public
Event
evt
```

Deprecated.

The next event. This field is set when putting events into a
linked list.
This has been replaced by EventQueue.

**See Also:** EventQueue

---

#### Field Detail

SHIFT_MASK

```java
public static final int SHIFT_MASK
```

Deprecated.

This flag indicates that the Shift key was down when the event
occurred.

**See Also:** Constant Field Values

---

#### SHIFT_MASK

public static final int SHIFT_MASK

This flag indicates that the Shift key was down when the event
occurred.

CTRL_MASK

```java
public static final int CTRL_MASK
```

Deprecated.

This flag indicates that the Control key was down when the event
occurred.

**See Also:** Constant Field Values

---

#### CTRL_MASK

public static final int CTRL_MASK

This flag indicates that the Control key was down when the event
occurred.

META_MASK

```java
public static final int META_MASK
```

Deprecated.

This flag indicates that the Meta key was down when the event
occurred. For mouse events, this flag indicates that the right
button was pressed or released.

**See Also:** Constant Field Values

---

#### META_MASK

public static final int META_MASK

This flag indicates that the Meta key was down when the event
occurred. For mouse events, this flag indicates that the right
button was pressed or released.

ALT_MASK

```java
public static final int ALT_MASK
```

Deprecated.

This flag indicates that the Alt key was down when
the event occurred. For mouse events, this flag indicates that the
middle mouse button was pressed or released.

**See Also:** Constant Field Values

---

#### ALT_MASK

public static final int ALT_MASK

This flag indicates that the Alt key was down when
the event occurred. For mouse events, this flag indicates that the
middle mouse button was pressed or released.

HOME

```java
public static final int HOME
```

Deprecated.

The Home key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### HOME

public static final int HOME

The Home key, a non-ASCII action key.

END

```java
public static final int END
```

Deprecated.

The End key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### END

public static final int END

The End key, a non-ASCII action key.

PGUP

```java
public static final int PGUP
```

Deprecated.

The Page Up key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### PGUP

public static final int PGUP

The Page Up key, a non-ASCII action key.

PGDN

```java
public static final int PGDN
```

Deprecated.

The Page Down key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### PGDN

public static final int PGDN

The Page Down key, a non-ASCII action key.

UP

```java
public static final int UP
```

Deprecated.

The Up Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### UP

public static final int UP

The Up Arrow key, a non-ASCII action key.

DOWN

```java
public static final int DOWN
```

Deprecated.

The Down Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### DOWN

public static final int DOWN

The Down Arrow key, a non-ASCII action key.

LEFT

```java
public static final int LEFT
```

Deprecated.

The Left Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### LEFT

public static final int LEFT

The Left Arrow key, a non-ASCII action key.

RIGHT

```java
public static final int RIGHT
```

Deprecated.

The Right Arrow key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### RIGHT

public static final int RIGHT

The Right Arrow key, a non-ASCII action key.

F1

```java
public static final int F1
```

Deprecated.

The F1 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F1

public static final int F1

The F1 function key, a non-ASCII action key.

F2

```java
public static final int F2
```

Deprecated.

The F2 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F2

public static final int F2

The F2 function key, a non-ASCII action key.

F3

```java
public static final int F3
```

Deprecated.

The F3 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F3

public static final int F3

The F3 function key, a non-ASCII action key.

F4

```java
public static final int F4
```

Deprecated.

The F4 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F4

public static final int F4

The F4 function key, a non-ASCII action key.

F5

```java
public static final int F5
```

Deprecated.

The F5 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F5

public static final int F5

The F5 function key, a non-ASCII action key.

F6

```java
public static final int F6
```

Deprecated.

The F6 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F6

public static final int F6

The F6 function key, a non-ASCII action key.

F7

```java
public static final int F7
```

Deprecated.

The F7 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F7

public static final int F7

The F7 function key, a non-ASCII action key.

F8

```java
public static final int F8
```

Deprecated.

The F8 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F8

public static final int F8

The F8 function key, a non-ASCII action key.

F9

```java
public static final int F9
```

Deprecated.

The F9 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F9

public static final int F9

The F9 function key, a non-ASCII action key.

F10

```java
public static final int F10
```

Deprecated.

The F10 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F10

public static final int F10

The F10 function key, a non-ASCII action key.

F11

```java
public static final int F11
```

Deprecated.

The F11 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F11

public static final int F11

The F11 function key, a non-ASCII action key.

F12

```java
public static final int F12
```

Deprecated.

The F12 function key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### F12

public static final int F12

The F12 function key, a non-ASCII action key.

PRINT_SCREEN

```java
public static final int PRINT_SCREEN
```

Deprecated.

The Print Screen key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### PRINT_SCREEN

public static final int PRINT_SCREEN

The Print Screen key, a non-ASCII action key.

SCROLL_LOCK

```java
public static final int SCROLL_LOCK
```

Deprecated.

The Scroll Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### SCROLL_LOCK

public static final int SCROLL_LOCK

The Scroll Lock key, a non-ASCII action key.

CAPS_LOCK

```java
public static final int CAPS_LOCK
```

Deprecated.

The Caps Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### CAPS_LOCK

public static final int CAPS_LOCK

The Caps Lock key, a non-ASCII action key.

NUM_LOCK

```java
public static final int NUM_LOCK
```

Deprecated.

The Num Lock key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### NUM_LOCK

public static final int NUM_LOCK

The Num Lock key, a non-ASCII action key.

PAUSE

```java
public static final int PAUSE
```

Deprecated.

The Pause key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### PAUSE

public static final int PAUSE

The Pause key, a non-ASCII action key.

INSERT

```java
public static final int INSERT
```

Deprecated.

The Insert key, a non-ASCII action key.

**See Also:** Constant Field Values

---

#### INSERT

public static final int INSERT

The Insert key, a non-ASCII action key.

ENTER

```java
public static final int ENTER
```

Deprecated.

The Enter key.

**See Also:** Constant Field Values

---

#### ENTER

public static final int ENTER

The Enter key.

BACK_SPACE

```java
public static final int BACK_SPACE
```

Deprecated.

The BackSpace key.

**See Also:** Constant Field Values

---

#### BACK_SPACE

public static final int BACK_SPACE

The BackSpace key.

TAB

```java
public static final int TAB
```

Deprecated.

The Tab key.

**See Also:** Constant Field Values

---

#### TAB

public static final int TAB

The Tab key.

ESCAPE

```java
public static final int ESCAPE
```

Deprecated.

The Escape key.

**See Also:** Constant Field Values

---

#### ESCAPE

public static final int ESCAPE

The Escape key.

DELETE

```java
public static final int DELETE
```

Deprecated.

The Delete key.

**See Also:** Constant Field Values

---

#### DELETE

public static final int DELETE

The Delete key.

WINDOW_DESTROY

```java
public static final int WINDOW_DESTROY
```

Deprecated.

The user has asked the window manager to kill the window.

**See Also:** Constant Field Values

---

#### WINDOW_DESTROY

public static final int WINDOW_DESTROY

The user has asked the window manager to kill the window.

WINDOW_EXPOSE

```java
public static final int WINDOW_EXPOSE
```

Deprecated.

The user has asked the window manager to expose the window.

**See Also:** Constant Field Values

---

#### WINDOW_EXPOSE

public static final int WINDOW_EXPOSE

The user has asked the window manager to expose the window.

WINDOW_ICONIFY

```java
public static final int WINDOW_ICONIFY
```

Deprecated.

The user has asked the window manager to iconify the window.

**See Also:** Constant Field Values

---

#### WINDOW_ICONIFY

public static final int WINDOW_ICONIFY

The user has asked the window manager to iconify the window.

WINDOW_DEICONIFY

```java
public static final int WINDOW_DEICONIFY
```

Deprecated.

The user has asked the window manager to de-iconify the window.

**See Also:** Constant Field Values

---

#### WINDOW_DEICONIFY

public static final int WINDOW_DEICONIFY

The user has asked the window manager to de-iconify the window.

WINDOW_MOVED

```java
public static final int WINDOW_MOVED
```

Deprecated.

The user has asked the window manager to move the window.

**See Also:** Constant Field Values

---

#### WINDOW_MOVED

public static final int WINDOW_MOVED

The user has asked the window manager to move the window.

KEY_PRESS

```java
public static final int KEY_PRESS
```

Deprecated.

The user has pressed a normal key.

**See Also:** Constant Field Values

---

#### KEY_PRESS

public static final int KEY_PRESS

The user has pressed a normal key.

KEY_RELEASE

```java
public static final int KEY_RELEASE
```

Deprecated.

The user has released a normal key.

**See Also:** Constant Field Values

---

#### KEY_RELEASE

public static final int KEY_RELEASE

The user has released a normal key.

KEY_ACTION

```java
public static final int KEY_ACTION
```

Deprecated.

The user has pressed a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:** Constant Field Values

---

#### KEY_ACTION

public static final int KEY_ACTION

The user has pressed a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

KEY_ACTION_RELEASE

```java
public static final int KEY_ACTION_RELEASE
```

Deprecated.

The user has released a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

**See Also:** Constant Field Values

---

#### KEY_ACTION_RELEASE

public static final int KEY_ACTION_RELEASE

The user has released a non-ASCII

action

key.
The

key

field contains a value that indicates
that the event occurred on one of the action keys, which
comprise the 12 function keys, the arrow (cursor) keys,
Page Up, Page Down, Home, End, Print Screen, Scroll Lock,
Caps Lock, Num Lock, Pause, and Insert.

MOUSE_DOWN

```java
public static final int MOUSE_DOWN
```

Deprecated.

The user has pressed the mouse button. The

ALT_MASK

flag indicates that the middle button has been pressed.
The

META_MASK

flag indicates that the
right button has been pressed.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

---

#### MOUSE_DOWN

public static final int MOUSE_DOWN

The user has pressed the mouse button. The

ALT_MASK

flag indicates that the middle button has been pressed.
The

META_MASK

flag indicates that the
right button has been pressed.

MOUSE_UP

```java
public static final int MOUSE_UP
```

Deprecated.

The user has released the mouse button. The

ALT_MASK

flag indicates that the middle button has been released.
The

META_MASK

flag indicates that the
right button has been released.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

---

#### MOUSE_UP

public static final int MOUSE_UP

The user has released the mouse button. The

ALT_MASK

flag indicates that the middle button has been released.
The

META_MASK

flag indicates that the
right button has been released.

MOUSE_MOVE

```java
public static final int MOUSE_MOVE
```

Deprecated.

The mouse has moved with no button pressed.

**See Also:** Constant Field Values

---

#### MOUSE_MOVE

public static final int MOUSE_MOVE

The mouse has moved with no button pressed.

MOUSE_ENTER

```java
public static final int MOUSE_ENTER
```

Deprecated.

The mouse has entered a component.

**See Also:** Constant Field Values

---

#### MOUSE_ENTER

public static final int MOUSE_ENTER

The mouse has entered a component.

MOUSE_EXIT

```java
public static final int MOUSE_EXIT
```

Deprecated.

The mouse has exited a component.

**See Also:** Constant Field Values

---

#### MOUSE_EXIT

public static final int MOUSE_EXIT

The mouse has exited a component.

MOUSE_DRAG

```java
public static final int MOUSE_DRAG
```

Deprecated.

The user has moved the mouse with a button pressed. The

ALT_MASK

flag indicates that the middle
button is being pressed. The

META_MASK

flag indicates
that the right button is being pressed.

**See Also:** ALT_MASK

,

META_MASK

,

Constant Field Values

---

#### MOUSE_DRAG

public static final int MOUSE_DRAG

The user has moved the mouse with a button pressed. The

ALT_MASK

flag indicates that the middle
button is being pressed. The

META_MASK

flag indicates
that the right button is being pressed.

SCROLL_LINE_UP

```java
public static final int SCROLL_LINE_UP
```

Deprecated.

The user has activated the

line up

area of a scroll bar.

**See Also:** Constant Field Values

---

#### SCROLL_LINE_UP

public static final int SCROLL_LINE_UP

The user has activated the

line up

area of a scroll bar.

SCROLL_LINE_DOWN

```java
public static final int SCROLL_LINE_DOWN
```

Deprecated.

The user has activated the

line down

area of a scroll bar.

**See Also:** Constant Field Values

---

#### SCROLL_LINE_DOWN

public static final int SCROLL_LINE_DOWN

The user has activated the

line down

area of a scroll bar.

SCROLL_PAGE_UP

```java
public static final int SCROLL_PAGE_UP
```

Deprecated.

The user has activated the

page up

area of a scroll bar.

**See Also:** Constant Field Values

---

#### SCROLL_PAGE_UP

public static final int SCROLL_PAGE_UP

The user has activated the

page up

area of a scroll bar.

SCROLL_PAGE_DOWN

```java
public static final int SCROLL_PAGE_DOWN
```

Deprecated.

The user has activated the

page down

area of a scroll bar.

**See Also:** Constant Field Values

---

#### SCROLL_PAGE_DOWN

public static final int SCROLL_PAGE_DOWN

The user has activated the

page down

area of a scroll bar.

SCROLL_ABSOLUTE

```java
public static final int SCROLL_ABSOLUTE
```

Deprecated.

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

**See Also:** Constant Field Values

---

#### SCROLL_ABSOLUTE

public static final int SCROLL_ABSOLUTE

The user has moved the bubble (thumb) in a scroll bar,
moving to an "absolute" position, rather than to
an offset from the last position.

SCROLL_BEGIN

```java
public static final int SCROLL_BEGIN
```

Deprecated.

The scroll begin event.

**See Also:** Constant Field Values

---

#### SCROLL_BEGIN

public static final int SCROLL_BEGIN

The scroll begin event.

SCROLL_END

```java
public static final int SCROLL_END
```

Deprecated.

The scroll end event.

**See Also:** Constant Field Values

---

#### SCROLL_END

public static final int SCROLL_END

The scroll end event.

LIST_SELECT

```java
public static final int LIST_SELECT
```

Deprecated.

An item in a list has been selected.

**See Also:** Constant Field Values

---

#### LIST_SELECT

public static final int LIST_SELECT

An item in a list has been selected.

LIST_DESELECT

```java
public static final int LIST_DESELECT
```

Deprecated.

An item in a list has been deselected.

**See Also:** Constant Field Values

---

#### LIST_DESELECT

public static final int LIST_DESELECT

An item in a list has been deselected.

ACTION_EVENT

```java
public static final int ACTION_EVENT
```

Deprecated.

This event indicates that the user wants some action to occur.

**See Also:** Constant Field Values

---

#### ACTION_EVENT

public static final int ACTION_EVENT

This event indicates that the user wants some action to occur.

LOAD_FILE

```java
public static final int LOAD_FILE
```

Deprecated.

A file loading event.

**See Also:** Constant Field Values

---

#### LOAD_FILE

public static final int LOAD_FILE

A file loading event.

SAVE_FILE

```java
public static final int SAVE_FILE
```

Deprecated.

A file saving event.

**See Also:** Constant Field Values

---

#### SAVE_FILE

public static final int SAVE_FILE

A file saving event.

GOT_FOCUS

```java
public static final int GOT_FOCUS
```

Deprecated.

A component gained the focus.

**See Also:** Constant Field Values

---

#### GOT_FOCUS

public static final int GOT_FOCUS

A component gained the focus.

LOST_FOCUS

```java
public static final int LOST_FOCUS
```

Deprecated.

A component lost the focus.

**See Also:** Constant Field Values

---

#### LOST_FOCUS

public static final int LOST_FOCUS

A component lost the focus.

target

```java
public
Object
target
```

Deprecated.

The target component. This indicates the component over which the
event occurred or with which the event is associated.
This object has been replaced by AWTEvent.getSource()

**See Also:** EventObject.getSource()

---

#### target

public

Object

target

The target component. This indicates the component over which the
event occurred or with which the event is associated.
This object has been replaced by AWTEvent.getSource()

when

```java
public long when
```

Deprecated.

The time stamp.
Replaced by InputEvent.getWhen().

**See Also:** InputEvent.getWhen()

---

#### when

public long when

The time stamp.
Replaced by InputEvent.getWhen().

id

```java
public int id
```

Deprecated.

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.
This has been replaced by AWTEvent.getID()

**See Also:** AWTEvent.getID()

---

#### id

public int id

Indicates which type of event the event is, and which
other

Event

variables are relevant for the event.
This has been replaced by AWTEvent.getID()

x

```java
public int x
```

Deprecated.

The

x

coordinate of the event.
Replaced by MouseEvent.getX()

**See Also:** MouseEvent.getX()

---

#### x

public int x

The

x

coordinate of the event.
Replaced by MouseEvent.getX()

y

```java
public int y
```

Deprecated.

The

y

coordinate of the event.
Replaced by MouseEvent.getY()

**See Also:** MouseEvent.getY()

---

#### y

public int y

The

y

coordinate of the event.
Replaced by MouseEvent.getY()

key

```java
public int key
```

Deprecated.

The key code of the key that was pressed in a keyboard event.
This has been replaced by KeyEvent.getKeyCode()

**See Also:** KeyEvent.getKeyCode()

---

#### key

public int key

The key code of the key that was pressed in a keyboard event.
This has been replaced by KeyEvent.getKeyCode()

modifiers

```java
public int modifiers
```

Deprecated.

The state of the modifier keys.
This is replaced with InputEvent.getModifiers()
In java 1.1 MouseEvent and KeyEvent are subclasses
of InputEvent.

**See Also:** InputEvent.getModifiers()

---

#### modifiers

public int modifiers

The state of the modifier keys.
This is replaced with InputEvent.getModifiers()
In java 1.1 MouseEvent and KeyEvent are subclasses
of InputEvent.

clickCount

```java
public int clickCount
```

Deprecated.

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks. For other events, its value is

0

.
This field has been replaced by MouseEvent.getClickCount().

**See Also:** MouseEvent.getClickCount()

---

#### clickCount

public int clickCount

For

MOUSE_DOWN

events, this field indicates the
number of consecutive clicks. For other events, its value is

0

.
This field has been replaced by MouseEvent.getClickCount().

arg

```java
public
Object
arg
```

Deprecated.

An arbitrary argument of the event. The value of this field
depends on the type of event.

arg

has been replaced by event specific property.

---

#### arg

public

Object

arg

An arbitrary argument of the event. The value of this field
depends on the type of event.

arg

has been replaced by event specific property.

evt

```java
public
Event
evt
```

Deprecated.

The next event. This field is set when putting events into a
linked list.
This has been replaced by EventQueue.

**See Also:** EventQueue

---

#### evt

public

Event

evt

The next event. This field is set when putting events into a
linked list.
This has been replaced by EventQueue.

Constructor Detail

- Event

```java
public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers,

Object
arg)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and
argument.

**Parameters:** target

- the target component.
**Parameters:** when

- the time stamp.
**Parameters:** id

- the event type.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** key

- the key pressed in a keyboard event.
**Parameters:** modifiers

- the state of the modifier keys.
**Parameters:** arg

- the specified argument.

- Event

```java
public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

, with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and an
argument set to

null

.

**Parameters:** target

- the target component.
**Parameters:** when

- the time stamp.
**Parameters:** id

- the event type.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** key

- the key pressed in a keyboard event.
**Parameters:** modifiers

- the state of the modifier keys.

- Event

```java
public Event​(
Object
target,
int id,

Object
arg)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified
target component, event type, and argument.

**Parameters:** target

- the target component.
**Parameters:** id

- the event type.
**Parameters:** arg

- the specified argument.

---

#### Constructor Detail

Event

```java
public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers,

Object
arg)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and
argument.

**Parameters:** target

- the target component.
**Parameters:** when

- the time stamp.
**Parameters:** id

- the event type.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** key

- the key pressed in a keyboard event.
**Parameters:** modifiers

- the state of the modifier keys.
**Parameters:** arg

- the specified argument.

---

#### Event

public Event​(

Object

target,
long when,
int id,
int x,
int y,
int key,
int modifiers,

Object

arg)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and
argument.

Creates an instance of

Event

with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and
argument.

Event

```java
public Event​(
Object
target,
long when,
int id,
int x,
int y,
int key,
int modifiers)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

, with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and an
argument set to

null

.

**Parameters:** target

- the target component.
**Parameters:** when

- the time stamp.
**Parameters:** id

- the event type.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** key

- the key pressed in a keyboard event.
**Parameters:** modifiers

- the state of the modifier keys.

---

#### Event

public Event​(

Object

target,
long when,
int id,
int x,
int y,
int key,
int modifiers)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

, with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and an
argument set to

null

.

Creates an instance of

Event

, with the specified target
component, time stamp, event type,

x

and

y

coordinates, keyboard key, state of the modifier keys, and an
argument set to

null

.

Event

```java
public Event​(
Object
target,
int id,

Object
arg)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified
target component, event type, and argument.

**Parameters:** target

- the target component.
**Parameters:** id

- the event type.
**Parameters:** arg

- the specified argument.

---

#### Event

public Event​(

Object

target,
int id,

Object

arg)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Creates an instance of

Event

with the specified
target component, event type, and argument.

Creates an instance of

Event

with the specified
target component, event type, and argument.

Method Detail

- translate

```java
public void translate​(int dx,
int dy)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Translates this event so that its

x

and

y

coordinates are increased by

dx

and

dy

,
respectively.

This method translates an event relative to the given component.
This involves, at a minimum, translating the coordinates into the
local coordinate system of the given component. It may also involve
translating a region in the case of an expose event.

**Parameters:** dx

- the distance to translate the

x

coordinate.
**Parameters:** dy

- the distance to translate the

y

coordinate.

- shiftDown

```java
public boolean shiftDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Shift key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

controlDown()

,

metaDown()

- controlDown

```java
public boolean controlDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Control key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

shiftDown()

,

metaDown()

- metaDown

```java
public boolean metaDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Meta key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

shiftDown()

,

controlDown()

- paramString

```java
protected
String
paramString()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a string representing the state of this

Event

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:** the parameter string of this event

- toString

```java
public
String
toString()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a representation of this event's values as a string.

**Overrides:** toString

in class

Object
**Returns:** a string that represents the event and the values
of its member fields.
**Since:** 1.1
**See Also:** paramString()

---

#### Method Detail

translate

```java
public void translate​(int dx,
int dy)
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Translates this event so that its

x

and

y

coordinates are increased by

dx

and

dy

,
respectively.

This method translates an event relative to the given component.
This involves, at a minimum, translating the coordinates into the
local coordinate system of the given component. It may also involve
translating a region in the case of an expose event.

**Parameters:** dx

- the distance to translate the

x

coordinate.
**Parameters:** dy

- the distance to translate the

y

coordinate.

---

#### translate

public void translate​(int dx,
int dy)

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Translates this event so that its

x

and

y

coordinates are increased by

dx

and

dy

,
respectively.

This method translates an event relative to the given component.
This involves, at a minimum, translating the coordinates into the
local coordinate system of the given component. It may also involve
translating a region in the case of an expose event.

Translates this event so that its

x

and

y

coordinates are increased by

dx

and

dy

,
respectively.

This method translates an event relative to the given component.
This involves, at a minimum, translating the coordinates into the
local coordinate system of the given component. It may also involve
translating a region in the case of an expose event.

This method translates an event relative to the given component.
This involves, at a minimum, translating the coordinates into the
local coordinate system of the given component. It may also involve
translating a region in the case of an expose event.

shiftDown

```java
public boolean shiftDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Shift key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

controlDown()

,

metaDown()

---

#### shiftDown

public boolean shiftDown()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Shift key is down.

Checks if the Shift key is down.

controlDown

```java
public boolean controlDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Control key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

shiftDown()

,

metaDown()

---

#### controlDown

public boolean controlDown()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Control key is down.

Checks if the Control key is down.

metaDown

```java
public boolean metaDown()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Meta key is down.

**Returns:** true

if the key is down;

false

otherwise.
**See Also:** modifiers

,

shiftDown()

,

controlDown()

---

#### metaDown

public boolean metaDown()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Checks if the Meta key is down.

Checks if the Meta key is down.

paramString

```java
protected
String
paramString()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a string representing the state of this

Event

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Returns:** the parameter string of this event

---

#### paramString

protected

String

paramString()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a string representing the state of this

Event

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

Returns a string representing the state of this

Event

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

toString

```java
public
String
toString()
```

Deprecated.

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a representation of this event's values as a string.

**Overrides:** toString

in class

Object
**Returns:** a string that represents the event and the values
of its member fields.
**Since:** 1.1
**See Also:** paramString()

---

#### toString

public

String

toString()

NOTE:

The

Event

class is obsolete and is
available only for backwards compatibility. It has been replaced
by the

AWTEvent

class and its subclasses.

Returns a representation of this event's values as a string.

Returns a representation of this event's values as a string.

---

