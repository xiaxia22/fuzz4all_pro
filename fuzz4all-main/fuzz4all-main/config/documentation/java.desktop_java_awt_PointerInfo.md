# Class PointerInfo

**Source:** `java.desktop\java\awt\PointerInfo.html`

### Class Description

```java
public class
PointerInfo

extends
Object
```

A class that describes the pointer position.
It provides the

GraphicsDevice

where the pointer is and
the

Point

that represents the coordinates of the pointer.

Instances of this class should be obtained via

MouseInfo.getPointerInfo()

.
The

PointerInfo

instance is not updated dynamically as the mouse
moves. To get the updated location, you must call

MouseInfo.getPointerInfo()

again.

**Since:** 1.5
**See Also:** MouseInfo.getPointerInfo()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
GraphicsDevice
getDevice()

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

**Returns:**
- GraphicsDevice

corresponding to the pointer

**Since:**
- 1.5

---

#### public
Point
getLocation()

Returns the

Point

that represents the coordinates of the pointer
on the screen. See

MouseInfo.getPointerInfo()

for more information
about coordinate calculation for multiscreen systems.

**Returns:**
- coordinates of mouse pointer

**See Also:**
- MouseInfo

,

MouseInfo.getPointerInfo()

**Since:**
- 1.5

---

### Additional Sections

#### Class PointerInfo

java.lang.Object

- java.awt.PointerInfo

java.awt.PointerInfo

```java
public class
PointerInfo

extends
Object
```

A class that describes the pointer position.
It provides the

GraphicsDevice

where the pointer is and
the

Point

that represents the coordinates of the pointer.

Instances of this class should be obtained via

MouseInfo.getPointerInfo()

.
The

PointerInfo

instance is not updated dynamically as the mouse
moves. To get the updated location, you must call

MouseInfo.getPointerInfo()

again.

**Since:** 1.5
**See Also:** MouseInfo.getPointerInfo()

public class

PointerInfo

extends

Object

A class that describes the pointer position.
It provides the

GraphicsDevice

where the pointer is and
the

Point

that represents the coordinates of the pointer.

Instances of this class should be obtained via

MouseInfo.getPointerInfo()

.
The

PointerInfo

instance is not updated dynamically as the mouse
moves. To get the updated location, you must call

MouseInfo.getPointerInfo()

again.

Instances of this class should be obtained via

MouseInfo.getPointerInfo()

.
The

PointerInfo

instance is not updated dynamically as the mouse
moves. To get the updated location, you must call

MouseInfo.getPointerInfo()

again.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

GraphicsDevice

getDevice

()

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

Point

getLocation

()

Returns the

Point

that represents the coordinates of the pointer
on the screen.

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

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

GraphicsDevice

getDevice

()

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

Point

getLocation

()

Returns the

Point

that represents the coordinates of the pointer
on the screen.

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

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

Returns the

Point

that represents the coordinates of the pointer
on the screen.

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

- getDevice

```java
public
GraphicsDevice
getDevice()
```

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

**Returns:** GraphicsDevice

corresponding to the pointer
**Since:** 1.5

- getLocation

```java
public
Point
getLocation()
```

Returns the

Point

that represents the coordinates of the pointer
on the screen. See

MouseInfo.getPointerInfo()

for more information
about coordinate calculation for multiscreen systems.

**Returns:** coordinates of mouse pointer
**Since:** 1.5
**See Also:** MouseInfo

,

MouseInfo.getPointerInfo()

Method Detail

- getDevice

```java
public
GraphicsDevice
getDevice()
```

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

**Returns:** GraphicsDevice

corresponding to the pointer
**Since:** 1.5

- getLocation

```java
public
Point
getLocation()
```

Returns the

Point

that represents the coordinates of the pointer
on the screen. See

MouseInfo.getPointerInfo()

for more information
about coordinate calculation for multiscreen systems.

**Returns:** coordinates of mouse pointer
**Since:** 1.5
**See Also:** MouseInfo

,

MouseInfo.getPointerInfo()

---

#### Method Detail

getDevice

```java
public
GraphicsDevice
getDevice()
```

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

**Returns:** GraphicsDevice

corresponding to the pointer
**Since:** 1.5

---

#### getDevice

public

GraphicsDevice

getDevice()

Returns the

GraphicsDevice

where the mouse pointer was at the
moment this

PointerInfo

was created.

getLocation

```java
public
Point
getLocation()
```

Returns the

Point

that represents the coordinates of the pointer
on the screen. See

MouseInfo.getPointerInfo()

for more information
about coordinate calculation for multiscreen systems.

**Returns:** coordinates of mouse pointer
**Since:** 1.5
**See Also:** MouseInfo

,

MouseInfo.getPointerInfo()

---

#### getLocation

public

Point

getLocation()

Returns the

Point

that represents the coordinates of the pointer
on the screen. See

MouseInfo.getPointerInfo()

for more information
about coordinate calculation for multiscreen systems.

---

