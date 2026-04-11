# Class TransferHandler.DropLocation

**Source:** `java.desktop\javax\swing\TransferHandler.DropLocation.html`

### Class Description

```java
public static class
TransferHandler.DropLocation

extends
Object
```

Represents a location where dropped data should be inserted.
This is a base class that only encapsulates a point.
Components supporting drop may provide subclasses of this
containing more information.

Developers typically shouldn't create instances of, or extend, this
class. Instead, these are something provided by the DnD
implementation by

TransferSupport

instances and by
components with a

getDropLocation()

method.

**Direct Known Subclasses:** JList.DropLocation

,

JTable.DropLocation

,

JTextComponent.DropLocation

,

JTree.DropLocation

---

### Field Details

*No entries found.*

### Constructor Details

#### protected DropLocation​(
Point
dropPoint)

Constructs a drop location for the given point.

**Parameters:**
- dropPoint

- the drop point, representing the mouse's
current location within the component.

**Throws:**
- IllegalArgumentException

- if the point
is

null

---

### Method Details

#### public final
Point
getDropPoint()

Returns the drop point, representing the mouse's
current location within the component.

**Returns:**
- the drop point.

---

#### public
String
toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this drop location

---

### Additional Sections

#### Class TransferHandler.DropLocation

java.lang.Object

- javax.swing.TransferHandler.DropLocation

javax.swing.TransferHandler.DropLocation

**Direct Known Subclasses:** JList.DropLocation

,

JTable.DropLocation

,

JTextComponent.DropLocation

,

JTree.DropLocation

**Enclosing class:** TransferHandler

```java
public static class
TransferHandler.DropLocation

extends
Object
```

Represents a location where dropped data should be inserted.
This is a base class that only encapsulates a point.
Components supporting drop may provide subclasses of this
containing more information.

Developers typically shouldn't create instances of, or extend, this
class. Instead, these are something provided by the DnD
implementation by

TransferSupport

instances and by
components with a

getDropLocation()

method.

**Since:** 1.6
**See Also:** TransferHandler.TransferSupport.getDropLocation()

public static class

TransferHandler.DropLocation

extends

Object

Represents a location where dropped data should be inserted.
This is a base class that only encapsulates a point.
Components supporting drop may provide subclasses of this
containing more information.

Developers typically shouldn't create instances of, or extend, this
class. Instead, these are something provided by the DnD
implementation by

TransferSupport

instances and by
components with a

getDropLocation()

method.

Developers typically shouldn't create instances of, or extend, this
class. Instead, these are something provided by the DnD
implementation by

TransferSupport

instances and by
components with a

getDropLocation()

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DropLocation

​(

Point

dropPoint)

Constructs a drop location for the given point.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Point

getDropPoint

()

Returns the drop point, representing the mouse's
current location within the component.

String

toString

()

Returns a string representation of this drop location.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DropLocation

​(

Point

dropPoint)

Constructs a drop location for the given point.

---

#### Constructor Summary

Constructs a drop location for the given point.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Point

getDropPoint

()

Returns the drop point, representing the mouse's
current location within the component.

String

toString

()

Returns a string representation of this drop location.

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

Returns the drop point, representing the mouse's
current location within the component.

Returns a string representation of this drop location.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DropLocation

```java
protected DropLocation​(
Point
dropPoint)
```

Constructs a drop location for the given point.

**Parameters:** dropPoint

- the drop point, representing the mouse's
current location within the component.
**Throws:** IllegalArgumentException

- if the point
is

null

============ METHOD DETAIL ==========

- Method Detail

- getDropPoint

```java
public final
Point
getDropPoint()
```

Returns the drop point, representing the mouse's
current location within the component.

**Returns:** the drop point.

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this drop location

Constructor Detail

- DropLocation

```java
protected DropLocation​(
Point
dropPoint)
```

Constructs a drop location for the given point.

**Parameters:** dropPoint

- the drop point, representing the mouse's
current location within the component.
**Throws:** IllegalArgumentException

- if the point
is

null

---

#### Constructor Detail

DropLocation

```java
protected DropLocation​(
Point
dropPoint)
```

Constructs a drop location for the given point.

**Parameters:** dropPoint

- the drop point, representing the mouse's
current location within the component.
**Throws:** IllegalArgumentException

- if the point
is

null

---

#### DropLocation

protected DropLocation​(

Point

dropPoint)

Constructs a drop location for the given point.

Method Detail

- getDropPoint

```java
public final
Point
getDropPoint()
```

Returns the drop point, representing the mouse's
current location within the component.

**Returns:** the drop point.

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this drop location

---

#### Method Detail

getDropPoint

```java
public final
Point
getDropPoint()
```

Returns the drop point, representing the mouse's
current location within the component.

**Returns:** the drop point.

---

#### getDropPoint

public final

Point

getDropPoint()

Returns the drop point, representing the mouse's
current location within the component.

toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this drop location

---

#### toString

public

String

toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

---

