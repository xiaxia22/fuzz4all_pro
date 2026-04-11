# Class Oid

**Source:** `java.security.jgss\org\ietf\jgss\Oid.html`

### Class Description

```java
public class
Oid

extends
Object
```

This class represents Universal Object Identifiers (Oids) and their
associated operations.

Oids are hierarchically globally-interpretable identifiers used
within the GSS-API framework to identify mechanisms and name formats.

The structure and encoding of Oids is defined in ISOIEC-8824 and
ISOIEC-8825. For example the Oid representation of Kerberos V5
mechanism is "1.2.840.113554.1.2.2"

The GSSName name class contains public static Oid objects
representing the standard name types defined in GSS-API.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public Oid​(
String
strOid)
throws
GSSException

Constructs an Oid object from a string representation of its
integer components.

**Parameters:**
- strOid

- the dot separated string representation of the oid.
For instance, "1.2.840.113554.1.2.2".

**Throws:**
- GSSException

- may be thrown when the string is incorrectly
formatted

---

#### public Oid​(
InputStream
derOid)
throws
GSSException

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its byte array counterpart.

**Parameters:**
- derOid

- stream containing the DER encoded oid

**Throws:**
- GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

---

#### public Oid​(byte[] data)
throws
GSSException

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its InputStream conterpart.

**Parameters:**
- data

- byte array containing the DER encoded oid

**Throws:**
- GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

---

### Method Details

#### public
String
toString()

Returns a string representation of the oid's integer components
in dot separated notation.

**Overrides:**
- toString

in class

Object

**Returns:**
- string representation in the following format: "1.2.3.4.5"

---

#### public boolean equals​(
Object
other)

Tests if two Oid objects represent the same Object identifier
value.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the Oid object that has to be compared to this one

**Returns:**
- true

if the two Oid objects represent the same
value,

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public byte[] getDER()
throws
GSSException

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

**Returns:**
- byte array containing the DER encoding of this oid object.

**Throws:**
- GSSException

- may be thrown when the oid can't be encoded

---

#### public boolean containedIn​(
Oid
[] oids)

A utility method to test if this Oid value is contained within the
supplied Oid array.

**Parameters:**
- oids

- the array of Oid's to search

**Returns:**
- true if the array contains this Oid value, false otherwise

---

#### public int hashCode()

Returns a hashcode value for this Oid.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashCode value

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class Oid

java.lang.Object

- org.ietf.jgss.Oid

org.ietf.jgss.Oid

```java
public class
Oid

extends
Object
```

This class represents Universal Object Identifiers (Oids) and their
associated operations.

Oids are hierarchically globally-interpretable identifiers used
within the GSS-API framework to identify mechanisms and name formats.

The structure and encoding of Oids is defined in ISOIEC-8824 and
ISOIEC-8825. For example the Oid representation of Kerberos V5
mechanism is "1.2.840.113554.1.2.2"

The GSSName name class contains public static Oid objects
representing the standard name types defined in GSS-API.

**Since:** 1.4

public class

Oid

extends

Object

This class represents Universal Object Identifiers (Oids) and their
associated operations.

Oids are hierarchically globally-interpretable identifiers used
within the GSS-API framework to identify mechanisms and name formats.

The structure and encoding of Oids is defined in ISOIEC-8824 and
ISOIEC-8825. For example the Oid representation of Kerberos V5
mechanism is "1.2.840.113554.1.2.2"

The GSSName name class contains public static Oid objects
representing the standard name types defined in GSS-API.

Oids are hierarchically globally-interpretable identifiers used
within the GSS-API framework to identify mechanisms and name formats.

The structure and encoding of Oids is defined in ISOIEC-8824 and
ISOIEC-8825. For example the Oid representation of Kerberos V5
mechanism is "1.2.840.113554.1.2.2"

The GSSName name class contains public static Oid objects
representing the standard name types defined in GSS-API.

The structure and encoding of Oids is defined in ISOIEC-8824 and
ISOIEC-8825. For example the Oid representation of Kerberos V5
mechanism is "1.2.840.113554.1.2.2"

