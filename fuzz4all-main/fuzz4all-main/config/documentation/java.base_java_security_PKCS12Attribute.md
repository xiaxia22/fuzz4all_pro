# Class PKCS12Attribute

**Source:** `java.base\java\security\PKCS12Attribute.html`

### Class Description

```java
public final class
PKCS12Attribute

extends
Object

implements
KeyStore.Entry.Attribute
```

An attribute associated with a PKCS12 keystore entry.
The attribute name is an ASN.1 Object Identifier and the attribute
value is a set of ASN.1 types.

**All Implemented Interfaces:** KeyStore.Entry.Attribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public PKCS12Attribute​(
String
name,

String
value)

Constructs a PKCS12 attribute from its name and value.
The name is an ASN.1 Object Identifier represented as a list of
dot-separated integers.
A string value is represented as the string itself.
A binary value is represented as a string of colon-separated
pairs of hexadecimal digits.
Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

A string value will be DER-encoded as an ASN.1 UTF8String and a
binary value will be DER-encoded as an ASN.1 Octet String.

**Parameters:**
- name

- the attribute's identifier
- value

- the attribute's value

**Throws:**
- NullPointerException

- if

name

or

value

is

null
- IllegalArgumentException

- if

name

or

value

is incorrectly formatted

---

#### public PKCS12Attribute​(byte[] encoded)

Constructs a PKCS12 attribute from its ASN.1 DER encoding.
The DER encoding is specified by the following ASN.1 definition:

```java
Attribute ::= SEQUENCE {
type AttributeType,
values SET OF AttributeValue
}
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY defined by type
```

**Parameters:**
- encoded

- the attribute's ASN.1 DER encoding. It is cloned
to prevent subsequent modificaion.

**Throws:**
- NullPointerException

- if

encoded

is

null
- IllegalArgumentException

- if

encoded

is
incorrectly formatted

---

### Method Details

#### public
String
getName()

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

**Specified by:**
- getName

in interface

KeyStore.Entry.Attribute

**Returns:**
- the attribute's identifier

---

#### public
String
getValue()

Returns the attribute's ASN.1 DER-encoded value as a string.
An ASN.1 DER-encoded value is returned in one of the following

String

formats:

- the DER encoding of a basic ASN.1 type that has a natural
string representation is returned as the string itself.
Such types are currently limited to BOOLEAN, INTEGER,
OBJECT IDENTIFIER, UTCTime, GeneralizedTime and the
following six ASN.1 string types: UTF8String,
PrintableString, T61String, IA5String, BMPString and
GeneralString.

the DER encoding of any other ASN.1 type is not decoded but
returned as a binary string of colon-separated pairs of
hexadecimal digits.

Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

**Specified by:**
- getValue

in interface

KeyStore.Entry.Attribute

**Returns:**
- the attribute value's string encoding

---

#### public byte[] getEncoded()

Returns the attribute's ASN.1 DER encoding.

**Returns:**
- a clone of the attribute's DER encoding

---

#### public boolean equals​(
Object
obj)

Compares this

PKCS12Attribute

and a specified object for
equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the comparison object

**Returns:**
- true if

obj

is a

PKCS12Attribute

and
their DER encodings are equal.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hashcode for this

PKCS12Attribute

.
The hash code is computed from its DER encoding.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this

PKCS12Attribute

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a name/value pair separated by an 'equals' symbol

---

### Additional Sections

#### Class PKCS12Attribute

java.lang.Object

- java.security.PKCS12Attribute

java.security.PKCS12Attribute

**All Implemented Interfaces:** KeyStore.Entry.Attribute

```java
public final class
PKCS12Attribute

extends
Object

implements
KeyStore.Entry.Attribute
```

An attribute associated with a PKCS12 keystore entry.
The attribute name is an ASN.1 Object Identifier and the attribute
value is a set of ASN.1 types.

**Since:** 1.8

public final class

PKCS12Attribute

extends

Object

implements

KeyStore.Entry.Attribute

An attribute associated with a PKCS12 keystore entry.
The attribute name is an ASN.1 Object Identifier and the attribute
value is a set of ASN.1 types.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PKCS12Attribute

​(byte[] encoded)

Constructs a PKCS12 attribute from its ASN.1 DER encoding.

PKCS12Attribute

​(

String

name,

String

value)

