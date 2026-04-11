# Class AWTKeyStroke

**Source:** `java.desktop\java\awt\AWTKeyStroke.html`

### Class Description

```java
public class
AWTKeyStroke

extends
Object

implements
Serializable
```

An

AWTKeyStroke

represents a key action on the
keyboard, or equivalent input device.

AWTKeyStroke

s
can correspond to only a press or release of a
particular key, just as

KEY_PRESSED

and

KEY_RELEASED KeyEvent

s do;
alternately, they can correspond to typing a specific Java character, just
as

KEY_TYPED KeyEvent

s do.
In all cases,

AWTKeyStroke

s can specify modifiers
(alt, shift, control, meta, altGraph, or a combination thereof) which must be present
during the action for an exact match.

AWTKeyStrokes

are immutable, and are intended
to be unique. Client code should never create an

AWTKeyStroke

on its own, but should instead use
a variant of

getAWTKeyStroke

. Client use of these factory
methods allows the

AWTKeyStroke

implementation
to cache and share instances efficiently.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AWTKeyStroke()

Constructs an

AWTKeyStroke

with default values.
The default values used are:

AWTKeyStroke default values

Property

Default Value

Key Char

KeyEvent.CHAR_UNDEFINED

Key Code

KeyEvent.VK_UNDEFINED

Modifiers

none

On key release?

false

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**See Also:**
- getAWTKeyStroke(char)

---

#### protected AWTKeyStroke​(char keyChar,
int keyCode,
int modifiers,
boolean onKeyRelease)

Constructs an

AWTKeyStroke

with the specified
values.

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**Parameters:**
- keyChar

- the character value for a keyboard key
- keyCode

- the key code for this

AWTKeyStroke
- modifiers

- a bitwise-ored combination of any modifiers
- onKeyRelease

-

true

if this

AWTKeyStroke

corresponds
to a key release;

false

otherwise

**See Also:**
- getAWTKeyStroke(char)

---

### Method Details

#### @Deprecated

protected static void registerSubclass​(
Class
<?> subclass)

The method has no effect and is only left present to avoid introducing
a binary incompatibility.

**Parameters:**
- subclass

- the new Class of which the factory methods should create
instances

---

#### public static
AWTKeyStroke
getAWTKeyStroke​(char keyChar)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:**
- keyChar

- the character value for a keyboard key

**Returns:**
- an

AWTKeyStroke

object for that key

---

