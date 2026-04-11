# Interface ObjectStreamConstants

**Source:** `java.base\java\io\ObjectStreamConstants.html`

### Class Description

```java
public interface
ObjectStreamConstants
```

Constants written into the Object Serialization Stream.

**All Known Implementing Classes:** ObjectInputStream

,

ObjectOutputStream

---

### Field Details

#### static final short STREAM_MAGIC

Magic number that is written to the stream header.

**See Also:**
- Constant Field Values

---

#### static final short STREAM_VERSION

Version number that is written to the stream header.

**See Also:**
- Constant Field Values

---

#### static final byte TC_BASE

First tag value.

**See Also:**
- Constant Field Values

---

#### static final byte TC_NULL

Null object reference.

**See Also:**
- Constant Field Values

---

#### static final byte TC_REFERENCE

Reference to an object already written into the stream.

**See Also:**
- Constant Field Values

---

#### static final byte TC_CLASSDESC

new Class Descriptor.

**See Also:**
- Constant Field Values

---

#### static final byte TC_OBJECT

new Object.

**See Also:**
- Constant Field Values

---

#### static final byte TC_STRING

new String.

**See Also:**
- Constant Field Values

---

#### static final byte TC_ARRAY

new Array.

**See Also:**
- Constant Field Values

---

#### static final byte TC_CLASS

Reference to Class.

**See Also:**
- Constant Field Values

---

#### static final byte TC_BLOCKDATA

Block of optional data. Byte following tag indicates number
of bytes in this block data.

**See Also:**
- Constant Field Values

---

#### static final byte TC_ENDBLOCKDATA

End of optional block data blocks for an object.

**See Also:**
- Constant Field Values

---

#### static final byte TC_RESET

Reset stream context. All handles written into stream are reset.

**See Also:**
- Constant Field Values

---

#### static final byte TC_BLOCKDATALONG

long Block data. The long following the tag indicates the
number of bytes in this block data.

**See Also:**
- Constant Field Values

---

#### static final byte TC_EXCEPTION

Exception during write.

**See Also:**
- Constant Field Values

---

#### static final byte TC_LONGSTRING

Long string.

**See Also:**
- Constant Field Values

---

#### static final byte TC_PROXYCLASSDESC

new Proxy Class Descriptor.

**See Also:**
- Constant Field Values

---

#### static final byte TC_ENUM

new Enum constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### static final byte TC_MAX

Last tag value.

**See Also:**
- Constant Field Values

---

#### static final int baseWireHandle

First wire handle to be assigned.

**See Also:**
- Constant Field Values

---

#### static final byte SC_WRITE_METHOD

Bit mask for ObjectStreamClass flag. Indicates a Serializable class
defines its own writeObject method.

**See Also:**
- Constant Field Values

---

#### static final byte SC_BLOCK_DATA

Bit mask for ObjectStreamClass flag. Indicates Externalizable data
written in Block Data mode.
Added for PROTOCOL_VERSION_2.

**See Also:**
- PROTOCOL_VERSION_2

,

Constant Field Values

**Since:**
- 1.2

---

#### static final byte SC_SERIALIZABLE

Bit mask for ObjectStreamClass flag. Indicates class is Serializable.

**See Also:**
- Constant Field Values

---

#### static final byte SC_EXTERNALIZABLE

Bit mask for ObjectStreamClass flag. Indicates class is Externalizable.

**See Also:**
- Constant Field Values

---

#### static final byte SC_ENUM

Bit mask for ObjectStreamClass flag. Indicates class is an enum type.

**See Also:**
- Constant Field Values

**Since:**
- 1.5

---

#### static final
SerializablePermission
SUBSTITUTION_PERMISSION

Enable substitution of one object for another during
serialization/deserialization.

**See Also:**
- ObjectOutputStream.enableReplaceObject(boolean)

,

ObjectInputStream.enableResolveObject(boolean)

**Since:**
- 1.2

---

#### static final
SerializablePermission
SUBCLASS_IMPLEMENTATION_PERMISSION

Enable overriding of readObject and writeObject.

**See Also:**
- ObjectOutputStream.writeObjectOverride(Object)

,

ObjectInputStream.readObjectOverride()

**Since:**
- 1.2

