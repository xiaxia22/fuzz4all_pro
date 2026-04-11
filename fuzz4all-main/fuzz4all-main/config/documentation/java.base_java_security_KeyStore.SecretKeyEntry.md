# Class KeyStore.SecretKeyEntry

**Source:** `java.base\java\security\KeyStore.SecretKeyEntry.html`

### Class Description

```java
public static final class
KeyStore.SecretKeyEntry

extends
Object

implements
KeyStore.Entry
```

A

KeyStore

entry that holds a

SecretKey

.

**All Implemented Interfaces:** KeyStore.Entry

---

### Field Details

*No entries found.*

### Constructor Details

#### public SecretKeyEntry​(
SecretKey
secretKey)

Constructs a

SecretKeyEntry

with a

SecretKey

.

**Parameters:**
- secretKey

- the

SecretKey

**Throws:**
- NullPointerException

- if

secretKey

is

null

---

#### public SecretKeyEntry​(
SecretKey
secretKey,

Set
<
KeyStore.Entry.Attribute
> attributes)

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

SecretKeyEntry

object.

**Parameters:**
- secretKey

- the

SecretKey
- attributes

- the attributes

**Throws:**
- NullPointerException

- if

secretKey

or

attributes

is

null

**Since:**
- 1.8

---

### Method Details

#### public
SecretKey
getSecretKey()

Gets the

SecretKey

from this entry.

**Returns:**
- the

SecretKey

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

Returns a string representation of this SecretKeyEntry.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this SecretKeyEntry.

---

### Additional Sections

#### Class KeyStore.SecretKeyEntry

java.lang.Object

- java.security.KeyStore.SecretKeyEntry

java.security.KeyStore.SecretKeyEntry

**All Implemented Interfaces:** KeyStore.Entry

**Enclosing class:** KeyStore

```java
public static final class
KeyStore.SecretKeyEntry

extends
Object

implements
KeyStore.Entry
```

A

KeyStore

entry that holds a

SecretKey

.

**Since:** 1.5

public static final class

KeyStore.SecretKeyEntry

extends

Object

implements

KeyStore.Entry

A

KeyStore

entry that holds a

SecretKey

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

SecretKeyEntry

​(

SecretKey

secretKey)

Constructs a

SecretKeyEntry

with a

SecretKey

.

SecretKeyEntry

​(

SecretKey

secretKey,

Set

<

KeyStore.Entry.Attribute

> attributes)

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

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

SecretKey

getSecretKey

()

Gets the

SecretKey

from this entry.

String

toString

()

Returns a string representation of this SecretKeyEntry.

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

SecretKeyEntry

​(

SecretKey

secretKey)

Constructs a

SecretKeyEntry

with a

SecretKey

.

SecretKeyEntry

​(

SecretKey

secretKey,

Set

<

KeyStore.Entry.Attribute

> attributes)

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

---

#### Constructor Summary

Constructs a

SecretKeyEntry

with a

SecretKey

.

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

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

SecretKey

getSecretKey

()

Gets the

SecretKey

from this entry.

String

toString

()

Returns a string representation of this SecretKeyEntry.

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

Gets the

SecretKey

from this entry.

Returns a string representation of this SecretKeyEntry.

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

- SecretKeyEntry

```java
public SecretKeyEntry​(
SecretKey
secretKey)
```

Constructs a

SecretKeyEntry

with a

SecretKey

.

**Parameters:** secretKey

- the

SecretKey
**Throws:** NullPointerException

- if

secretKey

is

null

- SecretKeyEntry

```java
public SecretKeyEntry​(
SecretKey
secretKey,

Set
<
KeyStore.Entry.Attribute
> attributes)
```

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

SecretKeyEntry

object.

**Parameters:** secretKey

- the

SecretKey
**Parameters:** attributes

- the attributes
**Throws:** NullPointerException

- if

secretKey

or

attributes

is

null
**Since:** 1.8

============ METHOD DETAIL ==========

- Method Detail

- getSecretKey

```java
public
SecretKey
getSecretKey()
```

Gets the

SecretKey

from this entry.

**Returns:** the

SecretKey

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

Returns a string representation of this SecretKeyEntry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this SecretKeyEntry.

Constructor Detail

- SecretKeyEntry

```java
public SecretKeyEntry​(
SecretKey
secretKey)
```

Constructs a

SecretKeyEntry

with a

SecretKey

.

**Parameters:** secretKey

- the

SecretKey
**Throws:** NullPointerException

- if

secretKey

is

null

- SecretKeyEntry

```java
public SecretKeyEntry​(
SecretKey
secretKey,

Set
<
KeyStore.Entry.Attribute
> attributes)
```

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

SecretKeyEntry

object.

**Parameters:** secretKey

- the

SecretKey
**Parameters:** attributes

- the attributes
**Throws:** NullPointerException

- if

secretKey

or

attributes

is

null
**Since:** 1.8

---

#### Constructor Detail

SecretKeyEntry

```java
public SecretKeyEntry​(
SecretKey
secretKey)
```

Constructs a

SecretKeyEntry

with a

SecretKey

.

**Parameters:** secretKey

- the

SecretKey
**Throws:** NullPointerException

- if

secretKey

is

null

---

#### SecretKeyEntry

public SecretKeyEntry​(

SecretKey

secretKey)

Constructs a

SecretKeyEntry

with a

SecretKey

.

SecretKeyEntry

```java
public SecretKeyEntry​(
SecretKey
secretKey,

Set
<
KeyStore.Entry.Attribute
> attributes)
```

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

SecretKeyEntry

object.

**Parameters:** secretKey

- the

SecretKey
**Parameters:** attributes

- the attributes
**Throws:** NullPointerException

- if

secretKey

or

attributes

is

null
**Since:** 1.8

---

#### SecretKeyEntry

public SecretKeyEntry​(

SecretKey

secretKey,

Set

<

KeyStore.Entry.Attribute

> attributes)

Constructs a

SecretKeyEntry

with a

SecretKey

and
associated entry attributes.

The specified

attributes

is cloned before it is stored
in the new

SecretKeyEntry

object.

The specified

attributes

is cloned before it is stored
in the new

SecretKeyEntry

object.

Method Detail

- getSecretKey

```java
public
SecretKey
getSecretKey()
```

Gets the

SecretKey

from this entry.

**Returns:** the

SecretKey

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

Returns a string representation of this SecretKeyEntry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this SecretKeyEntry.

---

#### Method Detail

getSecretKey

```java
public
SecretKey
getSecretKey()
```

Gets the

SecretKey

from this entry.

**Returns:** the

SecretKey

from this entry

---

#### getSecretKey

public

SecretKey

getSecretKey()

Gets the

SecretKey

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

Returns a string representation of this SecretKeyEntry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this SecretKeyEntry.

---

#### toString

public

String

toString()

Returns a string representation of this SecretKeyEntry.

---