The GSSName name class contains public static Oid objects
representing the standard name types defined in GSS-API.

The GSSName name class contains public static Oid objects
representing the standard name types defined in GSS-API.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Oid

​(byte[] data)

Creates an Oid object from its ASN.1 DER encoding.

Oid

​(

InputStream

derOid)

Creates an Oid object from its ASN.1 DER encoding.

Oid

​(

String

strOid)

Constructs an Oid object from a string representation of its
integer components.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

containedIn

​(

Oid

[] oids)

A utility method to test if this Oid value is contained within the
supplied Oid array.

boolean

equals

​(

Object

other)

Tests if two Oid objects represent the same Object identifier
value.

byte[]

getDER

()

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

int

hashCode

()

Returns a hashcode value for this Oid.

String

toString

()

Returns a string representation of the oid's integer components
in dot separated notation.

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

Oid

​(byte[] data)

Creates an Oid object from its ASN.1 DER encoding.

Oid

​(

InputStream

derOid)

Creates an Oid object from its ASN.1 DER encoding.

Oid

​(

String

strOid)

Constructs an Oid object from a string representation of its
integer components.

---

#### Constructor Summary

Creates an Oid object from its ASN.1 DER encoding.

Constructs an Oid object from a string representation of its
integer components.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

containedIn

​(

Oid

[] oids)

A utility method to test if this Oid value is contained within the
supplied Oid array.

boolean

equals

​(

Object

other)

Tests if two Oid objects represent the same Object identifier
value.

byte[]

getDER

()

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

int

hashCode

()

Returns a hashcode value for this Oid.

String

toString

()

Returns a string representation of the oid's integer components
in dot separated notation.

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

A utility method to test if this Oid value is contained within the
supplied Oid array.

Tests if two Oid objects represent the same Object identifier
value.

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

Returns a hashcode value for this Oid.

Returns a string representation of the oid's integer components
in dot separated notation.

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

- Oid

```java
public Oid​(
String
strOid)
throws
GSSException
```

Constructs an Oid object from a string representation of its
integer components.

**Parameters:** strOid

- the dot separated string representation of the oid.
For instance, "1.2.840.113554.1.2.2".
**Throws:** GSSException

- may be thrown when the string is incorrectly
formatted

- Oid

```java
public Oid​(
InputStream
derOid)
throws
GSSException
```

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its byte array counterpart.

**Parameters:** derOid

- stream containing the DER encoded oid
**Throws:** GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

- Oid

```java
public Oid​(byte[] data)
throws
GSSException
```

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its InputStream conterpart.

**Parameters:** data

- byte array containing the DER encoded oid
**Throws:** GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns a string representation of the oid's integer components
in dot separated notation.

**Overrides:** toString

in class

Object
**Returns:** string representation in the following format: "1.2.3.4.5"

- equals

```java
public boolean equals​(
Object
other)
```

Tests if two Oid objects represent the same Object identifier
value.

**Overrides:** equals

in class

Object
**Parameters:** other

- the Oid object that has to be compared to this one
**Returns:** true

if the two Oid objects represent the same
value,

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getDER

```java
public byte[] getDER()
throws
GSSException
```

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

**Returns:** byte array containing the DER encoding of this oid object.
**Throws:** GSSException

- may be thrown when the oid can't be encoded

- containedIn

```java
public boolean containedIn​(
Oid
[] oids)
```

A utility method to test if this Oid value is contained within the
supplied Oid array.

**Parameters:** oids

- the array of Oid's to search
**Returns:** true if the array contains this Oid value, false otherwise

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this Oid.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- Oid

```java
public Oid​(
String
strOid)
throws
GSSException
```

Constructs an Oid object from a string representation of its
integer components.

**Parameters:** strOid

- the dot separated string representation of the oid.
For instance, "1.2.840.113554.1.2.2".
**Throws:** GSSException

- may be thrown when the string is incorrectly
formatted

- Oid

```java
public Oid​(
InputStream
derOid)
throws
GSSException
```

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its byte array counterpart.

**Parameters:** derOid

- stream containing the DER encoded oid
**Throws:** GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

- Oid