---

#### static final
SerializablePermission
SERIAL_FILTER_PERMISSION

Enable setting the process-wide serial filter.

**See Also:**
- ObjectInputFilter.Config.setSerialFilter(ObjectInputFilter)

**Since:**
- 9

---

#### static final int PROTOCOL_VERSION_1

A Stream Protocol Version.

All externalizable data is written in JDK 1.1 external data
format after calling this method. This version is needed to write
streams containing Externalizable data that can be read by
pre-JDK 1.1.6 JVMs.

**See Also:**
- ObjectOutputStream.useProtocolVersion(int)

,

Constant Field Values

**Since:**
- 1.2

---

#### static final int PROTOCOL_VERSION_2

A Stream Protocol Version.

This protocol is written by JVM 1.2.

Externalizable data is written in block data mode and is
terminated with TC_ENDBLOCKDATA. Externalizable class descriptor
flags has SC_BLOCK_DATA enabled. JVM 1.1.6 and greater can
read this format change.

Enables writing a nonSerializable class descriptor into the
stream. The serialVersionUID of a nonSerializable class is
set to 0L.

**See Also:**
- ObjectOutputStream.useProtocolVersion(int)

,

SC_BLOCK_DATA

,

Constant Field Values

**Since:**
- 1.2

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface ObjectStreamConstants

**All Known Implementing Classes:** ObjectInputStream

,

ObjectOutputStream

```java
public interface
ObjectStreamConstants
```

Constants written into the Object Serialization Stream.

**Since:** 1.1

public interface

ObjectStreamConstants

Constants written into the Object Serialization Stream.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

baseWireHandle

First wire handle to be assigned.

static int

PROTOCOL_VERSION_1

A Stream Protocol Version.

static int

PROTOCOL_VERSION_2

A Stream Protocol Version.

static byte

SC_BLOCK_DATA

Bit mask for ObjectStreamClass flag.

static byte

SC_ENUM

Bit mask for ObjectStreamClass flag.

static byte

SC_EXTERNALIZABLE

Bit mask for ObjectStreamClass flag.

static byte

SC_SERIALIZABLE

Bit mask for ObjectStreamClass flag.

static byte

SC_WRITE_METHOD

Bit mask for ObjectStreamClass flag.

static

SerializablePermission

SERIAL_FILTER_PERMISSION

Enable setting the process-wide serial filter.

static short

STREAM_MAGIC

Magic number that is written to the stream header.

static short

STREAM_VERSION

Version number that is written to the stream header.

static

SerializablePermission

SUBCLASS_IMPLEMENTATION_PERMISSION

Enable overriding of readObject and writeObject.

static

SerializablePermission

SUBSTITUTION_PERMISSION

Enable substitution of one object for another during
serialization/deserialization.

static byte

TC_ARRAY

new Array.

static byte

TC_BASE

First tag value.

static byte

TC_BLOCKDATA

Block of optional data.

static byte

TC_BLOCKDATALONG

long Block data.

static byte

TC_CLASS

Reference to Class.

static byte

TC_CLASSDESC

new Class Descriptor.

static byte

TC_ENDBLOCKDATA

End of optional block data blocks for an object.

static byte

TC_ENUM

new Enum constant.

static byte

TC_EXCEPTION

Exception during write.

static byte

TC_LONGSTRING

Long string.

static byte

TC_MAX

Last tag value.

static byte

TC_NULL

Null object reference.

static byte

TC_OBJECT

new Object.

static byte

TC_PROXYCLASSDESC

new Proxy Class Descriptor.

static byte

TC_REFERENCE

Reference to an object already written into the stream.

static byte

TC_RESET

Reset stream context.

static byte

TC_STRING

new String.

Field Summary

Fields

Modifier and Type

Field

Description

static int

baseWireHandle

First wire handle to be assigned.

static int

PROTOCOL_VERSION_1

A Stream Protocol Version.

static int

PROTOCOL_VERSION_2

A Stream Protocol Version.

static byte

SC_BLOCK_DATA

Bit mask for ObjectStreamClass flag.

static byte

SC_ENUM

Bit mask for ObjectStreamClass flag.

static byte

SC_EXTERNALIZABLE

Bit mask for ObjectStreamClass flag.

