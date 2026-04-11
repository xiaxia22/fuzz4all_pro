# Class LookupTable

**Source:** `java.desktop\java\awt\image\LookupTable.html`

### Class Description

```java
public abstract class
LookupTable

extends
Object
```

This abstract class defines a lookup table object. ByteLookupTable
and ShortLookupTable are subclasses, which
contain byte and short data, respectively. A lookup table
contains data arrays for one or more bands (or components) of an image
(for example, separate arrays for R, G, and B),
and it contains an offset which will be subtracted from the
input values before indexing into the arrays. This allows an array
smaller than the native data size to be provided for a
constrained input. If there is only one array in the lookup
table, it will be applied to all bands. All arrays must be the
same size.

**Direct Known Subclasses:** ByteLookupTable

,

ShortLookupTable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected LookupTable​(int offset,
int numComponents)

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

**Parameters:**
- offset

- the offset to subtract from input values before indexing
into the data arrays for this

LookupTable
- numComponents

- the number of data arrays in this

LookupTable

**Throws:**
- IllegalArgumentException

- if

offset

is less than 0
or if

numComponents

is less than 1

---

### Method Details

#### public int getNumComponents()

Returns the number of components in the lookup table.

**Returns:**
- the number of components in this

LookupTable

.

---

#### public int getOffset()

Returns the offset.

**Returns:**
- the offset of this

LookupTable

.

---

#### public abstract int[] lookupPixel​(int[] src,
int[] dest)

Returns an

int

array of components for
one pixel. The

dest

array contains the
result of the lookup and is returned. If dest is

null

, a new array is allocated. The
source and destination can be equal.

**Parameters:**
- src

- the source array of components of one pixel
- dest

- the destination array of components for one pixel,
translated with this

LookupTable

**Returns:**
- an

int

array of components for one
pixel.

---

### Additional Sections

#### Class LookupTable

java.lang.Object

- java.awt.image.LookupTable

java.awt.image.LookupTable

**Direct Known Subclasses:** ByteLookupTable

,

ShortLookupTable

```java
public abstract class
LookupTable

extends
Object
```

This abstract class defines a lookup table object. ByteLookupTable
and ShortLookupTable are subclasses, which
contain byte and short data, respectively. A lookup table
contains data arrays for one or more bands (or components) of an image
(for example, separate arrays for R, G, and B),
and it contains an offset which will be subtracted from the
input values before indexing into the arrays. This allows an array
smaller than the native data size to be provided for a
constrained input. If there is only one array in the lookup
table, it will be applied to all bands. All arrays must be the
same size.

**See Also:** ByteLookupTable

,

ShortLookupTable

,

LookupOp

public abstract class

LookupTable

extends

Object

This abstract class defines a lookup table object. ByteLookupTable
and ShortLookupTable are subclasses, which
contain byte and short data, respectively. A lookup table
contains data arrays for one or more bands (or components) of an image
(for example, separate arrays for R, G, and B),
and it contains an offset which will be subtracted from the
input values before indexing into the arrays. This allows an array
smaller than the native data size to be provided for a
constrained input. If there is only one array in the lookup
table, it will be applied to all bands. All arrays must be the
same size.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

LookupTable

​(int offset,
int numComponents)

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

getNumComponents

()

Returns the number of components in the lookup table.

int

getOffset

()

Returns the offset.

abstract int[]

lookupPixel

​(int[] src,
int[] dest)

Returns an

int

array of components for
one pixel.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

LookupTable

​(int offset,
int numComponents)

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

---

#### Constructor Summary

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

getNumComponents

()

Returns the number of components in the lookup table.

int

getOffset

()

Returns the offset.

abstract int[]

lookupPixel

​(int[] src,
int[] dest)

Returns an

int

array of components for
one pixel.

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

Returns the number of components in the lookup table.

Returns the offset.

Returns an

int

array of components for
one pixel.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LookupTable

```java
protected LookupTable​(int offset,
int numComponents)
```

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

