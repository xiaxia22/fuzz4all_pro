# Class KeyStroke

**Source:** `java.desktop\javax\swing\KeyStroke.html`

### Class Description

```java
public class
KeyStroke

extends
AWTKeyStroke
```

A KeyStroke represents a key action on the keyboard, or equivalent input
device. KeyStrokes can correspond to only a press or release of a particular
key, just as KEY_PRESSED and KEY_RELEASED KeyEvents do; alternately, they
can correspond to typing a specific Java character, just as KEY_TYPED
KeyEvents do. In all cases, KeyStrokes can specify modifiers (alt, shift,
control, meta, altGraph, or a combination thereof) which must be present during the
action for an exact match.

KeyStrokes are used to define high-level (semantic) action events. Instead
of trapping every keystroke and throwing away the ones you are not
interested in, those keystrokes you care about automatically initiate
actions on the Components with which they are registered.

KeyStrokes are immutable, and are intended to be unique. Client code cannot
create a KeyStroke; a variant of

getKeyStroke

must be used
instead. These factory methods allow the KeyStroke implementation to cache
and share instances efficiently.

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

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
KeyStroke
getKeyStroke​(char keyChar)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:**
- keyChar

- the character value for a keyboard key

**Returns:**
- a KeyStroke object for that key

---

#### @Deprecated

public static
KeyStroke
getKeyStroke​(char keyChar,
boolean onKeyRelease)

Returns an instance of a KeyStroke, specifying whether the key is
considered to be activated when it is pressed or released. Unlike all
other factory methods in this class, the instances returned by this
method are not necessarily cached or shared.

**Parameters:**
- keyChar

- the character value for a keyboard key
- onKeyRelease

-

true

if this KeyStroke corresponds to a
key release;

false

otherwise.

**Returns:**
- a KeyStroke object for that key

---

#### public static
KeyStroke
getKeyStroke​(
Character
keyChar,
int modifiers)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers. Note that the first parameter is of type Character
rather than char. This is to avoid inadvertent clashes with calls to

getKeyStroke(int keyCode, int modifiers)

.

The modifiers consist of any combination of following:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers listed below also can be used, but they are
mapped to _DOWN_ modifiers.

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:**
- keyChar

- the Character object for a keyboard character
- modifiers

- a bitwise-ored combination of any modifiers

**Returns:**
- an KeyStroke object for that key

**Throws:**
- IllegalArgumentException

- if keyChar is null

**See Also:**
- InputEvent

**Since:**
- 1.3

---

#### public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:**
- keyCode

- an int specifying the numeric code for a keyboard key
- modifiers

- a bitwise-ored combination of any modifiers
- onKeyRelease

-

true

if the KeyStroke should represent
a key release;

false

otherwise.

**Returns:**
- a KeyStroke object for that key

**See Also:**
- KeyEvent

,

InputEvent

---

#### public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers. The returned KeyStroke will correspond to a key press.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:**
- keyCode

- an int specifying the numeric code for a keyboard key
- modifiers

- a bitwise-ored combination of any modifiers

**Returns:**
- a KeyStroke object for that key

**See Also:**
- KeyEvent

,

InputEvent

---

#### public static
KeyStroke
getKeyStrokeForEvent​(
KeyEvent
anEvent)

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

This method obtains the keyChar from a KeyTyped event, and the keyCode
from a KeyPressed or KeyReleased event. The KeyEvent modifiers are
obtained for all three types of KeyEvent.

**Parameters:**
- anEvent

- the KeyEvent from which to obtain the KeyStroke

**Returns:**
- the KeyStroke that precipitated the event

**Throws:**
- NullPointerException

- if

anEvent

is null

---

#### public static
KeyStroke
getKeyStroke​(
String
s)

Parses a string and returns a

KeyStroke

.
The string must have the following syntax:

```java
<modifiers>* (<typedID> | <pressedReleasedID>)

modifiers := shift | control | ctrl | meta | alt | altGraph
typedID := typed <typedKey>
typedKey := string of length 1 giving Unicode character.
pressedReleasedID := (pressed | released) key
key := KeyEvent key code name, i.e. the name following "VK_".
```

If typed, pressed or released is not specified, pressed is assumed. Here
are some examples:

```java
"INSERT" => getKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getKeyStroke('a');
```

In order to maintain backward-compatibility, specifying a null String,
or a String which is formatted incorrectly, returns null.

**Parameters:**
- s

- a String formatted as described above

**Returns:**
- a KeyStroke object for that String, or null if the specified
String is null, or is formatted incorrectly

**See Also:**
- KeyEvent

---

### Additional Sections

#### Class KeyStroke

java.lang.Object

