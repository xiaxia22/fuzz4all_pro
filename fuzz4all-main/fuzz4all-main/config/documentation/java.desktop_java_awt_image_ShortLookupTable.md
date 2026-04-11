# Class ShortLookupTable

**Source:** `java.desktop\java\awt\image\ShortLookupTable.html`

### Class Description

```java
public class
ShortLookupTable

extends
LookupTable
```

This class defines a lookup table object. The output of a
lookup operation using an object of this class is interpreted
as an unsigned short quantity. The lookup table contains short
data arrays for one or more bands (or components) of an image,
and it contains an offset which will be subtracted from the
input values before indexing the arrays. This allows an array
smaller than the native data size to be provided for a
constrained input. If there is only one array in the lookup
table, it will be applied to all bands.

**See Also:** ByteLookupTable

,

LookupOp

---

### Field Details

*No entries found.*

### Constructor Details

#### public ShortLookupTable​(int offset,
short[][] data)

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the arrays. The number of
bands is the length of the data argument. The
data array for each band is stored as a reference.

**Parameters:**
- offset

- the value subtracted from the input values
before indexing into the arrays
- data

- an array of short arrays representing a lookup
table for each band

---

#### public ShortLookupTable​(int offset,
short[] data)

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the array. The
data array is stored as a reference.

**Parameters:**
- offset

- the value subtracted from the input values
before indexing into the arrays
- data

- an array of shorts

---

### Method Details

#### public final short[][] getTable()

Returns the lookup table data by reference. If this ShortLookupTable
was constructed using a single short array, the length of the returned
array is one.

**Returns:**
- ShortLookupTable data array.

---

#### public int[] lookupPixel​(int[] src,
int[] dst)

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Specified by:**
- lookupPixel

in class

LookupTable

**Parameters:**
- src

- the source array.
- dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.

**Returns:**
- the array

dst

, an

int

array of
samples.

**Throws:**
- ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

---

#### public short[] lookupPixel​(short[] src,
short[] dst)

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Parameters:**
- src

- the source array.
- dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.

**Returns:**
- the array

dst

, an

int

array of
samples.

**Throws:**
- ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

---

### Additional Sections

#### Class ShortLookupTable

java.lang.Object

- java.awt.image.LookupTable
- - java.awt.image.ShortLookupTable

java.awt.image.LookupTable

- java.awt.image.ShortLookupTable

java.awt.image.ShortLookupTable

```java
public class
ShortLookupTable

extends
LookupTable
```

This class defines a lookup table object. The output of a
lookup operation using an object of this class is interpreted
as an unsigned short quantity. The lookup table contains short
data arrays for one or more bands (or components) of an image,
and it contains an offset which will be subtracted from the
input values before indexing the arrays. This allows an array
smaller than the native data size to be provided for a
constrained input. If there is only one array in the lookup
table, it will be applied to all bands.

**See Also:** ByteLookupTable

,

LookupOp

public class

ShortLookupTable

extends

LookupTable

This class defines a lookup table object. The output of a
lookup operation using an object of this class is interpreted
as an unsigned short quantity. The lookup table contains short
data arrays for one or more bands (or components) of an image,
and it contains an offset which will be subtracted from the
input values before indexing the arrays. This allows an array
smaller than the native data size to be provided for a
constrained input. If there is only one array in the lookup
table, it will be applied to all bands.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ShortLookupTable

​(int offset,
short[] data)

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band.

ShortLookupTable

​(int offset,
short[][] data)

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

short[][]

getTable

()

Returns the lookup table data by reference.

int[]

lookupPixel

​(int[] src,
int[] dst)

Returns an array of samples of a pixel, translated with the lookup
table.

short[]

lookupPixel

​(short[] src,
short[] dst)

Returns an array of samples of a pixel, translated with the lookup
table.

- Methods declared in class java.awt.image.

LookupTable

getNumComponents

,

getOffset

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

Constructor

Description

ShortLookupTable

​(int offset,
short[] data)

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band.

ShortLookupTable

​(int offset,
short[][] data)

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band.

---

#### Constructor Summary

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band.

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

short[][]

getTable

()

Returns the lookup table data by reference.

int[]

lookupPixel

​(int[] src,
int[] dst)

Returns an array of samples of a pixel, translated with the lookup
table.

short[]

lookupPixel

​(short[] src,
short[] dst)

Returns an array of samples of a pixel, translated with the lookup
table.

- Methods declared in class java.awt.image.

LookupTable

getNumComponents

,

getOffset

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

Returns the lookup table data by reference.

Returns an array of samples of a pixel, translated with the lookup
table.

Methods declared in class java.awt.image.

LookupTable

getNumComponents

,

getOffset

---

#### Methods declared in class java.awt.image. LookupTable

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

- ShortLookupTable

```java
public ShortLookupTable​(int offset,
short[][] data)
```

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the arrays. The number of
bands is the length of the data argument. The
data array for each band is stored as a reference.

**Parameters:** offset

- the value subtracted from the input values
before indexing into the arrays
**Parameters:** data

- an array of short arrays representing a lookup
table for each band

- ShortLookupTable

