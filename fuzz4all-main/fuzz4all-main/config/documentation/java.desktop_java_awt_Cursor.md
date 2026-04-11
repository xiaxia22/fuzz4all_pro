# Class Cursor

**Source:** `java.desktop\java\awt\Cursor.html`

### Class Description

```java
public class
Cursor

extends
Object

implements
Serializable
```

A class to encapsulate the bitmap representation of the mouse cursor.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int DEFAULT_CURSOR

The default cursor type (gets set if no cursor is defined).

**See Also:**
- Constant Field Values

---

#### public static final int CROSSHAIR_CURSOR

The crosshair cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int TEXT_CURSOR

The text cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int WAIT_CURSOR

The wait cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int SW_RESIZE_CURSOR

The south-west-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int SE_RESIZE_CURSOR

The south-east-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int NW_RESIZE_CURSOR

The north-west-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int NE_RESIZE_CURSOR

The north-east-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int N_RESIZE_CURSOR

The north-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int S_RESIZE_CURSOR

The south-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int W_RESIZE_CURSOR

The west-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int E_RESIZE_CURSOR

The east-resize cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int HAND_CURSOR

The hand cursor type.

**See Also:**
- Constant Field Values

---

#### public static final int MOVE_CURSOR

The move cursor type.

**See Also:**
- Constant Field Values

---

#### @Deprecated

protected static
Cursor
[] predefined

*No description found.*

---

#### public static final int CUSTOM_CURSOR

The type associated with all custom cursors.

**See Also:**
- Constant Field Values

---

#### protected
String
name

The user-visible name of the cursor.

**See Also:**
- getName()

---

### Constructor Details

#### @ConstructorProperties
("type")
public Cursor​(int type)

Creates a new cursor object with the specified type.

**Parameters:**
- type

- the type of cursor

**Throws:**
- IllegalArgumentException

- if the specified cursor type
is invalid

---

#### protected Cursor​(
String
name)

Creates a new custom cursor object with the specified name.

Note: this constructor should only be used by AWT implementations
as part of their support for custom cursors. Applications should
use Toolkit.createCustomCursor().

**Parameters:**
- name

- the user-visible name of the cursor.

**See Also:**
- Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

---

### Method Details

#### public static
Cursor
getPredefinedCursor​(int type)

Returns a cursor object with the specified predefined type.

**Parameters:**
- type

- the type of predefined cursor

**Returns:**
- the specified predefined cursor

**Throws:**
- IllegalArgumentException

- if the specified cursor type is
invalid

---

#### public static
Cursor
getSystemCustomCursor​(
String
name)
throws
AWTException
,

HeadlessException

Returns a system-specific custom cursor object matching the
specified name. Cursor names are, for example: "Invalid.16x16"

**Parameters:**
- name

- a string describing the desired system-specific custom cursor

**Returns:**
- the system specific custom cursor named

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
- AWTException

- in case of erroneous retrieving of the cursor

---

#### public static
Cursor
getDefaultCursor()

Return the system default cursor.

**Returns:**
- the default cursor

---

#### public int getType()

Returns the type for this cursor.

**Returns:**
- the cursor type

---

#### public
String
getName()

Returns the name of this cursor.

**Returns:**
- a localized description of this cursor.

**Since:**
- 1.2

---

#### public
String
toString()

Returns a string representation of this cursor.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this cursor.

**Since:**
- 1.2

---

### Additional Sections

#### Class Cursor

java.lang.Object

- java.awt.Cursor

java.awt.Cursor

**All Implemented Interfaces:** Serializable

```java
public class
Cursor

extends
Object

implements
Serializable
```

A class to encapsulate the bitmap representation of the mouse cursor.

**See Also:** Component.setCursor(java.awt.Cursor)

,

Serialized Form

public class

Cursor

extends

Object

implements

Serializable

A class to encapsulate the bitmap representation of the mouse cursor.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CROSSHAIR_CURSOR

The crosshair cursor type.

static int

CUSTOM_CURSOR

The type associated with all custom cursors.

static int

DEFAULT_CURSOR

The default cursor type (gets set if no cursor is defined).

static int

E_RESIZE_CURSOR

The east-resize cursor type.

static int

