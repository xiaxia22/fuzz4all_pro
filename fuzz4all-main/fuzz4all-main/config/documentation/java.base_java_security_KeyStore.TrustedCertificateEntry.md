# Class KeyStore.TrustedCertificateEntry

**Source:** `java.base\java\security\KeyStore.TrustedCertificateEntry.html`

### Class Description

```java
public static final class
KeyStore.TrustedCertificateEntry

extends
Object

implements
KeyStore.Entry
```

A

KeyStore

entry that holds a trusted

Certificate

.

**All Implemented Interfaces:** KeyStore.Entry

---

### Field Details

*No entries found.*

### Constructor Details

#### public TrustedCertificateEntry​(
Certificate
trustedCert)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

**Parameters:**
- trustedCert

- the trusted

Certificate

**Throws:**
- NullPointerException

- if

trustedCert

is

null

---

#### public TrustedCertificateEntry​(
Certificate
trustedCert,

Set
<
KeyStore.Entry.Attribute
> attributes)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

TrustedCertificateEntry

object.

**Parameters:**
- trustedCert

- the trusted

Certificate
- attributes

- the attributes

**Throws:**
- NullPointerException

- if

trustedCert

or

attributes

is

null

**Since:**
- 1.8

---

### Method Details

#### public
Certificate
getTrustedCertificate()

Gets the trusted

Certficate

from this entry.

**Returns:**
- the trusted

Certificate

from this entry

---

#### public
Set
<
KeyStore.Entry.Attribute
> getAttributes()

Retrieves the attributes associated with an entry.

**Specified by:**
- getAttributes

in interface

KeyStore.Entry

**Returns:**
- an unmodifiable

Set

of attributes, possibly empty

**Since:**
- 1.8

---

#### public
String
toString()

Returns a string representation of this TrustedCertificateEntry.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this TrustedCertificateEntry.

---

### Additional Sections

#### Class KeyStore.TrustedCertificateEntry

java.lang.Object

- java.security.KeyStore.TrustedCertificateEntry

java.security.KeyStore.TrustedCertificateEntry

**All Implemented Interfaces:** KeyStore.Entry

**Enclosing class:** KeyStore

```java
public static final class
KeyStore.TrustedCertificateEntry

extends
Object

implements
KeyStore.Entry
```

A

KeyStore

entry that holds a trusted

Certificate

.

**Since:** 1.5

public static final class

KeyStore.TrustedCertificateEntry

extends

Object

implements

KeyStore.Entry

A

KeyStore

entry that holds a trusted

Certificate

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface java.security.

KeyStore.Entry

KeyStore.Entry.Attribute

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TrustedCertificateEntry

​(

Certificate

trustedCert)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

TrustedCertificateEntry

​(

Certificate

trustedCert,

Set

<

KeyStore.Entry.Attribute

> attributes)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Set

<

KeyStore.Entry.Attribute

>

getAttributes

()

Retrieves the attributes associated with an entry.

Certificate

getTrustedCertificate

()

Gets the trusted

Certficate

from this entry.

String

toString

()

Returns a string representation of this TrustedCertificateEntry.

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

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in interface java.security.

KeyStore.Entry

KeyStore.Entry.Attribute

---

#### Nested Class Summary

Nested classes/interfaces declared in interface java.security.

KeyStore.Entry

KeyStore.Entry.Attribute

---

#### Nested classes/interfaces declared in interface java.security. KeyStore.Entry

Constructor Summary

Constructors

Constructor

Description

TrustedCertificateEntry

​(

Certificate

trustedCert)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

TrustedCertificateEntry

​(

Certificate

trustedCert,

Set

<

KeyStore.Entry.Attribute

> attributes)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

---

#### Constructor Summary

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Set

<

KeyStore.Entry.Attribute

>

getAttributes

()

Retrieves the attributes associated with an entry.

Certificate

getTrustedCertificate

()

Gets the trusted

Certficate

from this entry.

String

toString

()

Returns a string representation of this TrustedCertificateEntry.

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

wait

,

wait

,

wait

---

#### Method Summary

Retrieves the attributes associated with an entry.

Gets the trusted

Certficate

from this entry.

Returns a string representation of this TrustedCertificateEntry.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TrustedCertificateEntry

```java
public TrustedCertificateEntry​(
Certificate
trustedCert)
```

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

**Parameters:** trustedCert

- the trusted

Certificate
**Throws:** NullPointerException

- if

trustedCert

is

null

- TrustedCertificateEntry

```java
public TrustedCertificateEntry​(
Certificate
trustedCert,

Set
<
KeyStore.Entry.Attribute
> attributes)
```

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

