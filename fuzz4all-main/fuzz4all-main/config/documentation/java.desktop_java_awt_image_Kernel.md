# Class Kernel

**Source:** `java.desktop\java\awt\image\Kernel.html`

### Class Description

```java
public class
Kernel

extends
Object

implements
Cloneable
```

The

Kernel

class defines a matrix that describes how a
specified pixel and its surrounding pixels affect the value
computed for the pixel's position in the output image of a filtering
operation. The X origin and Y origin indicate the kernel matrix element
that corresponds to the pixel position for which an output value is
being computed.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Kernel​(int width,
int height,
float[] data)

Constructs a

Kernel

object from an array of floats.
The first

width

*

height

elements of
the

data

array are copied.
If the length of the

data

array is less
than width*height, an

IllegalArgumentException

is thrown.
The X origin is (width-1)/2 and the Y origin is (height-1)/2.

**Parameters:**
- width

- width of the kernel
- height

- height of the kernel
- data

- kernel data in row major order

**Throws:**
- IllegalArgumentException

- if the length of

data

is less than the product of

width

and

height

---

### Method Details

#### public final int getXOrigin()

Returns the X origin of this

Kernel

.

**Returns:**
- the X origin.

---

#### public final int getYOrigin()

Returns the Y origin of this

Kernel

.

**Returns:**
- the Y origin.

---

#### public final int getWidth()

Returns the width of this

Kernel

.

**Returns:**
- the width of this

Kernel

.

---

#### public final int getHeight()

Returns the height of this

Kernel

.

**Returns:**
- the height of this

Kernel

.

---

#### public final float[] getKernelData​(float[] data)

Returns the kernel data in row major order.
The

data

array is returned. If

data

is

null

, a new array is allocated.

**Parameters:**
- data

- if non-null, contains the returned kernel data

**Returns:**
- the

data

array containing the kernel data
in row major order or, if

data

is

null

, a newly allocated array containing
the kernel data in row major order

**Throws:**
- IllegalArgumentException

- if

data

is less
than the size of this

Kernel

---

#### public
Object
clone()

Clones this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this object.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Kernel

java.lang.Object

- java.awt.image.Kernel

java.awt.image.Kernel

**All Implemented Interfaces:** Cloneable

```java
public class
Kernel

extends
Object

implements
Cloneable
```

The

Kernel

class defines a matrix that describes how a
specified pixel and its surrounding pixels affect the value
computed for the pixel's position in the output image of a filtering
operation. The X origin and Y origin indicate the kernel matrix element
that corresponds to the pixel position for which an output value is
being computed.

**See Also:** ConvolveOp

public class

Kernel

extends

Object

implements

Cloneable

The

Kernel

class defines a matrix that describes how a
specified pixel and its surrounding pixels affect the value
computed for the pixel's position in the output image of a filtering
operation. The X origin and Y origin indicate the kernel matrix element
that corresponds to the pixel position for which an output value is
being computed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Kernel

​(int width,
int height,
float[] data)

Constructs a

Kernel

object from an array of floats.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clones this object.

int

getHeight

()

Returns the height of this

Kernel

.

float[]

getKernelData

​(float[] data)

Returns the kernel data in row major order.

int

getWidth

()

Returns the width of this

Kernel

.

int

getXOrigin

()

Returns the X origin of this

Kernel

.

int

getYOrigin

()

Returns the Y origin of this

Kernel

.

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

Constructor

Description

Kernel

​(int width,
int height,
float[] data)

Constructs a

Kernel

object from an array of floats.

---

#### Constructor Summary

Constructs a

Kernel

object from an array of floats.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clones this object.

int

getHeight

()

Returns the height of this

Kernel

.

float[]

getKernelData

​(float[] data)

Returns the kernel data in row major order.

int

getWidth

()

Returns the width of this

Kernel

.

int

getXOrigin

()

Returns the X origin of this

Kernel

.

int

getYOrigin

()

Returns the Y origin of this

Kernel

.

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

Clones this object.

Returns the height of this

Kernel

.

Returns the kernel data in row major order.

Returns the width of this

Kernel

.

Returns the X origin of this

Kernel

.

Returns the Y origin of this

Kernel

.

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

- Kernel

```java
public Kernel​(int width,
int height,
float[] data)
```

Constructs a

Kernel

object from an array of floats.
The first

width

*

height

elements of
the

data

array are copied.
If the length of the

data

array is less
than width*height, an

IllegalArgumentException

is thrown.
The X origin is (width-1)/2 and the Y origin is (height-1)/2.

**Parameters:** width

- width of the kernel
**Parameters:** height

- height of the kernel
**Parameters:** data

- kernel data in row major order
**Throws:** IllegalArgumentException

- if the length of

data

is less than the product of

width

and

height

============ METHOD DETAIL ==========

- Method Detail

- getXOrigin

```java
public final int getXOrigin()
```

Returns the X origin of this

Kernel

.

**Returns:** the X origin.

- getYOrigin

```java
public final int getYOrigin()
```

Returns the Y origin of this

Kernel

.

**Returns:** the Y origin.

- getWidth

