# Class MouseInfo

**Source:** `java.desktop\java\awt\MouseInfo.html`

### Class Description

```java
public class
MouseInfo

extends
Object
```

MouseInfo

provides methods for getting information about the mouse,
such as mouse pointer location and the number of mouse buttons.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
PointerInfo
getPointerInfo()
throws
HeadlessException

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.
The

GraphicsDevice

stored in this

PointerInfo

contains the mouse pointer. The coordinate system used for the mouse position
depends on whether or not the

GraphicsDevice

is part of a virtual
screen device.
For virtual screen devices, the coordinates are given in the virtual
coordinate system, otherwise they are returned in the coordinate system
of the

GraphicsDevice

. See

GraphicsConfiguration

for more information about the virtual screen devices.
On systems without a mouse, returns

null

.

If there is a security manager, its

checkPermission

method
is called with an

AWTPermission("watchMousePointer")

permission before creating and returning a

PointerInfo

object. This may result in a

SecurityException

.

**Returns:**
- location of the mouse pointer

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow the operation

**See Also:**
- GraphicsConfiguration

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

**Since:**
- 1.5

---

#### public static int getNumberOfButtons()
throws
HeadlessException

Returns the number of buttons on the mouse.
On systems without a mouse, returns

-1

.
The number of buttons is obtained from the AWT Toolkit
by requesting the

"awt.mouse.numButtons"

desktop property
which is set by the underlying native platform.

**Returns:**
- number of buttons on the mouse

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless() returns true

**See Also:**
- Toolkit.getDesktopProperty(java.lang.String)

**Since:**
- 1.5

---

### Additional Sections

#### Class MouseInfo

java.lang.Object

- java.awt.MouseInfo

java.awt.MouseInfo

```java
public class
MouseInfo

extends
Object
```

MouseInfo

provides methods for getting information about the mouse,
such as mouse pointer location and the number of mouse buttons.

**Since:** 1.5

public class

MouseInfo

extends

Object

MouseInfo

provides methods for getting information about the mouse,
such as mouse pointer location and the number of mouse buttons.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

getNumberOfButtons

()

Returns the number of buttons on the mouse.

static

PointerInfo

getPointerInfo

()

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

getNumberOfButtons

()

Returns the number of buttons on the mouse.

static

PointerInfo

getPointerInfo

()

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.

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

Returns the number of buttons on the mouse.

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.

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

============ METHOD DETAIL ==========

- Method Detail

- getPointerInfo

```java
public static
PointerInfo
getPointerInfo()
throws
HeadlessException
```

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.
The

GraphicsDevice

stored in this

PointerInfo

contains the mouse pointer. The coordinate system used for the mouse position
depends on whether or not the

GraphicsDevice

is part of a virtual
screen device.
For virtual screen devices, the coordinates are given in the virtual
coordinate system, otherwise they are returned in the coordinate system
of the

GraphicsDevice

. See

GraphicsConfiguration

for more information about the virtual screen devices.
On systems without a mouse, returns

null

.

If there is a security manager, its

checkPermission

method
is called with an

AWTPermission("watchMousePointer")

permission before creating and returning a

PointerInfo

object. This may result in a

SecurityException

.

**Returns:** location of the mouse pointer
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow the operation
**Since:** 1.5
**See Also:** GraphicsConfiguration

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

- getNumberOfButtons

```java
public static int getNumberOfButtons()
throws
HeadlessException
```

Returns the number of buttons on the mouse.
On systems without a mouse, returns

-1

.
The number of buttons is obtained from the AWT Toolkit
by requesting the

"awt.mouse.numButtons"

desktop property
which is set by the underlying native platform.

**Returns:** number of buttons on the mouse
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** Toolkit.getDesktopProperty(java.lang.String)

Method Detail

- getPointerInfo

```java
public static
PointerInfo
getPointerInfo()
throws
HeadlessException
```

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.
The

GraphicsDevice

