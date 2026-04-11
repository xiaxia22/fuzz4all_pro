# Class DataBufferUShort

**Source:** `java.desktop\java\awt\image\DataBufferUShort.html`

### Class Description

```java
public final class
DataBufferUShort

extends
DataBuffer
```

This class extends

DataBuffer

and stores data internally as
shorts. Values stored in the short array(s) of this

DataBuffer

are treated as unsigned values.

Note that some implementations may function more efficiently
if they can maintain control over how the data for an image is
stored.
For example, optimizations such as caching an image in video
memory require that the implementation track all modifications
to that data.
Other implementations may operate better if they can store the
data in locations other than a Java array.
To maintain optimum compatibility with various optimizations
it is best to avoid constructors and methods which expose the
underlying storage as a Java array as noted below in the
documentation for those methods.

---

### Field Details

*No entries found.*

### Constructor Details

#### public DataBufferUShort​(int size)

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

**Parameters:**
- size

- The size of the

DataBuffer

.

---

#### public DataBufferUShort​(int size,
int numBanks)

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

**Parameters:**
- size

- The size of the banks in the

DataBuffer

.
- numBanks

- The number of banks in the a

DataBuffer

.

---

#### public DataBufferUShort​(short[] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.
Only the first

size

elements should be used by accessors of
this

DataBuffer

.

dataArray

must be large enough to
hold

size

elements.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:**
- dataArray

- The unsigned-short array for the

DataBuffer

.
- size

- The size of the

DataBuffer

bank.

---

#### public DataBufferUShort​(short[] dataArray,
int size,
int offset)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

dataArray

must have at
least

offset

+

size

elements. Only elements

offset

through

offset

+

size

- 1 should
be used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:**
- dataArray

- The unsigned-short array for the

DataBuffer

.
- size

- The size of the

DataBuffer

bank.
- offset

- The offset into the

dataArray

.

---

#### public DataBufferUShort​(short[][] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with the specified arrays.
The number of banks will be equal to

dataArray.length

.
Only the first

size

elements of each array should be used by
accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:**
- dataArray

- The unsigned-short arrays for the

DataBuffer

.
- size

- The size of the banks in the

DataBuffer

.

---

#### public DataBufferUShort​(short[][] dataArray,
int size,
int[] offsets)

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.
The number of banks is equal to

dataArray.length

. Each array must
be at least as large as

size

+ the corresponding offset. There must
be an entry in the offset array for each

dataArray

entry. For each
bank, only elements

offset

through

offset

+

size

- 1 should be
used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:**
- dataArray

- The unsigned-short arrays for the

DataBuffer

.
- size

- The size of the banks in the

DataBuffer

.
- offsets

- The offsets into each array.

---

### Method Details

#### public short[] getData()

Returns the default (first) unsigned-short data array.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:**
- The first unsigned-short data array.

---

#### public short[] getData​(int bank)

Returns the data array for the specified bank.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:**
- bank

- The bank whose data array you want to get.

**Returns:**
- The data array for the specified bank.

---

#### public short[][] getBankData()

Returns the data arrays for all banks.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:**
- All of the data arrays.

---

#### public int getElem​(int i)

Returns the requested data array element from the first (default) bank.

**Overrides:**
- getElem

in class

DataBuffer

**Parameters:**
- i

- The data array element you want to get.

**Returns:**
- The requested data array element as an integer.

**See Also:**
- setElem(int, int)

,

setElem(int, int, int)

---

#### public int getElem​(int bank,
int i)

Returns the requested data array element from the specified bank.

**Specified by:**
- getElem

in class

DataBuffer

**Parameters:**
- bank

- The bank from which you want to get a data array element.
- i

- The data array element you want to get.

**Returns:**
- The requested data array element as an integer.

**See Also:**
- setElem(int, int)

,

setElem(int, int, int)

---

#### public void setElem​(int i,
int val)

Sets the requested data array element in the first (default) bank
to the specified value.

**Overrides:**
- setElem

in class

DataBuffer

**Parameters:**
- i

- The data array element you want to set.
- val

- The integer value to which you want to set the data array element.

**See Also:**
- getElem(int)

,

getElem(int, int)