```java
public final int getWidth()
```

Returns the width of this

Kernel

.

**Returns:** the width of this

Kernel

.

- getHeight

```java
public final int getHeight()
```

Returns the height of this

Kernel

.

**Returns:** the height of this

Kernel

.

- getKernelData

```java
public final float[] getKernelData​(float[] data)
```

Returns the kernel data in row major order.
The

data

array is returned. If

data

is

null

, a new array is allocated.

**Parameters:** data

- if non-null, contains the returned kernel data
**Returns:** the

data

array containing the kernel data
in row major order or, if

data

is

null

, a newly allocated array containing
the kernel data in row major order
**Throws:** IllegalArgumentException

- if

data

is less
than the size of this

Kernel

- clone

```java
public
Object
clone()
```

Clones this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this object.
**See Also:** Cloneable

Constructor Detail

- Kernel

```java
public Kernel​(int width,
int height,
float[] data)
```

Constructs a

Kernel

object from an array of floats.
The first

width

*

height

elements of
the

data

array are copied.
If the length of the

data

array is less
than width*height, an

IllegalArgumentException

is thrown.
The X origin is (width-1)/2 and the Y origin is (height-1)/2.

**Parameters:** width

- width of the kernel
**Parameters:** height

- height of the kernel
**Parameters:** data

- kernel data in row major order
**Throws:** IllegalArgumentException

- if the length of

data

is less than the product of

width

and

height

---

#### Constructor Detail

Kernel

```java
public Kernel​(int width,
int height,
float[] data)
```

Constructs a

Kernel

object from an array of floats.
The first

width

*

height

elements of
the

data

array are copied.
If the length of the

data

array is less
than width*height, an

IllegalArgumentException

is thrown.
The X origin is (width-1)/2 and the Y origin is (height-1)/2.

**Parameters:** width

- width of the kernel
**Parameters:** height

- height of the kernel
**Parameters:** data

- kernel data in row major order
**Throws:** IllegalArgumentException

- if the length of

data

is less than the product of

width

and

height

---

#### Kernel

public Kernel​(int width,
int height,
float[] data)

Constructs a

Kernel

object from an array of floats.
The first

width

*

height

elements of
the

data

array are copied.
If the length of the

data

array is less
than width*height, an

IllegalArgumentException

is thrown.
The X origin is (width-1)/2 and the Y origin is (height-1)/2.

Method Detail

- getXOrigin

```java
public final int getXOrigin()
```

Returns the X origin of this

Kernel

.

**Returns:** the X origin.

- getYOrigin

```java
public final int getYOrigin()
```

Returns the Y origin of this

Kernel

.

**Returns:** the Y origin.

- getWidth

```java
public final int getWidth()
```

Returns the width of this

Kernel

.

**Returns:** the width of this

Kernel

.

- getHeight

```java
public final int getHeight()
```

Returns the height of this

Kernel

.

**Returns:** the height of this

Kernel

.

- getKernelData

```java
public final float[] getKernelData​(float[] data)
```

Returns the kernel data in row major order.
The

data

array is returned. If

data

is

null

, a new array is allocated.

**Parameters:** data

- if non-null, contains the returned kernel data
**Returns:** the

data

array containing the kernel data
in row major order or, if

data

is

null

, a newly allocated array containing
the kernel data in row major order
**Throws:** IllegalArgumentException

- if

data

is less
than the size of this

Kernel

- clone

```java
public
Object
clone()
```

Clones this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this object.
**See Also:** Cloneable

---

#### Method Detail

getXOrigin

```java
public final int getXOrigin()
```

Returns the X origin of this

Kernel

.

**Returns:** the X origin.

---

#### getXOrigin

public final int getXOrigin()

Returns the X origin of this

Kernel

.

getYOrigin

```java
public final int getYOrigin()
```

Returns the Y origin of this

Kernel

.

**Returns:** the Y origin.

---

#### getYOrigin

public final int getYOrigin()

Returns the Y origin of this

Kernel

.

getWidth

```java
public final int getWidth()
```

Returns the width of this

Kernel

.

**Returns:** the width of this

Kernel

.

---

#### getWidth

public final int getWidth()

Returns the width of this

Kernel

.

getHeight

```java
public final int getHeight()
```

Returns the height of this

Kernel

.

**Returns:** the height of this

Kernel

.

---

#### getHeight

public final int getHeight()

Returns the height of this

Kernel

.

getKernelData

```java
public final float[] getKernelData​(float[] data)
```

Returns the kernel data in row major order.
The

data

array is returned. If

data

is

null

, a new array is allocated.

**Parameters:** data

- if non-null, contains the returned kernel data
**Returns:** the

data

array containing the kernel data
in row major order or, if

data

is

null

, a newly allocated array containing
the kernel data in row major order
**Throws:** IllegalArgumentException

- if

data

is less
than the size of this

Kernel

---

#### getKernelData

public final float[] getKernelData​(float[] data)

Returns the kernel data in row major order.
The

data

array is returned. If

data

is

null

, a new array is allocated.

clone

```java
public
Object
clone()
```

Clones this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this object.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Clones this object.

---

