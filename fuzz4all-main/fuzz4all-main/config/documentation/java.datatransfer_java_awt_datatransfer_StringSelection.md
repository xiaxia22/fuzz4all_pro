# Class StringSelection

**Source:** `java.datatransfer\java\awt\datatransfer\StringSelection.html`

### Class Description

```java
public class
StringSelection

extends
Object

implements
Transferable
,
ClipboardOwner
```

A

Transferable

which implements the capability required to transfer a

String

.

This

Transferable

properly supports

DataFlavor.stringFlavor

and all equivalent flavors. Support for

DataFlavor.plainTextFlavor

and all equivalent flavors is

deprecated

. No other

DataFlavor

s
are supported.

**All Implemented Interfaces:** ClipboardOwner

,

Transferable

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringSelection​(
String
data)

Creates a

Transferable

capable of transferring the specified

String

.

**Parameters:**
- data

- the string to be transferred

---

### Method Details

#### public
DataFlavor
[] getTransferDataFlavors()

Returns an array of flavors in which this

Transferable

can
provide the data.

DataFlavor.stringFlavor

is properly supported.
Support for

DataFlavor.plainTextFlavor

is

deprecated

.

**Specified by:**
- getTransferDataFlavors

in interface

Transferable

**Returns:**
- an array of length two, whose elements are

DataFlavor.stringFlavor

and

DataFlavor.plainTextFlavor

---

#### public boolean isDataFlavorSupported​(
DataFlavor
flavor)

Returns whether the requested flavor is supported by this

Transferable

.

**Specified by:**
- isDataFlavorSupported

in interface

Transferable

**Parameters:**
- flavor

- the requested flavor for the data

**Returns:**
- true

if

flavor

is equal to

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor

;

false

if

flavor

is not one of the above flavors

**Throws:**
- NullPointerException

- if

flavor

is

null

---

#### public
Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException

Returns the

Transferable

's data in the requested

DataFlavor

if possible. If the desired flavor is

DataFlavor.stringFlavor

, or an equivalent flavor, the

String

representing the selection is returned. If the desired
flavor is

DataFlavor.plainTextFlavor

, or an equivalent flavor, a

Reader

is returned.

Note:

The behavior of this method for

DataFlavor.plainTextFlavor

and equivalent

DataFlavor

s is inconsistent with the definition of

DataFlavor.plainTextFlavor

.

**Specified by:**
- getTransferData

in interface

Transferable

**Parameters:**
- flavor

- the requested flavor for the data

**Returns:**
- the data in the requested flavor, as outlined above

**Throws:**
- UnsupportedFlavorException

- if the requested data flavor is not
equivalent to either

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor
- IOException

- if an IOException occurs while retrieving the data.
By default, StringSelection never throws this exception, but a
subclass may.
- NullPointerException

- if

flavor

is

null

**See Also:**
- Reader

---

### Additional Sections

#### Class StringSelection

java.lang.Object

- java.awt.datatransfer.StringSelection

java.awt.datatransfer.StringSelection

**All Implemented Interfaces:** ClipboardOwner

,

Transferable

```java
public class
StringSelection

extends
Object

implements
Transferable
,
ClipboardOwner
```

A

Transferable

which implements the capability required to transfer a

String

.

This

Transferable

properly supports

DataFlavor.stringFlavor

and all equivalent flavors. Support for

DataFlavor.plainTextFlavor

and all equivalent flavors is

deprecated

. No other

DataFlavor

s
are supported.

**Since:** 1.1
**See Also:** DataFlavor.stringFlavor

,

DataFlavor.plainTextFlavor

public class

StringSelection

extends

Object

implements

Transferable

,

ClipboardOwner

A

Transferable

which implements the capability required to transfer a

String

.

This

Transferable

properly supports

DataFlavor.stringFlavor

and all equivalent flavors. Support for

DataFlavor.plainTextFlavor

and all equivalent flavors is

deprecated

. No other

DataFlavor

s
are supported.

This

Transferable

properly supports

DataFlavor.stringFlavor

and all equivalent flavors. Support for

DataFlavor.plainTextFlavor

and all equivalent flavors is

deprecated

. No other

DataFlavor

s
are supported.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringSelection

​(

String

data)

Creates a

Transferable

capable of transferring the specified

String

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getTransferData

​(

DataFlavor

flavor)

Returns the

Transferable

's data in the requested

DataFlavor

if possible.

DataFlavor

[]

getTransferDataFlavors

()

Returns an array of flavors in which this

Transferable

