# Class ResponseAPDU

**Source:** `java.smartcardio\javax\smartcardio\ResponseAPDU.html`

### Class Description

```java
public final class
ResponseAPDU

extends
Object

implements
Serializable
```

A response APDU as defined in ISO/IEC 7816-4. It consists of a conditional
body and a two byte trailer.
This class does not attempt to verify that the APDU encodes a semantically
valid response.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ResponseAPDU​(byte[] apdu)

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

Note that the byte array is cloned to protect against subsequent
modification.

**Parameters:**
- apdu

- the complete response APDU

**Throws:**
- NullPointerException

- if apdu is null
- IllegalArgumentException

- if apdu.length is less than 2

---

### Method Details

#### public int getNr()

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body. This call is equivalent to

getData().length

.

**Returns:**
- the number of data bytes in the response body or 0 if this APDU
has no body.

---

#### public byte[] getData()

Returns a copy of the data bytes in the response body. If this APDU as
no body, this method returns a byte array with a length of zero.

**Returns:**
- a copy of the data bytes in the response body or the empty
byte array if this APDU has no body.

---

#### public int getSW1()

Returns the value of the status byte SW1 as a value between 0 and 255.

**Returns:**
- the value of the status byte SW1 as a value between 0 and 255.

---

#### public int getSW2()

Returns the value of the status byte SW2 as a value between 0 and 255.

**Returns:**
- the value of the status byte SW2 as a value between 0 and 255.

---

#### public int getSW()

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.
It is defined as

(getSW1() << 8) | getSW2()

**Returns:**
- the value of the status word SW.

---

#### public byte[] getBytes()

Returns a copy of the bytes in this APDU.

**Returns:**
- a copy of the bytes in this APDU.

---

#### public
String
toString()

Returns a string representation of this response APDU.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this response APDU.

---

#### public boolean equals​(
Object
obj)

Compares the specified object with this response APDU for equality.
Returns true if the given object is also a ResponseAPDU and its bytes are
identical to the bytes in this ResponseAPDU.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared for equality with this response APDU

**Returns:**
- true if the specified object is equal to this response APDU

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this response APDU.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this response APDU.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class ResponseAPDU

java.lang.Object

- javax.smartcardio.ResponseAPDU

javax.smartcardio.ResponseAPDU

**All Implemented Interfaces:** Serializable

```java
public final class
ResponseAPDU

extends
Object

implements
Serializable
```

A response APDU as defined in ISO/IEC 7816-4. It consists of a conditional
body and a two byte trailer.
This class does not attempt to verify that the APDU encodes a semantically
valid response.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

**Since:** 1.6
**See Also:** CommandAPDU

,

CardChannel.transmit

,

Serialized Form

public final class

ResponseAPDU

extends

Object

implements

Serializable

A response APDU as defined in ISO/IEC 7816-4. It consists of a conditional
body and a two byte trailer.
This class does not attempt to verify that the APDU encodes a semantically
valid response.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

Instances of this class are immutable. Where data is passed in or out
via byte arrays, defensive cloning is performed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ResponseAPDU

​(byte[] apdu)

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

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

Compares the specified object with this response APDU for equality.

byte[]

getBytes

()

Returns a copy of the bytes in this APDU.

byte[]

getData

()

Returns a copy of the data bytes in the response body.

int

getNr

()

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body.

int

getSW

()

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.

int

getSW1

()

Returns the value of the status byte SW1 as a value between 0 and 255.

int

getSW2

()

Returns the value of the status byte SW2 as a value between 0 and 255.

int

hashCode

()

Returns the hash code value for this response APDU.

String

toString

()

Returns a string representation of this response APDU.

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

Constructor Summary

Constructors

Constructor

Description

ResponseAPDU

​(byte[] apdu)

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

---

#### Constructor Summary

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

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

Compares the specified object with this response APDU for equality.

byte[]

getBytes

()

Returns a copy of the bytes in this APDU.

byte[]

getData

()

Returns a copy of the data bytes in the response body.

int

getNr

()

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body.

int

getSW

()

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.

int

getSW1

()

Returns the value of the status byte SW1 as a value between 0 and 255.

int

getSW2

()

Returns the value of the status byte SW2 as a value between 0 and 255.

int

hashCode

()

Returns the hash code value for this response APDU.

String

toString

()

Returns a string representation of this response APDU.

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

Compares the specified object with this response APDU for equality.

Returns a copy of the bytes in this APDU.

Returns a copy of the data bytes in the response body.

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body.

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.

Returns the value of the status byte SW1 as a value between 0 and 255.

Returns the value of the status byte SW2 as a value between 0 and 255.

Returns the hash code value for this response APDU.

Returns a string representation of this response APDU.

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

- ResponseAPDU

```java
public ResponseAPDU​(byte[] apdu)
```

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

Note that the byte array is cloned to protect against subsequent
modification.

**Parameters:** apdu

- the complete response APDU
**Throws:** NullPointerException

- if apdu is null
**Throws:** IllegalArgumentException

- if apdu.length is less than 2

============ METHOD DETAIL ==========

- Method Detail

- getNr

```java
public int getNr()
```

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body. This call is equivalent to

getData().length

.

**Returns:** the number of data bytes in the response body or 0 if this APDU
has no body.

- getData

```java
public byte[] getData()
```

Returns a copy of the data bytes in the response body. If this APDU as
no body, this method returns a byte array with a length of zero.

**Returns:** a copy of the data bytes in the response body or the empty
byte array if this APDU has no body.

- getSW1

```java
public int getSW1()
```

Returns the value of the status byte SW1 as a value between 0 and 255.

**Returns:** the value of the status byte SW1 as a value between 0 and 255.

- getSW2