static byte

SC_SERIALIZABLE

Bit mask for ObjectStreamClass flag.

static byte

SC_WRITE_METHOD

Bit mask for ObjectStreamClass flag.

static

SerializablePermission

SERIAL_FILTER_PERMISSION

Enable setting the process-wide serial filter.

static short

STREAM_MAGIC

Magic number that is written to the stream header.

static short

STREAM_VERSION

Version number that is written to the stream header.

static

SerializablePermission

SUBCLASS_IMPLEMENTATION_PERMISSION

Enable overriding of readObject and writeObject.

static

SerializablePermission

SUBSTITUTION_PERMISSION

Enable substitution of one object for another during
serialization/deserialization.

static byte

TC_ARRAY

new Array.

static byte

TC_BASE

First tag value.

static byte

TC_BLOCKDATA

Block of optional data.

static byte

TC_BLOCKDATALONG

long Block data.

static byte

TC_CLASS

Reference to Class.

static byte

TC_CLASSDESC

new Class Descriptor.

static byte

TC_ENDBLOCKDATA

End of optional block data blocks for an object.

static byte

TC_ENUM

new Enum constant.

static byte

TC_EXCEPTION

Exception during write.

static byte

TC_LONGSTRING

Long string.

static byte

TC_MAX

Last tag value.

static byte

TC_NULL

Null object reference.

static byte

TC_OBJECT

new Object.

static byte

TC_PROXYCLASSDESC

new Proxy Class Descriptor.

static byte

TC_REFERENCE

Reference to an object already written into the stream.

static byte

TC_RESET

Reset stream context.

static byte

TC_STRING

new String.

---

#### Field Summary

First wire handle to be assigned.

A Stream Protocol Version.

Bit mask for ObjectStreamClass flag.

Enable setting the process-wide serial filter.

Magic number that is written to the stream header.

Version number that is written to the stream header.

Enable overriding of readObject and writeObject.

Enable substitution of one object for another during
serialization/deserialization.

new Array.

First tag value.

Block of optional data.

long Block data.

Reference to Class.

new Class Descriptor.

End of optional block data blocks for an object.

new Enum constant.

Exception during write.

Long string.

Last tag value.

Null object reference.

new Object.

new Proxy Class Descriptor.

Reference to an object already written into the stream.

Reset stream context.

new String.

============ FIELD DETAIL ===========

- Field Detail

- STREAM_MAGIC

```java
static final short STREAM_MAGIC
```

Magic number that is written to the stream header.

**See Also:** Constant Field Values

- STREAM_VERSION

```java
static final short STREAM_VERSION
```

Version number that is written to the stream header.

**See Also:** Constant Field Values

- TC_BASE

```java
static final byte TC_BASE
```

First tag value.

**See Also:** Constant Field Values

- TC_NULL

```java
static final byte TC_NULL
```

Null object reference.

**See Also:** Constant Field Values

- TC_REFERENCE

```java
static final byte TC_REFERENCE
```

Reference to an object already written into the stream.

**See Also:** Constant Field Values

- TC_CLASSDESC

```java
static final byte TC_CLASSDESC
```

new Class Descriptor.

**See Also:** Constant Field Values

- TC_OBJECT

```java
static final byte TC_OBJECT
```

new Object.

**See Also:** Constant Field Values

- TC_STRING

```java
static final byte TC_STRING
```

new String.

**See Also:** Constant Field Values

- TC_ARRAY

```java
static final byte TC_ARRAY
```

new Array.

**See Also:** Constant Field Values

- TC_CLASS

```java
static final byte TC_CLASS
```

Reference to Class.

**See Also:** Constant Field Values

- TC_BLOCKDATA

```java
static final byte TC_BLOCKDATA
```

Block of optional data. Byte following tag indicates number
of bytes in this block data.

**See Also:** Constant Field Values

- TC_ENDBLOCKDATA

```java
static final byte TC_ENDBLOCKDATA
```

End of optional block data blocks for an object.

**See Also:** Constant Field Values

- TC_RESET

```java
static final byte TC_RESET
```

Reset stream context. All handles written into stream are reset.

**See Also:** Constant Field Values

- TC_BLOCKDATALONG