Constructs a PKCS12 attribute from its name and value.

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

Compares this

PKCS12Attribute

and a specified object for
equality.

byte[]

getEncoded

()

Returns the attribute's ASN.1 DER encoding.

String

getName

()

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

String

getValue

()

Returns the attribute's ASN.1 DER-encoded value as a string.

int

hashCode

()

Returns the hashcode for this

PKCS12Attribute

.

String

toString

()

Returns a string representation of this

PKCS12Attribute

.

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

PKCS12Attribute

​(byte[] encoded)

Constructs a PKCS12 attribute from its ASN.1 DER encoding.

PKCS12Attribute

​(

String

name,

String

value)

Constructs a PKCS12 attribute from its name and value.

---

#### Constructor Summary

Constructs a PKCS12 attribute from its ASN.1 DER encoding.

Constructs a PKCS12 attribute from its name and value.

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

Compares this

PKCS12Attribute

and a specified object for
equality.

byte[]

getEncoded

()

Returns the attribute's ASN.1 DER encoding.

String

getName

()

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

String

getValue

()

Returns the attribute's ASN.1 DER-encoded value as a string.

int

hashCode

()

Returns the hashcode for this

PKCS12Attribute

.

String

toString

()

Returns a string representation of this

PKCS12Attribute

.

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

Compares this

PKCS12Attribute

and a specified object for
equality.

Returns the attribute's ASN.1 DER encoding.

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

Returns the attribute's ASN.1 DER-encoded value as a string.

Returns the hashcode for this

PKCS12Attribute

.

Returns a string representation of this

PKCS12Attribute

.

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

- PKCS12Attribute

```java
public PKCS12Attribute​(
String
name,

String
value)
```

Constructs a PKCS12 attribute from its name and value.
The name is an ASN.1 Object Identifier represented as a list of
dot-separated integers.
A string value is represented as the string itself.
A binary value is represented as a string of colon-separated
pairs of hexadecimal digits.
Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

A string value will be DER-encoded as an ASN.1 UTF8String and a
binary value will be DER-encoded as an ASN.1 Octet String.

**Parameters:** name

- the attribute's identifier
**Parameters:** value

- the attribute's value
**Throws:** NullPointerException

- if

name

or

value

is

null
**Throws:** IllegalArgumentException

- if

name

or

value

is incorrectly formatted

- PKCS12Attribute

```java
public PKCS12Attribute​(byte[] encoded)
```

Constructs a PKCS12 attribute from its ASN.1 DER encoding.
The DER encoding is specified by the following ASN.1 definition:

```java
Attribute ::= SEQUENCE {
type AttributeType,
values SET OF AttributeValue
}
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY defined by type
```

**Parameters:** encoded

- the attribute's ASN.1 DER encoding. It is cloned
to prevent subsequent modificaion.
**Throws:** NullPointerException

- if

encoded

is

null
**Throws:** IllegalArgumentException

- if

encoded

is
incorrectly formatted

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

**Specified by:** getName

in interface

KeyStore.Entry.Attribute
**Returns:** the attribute's identifier

- getValue

```java
public
String
getValue()
```

Returns the attribute's ASN.1 DER-encoded value as a string.
An ASN.1 DER-encoded value is returned in one of the following

String

formats:

- the DER encoding of a basic ASN.1 type that has a natural
string representation is returned as the string itself.
Such types are currently limited to BOOLEAN, INTEGER,
OBJECT IDENTIFIER, UTCTime, GeneralizedTime and the
following six ASN.1 string types: UTF8String,
PrintableString, T61String, IA5String, BMPString and
GeneralString.

the DER encoding of any other ASN.1 type is not decoded but
returned as a binary string of colon-separated pairs of
hexadecimal digits.

Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

**Specified by:** getValue

in interface

KeyStore.Entry.Attribute
**Returns:** the attribute value's string encoding

- getEncoded

```java
public byte[] getEncoded()
```

Returns the attribute's ASN.1 DER encoding.

**Returns:** a clone of the attribute's DER encoding

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

PKCS12Attribute

and a specified object for
equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the comparison object
**Returns:** true if

obj

is a

PKCS12Attribute

and
their DER encodings are equal.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this

PKCS12Attribute

.
The hash code is computed from its DER encoding.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

PKCS12Attribute

.

**Overrides:** toString

in class

Object
**Returns:** a name/value pair separated by an 'equals' symbol