- java.awt.AWTKeyStroke
- - javax.swing.KeyStroke

java.awt.AWTKeyStroke

- javax.swing.KeyStroke

javax.swing.KeyStroke

**All Implemented Interfaces:** Serializable

```java
public class
KeyStroke

extends
AWTKeyStroke
```

A KeyStroke represents a key action on the keyboard, or equivalent input
device. KeyStrokes can correspond to only a press or release of a particular
key, just as KEY_PRESSED and KEY_RELEASED KeyEvents do; alternately, they
can correspond to typing a specific Java character, just as KEY_TYPED
KeyEvents do. In all cases, KeyStrokes can specify modifiers (alt, shift,
control, meta, altGraph, or a combination thereof) which must be present during the
action for an exact match.

KeyStrokes are used to define high-level (semantic) action events. Instead
of trapping every keystroke and throwing away the ones you are not
interested in, those keystrokes you care about automatically initiate
actions on the Components with which they are registered.

KeyStrokes are immutable, and are intended to be unique. Client code cannot
create a KeyStroke; a variant of

getKeyStroke

must be used
instead. These factory methods allow the KeyStroke implementation to cache
and share instances efficiently.

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
**See Also:** Keymap

,

getKeyStroke(char)

,

Serialized Form

public class

KeyStroke

extends

AWTKeyStroke

A KeyStroke represents a key action on the keyboard, or equivalent input
device. KeyStrokes can correspond to only a press or release of a particular
key, just as KEY_PRESSED and KEY_RELEASED KeyEvents do; alternately, they
can correspond to typing a specific Java character, just as KEY_TYPED
KeyEvents do. In all cases, KeyStrokes can specify modifiers (alt, shift,
control, meta, altGraph, or a combination thereof) which must be present during the
action for an exact match.

KeyStrokes are used to define high-level (semantic) action events. Instead
of trapping every keystroke and throwing away the ones you are not
interested in, those keystrokes you care about automatically initiate
actions on the Components with which they are registered.

KeyStrokes are immutable, and are intended to be unique. Client code cannot
create a KeyStroke; a variant of

getKeyStroke

must be used
instead. These factory methods allow the KeyStroke implementation to cache
and share instances efficiently.

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

KeyStrokes are used to define high-level (semantic) action events. Instead
of trapping every keystroke and throwing away the ones you are not
interested in, those keystrokes you care about automatically initiate
actions on the Components with which they are registered.

KeyStrokes are immutable, and are intended to be unique. Client code cannot
create a KeyStroke; a variant of

getKeyStroke

must be used
instead. These factory methods allow the KeyStroke implementation to cache
and share instances efficiently.

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

KeyStrokes are immutable, and are intended to be unique. Client code cannot
create a KeyStroke; a variant of

getKeyStroke

must be used
instead. These factory methods allow the KeyStroke implementation to cache
and share instances efficiently.

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

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

KeyStroke

getKeyStroke

​(char keyChar)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

static

KeyStroke

getKeyStroke

​(char keyChar,
boolean onKeyRelease)

Deprecated.

use getKeyStroke(char)

static

KeyStroke

getKeyStroke

​(int keyCode,
int modifiers)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers.

static

KeyStroke

getKeyStroke

​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

static

KeyStroke

getKeyStroke

​(

Character

keyChar,
int modifiers)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers.

static

KeyStroke

getKeyStroke

​(

String

s)

Parses a string and returns a

KeyStroke

.

static

KeyStroke

getKeyStrokeForEvent

​(

KeyEvent

anEvent)

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

- Methods declared in class java.awt.

AWTKeyStroke

equals

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStrokeForEvent

,

getKeyChar

,

getKeyCode

,

getKeyEventType

,

getModifiers

,

hashCode

,

isOnKeyRelease

,

readResolve

,

registerSubclass

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

KeyStroke

getKeyStroke

​(char keyChar)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

static

KeyStroke

getKeyStroke

​(char keyChar,
boolean onKeyRelease)

Deprecated.

use getKeyStroke(char)

static

KeyStroke

getKeyStroke

​(int keyCode,
int modifiers)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers.

static

KeyStroke

getKeyStroke

​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

static

KeyStroke

getKeyStroke

​(

Character

keyChar,
int modifiers)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers.

static

KeyStroke

getKeyStroke

​(

String

s)

Parses a string and returns a

KeyStroke

.

static

KeyStroke

getKeyStrokeForEvent

​(

KeyEvent

anEvent)

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

- Methods declared in class java.awt.

AWTKeyStroke

equals

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStrokeForEvent

,

getKeyChar

,

getKeyCode

,

getKeyEventType

,

getModifiers