HAND_CURSOR

The hand cursor type.

static int

MOVE_CURSOR

The move cursor type.

static int

N_RESIZE_CURSOR

The north-resize cursor type.

protected

String

name

The user-visible name of the cursor.

static int

NE_RESIZE_CURSOR

The north-east-resize cursor type.

static int

NW_RESIZE_CURSOR

The north-west-resize cursor type.

protected static

Cursor

[]

predefined

Deprecated.

As of JDK version 1.7, the

getPredefinedCursor(int)

method should be used instead.

static int

S_RESIZE_CURSOR

The south-resize cursor type.

static int

SE_RESIZE_CURSOR

The south-east-resize cursor type.

static int

SW_RESIZE_CURSOR

The south-west-resize cursor type.

static int

TEXT_CURSOR

The text cursor type.

static int

W_RESIZE_CURSOR

The west-resize cursor type.

static int

WAIT_CURSOR

The wait cursor type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

Cursor

​(int type)

Creates a new cursor object with the specified type.

protected

Cursor

​(

String

name)

Creates a new custom cursor object with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Cursor

getDefaultCursor

()

Return the system default cursor.

String

getName

()

Returns the name of this cursor.

static

Cursor

getPredefinedCursor

​(int type)

Returns a cursor object with the specified predefined type.

static

Cursor

getSystemCustomCursor

​(

String

name)

Returns a system-specific custom cursor object matching the
specified name.

int

getType

()

Returns the type for this cursor.

String

toString

()

Returns a string representation of this cursor.

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

CROSSHAIR_CURSOR

The crosshair cursor type.

static int

CUSTOM_CURSOR

The type associated with all custom cursors.

static int

DEFAULT_CURSOR

The default cursor type (gets set if no cursor is defined).

static int

E_RESIZE_CURSOR

The east-resize cursor type.

static int

HAND_CURSOR

The hand cursor type.

static int

MOVE_CURSOR

The move cursor type.

static int

N_RESIZE_CURSOR

The north-resize cursor type.

protected

String

name

The user-visible name of the cursor.

static int

NE_RESIZE_CURSOR

The north-east-resize cursor type.

static int

NW_RESIZE_CURSOR

The north-west-resize cursor type.

protected static

Cursor

[]

predefined

Deprecated.

As of JDK version 1.7, the

getPredefinedCursor(int)

method should be used instead.

static int

S_RESIZE_CURSOR

The south-resize cursor type.

static int

SE_RESIZE_CURSOR

The south-east-resize cursor type.

static int

SW_RESIZE_CURSOR

The south-west-resize cursor type.

static int

TEXT_CURSOR

The text cursor type.

static int

W_RESIZE_CURSOR

The west-resize cursor type.

static int

WAIT_CURSOR

The wait cursor type.

---

#### Field Summary

The crosshair cursor type.

The type associated with all custom cursors.

The default cursor type (gets set if no cursor is defined).

The east-resize cursor type.

The hand cursor type.

The move cursor type.

The north-resize cursor type.

The user-visible name of the cursor.

The north-east-resize cursor type.

The north-west-resize cursor type.

Deprecated.

As of JDK version 1.7, the

getPredefinedCursor(int)

method should be used instead.

The south-resize cursor type.

The south-east-resize cursor type.

The south-west-resize cursor type.

The text cursor type.

The west-resize cursor type.

The wait cursor type.

Constructor Summary

Constructors

Modifier

Constructor

Description

Cursor

​(int type)

Creates a new cursor object with the specified type.

protected

Cursor

​(

String

name)

Creates a new custom cursor object with the specified name.

---

#### Constructor Summary

Creates a new cursor object with the specified type.

Creates a new custom cursor object with the specified name.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Cursor

getDefaultCursor

()

Return the system default cursor.

String

getName

()

Returns the name of this cursor.

static

Cursor

getPredefinedCursor

​(int type)

Returns a cursor object with the specified predefined type.

static

Cursor

getSystemCustomCursor

​(

String

name)

Returns a system-specific custom cursor object matching the
specified name.

int

getType

()

Returns the type for this cursor.

String

toString

()

Returns a string representation of this cursor.

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

Return the system default cursor.

Returns the name of this cursor.