**Parameters:** offset

- the offset to subtract from input values before indexing
into the data arrays for this

LookupTable
**Parameters:** numComponents

- the number of data arrays in this

LookupTable
**Throws:** IllegalArgumentException

- if

offset

is less than 0
or if

numComponents

is less than 1

============ METHOD DETAIL ==========

- Method Detail

- getNumComponents

```java
public int getNumComponents()
```

Returns the number of components in the lookup table.

**Returns:** the number of components in this

LookupTable

.

- getOffset

```java
public int getOffset()
```

Returns the offset.

**Returns:** the offset of this

LookupTable

.

- lookupPixel

```java
public abstract int[] lookupPixel​(int[] src,
int[] dest)
```

Returns an

int

array of components for
one pixel. The

dest

array contains the
result of the lookup and is returned. If dest is

null

, a new array is allocated. The
source and destination can be equal.

**Parameters:** src

- the source array of components of one pixel
**Parameters:** dest

- the destination array of components for one pixel,
translated with this

LookupTable
**Returns:** an

int

array of components for one
pixel.

Constructor Detail

- LookupTable

```java
protected LookupTable​(int offset,
int numComponents)
```

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

**Parameters:** offset

- the offset to subtract from input values before indexing
into the data arrays for this

LookupTable
**Parameters:** numComponents

- the number of data arrays in this

LookupTable
**Throws:** IllegalArgumentException

- if

offset

is less than 0
or if

numComponents

is less than 1

---

#### Constructor Detail

LookupTable

```java
protected LookupTable​(int offset,
int numComponents)
```

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

**Parameters:** offset

- the offset to subtract from input values before indexing
into the data arrays for this

LookupTable
**Parameters:** numComponents

- the number of data arrays in this

LookupTable
**Throws:** IllegalArgumentException

- if

offset

is less than 0
or if

numComponents

is less than 1

---

#### LookupTable

protected LookupTable​(int offset,
int numComponents)

Constructs a new LookupTable from the number of components and an offset
into the lookup table.

Method Detail

- getNumComponents

```java
public int getNumComponents()
```

Returns the number of components in the lookup table.

**Returns:** the number of components in this

LookupTable

.

- getOffset

```java
public int getOffset()
```

Returns the offset.

**Returns:** the offset of this

LookupTable

.

- lookupPixel

```java
public abstract int[] lookupPixel​(int[] src,
int[] dest)
```

Returns an

int

array of components for
one pixel. The

dest

array contains the
result of the lookup and is returned. If dest is

null

, a new array is allocated. The
source and destination can be equal.

**Parameters:** src

- the source array of components of one pixel
**Parameters:** dest

- the destination array of components for one pixel,
translated with this

LookupTable
**Returns:** an

int

array of components for one
pixel.

---

#### Method Detail

getNumComponents

```java
public int getNumComponents()
```

Returns the number of components in the lookup table.

**Returns:** the number of components in this

LookupTable

.

---

#### getNumComponents

public int getNumComponents()

Returns the number of components in the lookup table.

getOffset

```java
public int getOffset()
```

Returns the offset.

**Returns:** the offset of this

LookupTable

.

---

#### getOffset

public int getOffset()

Returns the offset.

lookupPixel

```java
public abstract int[] lookupPixel​(int[] src,
int[] dest)
```

Returns an

int

array of components for
one pixel. The

dest

array contains the
result of the lookup and is returned. If dest is

null

, a new array is allocated. The
source and destination can be equal.

**Parameters:** src

- the source array of components of one pixel
**Parameters:** dest

- the destination array of components for one pixel,
translated with this

LookupTable
**Returns:** an

int

array of components for one
pixel.

---

#### lookupPixel

public abstract int[] lookupPixel​(int[] src,
int[] dest)

Returns an

int

array of components for
one pixel. The

dest

array contains the
result of the lookup and is returned. If dest is

null

, a new array is allocated. The
source and destination can be equal.

---

