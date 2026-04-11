# Class DataBuffer

**Source:** `java.desktop\java\awt\image\DataBuffer.html`

### Class Description

```java
public abstract class
DataBuffer

extends
Object
```

This class exists to wrap one or more data arrays. Each data array in
the DataBuffer is referred to as a bank. Accessor methods for getting
and setting elements of the DataBuffer's banks exist with and without
a bank specifier. The methods without a bank specifier use the default 0th
bank. The DataBuffer can optionally take an offset per bank, so that
data in an existing array can be used even if the interesting data
doesn't start at array location zero. Getting or setting the 0th
element of a bank, uses the (0+offset)th element of the array. The
size field specifies how much of the data array is available for
use. Size + offset for a given bank should never be greater
than the length of the associated data array. The data type of
a data buffer indicates the type of the data array(s) and may also
indicate additional semantics, e.g. storing unsigned 8-bit data
in elements of a byte array. The data type may be TYPE_UNDEFINED
or one of the types defined below. Other types may be added in
the future. Generally, an object of class DataBuffer will be cast down
to one of its data type specific subclasses to access data type specific
methods for improved performance. Currently, the Java 2D(tm) API
image classes use TYPE_BYTE, TYPE_USHORT, TYPE_INT, TYPE_SHORT,
TYPE_FLOAT, and TYPE_DOUBLE DataBuffers to store image data.

**Direct Known Subclasses:** DataBufferByte

,

DataBufferDouble

,

DataBufferFloat

,

DataBufferInt

,

DataBufferShort

,

DataBufferUShort

---

### Field Details

#### @Native

public static final int TYPE_BYTE

Tag for unsigned byte data.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_USHORT

Tag for unsigned short data.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_SHORT

Tag for signed short data. Placeholder for future use.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_INT

Tag for int data.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_FLOAT

Tag for float data. Placeholder for future use.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_DOUBLE

Tag for double data. Placeholder for future use.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_UNDEFINED

Tag for undefined data.

**See Also:**
- Constant Field Values

---

#### protected int dataType

The data type of this DataBuffer.

---

#### protected int banks

The number of banks in this DataBuffer.

---

#### protected int offset

Offset into default (first) bank from which to get the first element.

---

#### protected int size

Usable size of all banks.

---

#### protected int[] offsets

Offsets into all banks.

---

### Constructor Details

#### protected DataBuffer​(int dataType,
int size)

Constructs a DataBuffer containing one bank of the specified
data type and size.

**Parameters:**
- dataType

- the data type of this

DataBuffer
- size

- the size of the banks

---

#### protected DataBuffer​(int dataType,
int size,
int numBanks)

Constructs a DataBuffer containing the specified number of
banks. Each bank has the specified size and an offset of 0.

**Parameters:**
- dataType

- the data type of this

DataBuffer
- size

- the size of the banks
- numBanks

- the number of banks in this

DataBuffer

---

#### protected DataBuffer​(int dataType,
int size,
int numBanks,
int offset)

Constructs a DataBuffer that contains the specified number
of banks. Each bank has the specified datatype, size and offset.

**Parameters:**
- dataType

- the data type of this

DataBuffer
- size

- the size of the banks
- numBanks

- the number of banks in this

DataBuffer
- offset

- the offset for each bank

---

#### protected DataBuffer​(int dataType,
int size,
int numBanks,
int[] offsets)

Constructs a DataBuffer which contains the specified number
of banks. Each bank has the specified datatype and size. The
offset for each bank is specified by its respective entry in
the offsets array.

**Parameters:**
- dataType

- the data type of this

DataBuffer
- size

- the size of the banks
- numBanks

- the number of banks in this

DataBuffer
- offsets

- an array containing an offset for each bank.

**Throws:**
- ArrayIndexOutOfBoundsException

- if

numBanks

does not equal the length of

offsets

---

### Method Details

#### public static int getDataTypeSize​(int type)

Returns the size (in bits) of the data type, given a datatype tag.

**Parameters:**
- type

- the value of one of the defined datatype tags

**Returns:**
- the size of the data type

**Throws:**
- IllegalArgumentException

- if

type

is less than
zero or greater than

TYPE_DOUBLE

---

#### public int getDataType()

Returns the data type of this DataBuffer.

**Returns:**
- the data type of this

DataBuffer

.

---

#### public int getSize()

Returns the size (in array elements) of all banks.

**Returns:**
- the size of all banks.

---

#### public int getOffset()

Returns the offset of the default bank in array elements.

**Returns:**
- the offset of the default bank.

---

#### public int[] getOffsets()

Returns the offsets (in array elements) of all the banks.

**Returns:**
- the offsets of all banks.

---

#### public int getNumBanks()

Returns the number of banks in this DataBuffer.

**Returns:**
- the number of banks.

---

#### public int getElem​(int i)

Returns the requested data array element from the first (default) bank
as an integer.

**Parameters:**
- i

- the index of the requested data array element

**Returns:**
- the data array element at the specified index.

**See Also:**
- setElem(int, int)

,

setElem(int, int, int)

---

#### public abstract int getElem​(int bank,
int i)

Returns the requested data array element from the specified bank
as an integer.

**Parameters:**
- bank

- the specified bank
- i

- the index of the requested data array element

**Returns:**
- the data array element at the specified index from the
specified bank at the specified index.

**See Also:**
- setElem(int, int)

,

setElem(int, int, int)

---

#### public void setElem​(int i,
int val)

Sets the requested data array element in the first (default) bank
from the given integer.

**Parameters:**
- i

- the specified index into the data array
- val

- the data to set the element at the specified index in
the data array

**See Also:**
- getElem(int)