#### public static
AWTKeyStroke
getAWTKeyStroke​(
Character
keyChar,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers. Note
that the first parameter is of type Character rather than
char. This is to avoid inadvertent clashes with
calls to

getAWTKeyStroke(int keyCode, int modifiers)

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
- an

AWTKeyStroke

object for that key

**Throws:**
- IllegalArgumentException

- if

keyChar

is

null

**See Also:**
- InputEvent

---

#### public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
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

if the

AWTKeyStroke

should represent a key release;

false

otherwise

**Returns:**
- an AWTKeyStroke object for that key

**See Also:**
- KeyEvent

,

InputEvent

---

#### public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers. The returned

AWTKeyStroke

will correspond to a key press.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

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
- an

AWTKeyStroke

object for that key

**See Also:**
- KeyEvent

,

InputEvent

---

#### public static
AWTKeyStroke
getAWTKeyStrokeForEvent​(
KeyEvent
anEvent)

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

This method obtains the keyChar from a

KeyTyped

event, and the keyCode from a

KeyPressed

or

KeyReleased

event. The

KeyEvent

modifiers are
obtained for all three types of

KeyEvent

.

**Parameters:**
- anEvent

- the

KeyEvent

from which to
obtain the

AWTKeyStroke

**Returns:**
- the

AWTKeyStroke

that precipitated the event

**Throws:**
- NullPointerException

- if

anEvent

is null

---

#### public static
AWTKeyStroke
getAWTKeyStroke​(
String
s)

Parses a string and returns an

AWTKeyStroke

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
"INSERT" => getAWTKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getAWTKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getAWTKeyStroke('a');
```

**Parameters:**
- s

- a String formatted as described above

**Returns:**
- an

AWTKeyStroke

object for that String

**Throws:**
- IllegalArgumentException

- if

s

is

null

,
or is formatted incorrectly

---

#### public final char getKeyChar()

Returns the character for this

AWTKeyStroke

.

**Returns:**
- a char value

**See Also:**
- getAWTKeyStroke(char)

,

KeyEvent.getKeyChar()

---

#### public final int getKeyCode()

Returns the numeric key code for this

AWTKeyStroke

.

**Returns:**
- an int containing the key code value

**See Also:**
- getAWTKeyStroke(int,int)

,

KeyEvent.getKeyCode()

---

#### public final int getModifiers()

Returns the modifier keys for this

AWTKeyStroke

.

**Returns:**
- an int containing the modifiers

**See Also:**
- getAWTKeyStroke(int,int)

---

#### public final boolean isOnKeyRelease()

Returns whether this

AWTKeyStroke

represents a key release.

**Returns:**
- true

if this

AWTKeyStroke

represents a key release;

false

otherwise

**See Also:**
- getAWTKeyStroke(int,int,boolean)

---

#### public final int getKeyEventType()

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

**Returns:**
- KeyEvent.KEY_PRESSED

,

KeyEvent.KEY_TYPED

,
or

KeyEvent.KEY_RELEASED

**See Also:**
- KeyEvent

---

#### public int hashCode()

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- an int that represents this object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public final boolean equals​(
Object
anObject)

Returns true if this object is identical to the specified object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- anObject

- the Object to compare this object to

**Returns:**
- true if the objects are identical

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string that displays and identifies this object's properties.
The

String

returned by this method can be passed
as a parameter to

getAWTKeyStroke(String)

to produce
a key stroke equal to this key stroke.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this object

**See Also:**
- getAWTKeyStroke(String)

---

#### protected
Object
readResolve()
throws
ObjectStreamException

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

**Returns:**
- a cached instance which is equal to this instance

**Throws:**
- ObjectStreamException

- if a serialization problem occurs

---

### Additional Sections

#### Class AWTKeyStroke

java.lang.Object

- java.awt.AWTKeyStroke

java.awt.AWTKeyStroke

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** KeyStroke

```java
public class
AWTKeyStroke

extends
Object

implements
Serializable
```

An

AWTKeyStroke

represents a key action on the
keyboard, or equivalent input device.

AWTKeyStroke

s
can correspond to only a press or release of a
particular key, just as

KEY_PRESSED

and

KEY_RELEASED KeyEvent

s do;
alternately, they can correspond to typing a specific Java character, just
as

KEY_TYPED KeyEvent

s do.
In all cases,

AWTKeyStroke

s can specify modifiers
(alt, shift, control, meta, altGraph, or a combination thereof) which must be present
during the action for an exact match.

AWTKeyStrokes

are immutable, and are intended
to be unique. Client code should never create an

AWTKeyStroke

on its own, but should instead use
a variant of

getAWTKeyStroke

. Client use of these factory
methods allows the

AWTKeyStroke

implementation
to cache and share instances efficiently.

**Since:** 1.4
**See Also:** getAWTKeyStroke(char)

,

Serialized Form

public class

AWTKeyStroke

extends

Object

implements

Serializable

An

AWTKeyStroke

represents a key action on the
keyboard, or equivalent input device.

AWTKeyStroke

s
can correspond to only a press or release of a
particular key, just as

KEY_PRESSED

and

KEY_RELEASED KeyEvent

s do;
alternately, they can correspond to typing a specific Java character, just
as

KEY_TYPED KeyEvent

s do.
In all cases,

AWTKeyStroke

s can specify modifiers
(alt, shift, control, meta, altGraph, or a combination thereof) which must be present
during the action for an exact match.

AWTKeyStrokes

are immutable, and are intended
to be unique. Client code should never create an

AWTKeyStroke

on its own, but should instead use
a variant of

getAWTKeyStroke

. Client use of these factory
methods allows the

AWTKeyStroke

implementation
to cache and share instances efficiently.

AWTKeyStrokes

are immutable, and are intended
to be unique. Client code should never create an

AWTKeyStroke

on its own, but should instead use
a variant of

getAWTKeyStroke

. Client use of these factory
methods allows the

AWTKeyStroke

implementation
to cache and share instances efficiently.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AWTKeyStroke

()

Constructs an

AWTKeyStroke

with default values.

protected

AWTKeyStroke

​(char keyChar,
int keyCode,
int modifiers,
boolean onKeyRelease)

Constructs an

AWTKeyStroke

with the specified
values.

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

boolean

equals

​(

Object

anObject)

Returns true if this object is identical to the specified object.

static

AWTKeyStroke

getAWTKeyStroke

​(char keyChar)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

static

AWTKeyStroke

getAWTKeyStroke

​(int keyCode,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers.

static

AWTKeyStroke

getAWTKeyStroke

​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

static

AWTKeyStroke

getAWTKeyStroke

​(

Character

keyChar,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers.

static

AWTKeyStroke

getAWTKeyStroke

​(

String

s)

Parses a string and returns an

AWTKeyStroke

.

static

AWTKeyStroke

getAWTKeyStrokeForEvent

​(

KeyEvent

anEvent)

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

char

getKeyChar

()

Returns the character for this

AWTKeyStroke

.

int

getKeyCode

()

Returns the numeric key code for this

AWTKeyStroke

.

int

getKeyEventType

()

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

int

getModifiers

()

Returns the modifier keys for this

AWTKeyStroke

.

int

hashCode

()

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

boolean

isOnKeyRelease

()

Returns whether this

AWTKeyStroke

represents a key release.

protected

Object

readResolve

()

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

protected static void

registerSubclass

​(

Class

<?> subclass)

Deprecated.

String

toString

()

Returns a string that displays and identifies this object's properties.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AWTKeyStroke

()

Constructs an

AWTKeyStroke

with default values.

protected

AWTKeyStroke

​(char keyChar,
int keyCode,
int modifiers,
boolean onKeyRelease)

Constructs an

AWTKeyStroke

with the specified
values.

---

#### Constructor Summary

Constructs an

AWTKeyStroke

with default values.

Constructs an

AWTKeyStroke

with the specified
values.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

anObject)

Returns true if this object is identical to the specified object.

static

AWTKeyStroke

getAWTKeyStroke

​(char keyChar)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

static

AWTKeyStroke

getAWTKeyStroke

​(int keyCode,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers.

static

AWTKeyStroke

getAWTKeyStroke

​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

static

AWTKeyStroke

getAWTKeyStroke

​(

Character

keyChar,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers.

static

AWTKeyStroke

getAWTKeyStroke

​(

String

s)

Parses a string and returns an

AWTKeyStroke

.

static

AWTKeyStroke

getAWTKeyStrokeForEvent

​(

KeyEvent

anEvent)

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

char

getKeyChar

()

Returns the character for this

AWTKeyStroke

.

int

getKeyCode

()

Returns the numeric key code for this

AWTKeyStroke

.

int

getKeyEventType

()

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

int

getModifiers

()

Returns the modifier keys for this

AWTKeyStroke

.

int

hashCode

()

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

boolean

isOnKeyRelease

()

Returns whether this

AWTKeyStroke

represents a key release.

protected

Object

readResolve

()

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

protected static void

registerSubclass

​(

Class

<?> subclass)

Deprecated.

String

toString

()

Returns a string that displays and identifies this object's properties.

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

Returns true if this object is identical to the specified object.

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers.

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers.

Parses a string and returns an

AWTKeyStroke

.

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

Returns the character for this

AWTKeyStroke

.

Returns the numeric key code for this

AWTKeyStroke

.

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

Returns the modifier keys for this

AWTKeyStroke

.

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

Returns whether this

AWTKeyStroke

represents a key release.

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

Deprecated.

Returns a string that displays and identifies this object's properties.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AWTKeyStroke

```java
protected AWTKeyStroke()
```

Constructs an

AWTKeyStroke

with default values.
The default values used are:

AWTKeyStroke default values

Property

Default Value

Key Char

KeyEvent.CHAR_UNDEFINED

Key Code

KeyEvent.VK_UNDEFINED

Modifiers

none

On key release?

false

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**See Also:** getAWTKeyStroke(char)

- AWTKeyStroke

```java
protected AWTKeyStroke​(char keyChar,
int keyCode,
int modifiers,
boolean onKeyRelease)
```

Constructs an

AWTKeyStroke

with the specified
values.

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**Parameters:** keyChar

- the character value for a keyboard key
**Parameters:** keyCode

- the key code for this

AWTKeyStroke
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Parameters:** onKeyRelease

-

true

if this

AWTKeyStroke

corresponds
to a key release;

false

otherwise
**See Also:** getAWTKeyStroke(char)

============ METHOD DETAIL ==========

- Method Detail

- registerSubclass

```java
@Deprecated

protected static void registerSubclass​(
Class
<?> subclass)
```

Deprecated.

The method has no effect and is only left present to avoid introducing
a binary incompatibility.

**Parameters:** subclass

- the new Class of which the factory methods should create
instances

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(char keyChar)
```

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:** keyChar

- the character value for a keyboard key
**Returns:** an

AWTKeyStroke

object for that key

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(
Character
keyChar,
int modifiers)
```

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers. Note
that the first parameter is of type Character rather than
char. This is to avoid inadvertent clashes with
calls to

getAWTKeyStroke(int keyCode, int modifiers)

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
**Returns:** an

AWTKeyStroke

object for that key
**Throws:** IllegalArgumentException

- if

keyChar

is

null
**See Also:** InputEvent

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)
```

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
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

if the

AWTKeyStroke

should represent a key release;

false

otherwise
**Returns:** an AWTKeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers)
```

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers. The returned

AWTKeyStroke

will correspond to a key press.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

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
**Returns:** an

AWTKeyStroke

object for that key
**See Also:** KeyEvent

,

InputEvent

- getAWTKeyStrokeForEvent

```java
public static
AWTKeyStroke
getAWTKeyStrokeForEvent​(
KeyEvent
anEvent)
```

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

This method obtains the keyChar from a

KeyTyped

event, and the keyCode from a

KeyPressed

or

KeyReleased

event. The

KeyEvent

modifiers are
obtained for all three types of

KeyEvent

.

**Parameters:** anEvent

- the

KeyEvent

from which to
obtain the

AWTKeyStroke
**Returns:** the

AWTKeyStroke

that precipitated the event
**Throws:** NullPointerException

- if

anEvent

is null

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(
String
s)
```