Returns a cursor object with the specified predefined type.

Returns a system-specific custom cursor object matching the
specified name.

Returns the type for this cursor.

Returns a string representation of this cursor.

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

- DEFAULT_CURSOR

```java
public static final int DEFAULT_CURSOR
```

The default cursor type (gets set if no cursor is defined).

**See Also:** Constant Field Values

- CROSSHAIR_CURSOR

```java
public static final int CROSSHAIR_CURSOR
```

The crosshair cursor type.

**See Also:** Constant Field Values

- TEXT_CURSOR

```java
public static final int TEXT_CURSOR
```

The text cursor type.

**See Also:** Constant Field Values

- WAIT_CURSOR

```java
public static final int WAIT_CURSOR
```

The wait cursor type.

**See Also:** Constant Field Values

- SW_RESIZE_CURSOR

```java
public static final int SW_RESIZE_CURSOR
```

The south-west-resize cursor type.

**See Also:** Constant Field Values

- SE_RESIZE_CURSOR

```java
public static final int SE_RESIZE_CURSOR
```

The south-east-resize cursor type.

**See Also:** Constant Field Values

- NW_RESIZE_CURSOR

```java
public static final int NW_RESIZE_CURSOR
```

The north-west-resize cursor type.

**See Also:** Constant Field Values

- NE_RESIZE_CURSOR

```java
public static final int NE_RESIZE_CURSOR
```

The north-east-resize cursor type.

**See Also:** Constant Field Values

- N_RESIZE_CURSOR

```java
public static final int N_RESIZE_CURSOR
```

The north-resize cursor type.

**See Also:** Constant Field Values

- S_RESIZE_CURSOR

```java
public static final int S_RESIZE_CURSOR
```

The south-resize cursor type.

**See Also:** Constant Field Values

- W_RESIZE_CURSOR

```java
public static final int W_RESIZE_CURSOR
```

The west-resize cursor type.

**See Also:** Constant Field Values

- E_RESIZE_CURSOR

```java
public static final int E_RESIZE_CURSOR
```

The east-resize cursor type.

**See Also:** Constant Field Values

- HAND_CURSOR

```java
public static final int HAND_CURSOR
```

The hand cursor type.

**See Also:** Constant Field Values

- MOVE_CURSOR

```java
public static final int MOVE_CURSOR
```

The move cursor type.

**See Also:** Constant Field Values

- predefined

```java
@Deprecated

protected static
Cursor
[] predefined
```

Deprecated.

As of JDK version 1.7, the

getPredefinedCursor(int)

method should be used instead.

- CUSTOM_CURSOR

```java
public static final int CUSTOM_CURSOR
```

The type associated with all custom cursors.

**See Also:** Constant Field Values

- name

```java
protected
String
name
```

The user-visible name of the cursor.

**See Also:** getName()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Cursor

```java
@ConstructorProperties
("type")
public Cursor​(int type)
```

Creates a new cursor object with the specified type.

**Parameters:** type

- the type of cursor
**Throws:** IllegalArgumentException

- if the specified cursor type
is invalid

- Cursor

```java
protected Cursor​(
String
name)
```

Creates a new custom cursor object with the specified name.

Note: this constructor should only be used by AWT implementations
as part of their support for custom cursors. Applications should
use Toolkit.createCustomCursor().

**Parameters:** name

- the user-visible name of the cursor.
**See Also:** Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

============ METHOD DETAIL ==========

- Method Detail

- getPredefinedCursor

```java
public static
Cursor
getPredefinedCursor​(int type)
```

Returns a cursor object with the specified predefined type.

**Parameters:** type

- the type of predefined cursor
**Returns:** the specified predefined cursor
**Throws:** IllegalArgumentException

- if the specified cursor type is
invalid

- getSystemCustomCursor

```java
public static
Cursor
getSystemCustomCursor​(
String
name)
throws
AWTException
,

HeadlessException
```

Returns a system-specific custom cursor object matching the
specified name. Cursor names are, for example: "Invalid.16x16"

**Parameters:** name

- a string describing the desired system-specific custom cursor
**Returns:** the system specific custom cursor named
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**Throws:** AWTException

- in case of erroneous retrieving of the cursor

- getDefaultCursor

