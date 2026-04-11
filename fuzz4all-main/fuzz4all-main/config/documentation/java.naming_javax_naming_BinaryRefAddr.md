# Class BinaryRefAddr

**Source:** `java.naming\javax\naming\BinaryRefAddr.html`

### Class Description

```java
public class
BinaryRefAddr

extends
RefAddr
```

This class represents the binary form of the address of
a communications end-point.

A BinaryRefAddr consists of a type that describes the communication mechanism
and an opaque buffer containing the address description
specific to that communication mechanism. The format and interpretation of
the address type and the contents of the opaque buffer are based on
the agreement of three parties: the client that uses the address,
the object/server that can be reached using the address,
and the administrator or program that creates the address.

An example of a binary reference address is an BER X.500 presentation address.
Another example of a binary reference address is a serialized form of
a service's object handle.

A binary reference address is immutable in the sense that its fields
once created, cannot be replaced. However, it is possible to access
the byte array used to hold the opaque buffer. Programs are strongly
recommended against changing this byte array. Changes to this
byte array need to be explicitly synchronized.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public BinaryRefAddr​(
String
addrType,
byte[] src)

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

**Parameters:**
- addrType

- A non-null string describing the type of the address.
- src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.

---

#### public BinaryRefAddr​(
String
addrType,
byte[] src,
int offset,
int count)

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

**Parameters:**
- addrType

- A non-null string describing the type of the address.
- src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.
- offset

- The starting index in src to get the bytes.

0 <= offset <= src.length

.
- count

- The number of bytes to extract from src.

0 <= count <= src.length-offset

.

---

### Method Details

#### public
Object
getContent()

Retrieves the contents of this address as an Object.
The result is a byte array.
Changes to this array will affect this BinaryRefAddr's contents.
Programs are recommended against changing this array's contents
and to lock the buffer if they need to change it.

**Specified by:**
- getContent

in class

RefAddr

**Returns:**
- The non-null buffer containing this address's contents.

---

#### public boolean equals​(
Object
obj)

Determines whether obj is equal to this address. It is equal if
it contains the same address type and their contents are byte-wise
equivalent.

**Overrides:**
- equals

in class

RefAddr

**Parameters:**
- obj

- The possibly null object to check.

**Returns:**
- true if the object is equal; false otherwise.

**See Also:**
- RefAddr.getContent()

,

RefAddr.getType()

---

#### public int hashCode()

Computes the hash code of this address using its address type and contents.
Two BinaryRefAddrs have the same hash code if they have
the same address type and the same contents.
It is also possible for different BinaryRefAddrs to have
the same hash code.

**Overrides:**
- hashCode

in class

RefAddr

**Returns:**
- The hash code of this address as an int.

**See Also:**
- Object.hashCode()

---

#### public
String
toString()

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
The first 32 bytes of contents are displayed (in hexadecimal).
If there are more than 32 bytes, "..." is used to indicate more.
This string is meant to used for debugging purposes and not
meant to be interpreted programmatically.

**Overrides:**
- toString

in class

RefAddr

**Returns:**
- The non-null string representation of this address.

---

### Additional Sections

#### Class BinaryRefAddr

java.lang.Object

- javax.naming.RefAddr
- - javax.naming.BinaryRefAddr

javax.naming.RefAddr

- javax.naming.BinaryRefAddr

javax.naming.BinaryRefAddr

**All Implemented Interfaces:** Serializable

```java
public class
BinaryRefAddr

extends
RefAddr
```

This class represents the binary form of the address of
a communications end-point.

A BinaryRefAddr consists of a type that describes the communication mechanism
and an opaque buffer containing the address description
specific to that communication mechanism. The format and interpretation of
the address type and the contents of the opaque buffer are based on
the agreement of three parties: the client that uses the address,
the object/server that can be reached using the address,
and the administrator or program that creates the address.

An example of a binary reference address is an BER X.500 presentation address.
Another example of a binary reference address is a serialized form of
a service's object handle.

A binary reference address is immutable in the sense that its fields
once created, cannot be replaced. However, it is possible to access
the byte array used to hold the opaque buffer. Programs are strongly
recommended against changing this byte array. Changes to this
byte array need to be explicitly synchronized.

**Since:** 1.3
**See Also:** RefAddr

,

StringRefAddr

,

Serialized Form

public class

BinaryRefAddr

extends

RefAddr

This class represents the binary form of the address of
a communications end-point.

A BinaryRefAddr consists of a type that describes the communication mechanism
and an opaque buffer containing the address description
specific to that communication mechanism. The format and interpretation of
the address type and the contents of the opaque buffer are based on
the agreement of three parties: the client that uses the address,
the object/server that can be reached using the address,
and the administrator or program that creates the address.

An example of a binary reference address is an BER X.500 presentation address.
Another example of a binary reference address is a serialized form of
a service's object handle.

A binary reference address is immutable in the sense that its fields
once created, cannot be replaced. However, it is possible to access
the byte array used to hold the opaque buffer. Programs are strongly
recommended against changing this byte array. Changes to this
byte array need to be explicitly synchronized.

