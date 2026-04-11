# Class Dimension2D

**Source:** `java.desktop\java\awt\geom\Dimension2D.html`

### Class Description

```java
public abstract class
Dimension2D

extends
Object

implements
Cloneable
```

The

Dimension2D

class is to encapsulate a width
and a height dimension.

This class is only the abstract superclass for all objects that
store a 2D dimension.
The actual storage representation of the sizes is left to
the subclass.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Dimension2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**See Also:**
- Dimension

**Since:**
- 1.2

---

### Method Details

#### public abstract double getWidth()

Returns the width of this

Dimension

in double
precision.

**Returns:**
- the width of this

Dimension

.

**Since:**
- 1.2

---

#### public abstract double getHeight()

Returns the height of this

Dimension

in double
precision.

**Returns:**
- the height of this

Dimension

.

**Since:**
- 1.2

---

#### public abstract void setSize​(double width,
double height)

Sets the size of this

Dimension

object to the
specified width and height.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:**
- width

- the new width for the

Dimension

object
- height

- the new height for the

Dimension

object

**Since:**
- 1.2

---

#### public void setSize​(
Dimension2D
d)

Sets the size of this

Dimension2D

object to
match the specified size.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:**
- d

- the new size for the

Dimension2D

object

**Since:**
- 1.2

---

#### public
Object
clone()

Creates a new object of the same class as this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- OutOfMemoryError

- if there is not enough memory.

**See Also:**
- Cloneable

**Since:**
- 1.2

---

### Additional Sections

#### Class Dimension2D

java.lang.Object

- java.awt.geom.Dimension2D

java.awt.geom.Dimension2D

**All Implemented Interfaces:** Cloneable

**Direct Known Subclasses:** Dimension

```java
public abstract class
Dimension2D

extends
Object

implements
Cloneable
```

The

Dimension2D

class is to encapsulate a width
and a height dimension.

This class is only the abstract superclass for all objects that
store a 2D dimension.
The actual storage representation of the sizes is left to
the subclass.

**Since:** 1.2

public abstract class

Dimension2D

extends

Object

implements

Cloneable

The

Dimension2D

class is to encapsulate a width
and a height dimension.

This class is only the abstract superclass for all objects that
store a 2D dimension.
The actual storage representation of the sizes is left to
the subclass.

This class is only the abstract superclass for all objects that
store a 2D dimension.
The actual storage representation of the sizes is left to
the subclass.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Dimension2D

()

This is an abstract class that cannot be instantiated directly.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a new object of the same class as this object.

abstract double

getHeight

()

Returns the height of this

Dimension

in double
precision.

abstract double

getWidth

()

Returns the width of this

Dimension

in double
precision.

abstract void

setSize

​(double width,
double height)

Sets the size of this

Dimension

object to the
specified width and height.

void

setSize

​(

Dimension2D

d)

Sets the size of this

Dimension2D

object to
match the specified size.

- Methods declared in class java.lang.

Object

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Dimension2D

()

This is an abstract class that cannot be instantiated directly.

---

#### Constructor Summary

This is an abstract class that cannot be instantiated directly.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a new object of the same class as this object.

abstract double

getHeight

()

Returns the height of this

Dimension

in double
precision.

abstract double

getWidth

()

Returns the width of this

Dimension

in double
precision.

abstract void

setSize

​(double width,
double height)

Sets the size of this

Dimension

object to the
specified width and height.

void

setSize

​(

Dimension2D

d)

Sets the size of this

Dimension2D

object to
match the specified size.

- Methods declared in class java.lang.

Object

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

Creates a new object of the same class as this object.

Returns the height of this

Dimension

in double
precision.

Returns the width of this

Dimension

in double
precision.

Sets the size of this

Dimension

object to the
specified width and height.

Sets the size of this

Dimension2D

object to
match the specified size.

Methods declared in class java.lang.

Object

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Dimension2D