```java
public static
Cursor
getDefaultCursor()
```

Return the system default cursor.

**Returns:** the default cursor

- getType

```java
public int getType()
```

Returns the type for this cursor.

**Returns:** the cursor type

- getName

```java
public
String
getName()
```

Returns the name of this cursor.

**Returns:** a localized description of this cursor.
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns a string representation of this cursor.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this cursor.
**Since:** 1.2

Field Detail

- DEFAULT_CURSOR

```java
public static final int DEFAULT_CURSOR
```

The default cursor type (gets set if no cursor is defined).

**See Also:** Constant Field Values

- CROSSHAIR_CURSOR

```java
public static final int CROSSHAIR_CURSOR
```

The crosshair cursor type.

**See Also:** Constant Field Values

- TEXT_CURSOR

```java
public static final int TEXT_CURSOR
```

The text cursor type.

**See Also:** Constant Field Values

- WAIT_CURSOR

```java
public static final int WAIT_CURSOR
```

The wait cursor type.

**See Also:** Constant Field Values

- SW_RESIZE_CURSOR

```java
public static final int SW_RESIZE_CURSOR
```

The south-west-resize cursor type.

**See Also:** Constant Field Values

- SE_RESIZE_CURSOR

```java
public static final int SE_RESIZE_CURSOR
```

The south-east-resize cursor type.

**See Also:** Constant Field Values

- NW_RESIZE_CURSOR

```java
public static final int NW_RESIZE_CURSOR
```

The north-west-resize cursor type.

**See Also:** Constant Field Values

- NE_RESIZE_CURSOR

```java
public static final int NE_RESIZE_CURSOR
```

The north-east-resize cursor type.

**See Also:** Constant Field Values

- N_RESIZE_CURSOR

```java
public static final int N_RESIZE_CURSOR
```

The north-resize cursor type.

**See Also:** Constant Field Values

- S_RESIZE_CURSOR

```java
public static final int S_RESIZE_CURSOR
```

The south-resize cursor type.

**See Also:** Constant Field Values

- W_RESIZE_CURSOR

```java
public static final int W_RESIZE_CURSOR
```

The west-resize cursor type.

**See Also:** Constant Field Values

- E_RESIZE_CURSOR

```java
public static final int E_RESIZE_CURSOR
```

The east-resize cursor type.

**See Also:** Constant Field Values

- HAND_CURSOR

```java
public static final int HAND_CURSOR
```

The hand cursor type.

**See Also:** Constant Field Values

- MOVE_CURSOR

```java
public static final int MOVE_CURSOR
```

The move cursor type.

**See Also:** Constant Field Values

- predefined

```java
@Deprecated

protected static
Cursor
[] predefined
```

Deprecated.

As of JDK version 1.7, the

getPredefinedCursor(int)

method should be used instead.

- CUSTOM_CURSOR

```java
public static final int CUSTOM_CURSOR
```

The type associated with all custom cursors.

**See Also:** Constant Field Values

- name

```java
protected
String
name
```

The user-visible name of the cursor.

**See Also:** getName()

---

#### Field Detail

DEFAULT_CURSOR

```java
public static final int DEFAULT_CURSOR
```

The default cursor type (gets set if no cursor is defined).

**See Also:** Constant Field Values

---

#### DEFAULT_CURSOR

public static final int DEFAULT_CURSOR

The default cursor type (gets set if no cursor is defined).

CROSSHAIR_CURSOR

```java
public static final int CROSSHAIR_CURSOR
```

The crosshair cursor type.

**See Also:** Constant Field Values

---

#### CROSSHAIR_CURSOR

public static final int CROSSHAIR_CURSOR

The crosshair cursor type.

TEXT_CURSOR

```java
public static final int TEXT_CURSOR
```

The text cursor type.

**See Also:** Constant Field Values

---

#### TEXT_CURSOR

public static final int TEXT_CURSOR

The text cursor type.

WAIT_CURSOR

```java
public static final int WAIT_CURSOR
```

The wait cursor type.

**See Also:** Constant Field Values

---

#### WAIT_CURSOR

public static final int WAIT_CURSOR

The wait cursor type.

SW_RESIZE_CURSOR