Parses a string and returns an

AWTKeyStroke

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
"INSERT" => getAWTKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getAWTKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getAWTKeyStroke('a');
```

**Parameters:** s

- a String formatted as described above
**Returns:** an

AWTKeyStroke

object for that String
**Throws:** IllegalArgumentException

- if

s

is

null

,
or is formatted incorrectly

- getKeyChar

```java
public final char getKeyChar()
```

Returns the character for this

AWTKeyStroke

.

**Returns:** a char value
**See Also:** getAWTKeyStroke(char)

,

KeyEvent.getKeyChar()

- getKeyCode

```java
public final int getKeyCode()
```

Returns the numeric key code for this

AWTKeyStroke

.

**Returns:** an int containing the key code value
**See Also:** getAWTKeyStroke(int,int)

,

KeyEvent.getKeyCode()

- getModifiers

```java
public final int getModifiers()
```

Returns the modifier keys for this

AWTKeyStroke

.

**Returns:** an int containing the modifiers
**See Also:** getAWTKeyStroke(int,int)

- isOnKeyRelease

```java
public final boolean isOnKeyRelease()
```

Returns whether this

AWTKeyStroke

represents a key release.

**Returns:** true

if this

AWTKeyStroke

represents a key release;

false

otherwise
**See Also:** getAWTKeyStroke(int,int,boolean)

- getKeyEventType

```java
public final int getKeyEventType()
```

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

**Returns:** KeyEvent.KEY_PRESSED

,

KeyEvent.KEY_TYPED

,
or

KeyEvent.KEY_RELEASED
**See Also:** KeyEvent

- hashCode

```java
public int hashCode()
```

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

**Overrides:** hashCode

in class

Object
**Returns:** an int that represents this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public final boolean equals​(
Object
anObject)
```