```java
protected Dimension2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Dimension

============ METHOD DETAIL ==========

- Method Detail

- getWidth

```java
public abstract double getWidth()
```

Returns the width of this

Dimension

in double
precision.

**Returns:** the width of this

Dimension

.
**Since:** 1.2

- getHeight

```java
public abstract double getHeight()
```

Returns the height of this

Dimension

in double
precision.

**Returns:** the height of this

Dimension

.
**Since:** 1.2

- setSize

```java
public abstract void setSize​(double width,
double height)
```

Sets the size of this

Dimension

object to the
specified width and height.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:** width

- the new width for the

Dimension

object
**Parameters:** height

- the new height for the

Dimension

object
**Since:** 1.2

- setSize

```java
public void setSize​(
Dimension2D
d)
```

Sets the size of this

Dimension2D

object to
match the specified size.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:** d

- the new size for the

Dimension2D

object
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Creates a new object of the same class as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

Constructor Detail

- Dimension2D

```java
protected Dimension2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Dimension

---

#### Constructor Detail

Dimension2D

```java
protected Dimension2D()
```

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

**Since:** 1.2
**See Also:** Dimension

---

#### Dimension2D

protected Dimension2D()

This is an abstract class that cannot be instantiated directly.
Type-specific implementation subclasses are available for
instantiation and provide a number of formats for storing
the information necessary to satisfy the various accessor
methods below.

Method Detail

- getWidth

```java
public abstract double getWidth()
```

Returns the width of this

Dimension

in double
precision.

**Returns:** the width of this

Dimension

.
**Since:** 1.2

- getHeight

```java
public abstract double getHeight()
```

Returns the height of this

Dimension

in double
precision.

**Returns:** the height of this

Dimension

.
**Since:** 1.2

- setSize

```java
public abstract void setSize​(double width,
double height)
```

Sets the size of this

Dimension

object to the
specified width and height.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:** width

- the new width for the

Dimension

object
**Parameters:** height

- the new height for the

Dimension

object
**Since:** 1.2

- setSize

```java
public void setSize​(
Dimension2D
d)
```

Sets the size of this

Dimension2D

object to
match the specified size.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:** d

- the new size for the

Dimension2D

object
**Since:** 1.2

- clone

```java
public
Object
clone()
```

Creates a new object of the same class as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

---

#### Method Detail

getWidth

```java
public abstract double getWidth()
```

Returns the width of this

Dimension

in double
precision.

**Returns:** the width of this

Dimension

.
**Since:** 1.2

---

#### getWidth

public abstract double getWidth()

Returns the width of this

Dimension

in double
precision.

getHeight

```java
public abstract double getHeight()
```

Returns the height of this

Dimension

in double
precision.

**Returns:** the height of this

Dimension

.
**Since:** 1.2

---

#### getHeight

public abstract double getHeight()

Returns the height of this

Dimension

in double
precision.

setSize

```java
public abstract void setSize​(double width,
double height)
```

Sets the size of this

Dimension

object to the
specified width and height.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:** width

- the new width for the

Dimension

object
**Parameters:** height

- the new height for the

Dimension

object
**Since:** 1.2

---

#### setSize

public abstract void setSize​(double width,
double height)

Sets the size of this

Dimension

object to the
specified width and height.
This method is included for completeness, to parallel the

getSize

method of

Component

.

setSize

```java
public void setSize​(
Dimension2D
d)
```

Sets the size of this

Dimension2D

object to
match the specified size.
This method is included for completeness, to parallel the

getSize

method of

Component

.

**Parameters:** d

- the new size for the

Dimension2D

object
**Since:** 1.2

---

#### setSize

public void setSize​(

Dimension2D

d)

Sets the size of this

Dimension2D

object to
match the specified size.
This method is included for completeness, to parallel the

getSize

method of

Component

.

clone

```java
public
Object
clone()
```

Creates a new object of the same class as this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** OutOfMemoryError

- if there is not enough memory.
**Since:** 1.2
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a new object of the same class as this object.

---

