# Interface KeyStore.Entry

**Source:** `java.base\java\security\KeyStore.Entry.html`

### Class Description

```java
public static interface
KeyStore.Entry
```

A marker interface for

KeyStore

entry types.

**All Known Implementing Classes:** KeyStore.PrivateKeyEntry

,

KeyStore.SecretKeyEntry

,

KeyStore.TrustedCertificateEntry

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default
Set
<
KeyStore.Entry.Attribute
> getAttributes()

Retrieves the attributes associated with an entry.

**Returns:**
- an unmodifiable

Set

of attributes, possibly empty

**Since:**
- 1.8

**Implementation Requirements:**
- The default implementation returns an empty

Set

.

---

### Additional Sections

#### Interface KeyStore.Entry

**All Known Implementing Classes:** KeyStore.PrivateKeyEntry

,

KeyStore.SecretKeyEntry

,

KeyStore.TrustedCertificateEntry

**Enclosing class:** KeyStore

```java
public static interface
KeyStore.Entry
```

A marker interface for

KeyStore

entry types.

**Since:** 1.5

public static interface

KeyStore.Entry

A marker interface for

KeyStore

entry types.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

KeyStore.Entry.Attribute

An attribute associated with a keystore entry.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

Set

<

KeyStore.Entry.Attribute

>

getAttributes

()

Retrieves the attributes associated with an entry.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

KeyStore.Entry.Attribute

An attribute associated with a keystore entry.

---

#### Nested Class Summary

An attribute associated with a keystore entry.

Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

Set

<

KeyStore.Entry.Attribute

>

getAttributes

()

Retrieves the attributes associated with an entry.

---

#### Method Summary

Retrieves the attributes associated with an entry.

============ METHOD DETAIL ==========

- Method Detail

- getAttributes

```java
default
Set
<
KeyStore.Entry.Attribute
> getAttributes()
```

Retrieves the attributes associated with an entry.

**Implementation Requirements:** The default implementation returns an empty

Set

.
**Returns:** an unmodifiable

Set

of attributes, possibly empty
**Since:** 1.8

Method Detail

- getAttributes

```java
default
Set
<
KeyStore.Entry.Attribute
> getAttributes()
```

Retrieves the attributes associated with an entry.

**Implementation Requirements:** The default implementation returns an empty

Set

.
**Returns:** an unmodifiable

Set

of attributes, possibly empty
**Since:** 1.8

---

#### Method Detail

getAttributes

```java
default
Set
<
KeyStore.Entry.Attribute
> getAttributes()
```

Retrieves the attributes associated with an entry.

**Implementation Requirements:** The default implementation returns an empty

Set

.
**Returns:** an unmodifiable

Set

of attributes, possibly empty
**Since:** 1.8

---

#### getAttributes

default

Set

<

KeyStore.Entry.Attribute

> getAttributes()

Retrieves the attributes associated with an entry.

---