Returns true if this object is identical to the specified object.

**Overrides:** equals

in class

Object
**Parameters:** anObject

- the Object to compare this object to
**Returns:** true if the objects are identical
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this object's properties.
The

String

returned by this method can be passed
as a parameter to

getAWTKeyStroke(String)

to produce
a key stroke equal to this key stroke.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object
**See Also:** getAWTKeyStroke(String)

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

**Returns:** a cached instance which is equal to this instance
**Throws:** ObjectStreamException

- if a serialization problem occurs

Constructor Detail

- AWTKeyStroke

```java
protected AWTKeyStroke()
```

Constructs an

AWTKeyStroke

with default values.
The default values used are:

AWTKeyStroke default values

Property

Default Value

Key Char

KeyEvent.CHAR_UNDEFINED

Key Code

KeyEvent.VK_UNDEFINED

Modifiers

none

On key release?

false

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**See Also:** getAWTKeyStroke(char)

- AWTKeyStroke

```java
protected AWTKeyStroke​(char keyChar,
int keyCode,
int modifiers,
boolean onKeyRelease)
```

Constructs an

AWTKeyStroke

with the specified
values.

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**Parameters:** keyChar

- the character value for a keyboard key
**Parameters:** keyCode

- the key code for this

AWTKeyStroke
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Parameters:** onKeyRelease