A BinaryRefAddr consists of a type that describes the communication mechanism
and an opaque buffer containing the address description
specific to that communication mechanism. The format and interpretation of
the address type and the contents of the opaque buffer are based on
the agreement of three parties: the client that uses the address,
the object/server that can be reached using the address,
and the administrator or program that creates the address.

An example of a binary reference address is an BER X.500 presentation address.
Another example of a binary reference address is a serialized form of
a service's object handle.

A binary reference address is immutable in the sense that its fields
once created, cannot be replaced. However, it is possible to access
the byte array used to hold the opaque buffer. Programs are strongly
recommended against changing this byte array. Changes to this
byte array need to be explicitly synchronized.

An example of a binary reference address is an BER X.500 presentation address.
Another example of a binary reference address is a serialized form of
a service's object handle.

A binary reference address is immutable in the sense that its fields
once created, cannot be replaced. However, it is possible to access
the byte array used to hold the opaque buffer. Programs are strongly
recommended against changing this byte array. Changes to this
byte array need to be explicitly synchronized.

A binary reference address is immutable in the sense that its fields
once created, cannot be replaced. However, it is possible to access
the byte array used to hold the opaque buffer. Programs are strongly
recommended against changing this byte array. Changes to this
byte array need to be explicitly synchronized.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

RefAddr

addrType

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BinaryRefAddr

​(

String

addrType,
byte[] src)

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

BinaryRefAddr

​(

String

addrType,
byte[] src,
int offset,
int count)

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether obj is equal to this address.

Object

getContent

()

Retrieves the contents of this address as an Object.

int

hashCode

()

Computes the hash code of this address using its address type and contents.

String

toString

()

Generates the string representation of this address.

- Methods declared in class javax.naming.

RefAddr

getType

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Field Summary

- Fields declared in class javax.naming.

RefAddr

addrType

---

#### Field Summary

Fields declared in class javax.naming.

RefAddr

addrType

---

#### Fields declared in class javax.naming. RefAddr

Constructor Summary

Constructors

Constructor

Description

BinaryRefAddr

​(

String

addrType,
byte[] src)

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

BinaryRefAddr

​(

String

addrType,
byte[] src,
int offset,
int count)

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

---

#### Constructor Summary

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Determines whether obj is equal to this address.

Object

getContent

()

Retrieves the contents of this address as an Object.

int

hashCode

()

Computes the hash code of this address using its address type and contents.

String

toString

()

Generates the string representation of this address.

- Methods declared in class javax.naming.

RefAddr

getType

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Determines whether obj is equal to this address.

Retrieves the contents of this address as an Object.

Computes the hash code of this address using its address type and contents.

Generates the string representation of this address.

Methods declared in class javax.naming.

RefAddr

getType

---

#### Methods declared in class javax.naming. RefAddr

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- BinaryRefAddr

```java
public BinaryRefAddr​(
String
addrType,
byte[] src)
```

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.

- BinaryRefAddr

```java
public BinaryRefAddr​(
String
addrType,
byte[] src,
int offset,
int count)
```

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.
**Parameters:** offset

- The starting index in src to get the bytes.

0 <= offset <= src.length

.
**Parameters:** count

- The number of bytes to extract from src.

0 <= count <= src.length-offset

.

============ METHOD DETAIL ==========

- Method Detail

- getContent

```java
public
Object
getContent()
```

Retrieves the contents of this address as an Object.
The result is a byte array.
Changes to this array will affect this BinaryRefAddr's contents.
Programs are recommended against changing this array's contents
and to lock the buffer if they need to change it.

**Specified by:** getContent

in class

RefAddr
**Returns:** The non-null buffer containing this address's contents.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this address. It is equal if
it contains the same address type and their contents are byte-wise
equivalent.

**Overrides:** equals

in class

RefAddr
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if the object is equal; false otherwise.
**See Also:** RefAddr.getContent()

,

RefAddr.getType()

- hashCode

```java
public int hashCode()
```

Computes the hash code of this address using its address type and contents.
Two BinaryRefAddrs have the same hash code if they have
the same address type and the same contents.
It is also possible for different BinaryRefAddrs to have
the same hash code.

**Overrides:** hashCode

in class

RefAddr
**Returns:** The hash code of this address as an int.
**See Also:** Object.hashCode()

- toString

```java
public
String
toString()
```

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
The first 32 bytes of contents are displayed (in hexadecimal).
If there are more than 32 bytes, "..." is used to indicate more.
This string is meant to used for debugging purposes and not
meant to be interpreted programmatically.

**Overrides:** toString

in class

RefAddr
**Returns:** The non-null string representation of this address.

Constructor Detail

- BinaryRefAddr

```java
public BinaryRefAddr​(
String
addrType,
byte[] src)
```

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.

- BinaryRefAddr

```java
public BinaryRefAddr​(
String
addrType,
byte[] src,
int offset,
int count)
```

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.
**Parameters:** offset