```java
static final byte TC_BLOCKDATALONG
```

long Block data. The long following the tag indicates the
number of bytes in this block data.

**See Also:** Constant Field Values

- TC_EXCEPTION

```java
static final byte TC_EXCEPTION
```

Exception during write.

**See Also:** Constant Field Values

- TC_LONGSTRING

```java
static final byte TC_LONGSTRING
```

Long string.

**See Also:** Constant Field Values

- TC_PROXYCLASSDESC

```java
static final byte TC_PROXYCLASSDESC
```

new Proxy Class Descriptor.

**See Also:** Constant Field Values

- TC_ENUM

```java
static final byte TC_ENUM
```

new Enum constant.

**Since:** 1.5
**See Also:** Constant Field Values

- TC_MAX

```java
static final byte TC_MAX
```

Last tag value.

**See Also:** Constant Field Values

- baseWireHandle

```java
static final int baseWireHandle
```

First wire handle to be assigned.

**See Also:** Constant Field Values

- SC_WRITE_METHOD

```java
static final byte SC_WRITE_METHOD
```

Bit mask for ObjectStreamClass flag. Indicates a Serializable class
defines its own writeObject method.

**See Also:** Constant Field Values

- SC_BLOCK_DATA

```java
static final byte SC_BLOCK_DATA
```

Bit mask for ObjectStreamClass flag. Indicates Externalizable data
written in Block Data mode.
Added for PROTOCOL_VERSION_2.

**Since:** 1.2
**See Also:** PROTOCOL_VERSION_2

,

Constant Field Values

- SC_SERIALIZABLE

```java
static final byte SC_SERIALIZABLE
```

Bit mask for ObjectStreamClass flag. Indicates class is Serializable.

**See Also:** Constant Field Values

- SC_EXTERNALIZABLE

```java
static final byte SC_EXTERNALIZABLE
```

Bit mask for ObjectStreamClass flag. Indicates class is Externalizable.

**See Also:** Constant Field Values

- SC_ENUM

```java
static final byte SC_ENUM
```

Bit mask for ObjectStreamClass flag. Indicates class is an enum type.

**Since:** 1.5
**See Also:** Constant Field Values

- SUBSTITUTION_PERMISSION

```java
static final
SerializablePermission
SUBSTITUTION_PERMISSION
```

Enable substitution of one object for another during
serialization/deserialization.

**Since:** 1.2
**See Also:** ObjectOutputStream.enableReplaceObject(boolean)

,

ObjectInputStream.enableResolveObject(boolean)

- SUBCLASS_IMPLEMENTATION_PERMISSION

```java
static final
SerializablePermission
SUBCLASS_IMPLEMENTATION_PERMISSION
```

Enable overriding of readObject and writeObject.

**Since:** 1.2
**See Also:** ObjectOutputStream.writeObjectOverride(Object)

,

ObjectInputStream.readObjectOverride()

- SERIAL_FILTER_PERMISSION

```java
static final
SerializablePermission
SERIAL_FILTER_PERMISSION
```

Enable setting the process-wide serial filter.

**Since:** 9
**See Also:** ObjectInputFilter.Config.setSerialFilter(ObjectInputFilter)

- PROTOCOL_VERSION_1

```java
static final int PROTOCOL_VERSION_1
```

A Stream Protocol Version.

All externalizable data is written in JDK 1.1 external data
format after calling this method. This version is needed to write
streams containing Externalizable data that can be read by
pre-JDK 1.1.6 JVMs.

**Since:** 1.2
**See Also:** ObjectOutputStream.useProtocolVersion(int)

,

Constant Field Values

- PROTOCOL_VERSION_2

```java
static final int PROTOCOL_VERSION_2
```

A Stream Protocol Version.

This protocol is written by JVM 1.2.

Externalizable data is written in block data mode and is
terminated with TC_ENDBLOCKDATA. Externalizable class descriptor
flags has SC_BLOCK_DATA enabled. JVM 1.1.6 and greater can
read this format change.

Enables writing a nonSerializable class descriptor into the
stream. The serialVersionUID of a nonSerializable class is
set to 0L.

**Since:** 1.2
**See Also:** ObjectOutputStream.useProtocolVersion(int)

,

SC_BLOCK_DATA