-

true

if this

AWTKeyStroke

corresponds
to a key release;

false

otherwise
**See Also:** getAWTKeyStroke(char)

---

#### Constructor Detail

AWTKeyStroke

```java
protected AWTKeyStroke()
```

Constructs an

AWTKeyStroke

with default values.
The default values used are:

AWTKeyStroke default values

Property

Default Value

Key Char

KeyEvent.CHAR_UNDEFINED

Key Code

KeyEvent.VK_UNDEFINED

Modifiers

none

On key release?

false

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**See Also:** getAWTKeyStroke(char)

---

#### AWTKeyStroke

protected AWTKeyStroke()

Constructs an

AWTKeyStroke

with default values.
The default values used are:

AWTKeyStroke default values

Property

Default Value

Key Char

KeyEvent.CHAR_UNDEFINED

Key Code

KeyEvent.VK_UNDEFINED

Modifiers

none

On key release?

false

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

AWTKeyStroke

```java
protected AWTKeyStroke​(char keyChar,
int keyCode,
int modifiers,
boolean onKeyRelease)
```

Constructs an

AWTKeyStroke

with the specified
values.

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

**Parameters:** keyChar

- the character value for a keyboard key
**Parameters:** keyCode

- the key code for this

AWTKeyStroke
**Parameters:** modifiers

- a bitwise-ored combination of any modifiers
**Parameters:** onKeyRelease

-

true

if this

AWTKeyStroke

corresponds
to a key release;

false

otherwise
**See Also:** getAWTKeyStroke(char)

---

#### AWTKeyStroke

protected AWTKeyStroke​(char keyChar,
int keyCode,
int modifiers,
boolean onKeyRelease)

Constructs an

AWTKeyStroke

with the specified
values.

AWTKeyStroke

s should not be constructed
by client code. Use a variant of

getAWTKeyStroke

instead.

Method Detail

- registerSubclass

```java
@Deprecated

protected static void registerSubclass​(
Class
<?> subclass)
```

Deprecated.

The method has no effect and is only left present to avoid introducing
a binary incompatibility.

**Parameters:** subclass

- the new Class of which the factory methods should create
instances

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(char keyChar)
```

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:** keyChar

- the character value for a keyboard key
**Returns:** an

AWTKeyStroke

object for that key

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(
Character
keyChar,
int modifiers)
```

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers. Note
that the first parameter is of type Character rather than
char. This is to avoid inadvertent clashes with
calls to