```java
public Oid​(byte[] data)
throws
GSSException
```

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its InputStream conterpart.

**Parameters:** data

- byte array containing the DER encoded oid
**Throws:** GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

---

#### Constructor Detail

Oid

```java
public Oid​(
String
strOid)
throws
GSSException
```

Constructs an Oid object from a string representation of its
integer components.

**Parameters:** strOid

- the dot separated string representation of the oid.
For instance, "1.2.840.113554.1.2.2".
**Throws:** GSSException

- may be thrown when the string is incorrectly
formatted

---

#### Oid

public Oid​(

String

strOid)
throws

GSSException

Constructs an Oid object from a string representation of its
integer components.

Oid

```java
public Oid​(
InputStream
derOid)
throws
GSSException
```

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its byte array counterpart.

**Parameters:** derOid

- stream containing the DER encoded oid
**Throws:** GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

---

#### Oid

public Oid​(

InputStream

derOid)
throws

GSSException

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its byte array counterpart.

Oid

```java
public Oid​(byte[] data)
throws
GSSException
```

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its InputStream conterpart.

**Parameters:** data

- byte array containing the DER encoded oid
**Throws:** GSSException

- may be thrown when the DER encoding does not
follow the prescribed format.

---

#### Oid

public Oid​(byte[] data)
throws

GSSException

Creates an Oid object from its ASN.1 DER encoding. This refers to
the full encoding including tag and length. The structure and
encoding of Oids is defined in ISOIEC-8824 and ISOIEC-8825. This
method is identical in functionality to its InputStream conterpart.

Method Detail

- toString

```java
public
String
toString()
```

Returns a string representation of the oid's integer components
in dot separated notation.

**Overrides:** toString

in class

Object
**Returns:** string representation in the following format: "1.2.3.4.5"

- equals

```java
public boolean equals​(
Object
other)
```

Tests if two Oid objects represent the same Object identifier
value.

**Overrides:** equals

in class

Object
**Parameters:** other

- the Oid object that has to be compared to this one
**Returns:** true

if the two Oid objects represent the same
value,

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getDER

```java
public byte[] getDER()
throws
GSSException
```

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

**Returns:** byte array containing the DER encoding of this oid object.
**Throws:** GSSException

- may be thrown when the oid can't be encoded

- containedIn

```java
public boolean containedIn​(
Oid
[] oids)
```

A utility method to test if this Oid value is contained within the
supplied Oid array.

**Parameters:** oids

- the array of Oid's to search
**Returns:** true if the array contains this Oid value, false otherwise

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this Oid.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns a string representation of the oid's integer components
in dot separated notation.

**Overrides:** toString

in class

Object
**Returns:** string representation in the following format: "1.2.3.4.5"

---

#### toString

public

String

toString()

Returns a string representation of the oid's integer components
in dot separated notation.

equals

```java
public boolean equals​(
Object
other)
```

Tests if two Oid objects represent the same Object identifier
value.

**Overrides:** equals

in class

Object
**Parameters:** other

- the Oid object that has to be compared to this one
**Returns:** true

if the two Oid objects represent the same
value,

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Tests if two Oid objects represent the same Object identifier
value.

getDER

```java
public byte[] getDER()
throws
GSSException
```

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

**Returns:** byte array containing the DER encoding of this oid object.
**Throws:** GSSException

- may be thrown when the oid can't be encoded

---

#### getDER

public byte[] getDER()
throws

GSSException

Returns the full ASN.1 DER encoding for this oid object, which
includes the tag and length.

containedIn

```java
public boolean containedIn​(
Oid
[] oids)
```

A utility method to test if this Oid value is contained within the
supplied Oid array.

**Parameters:** oids

- the array of Oid's to search
**Returns:** true if the array contains this Oid value, false otherwise

---

#### containedIn

public boolean containedIn​(

Oid

[] oids)

A utility method to test if this Oid value is contained within the
supplied Oid array.

hashCode

```java
public int hashCode()
```

Returns a hashcode value for this Oid.

**Overrides:** hashCode

in class

Object
**Returns:** a hashCode value
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode value for this Oid.

---