,

Constant Field Values

Field Detail

- STREAM_MAGIC

```java
static final short STREAM_MAGIC
```

Magic number that is written to the stream header.

**See Also:** Constant Field Values

- STREAM_VERSION

```java
static final short STREAM_VERSION
```

Version number that is written to the stream header.

**See Also:** Constant Field Values

- TC_BASE

```java
static final byte TC_BASE
```

First tag value.

**See Also:** Constant Field Values

- TC_NULL

```java
static final byte TC_NULL
```

Null object reference.

**See Also:** Constant Field Values

- TC_REFERENCE

```java
static final byte TC_REFERENCE
```

Reference to an object already written into the stream.

**See Also:** Constant Field Values

- TC_CLASSDESC

```java
static final byte TC_CLASSDESC
```

new Class Descriptor.

**See Also:** Constant Field Values

- TC_OBJECT

```java
static final byte TC_OBJECT
```

new Object.

**See Also:** Constant Field Values

- TC_STRING

```java
static final byte TC_STRING
```

new String.

**See Also:** Constant Field Values

- TC_ARRAY

```java
static final byte TC_ARRAY
```

new Array.

**See Also:** Constant Field Values

- TC_CLASS

```java
static final byte TC_CLASS
```

Reference to Class.

**See Also:** Constant Field Values

- TC_BLOCKDATA

```java
static final byte TC_BLOCKDATA
```

Block of optional data. Byte following tag indicates number
of bytes in this block data.

**See Also:** Constant Field Values

- TC_ENDBLOCKDATA

```java
static final byte TC_ENDBLOCKDATA
```

End of optional block data blocks for an object.

**See Also:** Constant Field Values

- TC_RESET

```java
static final byte TC_RESET
```

Reset stream context. All handles written into stream are reset.

**See Also:** Constant Field Values

- TC_BLOCKDATALONG

```java
static final byte TC_BLOCKDATALONG
```

long Block data. The long following the tag indicates the
number of bytes in this block data.

**See Also:** Constant Field Values

- TC_EXCEPTION

```java
static final byte TC_EXCEPTION
```

Exception during write.

**See Also:** Constant Field Values

- TC_LONGSTRING

```java
static final byte TC_LONGSTRING
```

Long string.

**See Also:** Constant Field Values

- TC_PROXYCLASSDESC

```java
static final byte TC_PROXYCLASSDESC
```

new Proxy Class Descriptor.

**See Also:** Constant Field Values

- TC_ENUM

```java
static final byte TC_ENUM
```

new Enum constant.

**Since:** 1.5
**See Also:** Constant Field Values

- TC_MAX

```java
static final byte TC_MAX
```

Last tag value.

**See Also:** Constant Field Values

- baseWireHandle

```java
static final int baseWireHandle
```

First wire handle to be assigned.

**See Also:** Constant Field Values

- SC_WRITE_METHOD

```java
static final byte SC_WRITE_METHOD
```

Bit mask for ObjectStreamClass flag. Indicates a Serializable class
defines its own writeObject method.

**See Also:** Constant Field Values

- SC_BLOCK_DATA

```java
static final byte SC_BLOCK_DATA
```

Bit mask for ObjectStreamClass flag. Indicates Externalizable data
written in Block Data mode.
Added for PROTOCOL_VERSION_2.

**Since:** 1.2
**See Also:** PROTOCOL_VERSION_2

,

Constant Field Values

- SC_SERIALIZABLE

```java
static final byte SC_SERIALIZABLE
```

Bit mask for ObjectStreamClass flag. Indicates class is Serializable.

**See Also:** Constant Field Values

- SC_EXTERNALIZABLE

```java
static final byte SC_EXTERNALIZABLE
```

Bit mask for ObjectStreamClass flag. Indicates class is Externalizable.

**See Also:** Constant Field Values

- SC_ENUM

```java
static final byte SC_ENUM
```

Bit mask for ObjectStreamClass flag. Indicates class is an enum type.

**Since:** 1.5
**See Also:** Constant Field Values

- SUBSTITUTION_PERMISSION

```java
static final
SerializablePermission
SUBSTITUTION_PERMISSION
```

Enable substitution of one object for another during
serialization/deserialization.