```java
public static final int SW_RESIZE_CURSOR
```

The south-west-resize cursor type.

**See Also:** Constant Field Values

---

#### SW_RESIZE_CURSOR

public static final int SW_RESIZE_CURSOR

The south-west-resize cursor type.

SE_RESIZE_CURSOR

```java
public static final int SE_RESIZE_CURSOR
```

The south-east-resize cursor type.

**See Also:** Constant Field Values

---

#### SE_RESIZE_CURSOR

public static final int SE_RESIZE_CURSOR

The south-east-resize cursor type.

NW_RESIZE_CURSOR

```java
public static final int NW_RESIZE_CURSOR
```

The north-west-resize cursor type.

**See Also:** Constant Field Values

---

#### NW_RESIZE_CURSOR

public static final int NW_RESIZE_CURSOR

The north-west-resize cursor type.

NE_RESIZE_CURSOR

```java
public static final int NE_RESIZE_CURSOR
```

The north-east-resize cursor type.

**See Also:** Constant Field Values

---

#### NE_RESIZE_CURSOR

public static final int NE_RESIZE_CURSOR

The north-east-resize cursor type.

N_RESIZE_CURSOR

```java
public static final int N_RESIZE_CURSOR
```

The north-resize cursor type.

**See Also:** Constant Field Values

---

#### N_RESIZE_CURSOR

public static final int N_RESIZE_CURSOR

The north-resize cursor type.

S_RESIZE_CURSOR

```java
public static final int S_RESIZE_CURSOR
```

The south-resize cursor type.

**See Also:** Constant Field Values

---

#### S_RESIZE_CURSOR

public static final int S_RESIZE_CURSOR

The south-resize cursor type.

W_RESIZE_CURSOR

```java
public static final int W_RESIZE_CURSOR
```

The west-resize cursor type.

**See Also:** Constant Field Values

---

#### W_RESIZE_CURSOR

public static final int W_RESIZE_CURSOR

The west-resize cursor type.

E_RESIZE_CURSOR

```java
public static final int E_RESIZE_CURSOR
```

The east-resize cursor type.

**See Also:** Constant Field Values

---

#### E_RESIZE_CURSOR

public static final int E_RESIZE_CURSOR

The east-resize cursor type.

HAND_CURSOR

```java
public static final int HAND_CURSOR
```

The hand cursor type.

**See Also:** Constant Field Values

---

#### HAND_CURSOR

public static final int HAND_CURSOR

The hand cursor type.

MOVE_CURSOR

```java
public static final int MOVE_CURSOR
```

The move cursor type.

**See Also:** Constant Field Values

---

#### MOVE_CURSOR

public static final int MOVE_CURSOR

The move cursor type.

predefined

```java
@Deprecated

protected static
Cursor
[] predefined
```

Deprecated.

As of JDK version 1.7, the

getPredefinedCursor(int)

method should be used instead.

---

#### predefined

@Deprecated

protected static

Cursor

[] predefined

CUSTOM_CURSOR

```java
public static final int CUSTOM_CURSOR
```

The type associated with all custom cursors.

**See Also:** Constant Field Values

---

#### CUSTOM_CURSOR

public static final int CUSTOM_CURSOR

The type associated with all custom cursors.

name

```java
protected
String
name
```

The user-visible name of the cursor.

**See Also:** getName()

---

#### name

protected

String

name

The user-visible name of the cursor.

Constructor Detail

- Cursor

```java
@ConstructorProperties
("type")
public Cursor​(int type)
```

Creates a new cursor object with the specified type.

**Parameters:** type

- the type of cursor
**Throws:** IllegalArgumentException

- if the specified cursor type
is invalid

- Cursor

```java
protected Cursor​(
String
name)
```

Creates a new custom cursor object with the specified name.

Note: this constructor should only be used by AWT implementations
as part of their support for custom cursors. Applications should
use Toolkit.createCustomCursor().

**Parameters:** name

- the user-visible name of the cursor.
**See Also:** Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

---

#### Constructor Detail

Cursor

```java
@ConstructorProperties
("type")
public Cursor​(int type)
```

Creates a new cursor object with the specified type.

**Parameters:** type

- the type of cursor
**Throws:** IllegalArgumentException