can
provide the data.

boolean

isDataFlavorSupported

​(

DataFlavor

flavor)

Returns whether the requested flavor is supported by this

Transferable

.

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

- Methods declared in interface java.awt.datatransfer.

ClipboardOwner

lostOwnership

Constructor Summary

Constructors

Constructor

Description

StringSelection

​(

String

data)

Creates a

Transferable

capable of transferring the specified

String

.

---

#### Constructor Summary

Creates a

Transferable

capable of transferring the specified

String

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getTransferData

​(

DataFlavor

flavor)

Returns the

Transferable

's data in the requested

DataFlavor

if possible.

DataFlavor

[]

getTransferDataFlavors

()

Returns an array of flavors in which this

Transferable

can
provide the data.

boolean

isDataFlavorSupported

​(

DataFlavor

flavor)

Returns whether the requested flavor is supported by this

Transferable

.

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

- Methods declared in interface java.awt.datatransfer.

ClipboardOwner

lostOwnership

---

#### Method Summary

Returns the

Transferable

's data in the requested

DataFlavor

if possible.

Returns an array of flavors in which this

Transferable

can
provide the data.

Returns whether the requested flavor is supported by this

Transferable

.

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

Methods declared in interface java.awt.datatransfer.

ClipboardOwner

lostOwnership

---

#### Methods declared in interface java.awt.datatransfer. ClipboardOwner

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StringSelection

```java
public StringSelection​(
String
data)
```

Creates a

Transferable

capable of transferring the specified

String

.

**Parameters:** data

- the string to be transferred

============ METHOD DETAIL ==========

- Method Detail

- getTransferDataFlavors

```java
public
DataFlavor
[] getTransferDataFlavors()
```

Returns an array of flavors in which this

Transferable

can
provide the data.

DataFlavor.stringFlavor

is properly supported.
Support for

DataFlavor.plainTextFlavor

is

deprecated

.

**Specified by:** getTransferDataFlavors

in interface

Transferable
**Returns:** an array of length two, whose elements are

DataFlavor.stringFlavor

and

DataFlavor.plainTextFlavor

- isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
flavor)
```

Returns whether the requested flavor is supported by this

Transferable

.

**Specified by:** isDataFlavorSupported

in interface

Transferable
**Parameters:** flavor

- the requested flavor for the data
**Returns:** true

if

flavor

is equal to

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor

;

false

if

flavor

is not one of the above flavors
**Throws:** NullPointerException

- if

flavor

is

null

- getTransferData

```java
public
Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns the

Transferable

's data in the requested

DataFlavor

if possible. If the desired flavor is

DataFlavor.stringFlavor

, or an equivalent flavor, the

String

representing the selection is returned. If the desired
flavor is

DataFlavor.plainTextFlavor

, or an equivalent flavor, a

Reader

is returned.

Note:

The behavior of this method for

DataFlavor.plainTextFlavor

and equivalent

DataFlavor

s is inconsistent with the definition of

DataFlavor.plainTextFlavor

.

**Specified by:** getTransferData

in interface

Transferable
**Parameters:** flavor

- the requested flavor for the data
**Returns:** the data in the requested flavor, as outlined above
**Throws:** UnsupportedFlavorException

- if the requested data flavor is not
equivalent to either

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor
**Throws:** IOException

- if an IOException occurs while retrieving the data.
By default, StringSelection never throws this exception, but a
subclass may.
**Throws:** NullPointerException

- if

flavor

is

null
**See Also:** Reader

Constructor Detail

- StringSelection

```java
public StringSelection​(
String
data)
```

Creates a

Transferable

capable of transferring the specified

String

.

**Parameters:** data

- the string to be transferred

---

#### Constructor Detail

StringSelection

```java
public StringSelection​(
String
data)
```

Creates a

Transferable

capable of transferring the specified

String

.

**Parameters:** data

- the string to be transferred

---

#### StringSelection

public StringSelection​(

String

data)

Creates a

Transferable

capable of transferring the specified

String

.

Method Detail

- getTransferDataFlavors

```java
public
DataFlavor
[] getTransferDataFlavors()
```

Returns an array of flavors in which this

Transferable

can
provide the data.

DataFlavor.stringFlavor

is properly supported.
Support for

DataFlavor.plainTextFlavor

is

deprecated

.

**Specified by:** getTransferDataFlavors

in interface

Transferable
**Returns:** an array of length two, whose elements are

DataFlavor.stringFlavor

and

DataFlavor.plainTextFlavor

- isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
flavor)
```

Returns whether the requested flavor is supported by this

Transferable

.

**Specified by:** isDataFlavorSupported

in interface

Transferable
**Parameters:** flavor

- the requested flavor for the data
**Returns:** true

if

flavor

is equal to

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor

;

false

if

flavor

is not one of the above flavors
**Throws:** NullPointerException

- if

flavor

is

null

- getTransferData

```java
public
Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns the

Transferable

's data in the requested

DataFlavor

if possible. If the desired flavor is

DataFlavor.stringFlavor

, or an equivalent flavor, the

String

representing the selection is returned. If the desired
flavor is

DataFlavor.plainTextFlavor

, or an equivalent flavor, a

Reader

is returned.

Note:

The behavior of this method for

DataFlavor.plainTextFlavor

and equivalent

DataFlavor

s is inconsistent with the definition of

DataFlavor.plainTextFlavor

.

**Specified by:** getTransferData

in interface

Transferable
**Parameters:** flavor

- the requested flavor for the data
**Returns:** the data in the requested flavor, as outlined above
**Throws:** UnsupportedFlavorException

- if the requested data flavor is not
equivalent to either

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor
**Throws:** IOException

- if an IOException occurs while retrieving the data.
By default, StringSelection never throws this exception, but a
subclass may.
**Throws:** NullPointerException

- if

flavor

is

null
**See Also:** Reader

---

#### Method Detail

getTransferDataFlavors

```java
public
DataFlavor
[] getTransferDataFlavors()
```

Returns an array of flavors in which this

Transferable

can
provide the data.

DataFlavor.stringFlavor

is properly supported.
Support for

DataFlavor.plainTextFlavor

is

deprecated

.

**Specified by:** getTransferDataFlavors

in interface

Transferable
**Returns:** an array of length two, whose elements are

DataFlavor.stringFlavor

and

DataFlavor.plainTextFlavor

---

#### getTransferDataFlavors

public

DataFlavor

[] getTransferDataFlavors()

Returns an array of flavors in which this

Transferable

can
provide the data.

DataFlavor.stringFlavor

is properly supported.
Support for

DataFlavor.plainTextFlavor

is

deprecated

.

isDataFlavorSupported

```java
public boolean isDataFlavorSupported​(
DataFlavor
flavor)
```

Returns whether the requested flavor is supported by this

Transferable

.

**Specified by:** isDataFlavorSupported

in interface

Transferable
**Parameters:** flavor

- the requested flavor for the data
**Returns:** true

if

flavor

is equal to

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor

;

false

if

flavor

is not one of the above flavors
**Throws:** NullPointerException

- if

flavor

is

null

---

#### isDataFlavorSupported

public boolean isDataFlavorSupported​(

DataFlavor

flavor)

Returns whether the requested flavor is supported by this

Transferable

.

getTransferData

```java
public
Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns the

Transferable

's data in the requested

DataFlavor

if possible. If the desired flavor is

DataFlavor.stringFlavor

, or an equivalent flavor, the

String

representing the selection is returned. If the desired
flavor is

DataFlavor.plainTextFlavor

, or an equivalent flavor, a

Reader

is returned.

Note:

The behavior of this method for

DataFlavor.plainTextFlavor

and equivalent

DataFlavor

s is inconsistent with the definition of

DataFlavor.plainTextFlavor

.

**Specified by:** getTransferData

in interface

Transferable
**Parameters:** flavor

- the requested flavor for the data
**Returns:** the data in the requested flavor, as outlined above
**Throws:** UnsupportedFlavorException

- if the requested data flavor is not
equivalent to either

DataFlavor.stringFlavor

or

DataFlavor.plainTextFlavor
**Throws:** IOException

- if an IOException occurs while retrieving the data.
By default, StringSelection never throws this exception, but a
subclass may.
**Throws:** NullPointerException

- if

flavor

is

null
**See Also:** Reader

---

#### getTransferData

public

Object

getTransferData​(

DataFlavor

flavor)
throws

UnsupportedFlavorException

,

IOException

Returns the

Transferable

's data in the requested

DataFlavor

if possible. If the desired flavor is

DataFlavor.stringFlavor

, or an equivalent flavor, the

String

representing the selection is returned. If the desired
flavor is

DataFlavor.plainTextFlavor

, or an equivalent flavor, a

Reader

is returned.

Note:

The behavior of this method for

DataFlavor.plainTextFlavor

and equivalent

DataFlavor

s is inconsistent with the definition of

DataFlavor.plainTextFlavor

.

---