**Since:** 1.2
**See Also:** ObjectOutputStream.enableReplaceObject(boolean)

,

ObjectInputStream.enableResolveObject(boolean)

- SUBCLASS_IMPLEMENTATION_PERMISSION

```java
static final
SerializablePermission
SUBCLASS_IMPLEMENTATION_PERMISSION
```

Enable overriding of readObject and writeObject.

**Since:** 1.2
**See Also:** ObjectOutputStream.writeObjectOverride(Object)

,

ObjectInputStream.readObjectOverride()

- SERIAL_FILTER_PERMISSION

```java
static final
SerializablePermission
SERIAL_FILTER_PERMISSION
```

Enable setting the process-wide serial filter.

**Since:** 9
**See Also:** ObjectInputFilter.Config.setSerialFilter(ObjectInputFilter)

- PROTOCOL_VERSION_1

```java
static final int PROTOCOL_VERSION_1
```

A Stream Protocol Version.

All externalizable data is written in JDK 1.1 external data
format after calling this method. This version is needed to write
streams containing Externalizable data that can be read by
pre-JDK 1.1.6 JVMs.

**Since:** 1.2
**See Also:** ObjectOutputStream.useProtocolVersion(int)

,

Constant Field Values

- PROTOCOL_VERSION_2

```java
static final int PROTOCOL_VERSION_2
```

A Stream Protocol Version.

This protocol is written by JVM 1.2.

Externalizable data is written in block data mode and is
terminated with TC_ENDBLOCKDATA. Externalizable class descriptor
flags has SC_BLOCK_DATA enabled. JVM 1.1.6 and greater can
read this format change.

Enables writing a nonSerializable class descriptor into the
stream. The serialVersionUID of a nonSerializable class is
set to 0L.

**Since:** 1.2
**See Also:** ObjectOutputStream.useProtocolVersion(int)

,

SC_BLOCK_DATA

,

Constant Field Values

---

#### Field Detail

STREAM_MAGIC

```java
static final short STREAM_MAGIC
```

Magic number that is written to the stream header.

**See Also:** Constant Field Values

---

#### STREAM_MAGIC

static final short STREAM_MAGIC

Magic number that is written to the stream header.

STREAM_VERSION

```java
static final short STREAM_VERSION
```

Version number that is written to the stream header.

**See Also:** Constant Field Values

---

#### STREAM_VERSION

static final short STREAM_VERSION

Version number that is written to the stream header.

TC_BASE

```java
static final byte TC_BASE
```

First tag value.

**See Also:** Constant Field Values

---

#### TC_BASE

static final byte TC_BASE

First tag value.

TC_NULL

```java
static final byte TC_NULL
```

Null object reference.

**See Also:** Constant Field Values

---

#### TC_NULL

static final byte TC_NULL

Null object reference.

TC_REFERENCE

```java
static final byte TC_REFERENCE
```

Reference to an object already written into the stream.

**See Also:** Constant Field Values

---

#### TC_REFERENCE

static final byte TC_REFERENCE

Reference to an object already written into the stream.

TC_CLASSDESC

```java
static final byte TC_CLASSDESC
```

new Class Descriptor.

**See Also:** Constant Field Values

---

#### TC_CLASSDESC

static final byte TC_CLASSDESC

new Class Descriptor.

TC_OBJECT

```java
static final byte TC_OBJECT
```

new Object.

**See Also:** Constant Field Values

---

#### TC_OBJECT

static final byte TC_OBJECT

new Object.

TC_STRING

```java
static final byte TC_STRING
```

new String.

**See Also:** Constant Field Values

---

#### TC_STRING

static final byte TC_STRING

new String.

TC_ARRAY

```java
static final byte TC_ARRAY
```

new Array.

**See Also:** Constant Field Values

---

#### TC_ARRAY

static final byte TC_ARRAY

new Array.

TC_CLASS

```java
static final byte TC_CLASS
```

Reference to Class.

**See Also:** Constant Field Values

---

#### TC_CLASS

static final byte TC_CLASS

Reference to Class.

TC_BLOCKDATA

```java
static final byte TC_BLOCKDATA
```

Block of optional data. Byte following tag indicates number
of bytes in this block data.

**See Also:** Constant Field Values