,

getElem(int, int)

---

#### public abstract void setElem​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

**Parameters:**
- bank

- the specified bank
- i

- the specified index into the data array
- val

- the data to set the element in the specified bank
at the specified index in the data array

**See Also:**
- getElem(int)

,

getElem(int, int)

---

#### public float getElemFloat​(int i)

Returns the requested data array element from the first (default) bank
as a float. The implementation in this class is to cast getElem(i)
to a float. Subclasses may override this method if another
implementation is needed.

**Parameters:**
- i

- the index of the requested data array element

**Returns:**
- a float value representing the data array element at the
specified index.

**See Also:**
- setElemFloat(int, float)

,

setElemFloat(int, int, float)

---

#### public float getElemFloat​(int bank,
int i)

Returns the requested data array element from the specified bank
as a float. The implementation in this class is to cast

getElem(int, int)

to a float. Subclasses can override this method if another
implementation is needed.

**Parameters:**
- bank

- the specified bank
- i

- the index of the requested data array element

**Returns:**
- a float value representing the data array element from the
specified bank at the specified index.

**See Also:**
- setElemFloat(int, float)

,

setElemFloat(int, int, float)

---

#### public void setElemFloat​(int i,
float val)

Sets the requested data array element in the first (default) bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses
can override this method if another implementation is needed.

**Parameters:**
- i

- the specified index
- val

- the value to set the element at the specified index in
the data array

**See Also:**
- getElemFloat(int)

,

getElemFloat(int, int)

---

#### public void setElemFloat​(int bank,
int i,
float val)

Sets the requested data array element in the specified bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:**
- bank

- the specified bank
- i

- the specified index
- val

- the value to set the element in the specified bank at
the specified index in the data array

**See Also:**
- getElemFloat(int)

,

getElemFloat(int, int)

---

#### public double getElemDouble​(int i)

Returns the requested data array element from the first (default) bank
as a double. The implementation in this class is to cast

getElem(int)

to a double. Subclasses can override this method if another
implementation is needed.

**Parameters:**
- i

- the specified index

**Returns:**
- a double value representing the element at the specified
index in the data array.

**See Also:**
- setElemDouble(int, double)

,

setElemDouble(int, int, double)

---

#### public double getElemDouble​(int bank,
int i)

Returns the requested data array element from the specified bank as
a double. The implementation in this class is to cast getElem(bank, i)
to a double. Subclasses may override this method if another
implementation is needed.

**Parameters:**
- bank

- the specified bank
- i

- the specified index

**Returns:**
- a double value representing the element from the specified
bank at the specified index in the data array.

**See Also:**
- setElemDouble(int, double)

,

setElemDouble(int, int, double)

---

#### public void setElemDouble​(int i,
double val)

Sets the requested data array element in the first (default) bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:**
- i

- the specified index
- val

- the value to set the element at the specified index
in the data array

**See Also:**
- getElemDouble(int)

,

getElemDouble(int, int)

---

#### public void setElemDouble​(int bank,
int i,
double val)

Sets the requested data array element in the specified bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:**
- bank

- the specified bank
- i

- the specified index
- val

- the value to set the element in the specified bank
at the specified index of the data array

**See Also:**
- getElemDouble(int)

,

getElemDouble(int, int)

---

### Additional Sections

#### Class DataBuffer

java.lang.Object

- java.awt.image.DataBuffer

java.awt.image.DataBuffer

**Direct Known Subclasses:** DataBufferByte

,

DataBufferDouble

,

DataBufferFloat

,

DataBufferInt

,

DataBufferShort

,

DataBufferUShort

```java
public abstract class
DataBuffer

extends
Object
```

This class exists to wrap one or more data arrays. Each data array in
the DataBuffer is referred to as a bank. Accessor methods for getting
and setting elements of the DataBuffer's banks exist with and without
a bank specifier. The methods without a bank specifier use the default 0th
bank. The DataBuffer can optionally take an offset per bank, so that
data in an existing array can be used even if the interesting data
doesn't start at array location zero. Getting or setting the 0th
element of a bank, uses the (0+offset)th element of the array. The
size field specifies how much of the data array is available for
use. Size + offset for a given bank should never be greater
than the length of the associated data array. The data type of
a data buffer indicates the type of the data array(s) and may also
indicate additional semantics, e.g. storing unsigned 8-bit data
in elements of a byte array. The data type may be TYPE_UNDEFINED
or one of the types defined below. Other types may be added in
the future. Generally, an object of class DataBuffer will be cast down
to one of its data type specific subclasses to access data type specific
methods for improved performance. Currently, the Java 2D(tm) API
image classes use TYPE_BYTE, TYPE_USHORT, TYPE_INT, TYPE_SHORT,
TYPE_FLOAT, and TYPE_DOUBLE DataBuffers to store image data.

**See Also:** Raster

,

SampleModel

public abstract class

DataBuffer

extends

Object

This class exists to wrap one or more data arrays. Each data array in
the DataBuffer is referred to as a bank. Accessor methods for getting
and setting elements of the DataBuffer's banks exist with and without
a bank specifier. The methods without a bank specifier use the default 0th
bank. The DataBuffer can optionally take an offset per bank, so that
data in an existing array can be used even if the interesting data
doesn't start at array location zero. Getting or setting the 0th
element of a bank, uses the (0+offset)th element of the array. The
size field specifies how much of the data array is available for
use. Size + offset for a given bank should never be greater
than the length of the associated data array. The data type of
a data buffer indicates the type of the data array(s) and may also
indicate additional semantics, e.g. storing unsigned 8-bit data
in elements of a byte array. The data type may be TYPE_UNDEFINED
or one of the types defined below. Other types may be added in
the future. Generally, an object of class DataBuffer will be cast down
to one of its data type specific subclasses to access data type specific
methods for improved performance. Currently, the Java 2D(tm) API
image classes use TYPE_BYTE, TYPE_USHORT, TYPE_INT, TYPE_SHORT,
TYPE_FLOAT, and TYPE_DOUBLE DataBuffers to store image data.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