,

hashCode

,

isOnKeyRelease

,

readResolve

,

registerSubclass

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

Deprecated.

use getKeyStroke(char)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers.

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers.

Parses a string and returns a

KeyStroke

.

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

Methods declared in class java.awt.

AWTKeyStroke

equals

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStroke

,

getAWTKeyStrokeForEvent

,

getKeyChar

,

getKeyCode

,

getKeyEventType

,

getModifiers

,

hashCode

,

isOnKeyRelease

,

readResolve

,

registerSubclass

,

toString

---

#### Methods declared in class java.awt. AWTKeyStroke

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

============ METHOD DETAIL ==========

- Method Detail

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(char keyChar)
```

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:** keyChar

- the character value for a keyboard key
**Returns:** a KeyStroke object for that key

- getKeyStroke

```java
@Deprecated

public static
KeyStroke
getKeyStroke​(char keyChar,
boolean onKeyRelease)
```

Deprecated.

use getKeyStroke(char)

Returns an instance of a KeyStroke, specifying whether the key is
considered to be activated when it is pressed or released. Unlike all
other factory methods in this class, the instances returned by this
method are not necessarily cached or shared.

**Parameters:** keyChar

- the character value for a keyboard key
**Parameters:** onKeyRelease

-

true

if this KeyStroke corresponds to a
key release;

false

otherwise.
**Returns:** a KeyStroke object for that key

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(
Character
keyChar,
int modifiers)
```

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers. Note that the first parameter is of type Character
rather than char. This is to avoid inadvertent clashes with calls to

getKeyStroke(int keyCode, int modifiers)

.

The modifiers consist of any combination of following:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers listed below also can be used, but they are
mapped to _DOWN_ modifiers.

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyChar

- the Character object for a keyboard character
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Returns:** an KeyStroke object for that key
**Throws:** IllegalArgumentException

- if keyChar is null
**Since:** 1.3
**See Also:** InputEvent

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)
```

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyCode

- an int specifying the numeric code for a keyboard key
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Parameters:** onKeyRelease

-

true

if the KeyStroke should represent
a key release;

false

otherwise.
**Returns:** a KeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers)
```

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers. The returned KeyStroke will correspond to a key press.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyCode

- an int specifying the numeric code for a keyboard key
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Returns:** a KeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

- getKeyStrokeForEvent

```java
public static
KeyStroke
getKeyStrokeForEvent​(
KeyEvent
anEvent)
```

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

This method obtains the keyChar from a KeyTyped event, and the keyCode
from a KeyPressed or KeyReleased event. The KeyEvent modifiers are
obtained for all three types of KeyEvent.

**Parameters:** anEvent

- the KeyEvent from which to obtain the KeyStroke
**Returns:** the KeyStroke that precipitated the event
**Throws:** NullPointerException

- if

anEvent

is null

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(
String
s)
```

Parses a string and returns a

KeyStroke

.
The string must have the following syntax:

```java
<modifiers>* (<typedID> | <pressedReleasedID>)

modifiers := shift | control | ctrl | meta | alt | altGraph
typedID := typed <typedKey>
typedKey := string of length 1 giving Unicode character.
pressedReleasedID := (pressed | released) key
key := KeyEvent key code name, i.e. the name following "VK_".
```

If typed, pressed or released is not specified, pressed is assumed. Here
are some examples:

```java
"INSERT" => getKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getKeyStroke('a');
```

In order to maintain backward-compatibility, specifying a null String,
or a String which is formatted incorrectly, returns null.

**Parameters:** s

- a String formatted as described above
**Returns:** a KeyStroke object for that String, or null if the specified
String is null, or is formatted incorrectly
**See Also:** KeyEvent

Method Detail

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(char keyChar)
```

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:** keyChar

- the character value for a keyboard key
**Returns:** a KeyStroke object for that key

- getKeyStroke

```java
@Deprecated

public static
KeyStroke
getKeyStroke​(char keyChar,
boolean onKeyRelease)
```

Deprecated.

use getKeyStroke(char)

Returns an instance of a KeyStroke, specifying whether the key is
considered to be activated when it is pressed or released. Unlike all
other factory methods in this class, the instances returned by this
method are not necessarily cached or shared.

**Parameters:** keyChar

- the character value for a keyboard key
**Parameters:** onKeyRelease

-

true

if this KeyStroke corresponds to a
key release;

false