TrustedCertificateEntry

object.

**Parameters:** trustedCert

- the trusted

Certificate
**Parameters:** attributes

- the attributes
**Throws:** NullPointerException

- if

trustedCert

or

attributes

is

null
**Since:** 1.8

============ METHOD DETAIL ==========

- Method Detail

- getTrustedCertificate

```java
public
Certificate
getTrustedCertificate()
```

Gets the trusted

Certficate

from this entry.

**Returns:** the trusted

Certificate

from this entry

- getAttributes

```java
public
Set
<
KeyStore.Entry.Attribute
> getAttributes()
```

Retrieves the attributes associated with an entry.

**Specified by:** getAttributes

in interface

KeyStore.Entry
**Returns:** an unmodifiable

Set

of attributes, possibly empty
**Since:** 1.8

- toString

```java
public
String
toString()
```

Returns a string representation of this TrustedCertificateEntry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this TrustedCertificateEntry.

Constructor Detail

- TrustedCertificateEntry

```java
public TrustedCertificateEntry​(
Certificate
trustedCert)
```

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

**Parameters:** trustedCert

- the trusted

Certificate
**Throws:** NullPointerException

- if

trustedCert

is

null

- TrustedCertificateEntry

```java
public TrustedCertificateEntry​(
Certificate
trustedCert,

Set
<
KeyStore.Entry.Attribute
> attributes)
```

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

TrustedCertificateEntry

object.

**Parameters:** trustedCert

- the trusted

Certificate
**Parameters:** attributes

- the attributes
**Throws:** NullPointerException

- if

trustedCert

or

attributes

is

null
**Since:** 1.8

---

#### Constructor Detail

TrustedCertificateEntry

```java
public TrustedCertificateEntry​(
Certificate
trustedCert)
```

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

**Parameters:** trustedCert

- the trusted

Certificate
**Throws:** NullPointerException

- if

trustedCert

is

null

---

#### TrustedCertificateEntry

public TrustedCertificateEntry​(

Certificate

trustedCert)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

.

TrustedCertificateEntry

```java
public TrustedCertificateEntry​(
Certificate
trustedCert,

Set
<
KeyStore.Entry.Attribute
> attributes)
```

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

TrustedCertificateEntry

object.

**Parameters:** trustedCert

- the trusted

Certificate
**Parameters:** attributes

- the attributes
**Throws:** NullPointerException

- if

trustedCert

or

attributes

is

null
**Since:** 1.8

---

#### TrustedCertificateEntry

public TrustedCertificateEntry​(

Certificate

trustedCert,

Set

<

KeyStore.Entry.Attribute

> attributes)

Constructs a

TrustedCertificateEntry

with a
trusted

Certificate

and associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

TrustedCertificateEntry

object.

The specified

attributes

is cloned before it is stored
in the new

TrustedCertificateEntry

object.

Method Detail

- getTrustedCertificate

```java
public
Certificate
getTrustedCertificate()
```

Gets the trusted

Certficate

from this entry.

**Returns:** the trusted

Certificate

from this entry

- getAttributes

```java
public
Set
<
KeyStore.Entry.Attribute
> getAttributes()
```

Retrieves the attributes associated with an entry.

**Specified by:** getAttributes

in interface

KeyStore.Entry
**Returns:** an unmodifiable

Set

of attributes, possibly empty
**Since:** 1.8

- toString

```java
public
String
toString()
```

Returns a string representation of this TrustedCertificateEntry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this TrustedCertificateEntry.

---

#### Method Detail

getTrustedCertificate

```java
public
Certificate
getTrustedCertificate()
```

Gets the trusted

Certficate

from this entry.

**Returns:** the trusted

Certificate

from this entry

---

#### getTrustedCertificate

public

Certificate

getTrustedCertificate()

Gets the trusted

Certficate

from this entry.

getAttributes

```java
public
Set
<
KeyStore.Entry.Attribute
> getAttributes()
```

Retrieves the attributes associated with an entry.

**Specified by:** getAttributes

in interface

KeyStore.Entry
**Returns:** an unmodifiable

Set

of attributes, possibly empty
**Since:** 1.8

---

#### getAttributes

public

Set

<

KeyStore.Entry.Attribute

> getAttributes()

Retrieves the attributes associated with an entry.

toString

```java
public
String
toString()
```

Returns a string representation of this TrustedCertificateEntry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this TrustedCertificateEntry.

---

#### toString

public

String

toString()

Returns a string representation of this TrustedCertificateEntry.

---