banks

The number of banks in this DataBuffer.

protected int

dataType

The data type of this DataBuffer.

protected int

offset

Offset into default (first) bank from which to get the first element.

protected int[]

offsets

Offsets into all banks.

protected int

size

Usable size of all banks.

static int

TYPE_BYTE

Tag for unsigned byte data.

static int

TYPE_DOUBLE

Tag for double data.

static int

TYPE_FLOAT

Tag for float data.

static int

TYPE_INT

Tag for int data.

static int

TYPE_SHORT

Tag for signed short data.

static int

TYPE_UNDEFINED

Tag for undefined data.

static int

TYPE_USHORT

Tag for unsigned short data.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DataBuffer

​(int dataType,
int size)

Constructs a DataBuffer containing one bank of the specified
data type and size.

protected

DataBuffer

​(int dataType,
int size,
int numBanks)

Constructs a DataBuffer containing the specified number of
banks.

protected

DataBuffer

​(int dataType,
int size,
int numBanks,
int offset)

Constructs a DataBuffer that contains the specified number
of banks.

protected

DataBuffer

​(int dataType,
int size,
int numBanks,
int[] offsets)

Constructs a DataBuffer which contains the specified number
of banks.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDataType

()

Returns the data type of this DataBuffer.

static int

getDataTypeSize

​(int type)

Returns the size (in bits) of the data type, given a datatype tag.

int

getElem

​(int i)

Returns the requested data array element from the first (default) bank
as an integer.

abstract int

getElem

​(int bank,
int i)

Returns the requested data array element from the specified bank
as an integer.

double

getElemDouble

​(int i)

Returns the requested data array element from the first (default) bank
as a double.

double

getElemDouble

​(int bank,
int i)

Returns the requested data array element from the specified bank as
a double.

float

getElemFloat

​(int i)

Returns the requested data array element from the first (default) bank
as a float.

float

getElemFloat

​(int bank,
int i)

Returns the requested data array element from the specified bank
as a float.

int

getNumBanks

()

Returns the number of banks in this DataBuffer.

int

getOffset

()

Returns the offset of the default bank in array elements.

int[]

getOffsets

()

Returns the offsets (in array elements) of all the banks.

int

getSize

()

Returns the size (in array elements) of all banks.

void

setElem

​(int i,
int val)

Sets the requested data array element in the first (default) bank
from the given integer.

abstract void

setElem

​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

void

setElemDouble

​(int i,
double val)

Sets the requested data array element in the first (default) bank
from the given double.

void

setElemDouble

​(int bank,
int i,
double val)

Sets the requested data array element in the specified bank
from the given double.

void

setElemFloat

​(int i,
float val)

Sets the requested data array element in the first (default) bank
from the given float.

void

setElemFloat

​(int bank,
int i,
float val)

Sets the requested data array element in the specified bank
from the given float.

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

Fields

Modifier and Type

Field

Description

protected int

banks

The number of banks in this DataBuffer.

protected int

dataType

The data type of this DataBuffer.

protected int

offset

Offset into default (first) bank from which to get the first element.

protected int[]

offsets

Offsets into all banks.

protected int

size

Usable size of all banks.

static int

TYPE_BYTE

Tag for unsigned byte data.

static int

TYPE_DOUBLE

Tag for double data.

static int

TYPE_FLOAT

Tag for float data.

static int

TYPE_INT

Tag for int data.

static int

TYPE_SHORT

Tag for signed short data.

static int

TYPE_UNDEFINED

Tag for undefined data.

static int

TYPE_USHORT

Tag for unsigned short data.

---

#### Field Summary

The number of banks in this DataBuffer.

The data type of this DataBuffer.

Offset into default (first) bank from which to get the first element.

Offsets into all banks.

Usable size of all banks.

Tag for unsigned byte data.

Tag for double data.

Tag for float data.

Tag for int data.

Tag for signed short data.

Tag for undefined data.

Tag for unsigned short data.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DataBuffer

​(int dataType,
int size)

Constructs a DataBuffer containing one bank of the specified
data type and size.

protected

DataBuffer

​(int dataType,
int size,
int numBanks)

Constructs a DataBuffer containing the specified number of
banks.

protected

DataBuffer

​(int dataType,
int size,
int numBanks,
int offset)

Constructs a DataBuffer that contains the specified number
of banks.

protected

DataBuffer

​(int dataType,
int size,
int numBanks,
int[] offsets)

Constructs a DataBuffer which contains the specified number
of banks.

---

#### Constructor Summary

Constructs a DataBuffer containing one bank of the specified
data type and size.

Constructs a DataBuffer containing the specified number of
banks.

Constructs a DataBuffer that contains the specified number
of banks.

Constructs a DataBuffer which contains the specified number
of banks.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDataType

()

Returns the data type of this DataBuffer.

static int

getDataTypeSize

​(int type)

Returns the size (in bits) of the data type, given a datatype tag.

int

getElem

​(int i)

Returns the requested data array element from the first (default) bank
as an integer.

abstract int

getElem

​(int bank,
int i)

Returns the requested data array element from the specified bank
as an integer.

double

getElemDouble

​(int i)

Returns the requested data array element from the first (default) bank
as a double.

double

getElemDouble

​(int bank,
int i)