otherwise.
**Returns:** a KeyStroke object for that key

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(
Character
keyChar,
int modifiers)
```

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers. Note that the first parameter is of type Character
rather than char. This is to avoid inadvertent clashes with calls to

getKeyStroke(int keyCode, int modifiers)

.

The modifiers consist of any combination of following:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers listed below also can be used, but they are
mapped to _DOWN_ modifiers.

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyChar

- the Character object for a keyboard character
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Returns:** an KeyStroke object for that key
**Throws:** IllegalArgumentException

- if keyChar is null
**Since:** 1.3
**See Also:** InputEvent

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)
```

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyCode

- an int specifying the numeric code for a keyboard key
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Parameters:** onKeyRelease

-

true

if the KeyStroke should represent
a key release;

false

otherwise.
**Returns:** a KeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers)
```

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers. The returned KeyStroke will correspond to a key press.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyCode

- an int specifying the numeric code for a keyboard key
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Returns:** a KeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

- getKeyStrokeForEvent

```java
public static
KeyStroke
getKeyStrokeForEvent​(
KeyEvent
anEvent)
```

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

This method obtains the keyChar from a KeyTyped event, and the keyCode
from a KeyPressed or KeyReleased event. The KeyEvent modifiers are
obtained for all three types of KeyEvent.

**Parameters:** anEvent

- the KeyEvent from which to obtain the KeyStroke
**Returns:** the KeyStroke that precipitated the event
**Throws:** NullPointerException

- if

anEvent

is null

- getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(
String
s)
```

Parses a string and returns a

KeyStroke

.
The string must have the following syntax:

```java
<modifiers>* (<typedID> | <pressedReleasedID>)

modifiers := shift | control | ctrl | meta | alt | altGraph
typedID := typed <typedKey>
typedKey := string of length 1 giving Unicode character.
pressedReleasedID := (pressed | released) key
key := KeyEvent key code name, i.e. the name following "VK_".
```

If typed, pressed or released is not specified, pressed is assumed. Here
are some examples:

```java
"INSERT" => getKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getKeyStroke('a');
```

In order to maintain backward-compatibility, specifying a null String,
or a String which is formatted incorrectly, returns null.

**Parameters:** s

- a String formatted as described above
**Returns:** a KeyStroke object for that String, or null if the specified
String is null, or is formatted incorrectly
**See Also:** KeyEvent

---

#### Method Detail

getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(char keyChar)
```

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:** keyChar

- the character value for a keyboard key
**Returns:** a KeyStroke object for that key

---

#### getKeyStroke

public static

KeyStroke

getKeyStroke​(char keyChar)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified character.

getKeyStroke

```java
@Deprecated

public static
KeyStroke
getKeyStroke​(char keyChar,
boolean onKeyRelease)
```

Deprecated.

use getKeyStroke(char)

Returns an instance of a KeyStroke, specifying whether the key is
considered to be activated when it is pressed or released. Unlike all
other factory methods in this class, the instances returned by this
method are not necessarily cached or shared.

**Parameters:** keyChar

- the character value for a keyboard key
**Parameters:** onKeyRelease

-

true

if this KeyStroke corresponds to a
key release;

false

otherwise.
**Returns:** a KeyStroke object for that key

---

#### getKeyStroke

@Deprecated

public static

KeyStroke

getKeyStroke​(char keyChar,
boolean onKeyRelease)

Returns an instance of a KeyStroke, specifying whether the key is
considered to be activated when it is pressed or released. Unlike all
other factory methods in this class, the instances returned by this
method are not necessarily cached or shared.

getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(
Character
keyChar,
int modifiers)
```

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers. Note that the first parameter is of type Character
rather than char. This is to avoid inadvertent clashes with calls to

getKeyStroke(int keyCode, int modifiers)

.

The modifiers consist of any combination of following:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers listed below also can be used, but they are
mapped to _DOWN_ modifiers.

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyChar

- the Character object for a keyboard character
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Returns:** an KeyStroke object for that key
**Throws:** IllegalArgumentException

- if keyChar is null
**Since:** 1.3
**See Also:** InputEvent

---

#### getKeyStroke

public static

KeyStroke

getKeyStroke​(

Character

keyChar,
int modifiers)

Returns a shared instance of a

KeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a
set of modifiers. Note that the first parameter is of type Character
rather than char. This is to avoid inadvertent clashes with calls to

getKeyStroke(int keyCode, int modifiers)

.

The modifiers consist of any combination of following:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers listed below also can be used, but they are
mapped to _DOWN_ modifiers.

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)
```

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyCode

- an int specifying the numeric code for a keyboard key
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Parameters:** onKeyRelease

-

true

if the KeyStroke should represent
a key release;

false

otherwise.
**Returns:** a KeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

---

#### getKeyStroke

public static

KeyStroke

getKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers, specifying whether the key is activated when it is
pressed or released.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(int keyCode,
int modifiers)
```

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers. The returned KeyStroke will correspond to a key press.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