```java
public ShortLookupTable​(int offset,
short[] data)
```

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the array. The
data array is stored as a reference.

**Parameters:** offset

- the value subtracted from the input values
before indexing into the arrays
**Parameters:** data

- an array of shorts

============ METHOD DETAIL ==========

- Method Detail

- getTable

```java
public final short[][] getTable()
```

Returns the lookup table data by reference. If this ShortLookupTable
was constructed using a single short array, the length of the returned
array is one.

**Returns:** ShortLookupTable data array.

- lookupPixel

```java
public int[] lookupPixel​(int[] src,
int[] dst)
```

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Specified by:** lookupPixel

in class

LookupTable
**Parameters:** src

- the source array.
**Parameters:** dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.
**Returns:** the array

dst

, an

int

array of
samples.
**Throws:** ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

- lookupPixel

```java
public short[] lookupPixel​(short[] src,
short[] dst)
```

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Parameters:** src

- the source array.
**Parameters:** dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.
**Returns:** the array

dst

, an

int

array of
samples.
**Throws:** ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

Constructor Detail

- ShortLookupTable

```java
public ShortLookupTable​(int offset,
short[][] data)
```

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the arrays. The number of
bands is the length of the data argument. The
data array for each band is stored as a reference.

**Parameters:** offset

- the value subtracted from the input values
before indexing into the arrays
**Parameters:** data

- an array of short arrays representing a lookup
table for each band

- ShortLookupTable

```java
public ShortLookupTable​(int offset,
short[] data)
```

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the array. The
data array is stored as a reference.

**Parameters:** offset

- the value subtracted from the input values
before indexing into the arrays
**Parameters:** data

- an array of shorts

---

#### Constructor Detail

ShortLookupTable

```java
public ShortLookupTable​(int offset,
short[][] data)
```

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the arrays. The number of
bands is the length of the data argument. The
data array for each band is stored as a reference.

**Parameters:** offset

- the value subtracted from the input values
before indexing into the arrays
**Parameters:** data

- an array of short arrays representing a lookup
table for each band

---

#### ShortLookupTable

public ShortLookupTable​(int offset,
short[][] data)

Constructs a ShortLookupTable object from an array of short
arrays representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the arrays. The number of
bands is the length of the data argument. The
data array for each band is stored as a reference.

ShortLookupTable

```java
public ShortLookupTable​(int offset,
short[] data)
```

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the array. The
data array is stored as a reference.

**Parameters:** offset

- the value subtracted from the input values
before indexing into the arrays
**Parameters:** data

- an array of shorts

---

#### ShortLookupTable

public ShortLookupTable​(int offset,
short[] data)

Constructs a ShortLookupTable object from an array
of shorts representing a lookup table for each
band. The offset will be subtracted from the input
values before indexing into the array. The
data array is stored as a reference.

Method Detail

- getTable

```java
public final short[][] getTable()
```

Returns the lookup table data by reference. If this ShortLookupTable
was constructed using a single short array, the length of the returned
array is one.

**Returns:** ShortLookupTable data array.

- lookupPixel

```java
public int[] lookupPixel​(int[] src,
int[] dst)
```

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Specified by:** lookupPixel

in class

LookupTable
**Parameters:** src

- the source array.
**Parameters:** dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.
**Returns:** the array

dst

, an

int

array of
samples.
**Throws:** ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

- lookupPixel

```java
public short[] lookupPixel​(short[] src,
short[] dst)
```

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Parameters:** src

- the source array.
**Parameters:** dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.
**Returns:** the array

dst

, an

int

array of
samples.
**Throws:** ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

---

#### Method Detail

getTable

```java
public final short[][] getTable()
```

Returns the lookup table data by reference. If this ShortLookupTable
was constructed using a single short array, the length of the returned
array is one.

**Returns:** ShortLookupTable data array.

---

#### getTable

public final short[][] getTable()

Returns the lookup table data by reference. If this ShortLookupTable
was constructed using a single short array, the length of the returned
array is one.

lookupPixel

```java
public int[] lookupPixel​(int[] src,
int[] dst)
```

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Specified by:** lookupPixel

in class

LookupTable
**Parameters:** src

- the source array.
**Parameters:** dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.
**Returns:** the array

dst

, an

int

array of
samples.
**Throws:** ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

---

#### lookupPixel

public int[] lookupPixel​(int[] src,
int[] dst)

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

lookupPixel

```java
public short[] lookupPixel​(short[] src,
short[] dst)
```

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

**Parameters:** src

- the source array.
**Parameters:** dst

- the destination array. This array must be at least as
long as

src

. If

dst

is

null

, a new array will be allocated having the
same length as

src

.
**Returns:** the array

dst

, an

int

array of
samples.
**Throws:** ArrayIndexOutOfBoundsException

- if

src

is
longer than

dst

or if for any element

i

of

src

,

(src[i]&0xffff)-offset

is either less than
zero or greater than or equal to the length of the
lookup table for any band.

---

#### lookupPixel

public short[] lookupPixel​(short[] src,
short[] dst)

Returns an array of samples of a pixel, translated with the lookup
table. The source and destination array can be the same array.
Array

dst

is returned.

---