---

#### public void setElem​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

**Specified by:**
- setElem

in class

DataBuffer

**Parameters:**
- bank

- The bank in which you want to set the data array element.
- i

- The data array element you want to set.
- val

- The integer value to which you want to set the specified data array element.

**See Also:**
- getElem(int)

,

getElem(int, int)

---

### Additional Sections

#### Class DataBufferUShort

java.lang.Object

- java.awt.image.DataBuffer
- - java.awt.image.DataBufferUShort

java.awt.image.DataBuffer

- java.awt.image.DataBufferUShort

java.awt.image.DataBufferUShort

```java
public final class
DataBufferUShort

extends
DataBuffer
```

This class extends

DataBuffer

and stores data internally as
shorts. Values stored in the short array(s) of this

DataBuffer

are treated as unsigned values.

Note that some implementations may function more efficiently
if they can maintain control over how the data for an image is
stored.
For example, optimizations such as caching an image in video
memory require that the implementation track all modifications
to that data.
Other implementations may operate better if they can store the
data in locations other than a Java array.
To maintain optimum compatibility with various optimizations
it is best to avoid constructors and methods which expose the
underlying storage as a Java array as noted below in the
documentation for those methods.

public final class

DataBufferUShort

extends

DataBuffer

This class extends

DataBuffer

and stores data internally as
shorts. Values stored in the short array(s) of this

DataBuffer

are treated as unsigned values.

Note that some implementations may function more efficiently
if they can maintain control over how the data for an image is
stored.
For example, optimizations such as caching an image in video
memory require that the implementation track all modifications
to that data.
Other implementations may operate better if they can store the
data in locations other than a Java array.
To maintain optimum compatibility with various optimizations
it is best to avoid constructors and methods which expose the
underlying storage as a Java array as noted below in the
documentation for those methods.

Note that some implementations may function more efficiently
if they can maintain control over how the data for an image is
stored.
For example, optimizations such as caching an image in video
memory require that the implementation track all modifications
to that data.
Other implementations may operate better if they can store the
data in locations other than a Java array.
To maintain optimum compatibility with various optimizations
it is best to avoid constructors and methods which expose the
underlying storage as a Java array as noted below in the
documentation for those methods.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

DataBuffer

banks

,

dataType

,

offset

,

offsets

,

size

,

TYPE_BYTE

,

TYPE_DOUBLE

,

TYPE_FLOAT

,

TYPE_INT

,

TYPE_SHORT

,

TYPE_UNDEFINED

,

TYPE_USHORT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DataBufferUShort

​(int size)

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

DataBufferUShort

​(int size,
int numBanks)

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

DataBufferUShort