getAWTKeyStroke(int keyCode, int modifiers)

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
**Returns:** an

AWTKeyStroke

object for that key
**Throws:** IllegalArgumentException

- if

keyChar

is

null
**See Also:** InputEvent

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)
```

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
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

if the

AWTKeyStroke

should represent a key release;

false

otherwise
**Returns:** an AWTKeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers)
```

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers. The returned

AWTKeyStroke

will correspond to a key press.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

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
**Returns:** an

AWTKeyStroke

object for that key
**See Also:** KeyEvent

,

InputEvent

- getAWTKeyStrokeForEvent

```java
public static
AWTKeyStroke
getAWTKeyStrokeForEvent​(
KeyEvent
anEvent)
```

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

This method obtains the keyChar from a

KeyTyped

event, and the keyCode from a

KeyPressed

or

KeyReleased

event. The

KeyEvent

modifiers are
obtained for all three types of

KeyEvent

.

**Parameters:** anEvent

- the

KeyEvent

from which to
obtain the

AWTKeyStroke
**Returns:** the

AWTKeyStroke

that precipitated the event
**Throws:** NullPointerException

- if

anEvent

is null

- getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(
String
s)
```

Parses a string and returns an

AWTKeyStroke

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
"INSERT" => getAWTKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getAWTKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getAWTKeyStroke('a');
```

**Parameters:** s

- a String formatted as described above
**Returns:** an

AWTKeyStroke

object for that String
**Throws:** IllegalArgumentException

- if

s

is

null

,
or is formatted incorrectly

- getKeyChar

```java
public final char getKeyChar()
```

Returns the character for this

AWTKeyStroke

.

**Returns:** a char value
**See Also:** getAWTKeyStroke(char)

,

KeyEvent.getKeyChar()

- getKeyCode

```java
public final int getKeyCode()
```

Returns the numeric key code for this

AWTKeyStroke

.

**Returns:** an int containing the key code value
**See Also:** getAWTKeyStroke(int,int)

,

KeyEvent.getKeyCode()

- getModifiers

```java
public final int getModifiers()
```

Returns the modifier keys for this

AWTKeyStroke

.

**Returns:** an int containing the modifiers
**See Also:** getAWTKeyStroke(int,int)

- isOnKeyRelease

```java
public final boolean isOnKeyRelease()
```

Returns whether this

AWTKeyStroke

represents a key release.

**Returns:** true

if this

AWTKeyStroke

represents a key release;

false

otherwise
**See Also:** getAWTKeyStroke(int,int,boolean)

- getKeyEventType

```java
public final int getKeyEventType()
```

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

**Returns:** KeyEvent.KEY_PRESSED

,

KeyEvent.KEY_TYPED

,
or

KeyEvent.KEY_RELEASED
**See Also:** KeyEvent

- hashCode

```java
public int hashCode()
```

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

**Overrides:** hashCode

in class

Object
**Returns:** an int that represents this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public final boolean equals​(
Object
anObject)
```

Returns true if this object is identical to the specified object.

**Overrides:** equals

in class

Object
**Parameters:** anObject

- the Object to compare this object to
**Returns:** true if the objects are identical
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this object's properties.
The

String

returned by this method can be passed
as a parameter to

getAWTKeyStroke(String)

to produce
a key stroke equal to this key stroke.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object
**See Also:** getAWTKeyStroke(String)

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

**Returns:** a cached instance which is equal to this instance
**Throws:** ObjectStreamException

- if a serialization problem occurs

---

#### Method Detail

registerSubclass

```java
@Deprecated

protected static void registerSubclass​(
Class
<?> subclass)
```

Deprecated.

The method has no effect and is only left present to avoid introducing
a binary incompatibility.

**Parameters:** subclass

- the new Class of which the factory methods should create
instances

---

#### registerSubclass

@Deprecated

protected static void registerSubclass​(

Class

<?> subclass)

The method has no effect and is only left present to avoid introducing
a binary incompatibility.

getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(char keyChar)
```

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

**Parameters:** keyChar

- the character value for a keyboard key
**Returns:** an