Returns the requested data array element from the specified bank as
a double.

float

getElemFloat

​(int i)

Returns the requested data array element from the first (default) bank
as a float.

float

getElemFloat

​(int bank,
int i)

Returns the requested data array element from the specified bank
as a float.

int

getNumBanks

()

Returns the number of banks in this DataBuffer.

int

getOffset

()

Returns the offset of the default bank in array elements.

int[]

getOffsets

()

Returns the offsets (in array elements) of all the banks.

int

getSize

()

Returns the size (in array elements) of all banks.

void

setElem

​(int i,
int val)

Sets the requested data array element in the first (default) bank
from the given integer.

abstract void

setElem

​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

void

setElemDouble

​(int i,
double val)

Sets the requested data array element in the first (default) bank
from the given double.

void

setElemDouble

​(int bank,
int i,
double val)

Sets the requested data array element in the specified bank
from the given double.

void

setElemFloat

​(int i,
float val)

Sets the requested data array element in the first (default) bank
from the given float.

void

setElemFloat

​(int bank,
int i,
float val)

Sets the requested data array element in the specified bank
from the given float.

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

Returns the data type of this DataBuffer.

Returns the size (in bits) of the data type, given a datatype tag.

Returns the requested data array element from the first (default) bank
as an integer.

Returns the requested data array element from the specified bank
as an integer.

Returns the requested data array element from the first (default) bank
as a double.

Returns the requested data array element from the specified bank as
a double.

Returns the requested data array element from the first (default) bank
as a float.

Returns the requested data array element from the specified bank
as a float.

Returns the number of banks in this DataBuffer.

Returns the offset of the default bank in array elements.

Returns the offsets (in array elements) of all the banks.

Returns the size (in array elements) of all banks.

Sets the requested data array element in the first (default) bank
from the given integer.

Sets the requested data array element in the specified bank
from the given integer.

Sets the requested data array element in the first (default) bank
from the given double.

Sets the requested data array element in the specified bank
from the given double.

Sets the requested data array element in the first (default) bank
from the given float.

Sets the requested data array element in the specified bank
from the given float.

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

============ FIELD DETAIL ===========

- Field Detail

- TYPE_BYTE

```java
@Native

public static final int TYPE_BYTE
```

Tag for unsigned byte data.

**See Also:** Constant Field Values

- TYPE_USHORT

```java
@Native

public static final int TYPE_USHORT
```

Tag for unsigned short data.

**See Also:** Constant Field Values

- TYPE_SHORT

```java
@Native

public static final int TYPE_SHORT
```

Tag for signed short data. Placeholder for future use.

**See Also:** Constant Field Values

- TYPE_INT

```java
@Native

public static final int TYPE_INT
```

Tag for int data.

**See Also:** Constant Field Values

- TYPE_FLOAT

```java
@Native

public static final int TYPE_FLOAT
```

Tag for float data. Placeholder for future use.

**See Also:** Constant Field Values

- TYPE_DOUBLE

```java
@Native

public static final int TYPE_DOUBLE
```

Tag for double data. Placeholder for future use.

**See Also:** Constant Field Values

- TYPE_UNDEFINED

```java
@Native

public static final int TYPE_UNDEFINED
```

Tag for undefined data.

**See Also:** Constant Field Values

- dataType

```java
protected int dataType
```

The data type of this DataBuffer.

- banks

```java
protected int banks
```

The number of banks in this DataBuffer.

- offset

```java
protected int offset
```

Offset into default (first) bank from which to get the first element.

- size

```java
protected int size
```

Usable size of all banks.

- offsets

```java
protected int[] offsets
```

Offsets into all banks.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size)
```

Constructs a DataBuffer containing one bank of the specified
data type and size.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks)
```

Constructs a DataBuffer containing the specified number of
banks. Each bank has the specified size and an offset of 0.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks,
int offset)
```

Constructs a DataBuffer that contains the specified number
of banks. Each bank has the specified datatype, size and offset.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer
**Parameters:** offset

- the offset for each bank

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks,
int[] offsets)
```

Constructs a DataBuffer which contains the specified number
of banks. Each bank has the specified datatype and size. The
offset for each bank is specified by its respective entry in
the offsets array.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer
**Parameters:** offsets

- an array containing an offset for each bank.
**Throws:** ArrayIndexOutOfBoundsException

- if

numBanks

does not equal the length of

offsets

============ METHOD DETAIL ==========

- Method Detail

- getDataTypeSize

```java
public static int getDataTypeSize​(int type)
```

Returns the size (in bits) of the data type, given a datatype tag.

**Parameters:** type

- the value of one of the defined datatype tags
**Returns:** the size of the data type
**Throws:** IllegalArgumentException

- if

type

is less than
zero or greater than

TYPE_DOUBLE

- getDataType

```java
public int getDataType()
```

Returns the data type of this DataBuffer.

**Returns:** the data type of this

DataBuffer

.

- getSize

```java
public int getSize()
```

Returns the size (in array elements) of all banks.

**Returns:** the size of all banks.

- getOffset

```java
public int getOffset()
```

Returns the offset of the default bank in array elements.

**Returns:** the offset of the default bank.

- getOffsets

```java
public int[] getOffsets()
```

Returns the offsets (in array elements) of all the banks.

**Returns:** the offsets of all banks.

- getNumBanks

```java
public int getNumBanks()
```

Returns the number of banks in this DataBuffer.

**Returns:** the number of banks.

- getElem

```java
public int getElem​(int i)
```

Returns the requested data array element from the first (default) bank
as an integer.

**Parameters:** i

- the index of the requested data array element
**Returns:** the data array element at the specified index.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- getElem