​(short[][] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with the specified arrays.

DataBufferUShort

​(short[][] dataArray,
int size,
int[] offsets)

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.

DataBufferUShort

​(short[] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.

DataBufferUShort

​(short[] dataArray,
int size,
int offset)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

short[][]

getBankData

()

Returns the data arrays for all banks.

short[]

getData

()

Returns the default (first) unsigned-short data array.

short[]

getData

​(int bank)

Returns the data array for the specified bank.

int

getElem

​(int i)

Returns the requested data array element from the first (default) bank.

int

getElem

​(int bank,
int i)

Returns the requested data array element from the specified bank.

void

setElem

​(int i,
int val)

Sets the requested data array element in the first (default) bank
to the specified value.

void

setElem

​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

- Methods declared in class java.awt.image.

DataBuffer

getDataType

,

getDataTypeSize

,

getElemDouble

,

getElemDouble

,

getElemFloat

,

getElemFloat

,

getNumBanks

,

getOffset

,

getOffsets

,

getSize

,

setElemDouble

,

setElemDouble

,

setElemFloat

,

setElemFloat

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

Field Summary

- Fields declared in class java.awt.image.

DataBuffer

banks

,

dataType

,

offset

,

offsets

,

size

,

TYPE_BYTE

,

TYPE_DOUBLE

,

TYPE_FLOAT

,

TYPE_INT

,

TYPE_SHORT

,

TYPE_UNDEFINED

,

TYPE_USHORT

---

#### Field Summary

Fields declared in class java.awt.image.

DataBuffer

banks

,

dataType

,

offset

,

offsets

,

size

,

TYPE_BYTE

,

TYPE_DOUBLE

,

TYPE_FLOAT

,

TYPE_INT

,

TYPE_SHORT

,

TYPE_UNDEFINED

,

TYPE_USHORT

---

#### Fields declared in class java.awt.image. DataBuffer

Constructor Summary

Constructors

Constructor

Description

DataBufferUShort

​(int size)

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

DataBufferUShort

​(int size,
int numBanks)

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

DataBufferUShort

​(short[][] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with the specified arrays.

DataBufferUShort

​(short[][] dataArray,
int size,
int[] offsets)

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.

DataBufferUShort

​(short[] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.

DataBufferUShort

​(short[] dataArray,
int size,
int offset)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

---

#### Constructor Summary

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

Constructs an unsigned-short based

DataBuffer

with the specified arrays.

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

short[][]

getBankData

()

Returns the data arrays for all banks.

short[]

getData

()

Returns the default (first) unsigned-short data array.

short[]

getData

​(int bank)

Returns the data array for the specified bank.

int

getElem

​(int i)

Returns the requested data array element from the first (default) bank.

int

getElem

​(int bank,
int i)

Returns the requested data array element from the specified bank.

void

setElem

​(int i,
int val)

Sets the requested data array element in the first (default) bank
to the specified value.

void

setElem

​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

- Methods declared in class java.awt.image.

DataBuffer

getDataType

,

getDataTypeSize

,

getElemDouble

,

getElemDouble

,

getElemFloat

,

getElemFloat

,

getNumBanks

,

getOffset

,

getOffsets

,

getSize

,

setElemDouble

,

setElemDouble

,

setElemFloat

,

setElemFloat

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

Returns the data arrays for all banks.

Returns the default (first) unsigned-short data array.

Returns the data array for the specified bank.

Returns the requested data array element from the first (default) bank.

Returns the requested data array element from the specified bank.

Sets the requested data array element in the first (default) bank
to the specified value.

Sets the requested data array element in the specified bank
from the given integer.

Methods declared in class java.awt.image.

DataBuffer

getDataType

,

getDataTypeSize

,

getElemDouble

,

getElemDouble

,

getElemFloat

,

getElemFloat

,

getNumBanks

,

getOffset

,

getOffsets

,

getSize

,

setElemDouble

,

setElemDouble

,

setElemFloat

,

setElemFloat

---

#### Methods declared in class java.awt.image. DataBuffer

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

- DataBufferUShort

```java
public DataBufferUShort​(int size)
```

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

**Parameters:** size

- The size of the

DataBuffer

.

- DataBufferUShort

```java
public DataBufferUShort​(int size,
int numBanks)
```

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

**Parameters:** size

- The size of the banks in the

DataBuffer

.
**Parameters:** numBanks

- The number of banks in the a

DataBuffer

.

- DataBufferUShort

```java
public DataBufferUShort​(short[] dataArray,
int size)
```

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.
Only the first

size

elements should be used by accessors of
this

DataBuffer

.

dataArray

must be large enough to
hold

size

elements.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short array for the

DataBuffer

.
**Parameters:** size

- The size of the

DataBuffer

bank.

- DataBufferUShort

```java
public DataBufferUShort​(short[] dataArray,
int size,
int offset)
```

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

dataArray

must have at
least

offset

+

size

elements. Only elements

offset

through

offset

+

size

- 1 should
be used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short array for the

DataBuffer

.
**Parameters:** size

- The size of the

DataBuffer

bank.
**Parameters:** offset

- The offset into the

dataArray

.

- DataBufferUShort

```java
public DataBufferUShort​(short[][] dataArray,
int size)
```

Constructs an unsigned-short based

DataBuffer

with the specified arrays.
The number of banks will be equal to

dataArray.length

.
Only the first

size

elements of each array should be used by
accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short arrays for the

DataBuffer

.
**Parameters:** size

- The size of the banks in the

DataBuffer

.

- DataBufferUShort

```java
public DataBufferUShort​(short[][] dataArray,
int size,
int[] offsets)
```

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.
The number of banks is equal to

dataArray.length

. Each array must
be at least as large as

size

+ the corresponding offset. There must
be an entry in the offset array for each

dataArray

entry. For each
bank, only elements

offset

through

offset

+

size

- 1 should be
used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short arrays for the

DataBuffer

.
**Parameters:** size

- The size of the banks in the

DataBuffer

.
**Parameters:** offsets

- The offsets into each array.

============ METHOD DETAIL ==========

- Method Detail

- getData

```java
public short[] getData()
```

Returns the default (first) unsigned-short data array.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:** The first unsigned-short data array.

- getData

```java
public short[] getData​(int bank)
```

Returns the data array for the specified bank.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** bank

- The bank whose data array you want to get.
**Returns:** The data array for the specified bank.

- getBankData

```java
public short[][] getBankData()
```

Returns the data arrays for all banks.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:** All of the data arrays.

- getElem

```java
public int getElem​(int i)
```

Returns the requested data array element from the first (default) bank.

**Overrides:** getElem

in class

DataBuffer
**Parameters:** i

- The data array element you want to get.
**Returns:** The requested data array element as an integer.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- getElem

```java
public int getElem​(int bank,
int i)
```

Returns the requested data array element from the specified bank.

**Specified by:** getElem

in class

DataBuffer
**Parameters:** bank

- The bank from which you want to get a data array element.
**Parameters:** i

- The data array element you want to get.
**Returns:** The requested data array element as an integer.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- setElem

```java
public void setElem​(int i,
int val)
```

Sets the requested data array element in the first (default) bank
to the specified value.

**Overrides:** setElem

in class

DataBuffer
**Parameters:** i

- The data array element you want to set.
**Parameters:** val

- The integer value to which you want to set the data array element.
**See Also:** getElem(int)

,

getElem(int, int)

- setElem

```java
public void setElem​(int bank,
int i,
int val)
```

Sets the requested data array element in the specified bank
from the given integer.

**Specified by:** setElem

in class

DataBuffer
**Parameters:** bank

- The bank in which you want to set the data array element.
**Parameters:** i

- The data array element you want to set.
**Parameters:** val

- The integer value to which you want to set the specified data array element.
**See Also:** getElem(int)

,

getElem(int, int)

Constructor Detail

- DataBufferUShort

```java
public DataBufferUShort​(int size)
```

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

**Parameters:** size

- The size of the

DataBuffer

.

- DataBufferUShort

```java
public DataBufferUShort​(int size,
int numBanks)
```

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

**Parameters:** size

- The size of the banks in the

DataBuffer

.
**Parameters:** numBanks

- The number of banks in the a

DataBuffer

.

- DataBufferUShort

```java
public DataBufferUShort​(short[] dataArray,
int size)
```

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.
Only the first

size

elements should be used by accessors of
this

DataBuffer

.

dataArray

must be large enough to
hold

size

elements.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short array for the

DataBuffer

.
**Parameters:** size

- The size of the

DataBuffer

bank.

- DataBufferUShort

```java
public DataBufferUShort​(short[] dataArray,
int size,
int offset)
```

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

dataArray

must have at
least

offset

+

size

elements. Only elements

offset

through

offset

+

size

- 1 should
be used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short array for the

DataBuffer

.
**Parameters:** size

- The size of the

DataBuffer

bank.
**Parameters:** offset

- The offset into the

dataArray

.

- DataBufferUShort

```java
public DataBufferUShort​(short[][] dataArray,
int size)
```

Constructs an unsigned-short based

DataBuffer

with the specified arrays.
The number of banks will be equal to

dataArray.length

.
Only the first

size

elements of each array should be used by
accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short arrays for the

DataBuffer

.
**Parameters:** size

- The size of the banks in the

DataBuffer

.

- DataBufferUShort

```java
public DataBufferUShort​(short[][] dataArray,
int size,
int[] offsets)
```

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.
The number of banks is equal to

dataArray.length

. Each array must
be at least as large as

size

+ the corresponding offset. There must
be an entry in the offset array for each

dataArray

entry. For each
bank, only elements

offset

through

offset

+

size

- 1 should be
used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short arrays for the

DataBuffer

.
**Parameters:** size

- The size of the banks in the

DataBuffer

.
**Parameters:** offsets

- The offsets into each array.

---

#### Constructor Detail

DataBufferUShort

```java
public DataBufferUShort​(int size)
```

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

**Parameters:** size

- The size of the

DataBuffer

.

---

#### DataBufferUShort

public DataBufferUShort​(int size)

Constructs an unsigned-short based

DataBuffer

with a single bank and the
specified size.

DataBufferUShort

```java
public DataBufferUShort​(int size,
int numBanks)
```

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

**Parameters:** size

- The size of the banks in the

DataBuffer

.
**Parameters:** numBanks

- The number of banks in the a

DataBuffer

.

---

#### DataBufferUShort

public DataBufferUShort​(int size,
int numBanks)

Constructs an unsigned-short based

DataBuffer

with the specified number of
banks, all of which are the specified size.

DataBufferUShort

```java
public DataBufferUShort​(short[] dataArray,
int size)
```

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.
Only the first

size

elements should be used by accessors of
this

DataBuffer

.

dataArray

must be large enough to
hold

size

elements.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short array for the

DataBuffer

.
**Parameters:** size

- The size of the

DataBuffer

bank.

---

#### DataBufferUShort

public DataBufferUShort​(short[] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array.
Only the first

size

elements should be used by accessors of
this

DataBuffer

.

dataArray

must be large enough to
hold

size

elements.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

DataBufferUShort

```java
public DataBufferUShort​(short[] dataArray,
int size,
int offset)
```

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

dataArray

must have at
least

offset

+

size

elements. Only elements

offset

through

offset

+

size

- 1 should
be used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short array for the

DataBuffer

.
**Parameters:** size

- The size of the

DataBuffer

bank.
**Parameters:** offset

- The offset into the

dataArray

.

---

#### DataBufferUShort

public DataBufferUShort​(short[] dataArray,
int size,
int offset)

Constructs an unsigned-short based

DataBuffer

with a single bank
using the specified array, size, and offset.

dataArray

must have at
least

offset

+

size

elements. Only elements

offset

through

offset

+

size

- 1 should
be used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

DataBufferUShort

```java
public DataBufferUShort​(short[][] dataArray,
int size)
```

Constructs an unsigned-short based

DataBuffer

with the specified arrays.
The number of banks will be equal to

dataArray.length

.
Only the first

size

elements of each array should be used by
accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short arrays for the

DataBuffer

.
**Parameters:** size

- The size of the banks in the

DataBuffer

.

---

#### DataBufferUShort

public DataBufferUShort​(short[][] dataArray,
int size)

Constructs an unsigned-short based

DataBuffer

with the specified arrays.
The number of banks will be equal to

dataArray.length

.
Only the first

size

elements of each array should be used by
accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

DataBufferUShort

```java
public DataBufferUShort​(short[][] dataArray,
int size,
int[] offsets)
```

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.
The number of banks is equal to

dataArray.length

. Each array must
be at least as large as

size

+ the corresponding offset. There must
be an entry in the offset array for each

dataArray

entry. For each
bank, only elements

offset

through

offset

+

size

- 1 should be
used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** dataArray

- The unsigned-short arrays for the

DataBuffer

.
**Parameters:** size

- The size of the banks in the

DataBuffer

.
**Parameters:** offsets

- The offsets into each array.

---

#### DataBufferUShort

public DataBufferUShort​(short[][] dataArray,
int size,
int[] offsets)

Constructs an unsigned-short based

DataBuffer

with specified arrays,
size, and offsets.
The number of banks is equal to

dataArray.length

. Each array must
be at least as large as

size

+ the corresponding offset. There must
be an entry in the offset array for each

dataArray

entry. For each
bank, only elements

offset

through

offset

+

size

- 1 should be
used by accessors of this

DataBuffer

.

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Note that

DataBuffer

objects created by this constructor
may be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Method Detail

- getData

```java
public short[] getData()
```

Returns the default (first) unsigned-short data array.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:** The first unsigned-short data array.

- getData

```java
public short[] getData​(int bank)
```

Returns the data array for the specified bank.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** bank

- The bank whose data array you want to get.
**Returns:** The data array for the specified bank.

- getBankData

```java
public short[][] getBankData()
```

Returns the data arrays for all banks.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:** All of the data arrays.

- getElem

```java
public int getElem​(int i)
```

Returns the requested data array element from the first (default) bank.

**Overrides:** getElem

in class

DataBuffer
**Parameters:** i

- The data array element you want to get.
**Returns:** The requested data array element as an integer.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- getElem

```java
public int getElem​(int bank,
int i)
```

Returns the requested data array element from the specified bank.

**Specified by:** getElem

in class

DataBuffer
**Parameters:** bank

- The bank from which you want to get a data array element.
**Parameters:** i

- The data array element you want to get.
**Returns:** The requested data array element as an integer.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- setElem

```java
public void setElem​(int i,
int val)
```

Sets the requested data array element in the first (default) bank
to the specified value.

**Overrides:** setElem

in class

DataBuffer
**Parameters:** i

- The data array element you want to set.
**Parameters:** val

- The integer value to which you want to set the data array element.
**See Also:** getElem(int)

,

getElem(int, int)

- setElem

```java
public void setElem​(int bank,
int i,
int val)
```

Sets the requested data array element in the specified bank
from the given integer.

**Specified by:** setElem

in class

DataBuffer
**Parameters:** bank

- The bank in which you want to set the data array element.
**Parameters:** i

- The data array element you want to set.
**Parameters:** val

- The integer value to which you want to set the specified data array element.
**See Also:** getElem(int)

,

getElem(int, int)

---

#### Method Detail

getData

```java
public short[] getData()
```

Returns the default (first) unsigned-short data array.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:** The first unsigned-short data array.

---

#### getData

public short[] getData()

Returns the default (first) unsigned-short data array.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

getData

```java
public short[] getData​(int bank)
```

Returns the data array for the specified bank.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Parameters:** bank

- The bank whose data array you want to get.
**Returns:** The data array for the specified bank.

---

#### getData

public short[] getData​(int bank)

Returns the data array for the specified bank.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

getBankData

```java
public short[][] getBankData()
```

Returns the data arrays for all banks.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

**Returns:** All of the data arrays.

---

#### getBankData

public short[][] getBankData()

Returns the data arrays for all banks.

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

Note that calling this method may cause this

DataBuffer

object to be incompatible with

performance
optimizations

used by some implementations (such as caching
an associated image in video memory).

getElem

```java
public int getElem​(int i)
```

Returns the requested data array element from the first (default) bank.

**Overrides:** getElem

in class

DataBuffer
**Parameters:** i

- The data array element you want to get.
**Returns:** The requested data array element as an integer.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

---

#### getElem

public int getElem​(int i)

Returns the requested data array element from the first (default) bank.

getElem

```java
public int getElem​(int bank,
int i)
```

Returns the requested data array element from the specified bank.

**Specified by:** getElem

in class

DataBuffer
**Parameters:** bank

- The bank from which you want to get a data array element.
**Parameters:** i

- The data array element you want to get.
**Returns:** The requested data array element as an integer.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

---

#### getElem

public int getElem​(int bank,
int i)

Returns the requested data array element from the specified bank.

setElem

```java
public void setElem​(int i,
int val)
```

Sets the requested data array element in the first (default) bank
to the specified value.

**Overrides:** setElem

in class

DataBuffer
**Parameters:** i

- The data array element you want to set.
**Parameters:** val

- The integer value to which you want to set the data array element.
**See Also:** getElem(int)

,

getElem(int, int)

---

#### setElem

public void setElem​(int i,
int val)

Sets the requested data array element in the first (default) bank
to the specified value.

setElem

```java
public void setElem​(int bank,
int i,
int val)
```

Sets the requested data array element in the specified bank
from the given integer.

**Specified by:** setElem

in class

DataBuffer
**Parameters:** bank

- The bank in which you want to set the data array element.
**Parameters:** i

- The data array element you want to set.
**Parameters:** val

- The integer value to which you want to set the specified data array element.
**See Also:** getElem(int)

,

getElem(int, int)

---

#### setElem

public void setElem​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

---

