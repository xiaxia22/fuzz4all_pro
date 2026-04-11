# Interface Transferable

**Source:** `java.datatransfer\java\awt\datatransfer\Transferable.html`

### Class Description

```java
public interface
Transferable
```

Defines the interface for classes that can be used to provide data for a
transfer operation.

For information on using data transfer with Swing, see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**All Known Implementing Classes:** DropTargetContext.TransferableProxy

,

StringSelection

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DataFlavor
[] getTransferDataFlavors()

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in. The array should be ordered according to preference
for providing the data (from most richly descriptive to least
descriptive).

**Returns:**
- an array of data flavors in which this data can be transferred

---

#### boolean isDataFlavorSupported​(
DataFlavor
flavor)

Returns whether or not the specified data flavor is supported for this
object.

**Parameters:**
- flavor

- the requested flavor for the data

**Returns:**
- boolean indicating whether or not the data flavor is supported

---

#### Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException

Returns an object which represents the data to be transferred. The class
of the object returned is defined by the representation class of the
flavor.

**Parameters:**
- flavor

- the requested flavor for the data

**Returns:**
- an object which represents the data to be transferred

**Throws:**
- IOException

- if the data is no longer available in the requested
flavor
- UnsupportedFlavorException

- if the requested data flavor is not
supported

**See Also:**
- DataFlavor.getRepresentationClass()

---

### Additional Sections

#### Interface Transferable

**All Known Implementing Classes:** DropTargetContext.TransferableProxy

,

StringSelection

```java
public interface
Transferable
```

Defines the interface for classes that can be used to provide data for a
transfer operation.

For information on using data transfer with Swing, see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

**Since:** 1.1

public interface

Transferable

Defines the interface for classes that can be used to provide data for a
transfer operation.

For information on using data transfer with Swing, see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

For information on using data transfer with Swing, see

How to Use Drag and Drop and Data Transfer

, a section in

The Java Tutorial

, for more information.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getTransferData

​(

DataFlavor

flavor)

Returns an object which represents the data to be transferred.

DataFlavor

[]

getTransferDataFlavors

()

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in.

boolean

isDataFlavorSupported

​(

DataFlavor

flavor)

Returns whether or not the specified data flavor is supported for this
object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getTransferData

​(

DataFlavor

flavor)

Returns an object which represents the data to be transferred.

DataFlavor

[]

getTransferDataFlavors

()

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in.

boolean

isDataFlavorSupported

​(

DataFlavor

flavor)

Returns whether or not the specified data flavor is supported for this
object.

---

#### Method Summary

Returns an object which represents the data to be transferred.

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in.

Returns whether or not the specified data flavor is supported for this
object.

============ METHOD DETAIL ==========

- Method Detail

- getTransferDataFlavors

```java
DataFlavor
[] getTransferDataFlavors()
```

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in. The array should be ordered according to preference
for providing the data (from most richly descriptive to least
descriptive).

**Returns:** an array of data flavors in which this data can be transferred

- isDataFlavorSupported

```java
boolean isDataFlavorSupported​(
DataFlavor
flavor)
```

Returns whether or not the specified data flavor is supported for this
object.

**Parameters:** flavor

- the requested flavor for the data
**Returns:** boolean indicating whether or not the data flavor is supported

- getTransferData

```java
Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns an object which represents the data to be transferred. The class
of the object returned is defined by the representation class of the
flavor.

**Parameters:** flavor

- the requested flavor for the data
**Returns:** an object which represents the data to be transferred
**Throws:** IOException

- if the data is no longer available in the requested
flavor
**Throws:** UnsupportedFlavorException

- if the requested data flavor is not
supported
**See Also:** DataFlavor.getRepresentationClass()

Method Detail

- getTransferDataFlavors

```java
DataFlavor
[] getTransferDataFlavors()
```

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in. The array should be ordered according to preference
for providing the data (from most richly descriptive to least
descriptive).

**Returns:** an array of data flavors in which this data can be transferred

- isDataFlavorSupported

```java
boolean isDataFlavorSupported​(
DataFlavor
flavor)
```

Returns whether or not the specified data flavor is supported for this
object.

**Parameters:** flavor

- the requested flavor for the data
**Returns:** boolean indicating whether or not the data flavor is supported

- getTransferData

```java
Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns an object which represents the data to be transferred. The class
of the object returned is defined by the representation class of the
flavor.

**Parameters:** flavor

- the requested flavor for the data
**Returns:** an object which represents the data to be transferred
**Throws:** IOException

- if the data is no longer available in the requested
flavor
**Throws:** UnsupportedFlavorException

- if the requested data flavor is not
supported
**See Also:** DataFlavor.getRepresentationClass()

---

#### Method Detail

getTransferDataFlavors

```java
DataFlavor
[] getTransferDataFlavors()
```

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in. The array should be ordered according to preference
for providing the data (from most richly descriptive to least
descriptive).

**Returns:** an array of data flavors in which this data can be transferred

---

#### getTransferDataFlavors

DataFlavor

[] getTransferDataFlavors()

Returns an array of DataFlavor objects indicating the flavors the data
can be provided in. The array should be ordered according to preference
for providing the data (from most richly descriptive to least
descriptive).

isDataFlavorSupported

```java
boolean isDataFlavorSupported​(
DataFlavor
flavor)
```

Returns whether or not the specified data flavor is supported for this
object.

**Parameters:** flavor

- the requested flavor for the data
**Returns:** boolean indicating whether or not the data flavor is supported

---

#### isDataFlavorSupported

boolean isDataFlavorSupported​(

DataFlavor

flavor)

Returns whether or not the specified data flavor is supported for this
object.

getTransferData

```java
Object
getTransferData​(
DataFlavor
flavor)
throws
UnsupportedFlavorException
,

IOException
```

Returns an object which represents the data to be transferred. The class
of the object returned is defined by the representation class of the
flavor.

**Parameters:** flavor

- the requested flavor for the data
**Returns:** an object which represents the data to be transferred
**Throws:** IOException

- if the data is no longer available in the requested
flavor
**Throws:** UnsupportedFlavorException

- if the requested data flavor is not
supported
**See Also:** DataFlavor.getRepresentationClass()

---

#### getTransferData

Object

getTransferData​(

DataFlavor

flavor)
throws

UnsupportedFlavorException

,

IOException

Returns an object which represents the data to be transferred. The class
of the object returned is defined by the representation class of the
flavor.

---