```java
public abstract int getElem​(int bank,
int i)
```

Returns the requested data array element from the specified bank
as an integer.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the index of the requested data array element
**Returns:** the data array element at the specified index from the
specified bank at the specified index.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- setElem

```java
public void setElem​(int i,
int val)
```

Sets the requested data array element in the first (default) bank
from the given integer.

**Parameters:** i

- the specified index into the data array
**Parameters:** val

- the data to set the element at the specified index in
the data array
**See Also:** getElem(int)

,

getElem(int, int)

- setElem

```java
public abstract void setElem​(int bank,
int i,
int val)
```

Sets the requested data array element in the specified bank
from the given integer.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index into the data array
**Parameters:** val

- the data to set the element in the specified bank
at the specified index in the data array
**See Also:** getElem(int)

,

getElem(int, int)

- getElemFloat

```java
public float getElemFloat​(int i)
```

Returns the requested data array element from the first (default) bank
as a float. The implementation in this class is to cast getElem(i)
to a float. Subclasses may override this method if another
implementation is needed.

**Parameters:** i

- the index of the requested data array element
**Returns:** a float value representing the data array element at the
specified index.
**See Also:** setElemFloat(int, float)

,

setElemFloat(int, int, float)

- getElemFloat

```java
public float getElemFloat​(int bank,
int i)
```

Returns the requested data array element from the specified bank
as a float. The implementation in this class is to cast

getElem(int, int)

to a float. Subclasses can override this method if another
implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the index of the requested data array element
**Returns:** a float value representing the data array element from the
specified bank at the specified index.
**See Also:** setElemFloat(int, float)

,

setElemFloat(int, int, float)

- setElemFloat

```java
public void setElemFloat​(int i,
float val)
```

Sets the requested data array element in the first (default) bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses
can override this method if another implementation is needed.

**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element at the specified index in
the data array
**See Also:** getElemFloat(int)

,

getElemFloat(int, int)

- setElemFloat

```java
public void setElemFloat​(int bank,
int i,
float val)
```

Sets the requested data array element in the specified bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element in the specified bank at
the specified index in the data array
**See Also:** getElemFloat(int)

,

getElemFloat(int, int)

- getElemDouble

```java
public double getElemDouble​(int i)
```

Returns the requested data array element from the first (default) bank
as a double. The implementation in this class is to cast

getElem(int)

to a double. Subclasses can override this method if another
implementation is needed.

**Parameters:** i

- the specified index
**Returns:** a double value representing the element at the specified
index in the data array.
**See Also:** setElemDouble(int, double)

,

setElemDouble(int, int, double)

- getElemDouble

```java
public double getElemDouble​(int bank,
int i)
```

Returns the requested data array element from the specified bank as
a double. The implementation in this class is to cast getElem(bank, i)
to a double. Subclasses may override this method if another
implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Returns:** a double value representing the element from the specified
bank at the specified index in the data array.
**See Also:** setElemDouble(int, double)

,

setElemDouble(int, int, double)

- setElemDouble

```java
public void setElemDouble​(int i,
double val)
```

Sets the requested data array element in the first (default) bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element at the specified index
in the data array
**See Also:** getElemDouble(int)

,

getElemDouble(int, int)

- setElemDouble

```java
public void setElemDouble​(int bank,
int i,
double val)
```

Sets the requested data array element in the specified bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element in the specified bank
at the specified index of the data array
**See Also:** getElemDouble(int)

,

getElemDouble(int, int)

Field Detail

- TYPE_BYTE

```java
@Native

public static final int TYPE_BYTE
```

Tag for unsigned byte data.

**See Also:** Constant Field Values

- TYPE_USHORT

```java
@Native

public static final int TYPE_USHORT
```

Tag for unsigned short data.

**See Also:** Constant Field Values

- TYPE_SHORT

```java
@Native

public static final int TYPE_SHORT
```

Tag for signed short data. Placeholder for future use.

**See Also:** Constant Field Values

- TYPE_INT

```java
@Native

public static final int TYPE_INT
```

Tag for int data.

**See Also:** Constant Field Values

- TYPE_FLOAT

```java
@Native

public static final int TYPE_FLOAT
```

Tag for float data. Placeholder for future use.

**See Also:** Constant Field Values

- TYPE_DOUBLE

```java
@Native

public static final int TYPE_DOUBLE
```

Tag for double data. Placeholder for future use.

**See Also:** Constant Field Values

- TYPE_UNDEFINED

```java
@Native

public static final int TYPE_UNDEFINED
```

Tag for undefined data.

**See Also:** Constant Field Values

- dataType

```java
protected int dataType
```

The data type of this DataBuffer.

- banks

```java
protected int banks
```

The number of banks in this DataBuffer.

- offset

```java
protected int offset
```

Offset into default (first) bank from which to get the first element.

- size

```java
protected int size
```

Usable size of all banks.

- offsets

```java
protected int[] offsets
```

Offsets into all banks.

---

#### Field Detail

TYPE_BYTE

```java
@Native

public static final int TYPE_BYTE
```

Tag for unsigned byte data.

**See Also:** Constant Field Values

---

#### TYPE_BYTE

@Native

public static final int TYPE_BYTE

Tag for unsigned byte data.

TYPE_USHORT

```java
@Native

public static final int TYPE_USHORT
```

Tag for unsigned short data.

**See Also:** Constant Field Values

---

#### TYPE_USHORT

@Native

public static final int TYPE_USHORT

Tag for unsigned short data.

TYPE_SHORT

```java
@Native

public static final int TYPE_SHORT
```

Tag for signed short data. Placeholder for future use.