Constructor Detail

- PKCS12Attribute

```java
public PKCS12Attribute​(
String
name,

String
value)
```

Constructs a PKCS12 attribute from its name and value.
The name is an ASN.1 Object Identifier represented as a list of
dot-separated integers.
A string value is represented as the string itself.
A binary value is represented as a string of colon-separated
pairs of hexadecimal digits.
Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

A string value will be DER-encoded as an ASN.1 UTF8String and a
binary value will be DER-encoded as an ASN.1 Octet String.

**Parameters:** name

- the attribute's identifier
**Parameters:** value

- the attribute's value
**Throws:** NullPointerException

- if

name

or

value

is

null
**Throws:** IllegalArgumentException

- if

name

or

value

is incorrectly formatted

- PKCS12Attribute

```java
public PKCS12Attribute​(byte[] encoded)
```

Constructs a PKCS12 attribute from its ASN.1 DER encoding.
The DER encoding is specified by the following ASN.1 definition:

```java
Attribute ::= SEQUENCE {
type AttributeType,
values SET OF AttributeValue
}
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY defined by type
```

**Parameters:** encoded

- the attribute's ASN.1 DER encoding. It is cloned
to prevent subsequent modificaion.
**Throws:** NullPointerException

- if

encoded

is

null
**Throws:** IllegalArgumentException

- if

encoded

is
incorrectly formatted

---

#### Constructor Detail

PKCS12Attribute

```java
public PKCS12Attribute​(
String
name,

String
value)
```

Constructs a PKCS12 attribute from its name and value.
The name is an ASN.1 Object Identifier represented as a list of
dot-separated integers.
A string value is represented as the string itself.
A binary value is represented as a string of colon-separated
pairs of hexadecimal digits.
Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

A string value will be DER-encoded as an ASN.1 UTF8String and a
binary value will be DER-encoded as an ASN.1 Octet String.

**Parameters:** name

- the attribute's identifier
**Parameters:** value

- the attribute's value
**Throws:** NullPointerException

- if

name

or

value

is

null
**Throws:** IllegalArgumentException

- if

name

or

value

is incorrectly formatted

---

#### PKCS12Attribute

public PKCS12Attribute​(

String

name,

String

value)

Constructs a PKCS12 attribute from its name and value.
The name is an ASN.1 Object Identifier represented as a list of
dot-separated integers.
A string value is represented as the string itself.
A binary value is represented as a string of colon-separated
pairs of hexadecimal digits.
Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

A string value will be DER-encoded as an ASN.1 UTF8String and a
binary value will be DER-encoded as an ASN.1 Octet String.

A string value will be DER-encoded as an ASN.1 UTF8String and a
binary value will be DER-encoded as an ASN.1 Octet String.

PKCS12Attribute

```java
public PKCS12Attribute​(byte[] encoded)
```

Constructs a PKCS12 attribute from its ASN.1 DER encoding.
The DER encoding is specified by the following ASN.1 definition:

```java
Attribute ::= SEQUENCE {
type AttributeType,
values SET OF AttributeValue
}
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY defined by type
```

**Parameters:** encoded

- the attribute's ASN.1 DER encoding. It is cloned
to prevent subsequent modificaion.
**Throws:** NullPointerException

- if

encoded

is

null
**Throws:** IllegalArgumentException

- if

encoded

is
incorrectly formatted

---

#### PKCS12Attribute

public PKCS12Attribute​(byte[] encoded)

Constructs a PKCS12 attribute from its ASN.1 DER encoding.
The DER encoding is specified by the following ASN.1 definition:

```java
Attribute ::= SEQUENCE {
type AttributeType,
values SET OF AttributeValue
}
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY defined by type
```

Attribute ::= SEQUENCE {
type AttributeType,
values SET OF AttributeValue
}
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY defined by type

Method Detail

- getName

```java
public
String
getName()
```

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

**Specified by:** getName

in interface

KeyStore.Entry.Attribute
**Returns:** the attribute's identifier

- getValue

```java
public
String
getValue()
```

Returns the attribute's ASN.1 DER-encoded value as a string.
An ASN.1 DER-encoded value is returned in one of the following

String

formats:

- the DER encoding of a basic ASN.1 type that has a natural
string representation is returned as the string itself.
Such types are currently limited to BOOLEAN, INTEGER,
OBJECT IDENTIFIER, UTCTime, GeneralizedTime and the
following six ASN.1 string types: UTF8String,
PrintableString, T61String, IA5String, BMPString and
GeneralString.

the DER encoding of any other ASN.1 type is not decoded but
returned as a binary string of colon-separated pairs of
hexadecimal digits.

Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

**Specified by:** getValue

in interface

KeyStore.Entry.Attribute
**Returns:** the attribute value's string encoding

- getEncoded

```java
public byte[] getEncoded()
```

Returns the attribute's ASN.1 DER encoding.

**Returns:** a clone of the attribute's DER encoding

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

PKCS12Attribute

and a specified object for
equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the comparison object
**Returns:** true if

obj

is a

PKCS12Attribute

and
their DER encodings are equal.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this

PKCS12Attribute

.
The hash code is computed from its DER encoding.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

PKCS12Attribute

.

**Overrides:** toString

in class

Object
**Returns:** a name/value pair separated by an 'equals' symbol

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

**Specified by:** getName

in interface

KeyStore.Entry.Attribute
**Returns:** the attribute's identifier

---

#### getName

public

String

getName()

Returns the attribute's ASN.1 Object Identifier represented as a
list of dot-separated integers.

getValue

```java
public
String
getValue()
```

Returns the attribute's ASN.1 DER-encoded value as a string.
An ASN.1 DER-encoded value is returned in one of the following

String

formats:

- the DER encoding of a basic ASN.1 type that has a natural
string representation is returned as the string itself.
Such types are currently limited to BOOLEAN, INTEGER,
OBJECT IDENTIFIER, UTCTime, GeneralizedTime and the
following six ASN.1 string types: UTF8String,
PrintableString, T61String, IA5String, BMPString and
GeneralString.

the DER encoding of any other ASN.1 type is not decoded but
returned as a binary string of colon-separated pairs of
hexadecimal digits.

Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

**Specified by:** getValue

in interface

KeyStore.Entry.Attribute
**Returns:** the attribute value's string encoding

---

#### getValue

public

String

getValue()

Returns the attribute's ASN.1 DER-encoded value as a string.
An ASN.1 DER-encoded value is returned in one of the following

String

formats:

- the DER encoding of a basic ASN.1 type that has a natural
string representation is returned as the string itself.
Such types are currently limited to BOOLEAN, INTEGER,
OBJECT IDENTIFIER, UTCTime, GeneralizedTime and the
following six ASN.1 string types: UTF8String,
PrintableString, T61String, IA5String, BMPString and
GeneralString.

the DER encoding of any other ASN.1 type is not decoded but
returned as a binary string of colon-separated pairs of
hexadecimal digits.

Multi-valued attributes are represented as a comma-separated
list of values, enclosed in square brackets. See

Arrays.toString(java.lang.Object[])

.

the DER encoding of a basic ASN.1 type that has a natural
string representation is returned as the string itself.
Such types are currently limited to BOOLEAN, INTEGER,
OBJECT IDENTIFIER, UTCTime, GeneralizedTime and the
following six ASN.1 string types: UTF8String,
PrintableString, T61String, IA5String, BMPString and
GeneralString.

the DER encoding of any other ASN.1 type is not decoded but
returned as a binary string of colon-separated pairs of
hexadecimal digits.

getEncoded

```java
public byte[] getEncoded()
```

Returns the attribute's ASN.1 DER encoding.

**Returns:** a clone of the attribute's DER encoding

---

#### getEncoded

public byte[] getEncoded()

Returns the attribute's ASN.1 DER encoding.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this

PKCS12Attribute

and a specified object for
equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the comparison object
**Returns:** true if

obj

is a

PKCS12Attribute

and
their DER encodings are equal.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this

PKCS12Attribute

and a specified object for
equality.

hashCode

```java
public int hashCode()
```

Returns the hashcode for this

PKCS12Attribute

.
The hash code is computed from its DER encoding.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashcode for this

PKCS12Attribute

.
The hash code is computed from its DER encoding.

toString

```java
public
String
toString()
```

Returns a string representation of this

PKCS12Attribute

.

**Overrides:** toString

in class

Object
**Returns:** a name/value pair separated by an 'equals' symbol

---

#### toString

public

String

toString()

Returns a string representation of this

PKCS12Attribute

.

---