AWTKeyStroke

object for that key

---

#### getAWTKeyStroke

public static

AWTKeyStroke

getAWTKeyStroke​(char keyChar)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified character.

getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(
Character
keyChar,
int modifiers)
```

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers. Note
that the first parameter is of type Character rather than
char. This is to avoid inadvertent clashes with
calls to

getAWTKeyStroke(int keyCode, int modifiers)

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
**Returns:** an

AWTKeyStroke

object for that key
**Throws:** IllegalArgumentException

- if

keyChar

is

null
**See Also:** InputEvent

---

#### getAWTKeyStroke

public static

AWTKeyStroke

getAWTKeyStroke​(

Character

keyChar,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

that represents a

KEY_TYPED

event for the
specified Character object and a set of modifiers. Note
that the first parameter is of type Character rather than
char. This is to avoid inadvertent clashes with
calls to

getAWTKeyStroke(int keyCode, int modifiers)

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

getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)
```

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
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

if the

AWTKeyStroke

should represent a key release;

false

otherwise
**Returns:** an AWTKeyStroke object for that key
**See Also:** KeyEvent

,

InputEvent

---

#### getAWTKeyStroke

public static

AWTKeyStroke

getAWTKeyStroke​(int keyCode,
int modifiers,
boolean onKeyRelease)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers, specifying
whether the key is activated when it is pressed or released.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
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

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
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

getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(int keyCode,
int modifiers)
```

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers. The returned

AWTKeyStroke

will correspond to a key press.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

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
**Returns:** an

AWTKeyStroke

object for that key
**See Also:** KeyEvent

,

InputEvent

---

#### getAWTKeyStroke

public static

AWTKeyStroke

getAWTKeyStroke​(int keyCode,
int modifiers)

Returns a shared instance of an

AWTKeyStroke

,
given a numeric key code and a set of modifiers. The returned

AWTKeyStroke

will correspond to a key press.

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

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

The "virtual key" constants defined in

java.awt.event.KeyEvent

can be
used to specify the key code. For example:

- java.awt.event.KeyEvent.VK_ENTER

java.awt.event.KeyEvent.VK_TAB

java.awt.event.KeyEvent.VK_SPACE

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

getAWTKeyStrokeForEvent

```java
public static
AWTKeyStroke
getAWTKeyStrokeForEvent​(
KeyEvent
anEvent)
```

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

This method obtains the keyChar from a

KeyTyped

event, and the keyCode from a

KeyPressed

or

KeyReleased

event. The

KeyEvent

modifiers are
obtained for all three types of

KeyEvent

.

**Parameters:** anEvent

- the

KeyEvent

from which to
obtain the

AWTKeyStroke
**Returns:** the

AWTKeyStroke

that precipitated the event
**Throws:** NullPointerException

- if

anEvent

is null

---

#### getAWTKeyStrokeForEvent

public static

AWTKeyStroke

getAWTKeyStrokeForEvent​(

KeyEvent

anEvent)

Returns an

AWTKeyStroke

which represents the
stroke which generated a given

KeyEvent

.

This method obtains the keyChar from a

KeyTyped

event, and the keyCode from a

KeyPressed

or

KeyReleased

event. The

KeyEvent

modifiers are
obtained for all three types of

KeyEvent

.

This method obtains the keyChar from a

KeyTyped

event, and the keyCode from a

KeyPressed

or

KeyReleased

event. The

KeyEvent

modifiers are
obtained for all three types of

KeyEvent

.

getAWTKeyStroke

```java
public static
AWTKeyStroke
getAWTKeyStroke​(
String
s)
```

Parses a string and returns an

AWTKeyStroke

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
"INSERT" => getAWTKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getAWTKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getAWTKeyStroke('a');
```

**Parameters:** s

- a String formatted as described above
**Returns:** an

AWTKeyStroke

object for that String
**Throws:** IllegalArgumentException

- if

s

is

null

,
or is formatted incorrectly

---

#### getAWTKeyStroke

public static

AWTKeyStroke

getAWTKeyStroke​(

String

s)