**See Also:** Constant Field Values

---

#### TYPE_SHORT

@Native

public static final int TYPE_SHORT

Tag for signed short data. Placeholder for future use.

TYPE_INT

```java
@Native

public static final int TYPE_INT
```

Tag for int data.

**See Also:** Constant Field Values

---

#### TYPE_INT

@Native

public static final int TYPE_INT

Tag for int data.

TYPE_FLOAT

```java
@Native

public static final int TYPE_FLOAT
```

Tag for float data. Placeholder for future use.

**See Also:** Constant Field Values

---

#### TYPE_FLOAT

@Native

public static final int TYPE_FLOAT

Tag for float data. Placeholder for future use.

TYPE_DOUBLE

```java
@Native

public static final int TYPE_DOUBLE
```

Tag for double data. Placeholder for future use.

**See Also:** Constant Field Values

---

#### TYPE_DOUBLE

@Native

public static final int TYPE_DOUBLE

Tag for double data. Placeholder for future use.

TYPE_UNDEFINED

```java
@Native

public static final int TYPE_UNDEFINED
```

Tag for undefined data.

**See Also:** Constant Field Values

---

#### TYPE_UNDEFINED

@Native

public static final int TYPE_UNDEFINED

Tag for undefined data.

dataType

```java
protected int dataType
```

The data type of this DataBuffer.

---

#### dataType

protected int dataType

The data type of this DataBuffer.

banks

```java
protected int banks
```

The number of banks in this DataBuffer.

---

#### banks

protected int banks

The number of banks in this DataBuffer.

offset

```java
protected int offset
```

Offset into default (first) bank from which to get the first element.

---

#### offset

protected int offset

Offset into default (first) bank from which to get the first element.

size

```java
protected int size
```

Usable size of all banks.

---

#### size

protected int size

Usable size of all banks.

offsets

```java
protected int[] offsets
```

Offsets into all banks.

---

#### offsets

protected int[] offsets

Offsets into all banks.

Constructor Detail

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size)
```

Constructs a DataBuffer containing one bank of the specified
data type and size.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks)
```

Constructs a DataBuffer containing the specified number of
banks. Each bank has the specified size and an offset of 0.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks,
int offset)
```

Constructs a DataBuffer that contains the specified number
of banks. Each bank has the specified datatype, size and offset.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer
**Parameters:** offset

- the offset for each bank

- DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks,
int[] offsets)
```

Constructs a DataBuffer which contains the specified number
of banks. Each bank has the specified datatype and size. The
offset for each bank is specified by its respective entry in
the offsets array.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer
**Parameters:** offsets

- an array containing an offset for each bank.
**Throws:** ArrayIndexOutOfBoundsException

- if

numBanks

does not equal the length of

offsets

---

#### Constructor Detail

DataBuffer

```java
protected DataBuffer​(int dataType,
int size)
```

Constructs a DataBuffer containing one bank of the specified
data type and size.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks

---

#### DataBuffer

protected DataBuffer​(int dataType,
int size)

Constructs a DataBuffer containing one bank of the specified
data type and size.

DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks)
```

Constructs a DataBuffer containing the specified number of
banks. Each bank has the specified size and an offset of 0.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer

---

#### DataBuffer

protected DataBuffer​(int dataType,
int size,
int numBanks)

Constructs a DataBuffer containing the specified number of
banks. Each bank has the specified size and an offset of 0.

DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks,
int offset)
```

Constructs a DataBuffer that contains the specified number
of banks. Each bank has the specified datatype, size and offset.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer
**Parameters:** offset

- the offset for each bank

---

#### DataBuffer

protected DataBuffer​(int dataType,
int size,
int numBanks,
int offset)

Constructs a DataBuffer that contains the specified number
of banks. Each bank has the specified datatype, size and offset.

DataBuffer

```java
protected DataBuffer​(int dataType,
int size,
int numBanks,
int[] offsets)
```

Constructs a DataBuffer which contains the specified number
of banks. Each bank has the specified datatype and size. The
offset for each bank is specified by its respective entry in
the offsets array.

**Parameters:** dataType

- the data type of this

DataBuffer
**Parameters:** size

- the size of the banks
**Parameters:** numBanks

- the number of banks in this

DataBuffer
**Parameters:** offsets

- an array containing an offset for each bank.
**Throws:** ArrayIndexOutOfBoundsException

- if

numBanks

does not equal the length of

offsets

---

#### DataBuffer

protected DataBuffer​(int dataType,
int size,
int numBanks,
int[] offsets)

Constructs a DataBuffer which contains the specified number
of banks. Each bank has the specified datatype and size. The
offset for each bank is specified by its respective entry in
the offsets array.

Method Detail

- getDataTypeSize

```java
public static int getDataTypeSize​(int type)
```

Returns the size (in bits) of the data type, given a datatype tag.

**Parameters:** type

- the value of one of the defined datatype tags
**Returns:** the size of the data type
**Throws:** IllegalArgumentException

- if

type

is less than
zero or greater than

TYPE_DOUBLE

- getDataType

```java
public int getDataType()
```

Returns the data type of this DataBuffer.

**Returns:** the data type of this

DataBuffer

.

- getSize

```java
public int getSize()
```

Returns the size (in array elements) of all banks.

**Returns:** the size of all banks.

- getOffset

```java
public int getOffset()
```

Returns the offset of the default bank in array elements.

**Returns:** the offset of the default bank.

- getOffsets

```java
public int[] getOffsets()
```

Returns the offsets (in array elements) of all the banks.

**Returns:** the offsets of all banks.

- getNumBanks

```java
public int getNumBanks()
```