- The starting index in src to get the bytes.

0 <= offset <= src.length

.
**Parameters:** count

- The number of bytes to extract from src.

0 <= count <= src.length-offset

.

---

#### Constructor Detail

BinaryRefAddr

```java
public BinaryRefAddr​(
String
addrType,
byte[] src)
```

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.

---

#### BinaryRefAddr

public BinaryRefAddr​(

String

addrType,
byte[] src)

Constructs a new instance of BinaryRefAddr using its address type and a byte
array for contents.

BinaryRefAddr

```java
public BinaryRefAddr​(
String
addrType,
byte[] src,
int offset,
int count)
```

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

**Parameters:** addrType

- A non-null string describing the type of the address.
**Parameters:** src

- The non-null contents of the address as a byte array.
The contents of src is copied into the new BinaryRefAddr.
**Parameters:** offset

- The starting index in src to get the bytes.

0 <= offset <= src.length

.
**Parameters:** count

- The number of bytes to extract from src.

0 <= count <= src.length-offset

.

---

#### BinaryRefAddr

public BinaryRefAddr​(

String

addrType,
byte[] src,
int offset,
int count)

Constructs a new instance of BinaryRefAddr using its address type and
a region of a byte array for contents.

Method Detail

- getContent

```java
public
Object
getContent()
```

Retrieves the contents of this address as an Object.
The result is a byte array.
Changes to this array will affect this BinaryRefAddr's contents.
Programs are recommended against changing this array's contents
and to lock the buffer if they need to change it.

**Specified by:** getContent

in class

RefAddr
**Returns:** The non-null buffer containing this address's contents.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this address. It is equal if
it contains the same address type and their contents are byte-wise
equivalent.

**Overrides:** equals

in class

RefAddr
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if the object is equal; false otherwise.
**See Also:** RefAddr.getContent()

,

RefAddr.getType()

- hashCode

```java
public int hashCode()
```

Computes the hash code of this address using its address type and contents.
Two BinaryRefAddrs have the same hash code if they have
the same address type and the same contents.
It is also possible for different BinaryRefAddrs to have
the same hash code.

**Overrides:** hashCode

in class

RefAddr
**Returns:** The hash code of this address as an int.
**See Also:** Object.hashCode()

- toString

```java
public
String
toString()
```

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
The first 32 bytes of contents are displayed (in hexadecimal).
If there are more than 32 bytes, "..." is used to indicate more.
This string is meant to used for debugging purposes and not
meant to be interpreted programmatically.

**Overrides:** toString

in class

RefAddr
**Returns:** The non-null string representation of this address.

---

#### Method Detail

getContent

```java
public
Object
getContent()
```

Retrieves the contents of this address as an Object.
The result is a byte array.
Changes to this array will affect this BinaryRefAddr's contents.
Programs are recommended against changing this array's contents
and to lock the buffer if they need to change it.

**Specified by:** getContent

in class

RefAddr
**Returns:** The non-null buffer containing this address's contents.

---

#### getContent

public

Object

getContent()

Retrieves the contents of this address as an Object.
The result is a byte array.
Changes to this array will affect this BinaryRefAddr's contents.
Programs are recommended against changing this array's contents
and to lock the buffer if they need to change it.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is equal to this address. It is equal if
it contains the same address type and their contents are byte-wise
equivalent.

**Overrides:** equals

in class

RefAddr
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if the object is equal; false otherwise.
**See Also:** RefAddr.getContent()

,

RefAddr.getType()

---

#### equals

public boolean equals​(

Object

obj)

Determines whether obj is equal to this address. It is equal if
it contains the same address type and their contents are byte-wise
equivalent.

hashCode

```java
public int hashCode()
```

Computes the hash code of this address using its address type and contents.
Two BinaryRefAddrs have the same hash code if they have
the same address type and the same contents.
It is also possible for different BinaryRefAddrs to have
the same hash code.

**Overrides:** hashCode

in class

RefAddr
**Returns:** The hash code of this address as an int.
**See Also:** Object.hashCode()

---

#### hashCode

public int hashCode()

Computes the hash code of this address using its address type and contents.
Two BinaryRefAddrs have the same hash code if they have
the same address type and the same contents.
It is also possible for different BinaryRefAddrs to have
the same hash code.

toString

```java
public
String
toString()
```

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
The first 32 bytes of contents are displayed (in hexadecimal).
If there are more than 32 bytes, "..." is used to indicate more.
This string is meant to used for debugging purposes and not
meant to be interpreted programmatically.

**Overrides:** toString

in class

RefAddr
**Returns:** The non-null string representation of this address.

---

#### toString

public

String

toString()

Generates the string representation of this address.
The string consists of the address's type and contents with labels.
The first 32 bytes of contents are displayed (in hexadecimal).
If there are more than 32 bytes, "..." is used to indicate more.
This string is meant to used for debugging purposes and not
meant to be interpreted programmatically.

---