- if the specified cursor type
is invalid

---

#### Cursor

@ConstructorProperties

("type")
public Cursor​(int type)

Creates a new cursor object with the specified type.

Cursor

```java
protected Cursor​(
String
name)
```

Creates a new custom cursor object with the specified name.

Note: this constructor should only be used by AWT implementations
as part of their support for custom cursors. Applications should
use Toolkit.createCustomCursor().

**Parameters:** name

- the user-visible name of the cursor.
**See Also:** Toolkit.createCustomCursor(java.awt.Image, java.awt.Point, java.lang.String)

---

#### Cursor

protected Cursor​(

String

name)

Creates a new custom cursor object with the specified name.

Note: this constructor should only be used by AWT implementations
as part of their support for custom cursors. Applications should
use Toolkit.createCustomCursor().

Note: this constructor should only be used by AWT implementations
as part of their support for custom cursors. Applications should
use Toolkit.createCustomCursor().

Method Detail

- getPredefinedCursor

```java
public static
Cursor
getPredefinedCursor​(int type)
```

Returns a cursor object with the specified predefined type.

**Parameters:** type

- the type of predefined cursor
**Returns:** the specified predefined cursor
**Throws:** IllegalArgumentException

- if the specified cursor type is
invalid

- getSystemCustomCursor

```java
public static
Cursor
getSystemCustomCursor​(
String
name)
throws
AWTException
,

HeadlessException
```

Returns a system-specific custom cursor object matching the
specified name. Cursor names are, for example: "Invalid.16x16"

**Parameters:** name

- a string describing the desired system-specific custom cursor
**Returns:** the system specific custom cursor named
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**Throws:** AWTException

- in case of erroneous retrieving of the cursor

- getDefaultCursor

```java
public static
Cursor
getDefaultCursor()
```

Return the system default cursor.

**Returns:** the default cursor

- getType

```java
public int getType()
```

Returns the type for this cursor.

**Returns:** the cursor type

- getName

```java
public
String
getName()
```

Returns the name of this cursor.

**Returns:** a localized description of this cursor.
**Since:** 1.2

- toString

```java
public
String
toString()
```

Returns a string representation of this cursor.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this cursor.
**Since:** 1.2

---

#### Method Detail

getPredefinedCursor

```java
public static
Cursor
getPredefinedCursor​(int type)
```

Returns a cursor object with the specified predefined type.

**Parameters:** type

- the type of predefined cursor
**Returns:** the specified predefined cursor
**Throws:** IllegalArgumentException

- if the specified cursor type is
invalid

---

#### getPredefinedCursor

public static

Cursor

getPredefinedCursor​(int type)

Returns a cursor object with the specified predefined type.

getSystemCustomCursor

```java
public static
Cursor
getSystemCustomCursor​(
String
name)
throws
AWTException
,

HeadlessException
```

Returns a system-specific custom cursor object matching the
specified name. Cursor names are, for example: "Invalid.16x16"

**Parameters:** name

- a string describing the desired system-specific custom cursor
**Returns:** the system specific custom cursor named
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns true
**Throws:** AWTException

- in case of erroneous retrieving of the cursor

---

#### getSystemCustomCursor

public static

Cursor

getSystemCustomCursor​(

String

name)
throws

AWTException

,

HeadlessException

Returns a system-specific custom cursor object matching the
specified name. Cursor names are, for example: "Invalid.16x16"

getDefaultCursor

```java
public static
Cursor
getDefaultCursor()
```

Return the system default cursor.

**Returns:** the default cursor

---

#### getDefaultCursor

public static

Cursor

getDefaultCursor()

Return the system default cursor.

getType

```java
public int getType()
```

Returns the type for this cursor.

**Returns:** the cursor type

---

#### getType

public int getType()

Returns the type for this cursor.

getName

```java
public
String
getName()
```

Returns the name of this cursor.

**Returns:** a localized description of this cursor.
**Since:** 1.2

---

#### getName

public

String

getName()

Returns the name of this cursor.

toString

```java
public
String
toString()
```

Returns a string representation of this cursor.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this cursor.
**Since:** 1.2

---

#### toString

public

String

toString()

Returns a string representation of this cursor.

---