Returns the number of banks in this DataBuffer.

**Returns:** the number of banks.

- getElem

```java
public int getElem​(int i)
```

Returns the requested data array element from the first (default) bank
as an integer.

**Parameters:** i

- the index of the requested data array element
**Returns:** the data array element at the specified index.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- getElem

```java
public abstract int getElem​(int bank,
int i)
```

Returns the requested data array element from the specified bank
as an integer.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the index of the requested data array element
**Returns:** the data array element at the specified index from the
specified bank at the specified index.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

- setElem

```java
public void setElem​(int i,
int val)
```

Sets the requested data array element in the first (default) bank
from the given integer.

**Parameters:** i

- the specified index into the data array
**Parameters:** val

- the data to set the element at the specified index in
the data array
**See Also:** getElem(int)

,

getElem(int, int)

- setElem

```java
public abstract void setElem​(int bank,
int i,
int val)
```

Sets the requested data array element in the specified bank
from the given integer.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index into the data array
**Parameters:** val

- the data to set the element in the specified bank
at the specified index in the data array
**See Also:** getElem(int)

,

getElem(int, int)

- getElemFloat

```java
public float getElemFloat​(int i)
```

Returns the requested data array element from the first (default) bank
as a float. The implementation in this class is to cast getElem(i)
to a float. Subclasses may override this method if another
implementation is needed.

**Parameters:** i

- the index of the requested data array element
**Returns:** a float value representing the data array element at the
specified index.
**See Also:** setElemFloat(int, float)

,

setElemFloat(int, int, float)

- getElemFloat

```java
public float getElemFloat​(int bank,
int i)
```

Returns the requested data array element from the specified bank
as a float. The implementation in this class is to cast

getElem(int, int)

to a float. Subclasses can override this method if another
implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the index of the requested data array element
**Returns:** a float value representing the data array element from the
specified bank at the specified index.
**See Also:** setElemFloat(int, float)

,

setElemFloat(int, int, float)

- setElemFloat

```java
public void setElemFloat​(int i,
float val)
```

Sets the requested data array element in the first (default) bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses
can override this method if another implementation is needed.

**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element at the specified index in
the data array
**See Also:** getElemFloat(int)

,

getElemFloat(int, int)

- setElemFloat

```java
public void setElemFloat​(int bank,
int i,
float val)
```

Sets the requested data array element in the specified bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element in the specified bank at
the specified index in the data array
**See Also:** getElemFloat(int)

,

getElemFloat(int, int)

- getElemDouble

```java
public double getElemDouble​(int i)
```

Returns the requested data array element from the first (default) bank
as a double. The implementation in this class is to cast

getElem(int)

to a double. Subclasses can override this method if another
implementation is needed.

**Parameters:** i

- the specified index
**Returns:** a double value representing the element at the specified
index in the data array.
**See Also:** setElemDouble(int, double)

,

setElemDouble(int, int, double)

- getElemDouble

```java
public double getElemDouble​(int bank,
int i)
```

Returns the requested data array element from the specified bank as
a double. The implementation in this class is to cast getElem(bank, i)
to a double. Subclasses may override this method if another
implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Returns:** a double value representing the element from the specified
bank at the specified index in the data array.
**See Also:** setElemDouble(int, double)

,

setElemDouble(int, int, double)

- setElemDouble

```java
public void setElemDouble​(int i,
double val)
```

Sets the requested data array element in the first (default) bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element at the specified index
in the data array
**See Also:** getElemDouble(int)

,

getElemDouble(int, int)

- setElemDouble

```java
public void setElemDouble​(int bank,
int i,
double val)
```

Sets the requested data array element in the specified bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element in the specified bank
at the specified index of the data array
**See Also:** getElemDouble(int)

,

getElemDouble(int, int)

---

#### Method Detail

getDataTypeSize

```java
public static int getDataTypeSize​(int type)
```

Returns the size (in bits) of the data type, given a datatype tag.

**Parameters:** type

- the value of one of the defined datatype tags
**Returns:** the size of the data type
**Throws:** IllegalArgumentException

- if

type

is less than
zero or greater than

TYPE_DOUBLE

---

#### getDataTypeSize

public static int getDataTypeSize​(int type)

Returns the size (in bits) of the data type, given a datatype tag.

getDataType

```java
public int getDataType()
```

Returns the data type of this DataBuffer.

**Returns:** the data type of this

DataBuffer

.

---

#### getDataType

public int getDataType()

Returns the data type of this DataBuffer.

getSize

```java
public int getSize()
```

Returns the size (in array elements) of all banks.

**Returns:** the size of all banks.

---

#### getSize

public int getSize()

Returns the size (in array elements) of all banks.

getOffset

```java
public int getOffset()
```

Returns the offset of the default bank in array elements.

**Returns:** the offset of the default bank.

---

#### getOffset

public int getOffset()

Returns the offset of the default bank in array elements.

getOffsets

```java
public int[] getOffsets()
```

Returns the offsets (in array elements) of all the banks.

**Returns:** the offsets of all banks.

---

#### getOffsets

public int[] getOffsets()

Returns the offsets (in array elements) of all the banks.

getNumBanks

```java
public int getNumBanks()
```

Returns the number of banks in this DataBuffer.

**Returns:** the number of banks.

---

#### getNumBanks

public int getNumBanks()

Returns the number of banks in this DataBuffer.

getElem

```java
public int getElem​(int i)
```

Returns the requested data array element from the first (default) bank
as an integer.

**Parameters:** i

- the index of the requested data array element
**Returns:** the data array element at the specified index.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

---

#### getElem

public int getElem​(int i)

Returns the requested data array element from the first (default) bank
as an integer.

