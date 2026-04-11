# Class KeyStoreBuilderParameters

**Source:** `java.base\javax\net\ssl\KeyStoreBuilderParameters.html`

### Class Description

```java
public class
KeyStoreBuilderParameters

extends
Object

implements
ManagerFactoryParameters
```

A parameters object for X509KeyManagers that encapsulates a List
of KeyStore.Builders.

**All Implemented Interfaces:** ManagerFactoryParameters

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyStoreBuilderParameters​(
KeyStore.Builder
builder)

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

**Parameters:**
- builder

- the Builder object

**Throws:**
- NullPointerException

- if builder is null

---

#### public KeyStoreBuilderParameters​(
List
<
KeyStore.Builder
> parameters)

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s. Note that the list
is cloned to protect against subsequent modification.

**Parameters:**
- parameters

- the List of Builder objects

**Throws:**
- NullPointerException

- if parameters is null
- IllegalArgumentException

- if parameters is an empty list

---

### Method Details

#### public
List
<
KeyStore.Builder
> getParameters()

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

**Returns:**
- the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

---

### Additional Sections

#### Class KeyStoreBuilderParameters

java.lang.Object

- javax.net.ssl.KeyStoreBuilderParameters

javax.net.ssl.KeyStoreBuilderParameters

**All Implemented Interfaces:** ManagerFactoryParameters

```java
public class
KeyStoreBuilderParameters

extends
Object

implements
ManagerFactoryParameters
```

A parameters object for X509KeyManagers that encapsulates a List
of KeyStore.Builders.

**Since:** 1.5
**See Also:** KeyStore.Builder

,

X509KeyManager

public class

KeyStoreBuilderParameters

extends

Object

implements

ManagerFactoryParameters

A parameters object for X509KeyManagers that encapsulates a List
of KeyStore.Builders.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyStoreBuilderParameters

​(

KeyStore.Builder

builder)

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

KeyStoreBuilderParameters

​(

List

<

KeyStore.Builder

> parameters)

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

KeyStore.Builder

>

getParameters

()

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

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

Constructor Summary

Constructors

Constructor

Description

KeyStoreBuilderParameters

​(

KeyStore.Builder

builder)

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

KeyStoreBuilderParameters

​(

List

<

KeyStore.Builder

> parameters)

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s.

---

#### Constructor Summary

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

KeyStore.Builder

>

getParameters

()

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

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

---

#### Method Summary

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- KeyStoreBuilderParameters

```java
public KeyStoreBuilderParameters​(
KeyStore.Builder
builder)
```

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

**Parameters:** builder

- the Builder object
**Throws:** NullPointerException

- if builder is null

- KeyStoreBuilderParameters

```java
public KeyStoreBuilderParameters​(
List
<
KeyStore.Builder
> parameters)
```

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s. Note that the list
is cloned to protect against subsequent modification.

**Parameters:** parameters

- the List of Builder objects
**Throws:** NullPointerException

- if parameters is null
**Throws:** IllegalArgumentException

- if parameters is an empty list

============ METHOD DETAIL ==========

- Method Detail

- getParameters

```java
public
List
<
KeyStore.Builder
> getParameters()
```

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

**Returns:** the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

Constructor Detail

- KeyStoreBuilderParameters

```java
public KeyStoreBuilderParameters​(
KeyStore.Builder
builder)
```

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

**Parameters:** builder

- the Builder object
**Throws:** NullPointerException

- if builder is null

- KeyStoreBuilderParameters

```java
public KeyStoreBuilderParameters​(
List
<
KeyStore.Builder
> parameters)
```

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s. Note that the list
is cloned to protect against subsequent modification.

**Parameters:** parameters

- the List of Builder objects
**Throws:** NullPointerException

- if parameters is null
**Throws:** IllegalArgumentException

- if parameters is an empty list

---

#### Constructor Detail

KeyStoreBuilderParameters

```java
public KeyStoreBuilderParameters​(
KeyStore.Builder
builder)
```

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

**Parameters:** builder

- the Builder object
**Throws:** NullPointerException

- if builder is null

---

#### KeyStoreBuilderParameters

public KeyStoreBuilderParameters​(

KeyStore.Builder

builder)

Construct new KeyStoreBuilderParameters from the specified

KeyStore.Builder

.

KeyStoreBuilderParameters

```java
public KeyStoreBuilderParameters​(
List
<
KeyStore.Builder
> parameters)
```

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s. Note that the list
is cloned to protect against subsequent modification.

**Parameters:** parameters

- the List of Builder objects
**Throws:** NullPointerException

- if parameters is null
**Throws:** IllegalArgumentException

- if parameters is an empty list

---

#### KeyStoreBuilderParameters

public KeyStoreBuilderParameters​(

List

<

KeyStore.Builder

> parameters)

Construct new KeyStoreBuilderParameters from a List
of

KeyStore.Builder

s. Note that the list
is cloned to protect against subsequent modification.

Method Detail

- getParameters

```java
public
List
<
KeyStore.Builder
> getParameters()
```

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

**Returns:** the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

---

#### Method Detail

getParameters

```java
public
List
<
KeyStore.Builder
> getParameters()
```

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

**Returns:** the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

---

#### getParameters

public

List

<

KeyStore.Builder

> getParameters()

Return the unmodifiable List of the

KeyStore.Builder

s
encapsulated by this object.

---