```java
public int getSW2()
```

Returns the value of the status byte SW2 as a value between 0 and 255.

**Returns:** the value of the status byte SW2 as a value between 0 and 255.

- getSW

```java
public int getSW()
```

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.
It is defined as

(getSW1() << 8) | getSW2()

**Returns:** the value of the status word SW.

- getBytes

```java
public byte[] getBytes()
```

Returns a copy of the bytes in this APDU.

**Returns:** a copy of the bytes in this APDU.

- toString

```java
public
String
toString()
```

Returns a string representation of this response APDU.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this response APDU.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this response APDU for equality.
Returns true if the given object is also a ResponseAPDU and its bytes are
identical to the bytes in this ResponseAPDU.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this response APDU
**Returns:** true if the specified object is equal to this response APDU
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this response APDU.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this response APDU.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- ResponseAPDU

```java
public ResponseAPDU​(byte[] apdu)
```

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

Note that the byte array is cloned to protect against subsequent
modification.

**Parameters:** apdu

- the complete response APDU
**Throws:** NullPointerException

- if apdu is null
**Throws:** IllegalArgumentException

- if apdu.length is less than 2

---

#### Constructor Detail

ResponseAPDU

```java
public ResponseAPDU​(byte[] apdu)
```

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

Note that the byte array is cloned to protect against subsequent
modification.

**Parameters:** apdu

- the complete response APDU
**Throws:** NullPointerException

- if apdu is null
**Throws:** IllegalArgumentException

- if apdu.length is less than 2

---

#### ResponseAPDU

public ResponseAPDU​(byte[] apdu)

Constructs a ResponseAPDU from a byte array containing the complete
APDU contents (conditional body and trailed).

Note that the byte array is cloned to protect against subsequent
modification.

Note that the byte array is cloned to protect against subsequent
modification.

Method Detail

- getNr

```java
public int getNr()
```

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body. This call is equivalent to

getData().length

.

**Returns:** the number of data bytes in the response body or 0 if this APDU
has no body.

- getData

```java
public byte[] getData()
```

Returns a copy of the data bytes in the response body. If this APDU as
no body, this method returns a byte array with a length of zero.

**Returns:** a copy of the data bytes in the response body or the empty
byte array if this APDU has no body.

- getSW1

```java
public int getSW1()
```

Returns the value of the status byte SW1 as a value between 0 and 255.

**Returns:** the value of the status byte SW1 as a value between 0 and 255.

- getSW2

```java
public int getSW2()
```

Returns the value of the status byte SW2 as a value between 0 and 255.

**Returns:** the value of the status byte SW2 as a value between 0 and 255.

- getSW

```java
public int getSW()
```

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.
It is defined as

(getSW1() << 8) | getSW2()

**Returns:** the value of the status word SW.

- getBytes

```java
public byte[] getBytes()
```

Returns a copy of the bytes in this APDU.

**Returns:** a copy of the bytes in this APDU.

- toString

```java
public
String
toString()
```

Returns a string representation of this response APDU.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this response APDU.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this response APDU for equality.
Returns true if the given object is also a ResponseAPDU and its bytes are
identical to the bytes in this ResponseAPDU.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this response APDU
**Returns:** true if the specified object is equal to this response APDU
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this response APDU.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this response APDU.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getNr

```java
public int getNr()
```

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body. This call is equivalent to

getData().length

.

**Returns:** the number of data bytes in the response body or 0 if this APDU
has no body.

---

#### getNr

public int getNr()

Returns the number of data bytes in the response body (Nr) or 0 if this
APDU has no body. This call is equivalent to

getData().length

.

getData

```java
public byte[] getData()
```

Returns a copy of the data bytes in the response body. If this APDU as
no body, this method returns a byte array with a length of zero.

**Returns:** a copy of the data bytes in the response body or the empty
byte array if this APDU has no body.

---

#### getData

public byte[] getData()

Returns a copy of the data bytes in the response body. If this APDU as
no body, this method returns a byte array with a length of zero.

getSW1

```java
public int getSW1()
```

Returns the value of the status byte SW1 as a value between 0 and 255.

**Returns:** the value of the status byte SW1 as a value between 0 and 255.

---

#### getSW1

public int getSW1()

Returns the value of the status byte SW1 as a value between 0 and 255.

getSW2

```java
public int getSW2()
```

Returns the value of the status byte SW2 as a value between 0 and 255.

**Returns:** the value of the status byte SW2 as a value between 0 and 255.

---

#### getSW2

public int getSW2()

Returns the value of the status byte SW2 as a value between 0 and 255.

getSW

```java
public int getSW()
```

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.
It is defined as

(getSW1() << 8) | getSW2()

**Returns:** the value of the status word SW.

---

#### getSW

public int getSW()

Returns the value of the status bytes SW1 and SW2 as a single
status word SW.
It is defined as

(getSW1() << 8) | getSW2()

getBytes

```java
public byte[] getBytes()
```

Returns a copy of the bytes in this APDU.

**Returns:** a copy of the bytes in this APDU.

---

#### getBytes

public byte[] getBytes()

Returns a copy of the bytes in this APDU.

toString

```java
public
String
toString()
```

Returns a string representation of this response APDU.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this response APDU.

---

#### toString

public

String

toString()

Returns a string representation of this response APDU.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this response APDU for equality.
Returns true if the given object is also a ResponseAPDU and its bytes are
identical to the bytes in this ResponseAPDU.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared for equality with this response APDU
**Returns:** true if the specified object is equal to this response APDU
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified object with this response APDU for equality.
Returns true if the given object is also a ResponseAPDU and its bytes are
identical to the bytes in this ResponseAPDU.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this response APDU.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this response APDU.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this response APDU.

---