getElem

```java
public abstract int getElem​(int bank,
int i)
```

Returns the requested data array element from the specified bank
as an integer.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the index of the requested data array element
**Returns:** the data array element at the specified index from the
specified bank at the specified index.
**See Also:** setElem(int, int)

,

setElem(int, int, int)

---

#### getElem

public abstract int getElem​(int bank,
int i)

Returns the requested data array element from the specified bank
as an integer.

setElem

```java
public void setElem​(int i,
int val)
```

Sets the requested data array element in the first (default) bank
from the given integer.

**Parameters:** i

- the specified index into the data array
**Parameters:** val

- the data to set the element at the specified index in
the data array
**See Also:** getElem(int)

,

getElem(int, int)

---

#### setElem

public void setElem​(int i,
int val)

Sets the requested data array element in the first (default) bank
from the given integer.

setElem

```java
public abstract void setElem​(int bank,
int i,
int val)
```

Sets the requested data array element in the specified bank
from the given integer.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index into the data array
**Parameters:** val

- the data to set the element in the specified bank
at the specified index in the data array
**See Also:** getElem(int)

,

getElem(int, int)

---

#### setElem

public abstract void setElem​(int bank,
int i,
int val)

Sets the requested data array element in the specified bank
from the given integer.

getElemFloat

```java
public float getElemFloat​(int i)
```

Returns the requested data array element from the first (default) bank
as a float. The implementation in this class is to cast getElem(i)
to a float. Subclasses may override this method if another
implementation is needed.

**Parameters:** i

- the index of the requested data array element
**Returns:** a float value representing the data array element at the
specified index.
**See Also:** setElemFloat(int, float)

,

setElemFloat(int, int, float)

---

#### getElemFloat

public float getElemFloat​(int i)

Returns the requested data array element from the first (default) bank
as a float. The implementation in this class is to cast getElem(i)
to a float. Subclasses may override this method if another
implementation is needed.

getElemFloat

```java
public float getElemFloat​(int bank,
int i)
```

Returns the requested data array element from the specified bank
as a float. The implementation in this class is to cast

getElem(int, int)

to a float. Subclasses can override this method if another
implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the index of the requested data array element
**Returns:** a float value representing the data array element from the
specified bank at the specified index.
**See Also:** setElemFloat(int, float)

,

setElemFloat(int, int, float)

---

#### getElemFloat

public float getElemFloat​(int bank,
int i)

Returns the requested data array element from the specified bank
as a float. The implementation in this class is to cast

getElem(int, int)

to a float. Subclasses can override this method if another
implementation is needed.

setElemFloat

```java
public void setElemFloat​(int i,
float val)
```

Sets the requested data array element in the first (default) bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses
can override this method if another implementation is needed.

**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element at the specified index in
the data array
**See Also:** getElemFloat(int)

,

getElemFloat(int, int)

---

#### setElemFloat

public void setElemFloat​(int i,
float val)

Sets the requested data array element in the first (default) bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses
can override this method if another implementation is needed.

setElemFloat

```java
public void setElemFloat​(int bank,
int i,
float val)
```

Sets the requested data array element in the specified bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element in the specified bank at
the specified index in the data array
**See Also:** getElemFloat(int)

,

getElemFloat(int, int)

---

#### setElemFloat

public void setElemFloat​(int bank,
int i,
float val)

Sets the requested data array element in the specified bank
from the given float. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

getElemDouble

```java
public double getElemDouble​(int i)
```

Returns the requested data array element from the first (default) bank
as a double. The implementation in this class is to cast

getElem(int)

to a double. Subclasses can override this method if another
implementation is needed.

**Parameters:** i

- the specified index
**Returns:** a double value representing the element at the specified
index in the data array.
**See Also:** setElemDouble(int, double)

,

setElemDouble(int, int, double)

---

#### getElemDouble

public double getElemDouble​(int i)

Returns the requested data array element from the first (default) bank
as a double. The implementation in this class is to cast

getElem(int)

to a double. Subclasses can override this method if another
implementation is needed.

getElemDouble

```java
public double getElemDouble​(int bank,
int i)
```

Returns the requested data array element from the specified bank as
a double. The implementation in this class is to cast getElem(bank, i)
to a double. Subclasses may override this method if another
implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Returns:** a double value representing the element from the specified
bank at the specified index in the data array.
**See Also:** setElemDouble(int, double)

,

setElemDouble(int, int, double)

---

#### getElemDouble

public double getElemDouble​(int bank,
int i)

Returns the requested data array element from the specified bank as
a double. The implementation in this class is to cast getElem(bank, i)
to a double. Subclasses may override this method if another
implementation is needed.

setElemDouble

```java
public void setElemDouble​(int i,
double val)
```

Sets the requested data array element in the first (default) bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element at the specified index
in the data array
**See Also:** getElemDouble(int)

,

getElemDouble(int, int)

---

#### setElemDouble

public void setElemDouble​(int i,
double val)

Sets the requested data array element in the first (default) bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

setElemDouble

```java
public void setElemDouble​(int bank,
int i,
double val)
```

Sets the requested data array element in the specified bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

**Parameters:** bank

- the specified bank
**Parameters:** i

- the specified index
**Parameters:** val

- the value to set the element in the specified bank
at the specified index of the data array
**See Also:** getElemDouble(int)

,

getElemDouble(int, int)

---

#### setElemDouble

public void setElemDouble​(int bank,
int i,
double val)

Sets the requested data array element in the specified bank
from the given double. The implementation in this class is to cast
val to an int and call

setElem(int, int)

. Subclasses can
override this method if another implementation is needed.

---