---

#### TC_BLOCKDATA

static final byte TC_BLOCKDATA

Block of optional data. Byte following tag indicates number
of bytes in this block data.

TC_ENDBLOCKDATA

```java
static final byte TC_ENDBLOCKDATA
```

End of optional block data blocks for an object.

**See Also:** Constant Field Values

---

#### TC_ENDBLOCKDATA

static final byte TC_ENDBLOCKDATA

End of optional block data blocks for an object.

TC_RESET

```java
static final byte TC_RESET
```

Reset stream context. All handles written into stream are reset.

**See Also:** Constant Field Values

---

#### TC_RESET

static final byte TC_RESET

Reset stream context. All handles written into stream are reset.

TC_BLOCKDATALONG

```java
static final byte TC_BLOCKDATALONG
```

long Block data. The long following the tag indicates the
number of bytes in this block data.

**See Also:** Constant Field Values

---

#### TC_BLOCKDATALONG

static final byte TC_BLOCKDATALONG

long Block data. The long following the tag indicates the
number of bytes in this block data.

TC_EXCEPTION

```java
static final byte TC_EXCEPTION
```

Exception during write.

**See Also:** Constant Field Values

---

#### TC_EXCEPTION

static final byte TC_EXCEPTION

Exception during write.

TC_LONGSTRING

```java
static final byte TC_LONGSTRING
```

Long string.

**See Also:** Constant Field Values

---

#### TC_LONGSTRING

static final byte TC_LONGSTRING

Long string.

TC_PROXYCLASSDESC

```java
static final byte TC_PROXYCLASSDESC
```

new Proxy Class Descriptor.

**See Also:** Constant Field Values

---

#### TC_PROXYCLASSDESC

static final byte TC_PROXYCLASSDESC

new Proxy Class Descriptor.

TC_ENUM

```java
static final byte TC_ENUM
```

new Enum constant.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### TC_ENUM

static final byte TC_ENUM

new Enum constant.

TC_MAX

```java
static final byte TC_MAX
```

Last tag value.

**See Also:** Constant Field Values

---

#### TC_MAX

static final byte TC_MAX

Last tag value.

baseWireHandle

```java
static final int baseWireHandle
```

First wire handle to be assigned.

**See Also:** Constant Field Values

---

#### baseWireHandle

static final int baseWireHandle

First wire handle to be assigned.

SC_WRITE_METHOD

```java
static final byte SC_WRITE_METHOD
```

Bit mask for ObjectStreamClass flag. Indicates a Serializable class
defines its own writeObject method.

**See Also:** Constant Field Values

---

#### SC_WRITE_METHOD

static final byte SC_WRITE_METHOD

Bit mask for ObjectStreamClass flag. Indicates a Serializable class
defines its own writeObject method.

SC_BLOCK_DATA

```java
static final byte SC_BLOCK_DATA
```

Bit mask for ObjectStreamClass flag. Indicates Externalizable data
written in Block Data mode.
Added for PROTOCOL_VERSION_2.

**Since:** 1.2
**See Also:** PROTOCOL_VERSION_2

,

Constant Field Values

---

#### SC_BLOCK_DATA

static final byte SC_BLOCK_DATA

Bit mask for ObjectStreamClass flag. Indicates Externalizable data
written in Block Data mode.
Added for PROTOCOL_VERSION_2.

SC_SERIALIZABLE

```java
static final byte SC_SERIALIZABLE
```

Bit mask for ObjectStreamClass flag. Indicates class is Serializable.

**See Also:** Constant Field Values

---

#### SC_SERIALIZABLE

static final byte SC_SERIALIZABLE

Bit mask for ObjectStreamClass flag. Indicates class is Serializable.

SC_EXTERNALIZABLE

```java
static final byte SC_EXTERNALIZABLE
```

Bit mask for ObjectStreamClass flag. Indicates class is Externalizable.

**See Also:** Constant Field Values

---

#### SC_EXTERNALIZABLE

static final byte SC_EXTERNALIZABLE

Bit mask for ObjectStreamClass flag. Indicates class is Externalizable.

SC_ENUM

```java
static final byte SC_ENUM
```

Bit mask for ObjectStreamClass flag. Indicates class is an enum type.