stored in this

PointerInfo

contains the mouse pointer. The coordinate system used for the mouse position
depends on whether or not the

GraphicsDevice

is part of a virtual
screen device.
For virtual screen devices, the coordinates are given in the virtual
coordinate system, otherwise they are returned in the coordinate system
of the

GraphicsDevice

. See

GraphicsConfiguration

for more information about the virtual screen devices.
On systems without a mouse, returns

null

.

If there is a security manager, its

checkPermission

method
is called with an

AWTPermission("watchMousePointer")

permission before creating and returning a

PointerInfo

object. This may result in a

SecurityException

.

**Returns:** location of the mouse pointer
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow the operation
**Since:** 1.5
**See Also:** GraphicsConfiguration

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

- getNumberOfButtons

```java
public static int getNumberOfButtons()
throws
HeadlessException
```

Returns the number of buttons on the mouse.
On systems without a mouse, returns

-1

.
The number of buttons is obtained from the AWT Toolkit
by requesting the

"awt.mouse.numButtons"

desktop property
which is set by the underlying native platform.

**Returns:** number of buttons on the mouse
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** Toolkit.getDesktopProperty(java.lang.String)

---

#### Method Detail

getPointerInfo

```java
public static
PointerInfo
getPointerInfo()
throws
HeadlessException
```

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.
The

GraphicsDevice

stored in this

PointerInfo

contains the mouse pointer. The coordinate system used for the mouse position
depends on whether or not the

GraphicsDevice

is part of a virtual
screen device.
For virtual screen devices, the coordinates are given in the virtual
coordinate system, otherwise they are returned in the coordinate system
of the

GraphicsDevice

. See

GraphicsConfiguration

for more information about the virtual screen devices.
On systems without a mouse, returns

null

.

If there is a security manager, its

checkPermission

method
is called with an

AWTPermission("watchMousePointer")

permission before creating and returning a

PointerInfo

object. This may result in a

SecurityException

.

**Returns:** location of the mouse pointer
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow the operation
**Since:** 1.5
**See Also:** GraphicsConfiguration

,

SecurityManager.checkPermission(java.security.Permission)

,

AWTPermission

---

#### getPointerInfo

public static

PointerInfo

getPointerInfo()
throws

HeadlessException

Returns a

PointerInfo

instance that represents the current
location of the mouse pointer.
The

GraphicsDevice

stored in this

PointerInfo

contains the mouse pointer. The coordinate system used for the mouse position
depends on whether or not the

GraphicsDevice

is part of a virtual
screen device.
For virtual screen devices, the coordinates are given in the virtual
coordinate system, otherwise they are returned in the coordinate system
of the

GraphicsDevice

. See

GraphicsConfiguration

for more information about the virtual screen devices.
On systems without a mouse, returns

null

.

If there is a security manager, its

checkPermission

method
is called with an

AWTPermission("watchMousePointer")

permission before creating and returning a

PointerInfo

object. This may result in a

SecurityException

.

If there is a security manager, its

checkPermission

method
is called with an

AWTPermission("watchMousePointer")

permission before creating and returning a

PointerInfo

object. This may result in a

SecurityException

.

getNumberOfButtons

```java
public static int getNumberOfButtons()
throws
HeadlessException
```

Returns the number of buttons on the mouse.
On systems without a mouse, returns

-1

.
The number of buttons is obtained from the AWT Toolkit
by requesting the

"awt.mouse.numButtons"

desktop property
which is set by the underlying native platform.

**Returns:** number of buttons on the mouse
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** Toolkit.getDesktopProperty(java.lang.String)

---

#### getNumberOfButtons

public static int getNumberOfButtons()
throws

HeadlessException

Returns the number of buttons on the mouse.
On systems without a mouse, returns

-1

.
The number of buttons is obtained from the AWT Toolkit
by requesting the

"awt.mouse.numButtons"

desktop property
which is set by the underlying native platform.

---