Parses a string and returns an

AWTKeyStroke

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
"INSERT" => getAWTKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getAWTKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getAWTKeyStroke('a');
```

<modifiers>* (<typedID> | <pressedReleasedID>)

modifiers := shift | control | ctrl | meta | alt | altGraph
typedID := typed <typedKey>
typedKey := string of length 1 giving Unicode character.
pressedReleasedID := (pressed | released) key
key := KeyEvent key code name, i.e. the name following "VK_".

"INSERT" => getAWTKeyStroke(KeyEvent.VK_INSERT, 0);
"control DELETE" => getAWTKeyStroke(KeyEvent.VK_DELETE, InputEvent.CTRL_MASK);
"alt shift X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK);
"alt shift released X" => getAWTKeyStroke(KeyEvent.VK_X, InputEvent.ALT_MASK | InputEvent.SHIFT_MASK, true);
"typed a" => getAWTKeyStroke('a');

getKeyChar

```java
public final char getKeyChar()
```

Returns the character for this

AWTKeyStroke

.

**Returns:** a char value
**See Also:** getAWTKeyStroke(char)

,

KeyEvent.getKeyChar()

---

#### getKeyChar

public final char getKeyChar()

Returns the character for this

AWTKeyStroke

.

getKeyCode

```java
public final int getKeyCode()
```

Returns the numeric key code for this

AWTKeyStroke

.

**Returns:** an int containing the key code value
**See Also:** getAWTKeyStroke(int,int)

,

KeyEvent.getKeyCode()

---

#### getKeyCode

public final int getKeyCode()

Returns the numeric key code for this

AWTKeyStroke

.

getModifiers

```java
public final int getModifiers()
```

Returns the modifier keys for this

AWTKeyStroke

.

**Returns:** an int containing the modifiers
**See Also:** getAWTKeyStroke(int,int)

---

#### getModifiers

public final int getModifiers()

Returns the modifier keys for this

AWTKeyStroke

.

isOnKeyRelease

```java
public final boolean isOnKeyRelease()
```

Returns whether this

AWTKeyStroke

represents a key release.

**Returns:** true

if this

AWTKeyStroke

represents a key release;

false

otherwise
**See Also:** getAWTKeyStroke(int,int,boolean)

---

#### isOnKeyRelease

public final boolean isOnKeyRelease()

Returns whether this

AWTKeyStroke

represents a key release.

getKeyEventType

```java
public final int getKeyEventType()
```

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

**Returns:** KeyEvent.KEY_PRESSED

,

KeyEvent.KEY_TYPED

,
or

KeyEvent.KEY_RELEASED
**See Also:** KeyEvent

---

#### getKeyEventType

public final int getKeyEventType()

Returns the type of

KeyEvent

which corresponds to
this

AWTKeyStroke

.

hashCode

```java
public int hashCode()
```

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

**Overrides:** hashCode

in class

Object
**Returns:** an int that represents this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a numeric value for this object that is likely to be unique,
making it a good choice as the index value in a hash table.

equals

```java
public final boolean equals​(
Object
anObject)
```

Returns true if this object is identical to the specified object.

**Overrides:** equals

in class

Object
**Parameters:** anObject

- the Object to compare this object to
**Returns:** true if the objects are identical
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

anObject)

Returns true if this object is identical to the specified object.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this object's properties.
The

String

returned by this method can be passed
as a parameter to

getAWTKeyStroke(String)

to produce
a key stroke equal to this key stroke.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object
**See Also:** getAWTKeyStroke(String)

---

#### toString

public

String

toString()

Returns a string that displays and identifies this object's properties.
The

String

returned by this method can be passed
as a parameter to

getAWTKeyStroke(String)

to produce
a key stroke equal to this key stroke.

readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

**Returns:** a cached instance which is equal to this instance
**Throws:** ObjectStreamException

- if a serialization problem occurs

---

#### readResolve

protected

Object

readResolve()
throws

ObjectStreamException

Returns a cached instance of

AWTKeyStroke

(or a subclass of

AWTKeyStroke

) which is equal to this instance.

---