**Since:** 1.5
**See Also:** Constant Field Values

---

#### SC_ENUM

static final byte SC_ENUM

Bit mask for ObjectStreamClass flag. Indicates class is an enum type.

SUBSTITUTION_PERMISSION

```java
static final
SerializablePermission
SUBSTITUTION_PERMISSION
```

Enable substitution of one object for another during
serialization/deserialization.

**Since:** 1.2
**See Also:** ObjectOutputStream.enableReplaceObject(boolean)

,

ObjectInputStream.enableResolveObject(boolean)

---

#### SUBSTITUTION_PERMISSION

static final

SerializablePermission

SUBSTITUTION_PERMISSION

Enable substitution of one object for another during
serialization/deserialization.

SUBCLASS_IMPLEMENTATION_PERMISSION

```java
static final
SerializablePermission
SUBCLASS_IMPLEMENTATION_PERMISSION
```

Enable overriding of readObject and writeObject.

**Since:** 1.2
**See Also:** ObjectOutputStream.writeObjectOverride(Object)

,

ObjectInputStream.readObjectOverride()

---

#### SUBCLASS_IMPLEMENTATION_PERMISSION

static final

SerializablePermission

SUBCLASS_IMPLEMENTATION_PERMISSION

Enable overriding of readObject and writeObject.

SERIAL_FILTER_PERMISSION

```java
static final
SerializablePermission
SERIAL_FILTER_PERMISSION
```

Enable setting the process-wide serial filter.

**Since:** 9
**See Also:** ObjectInputFilter.Config.setSerialFilter(ObjectInputFilter)

---

#### SERIAL_FILTER_PERMISSION

static final

SerializablePermission

SERIAL_FILTER_PERMISSION

Enable setting the process-wide serial filter.

PROTOCOL_VERSION_1

```java
static final int PROTOCOL_VERSION_1
```

A Stream Protocol Version.

All externalizable data is written in JDK 1.1 external data
format after calling this method. This version is needed to write
streams containing Externalizable data that can be read by
pre-JDK 1.1.6 JVMs.

**Since:** 1.2
**See Also:** ObjectOutputStream.useProtocolVersion(int)

,

Constant Field Values

---

#### PROTOCOL_VERSION_1

static final int PROTOCOL_VERSION_1

A Stream Protocol Version.

All externalizable data is written in JDK 1.1 external data
format after calling this method. This version is needed to write
streams containing Externalizable data that can be read by
pre-JDK 1.1.6 JVMs.

All externalizable data is written in JDK 1.1 external data
format after calling this method. This version is needed to write
streams containing Externalizable data that can be read by
pre-JDK 1.1.6 JVMs.

PROTOCOL_VERSION_2

```java
static final int PROTOCOL_VERSION_2
```

A Stream Protocol Version.

This protocol is written by JVM 1.2.

Externalizable data is written in block data mode and is
terminated with TC_ENDBLOCKDATA. Externalizable class descriptor
flags has SC_BLOCK_DATA enabled. JVM 1.1.6 and greater can
read this format change.

Enables writing a nonSerializable class descriptor into the
stream. The serialVersionUID of a nonSerializable class is
set to 0L.

**Since:** 1.2
**See Also:** ObjectOutputStream.useProtocolVersion(int)

,

SC_BLOCK_DATA

,

Constant Field Values

---

#### PROTOCOL_VERSION_2

static final int PROTOCOL_VERSION_2

A Stream Protocol Version.

This protocol is written by JVM 1.2.

Externalizable data is written in block data mode and is
terminated with TC_ENDBLOCKDATA. Externalizable class descriptor
flags has SC_BLOCK_DATA enabled. JVM 1.1.6 and greater can
read this format change.

Enables writing a nonSerializable class descriptor into the
stream. The serialVersionUID of a nonSerializable class is
set to 0L.

This protocol is written by JVM 1.2.

Externalizable data is written in block data mode and is
terminated with TC_ENDBLOCKDATA. Externalizable class descriptor
flags has SC_BLOCK_DATA enabled. JVM 1.1.6 and greater can
read this format change.

Enables writing a nonSerializable class descriptor into the
stream. The serialVersionUID of a nonSerializable class is
set to 0L.

---