**Parameters:** keyCode

- an int specifying the numeric code for a keyboard key
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Returns:** a KeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

---

#### getKeyStroke

public static

KeyStroke

getKeyStroke​(int keyCode,
int modifiers)

Returns a shared instance of a KeyStroke, given a numeric key code and a
set of modifiers. The returned KeyStroke will correspond to a key press.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

The "virtual key" constants defined in java.awt.event.KeyEvent can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

Alternatively, the key code may be obtained by calling

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.

The modifiers consist of any combination of:

- java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

The old modifiers

- java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

also can be used, but they are mapped to _DOWN_ modifiers.

Since these numbers are all different powers of two, any combination of
them is an integer in which each bit represents a different modifier
key. Use 0 to specify no modifiers.

java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

java.awt.event.InputEvent.SHIFT_DOWN_MASK

java.awt.event.InputEvent.CTRL_DOWN_MASK

java.awt.event.InputEvent.META_DOWN_MASK

java.awt.event.InputEvent.ALT_DOWN_MASK

java.awt.event.InputEvent.ALT_GRAPH_DOWN_MASK

java.awt.event.InputEvent.SHIFT_MASK

java.awt.event.InputEvent.CTRL_MASK

java.awt.event.InputEvent.META_MASK

java.awt.event.InputEvent.ALT_MASK

java.awt.event.InputEvent.ALT_GRAPH_MASK

getKeyStrokeForEvent

```java
public static
KeyStroke
getKeyStrokeForEvent​(
KeyEvent
anEvent)
```

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

This method obtains the keyChar from a KeyTyped event, and the keyCode
from a KeyPressed or KeyReleased event. The KeyEvent modifiers are
obtained for all three types of KeyEvent.

**Parameters:** anEvent

- the KeyEvent from which to obtain the KeyStroke
**Returns:** the KeyStroke that precipitated the event
**Throws:** NullPointerException

- if

anEvent

is null

---

#### getKeyStrokeForEvent

public static

KeyStroke

getKeyStrokeForEvent​(

KeyEvent

anEvent)

Returns a KeyStroke which represents the stroke which generated a given
KeyEvent.

This method obtains the keyChar from a KeyTyped event, and the keyCode
from a KeyPressed or KeyReleased event. The KeyEvent modifiers are
obtained for all three types of KeyEvent.

This method obtains the keyChar from a KeyTyped event, and the keyCode
from a KeyPressed or KeyReleased event. The KeyEvent modifiers are
obtained for all three types of KeyEvent.

getKeyStroke

```java
public static
KeyStroke
getKeyStroke​(
String
s)
```

Parses a string and returns a

KeyStroke

.
The string must have the following syntax:

```java
<modifiers>* (<typedID> | <pressedReleasedID>)

modifiers := shift | control | ctrl | meta | alt | altGraph
typedID := typed <typedKey>
typedKey := string of length 1 giving Unicode character.
pressedReleasedID := (pressed | released) key
key := KeyEvent key code name, i.e. the name following "VK_".
```

If typed, pressed or released is not specified, pressed is assumed. Here
are some examples:

```java
"INSERT" => getKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getKeyStroke('a');
```

In order to maintain backward-compatibility, specifying a null String,
or a String which is formatted incorrectly, returns null.

**Parameters:** s

- a String formatted as described above
**Returns:** a KeyStroke object for that String, or null if the specified
String is null, or is formatted incorrectly
**See Also:** KeyEvent

---

#### getKeyStroke

public static

KeyStroke

getKeyStroke​(

String

s)

Parses a string and returns a

KeyStroke

.
The string must have the following syntax:

```java
<modifiers>* (<typedID> | <pressedReleasedID>)

modifiers := shift | control | ctrl | meta | alt | altGraph
typedID := typed <typedKey>
typedKey := string of length 1 giving Unicode character.
pressedReleasedID := (pressed | released) key
key := KeyEvent key code name, i.e. the name following "VK_".
```

If typed, pressed or released is not specified, pressed is assumed. Here
are some examples:

```java
"INSERT" => getKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getKeyStroke('a');
```

In order to maintain backward-compatibility, specifying a null String,
or a String which is formatted incorrectly, returns null.

<modifiers>* (<typedID> | <pressedReleasedID>)

modifiers := shift | control | ctrl | meta | alt | altGraph
typedID := typed <typedKey>
typedKey := string of length 1 giving Unicode character.
pressedReleasedID := (pressed | released) key
key := KeyEvent key code name, i.e. the name following "VK_".

"INSERT" => getKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getKeyStroke('a');

---

