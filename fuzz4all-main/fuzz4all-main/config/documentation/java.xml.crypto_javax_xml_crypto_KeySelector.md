# Class KeySelector

**Source:** `java.xml.crypto\javax\xml\crypto\KeySelector.html`

### Class Description

```java
public abstract class
KeySelector

extends
Object
```

A selector that finds and returns a key using the data contained in a

KeyInfo

object. An example of an implementation of
this class is one that searches a

KeyStore

for
trusted keys that match information contained in a

KeyInfo

.

Whether or not the returned key is trusted and the mechanisms
used to determine that is implementation-specific.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected KeySelector()

Default no-args constructor; intended for invocation by subclasses only.

---

### Method Details

#### public abstract
KeySelectorResult
select​(
KeyInfo
keyInfo,

KeySelector.Purpose
purpose,

AlgorithmMethod
method,

XMLCryptoContext
context)
throws
KeySelectorException

Attempts to find a key that satisfies the specified constraints.

**Parameters:**
- keyInfo

- a

KeyInfo

(may be

null

)
- purpose

- the key's purpose (

KeySelector.Purpose.SIGN

,

KeySelector.Purpose.VERIFY

,

KeySelector.Purpose.ENCRYPT

, or

KeySelector.Purpose.DECRYPT

)
- method

- the algorithm method that this key is to be used for.
Only keys that are compatible with the algorithm and meet the
constraints of the specified algorithm should be returned.
- context

- an

XMLCryptoContext

that may contain
useful information for finding an appropriate key. If this key
selector supports resolving

RetrievalMethod

types, the
context's

baseURI

and

dereferencer

parameters (if specified) should be used by the selector to
resolve and dereference the URI.

**Returns:**
- the result of the key selector

**Throws:**
- KeySelectorException

- if an exceptional condition occurs while
attempting to find a key. Note that an inability to find a key is not
considered an exception (

null

should be
returned in that case). However, an error condition (ex: network
communications failure) that prevented the

KeySelector

from finding a potential key should be considered an exception.
- ClassCastException

- if the data type of

method

is not supported by this key selector

---

#### public static
KeySelector
singletonKeySelector​(
Key
key)

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

**Parameters:**
- key

- the sole key to be stored in the key selector

**Returns:**
- a key selector that always selects the specified key

**Throws:**
- NullPointerException

- if

key

is

null

---

### Additional Sections

#### Class KeySelector

java.lang.Object

- javax.xml.crypto.KeySelector

javax.xml.crypto.KeySelector

```java
public abstract class
KeySelector

extends
Object
```

A selector that finds and returns a key using the data contained in a

KeyInfo

object. An example of an implementation of
this class is one that searches a

KeyStore

for
trusted keys that match information contained in a

KeyInfo

.

Whether or not the returned key is trusted and the mechanisms
used to determine that is implementation-specific.

**Since:** 1.6

public abstract class

KeySelector

extends

Object

A selector that finds and returns a key using the data contained in a

KeyInfo

object. An example of an implementation of
this class is one that searches a

KeyStore

for
trusted keys that match information contained in a

KeyInfo

.

Whether or not the returned key is trusted and the mechanisms
used to determine that is implementation-specific.

Whether or not the returned key is trusted and the mechanisms
used to determine that is implementation-specific.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

KeySelector.Purpose

The purpose of the key that is to be selected.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

KeySelector

()

Default no-args constructor; intended for invocation by subclasses only.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

KeySelectorResult

select

​(

KeyInfo

keyInfo,

KeySelector.Purpose

purpose,

AlgorithmMethod

method,

XMLCryptoContext

context)

Attempts to find a key that satisfies the specified constraints.

static

KeySelector

singletonKeySelector

​(

Key

key)

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

KeySelector.Purpose

The purpose of the key that is to be selected.

---

#### Nested Class Summary

The purpose of the key that is to be selected.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

KeySelector

()

Default no-args constructor; intended for invocation by subclasses only.

---

#### Constructor Summary

Default no-args constructor; intended for invocation by subclasses only.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

KeySelectorResult

select

​(

KeyInfo

keyInfo,

KeySelector.Purpose

purpose,

AlgorithmMethod

method,

XMLCryptoContext

context)

Attempts to find a key that satisfies the specified constraints.

static

KeySelector

singletonKeySelector

​(

Key

key)

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

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

Attempts to find a key that satisfies the specified constraints.

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

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

- KeySelector

```java
protected KeySelector()
```

Default no-args constructor; intended for invocation by subclasses only.

============ METHOD DETAIL ==========

- Method Detail

- select

```java
public abstract
KeySelectorResult
select​(
KeyInfo
keyInfo,

KeySelector.Purpose
purpose,

AlgorithmMethod
method,

XMLCryptoContext
context)
throws
KeySelectorException
```

Attempts to find a key that satisfies the specified constraints.

**Parameters:** keyInfo

- a

KeyInfo

(may be

null

)
**Parameters:** purpose

- the key's purpose (

KeySelector.Purpose.SIGN

,

KeySelector.Purpose.VERIFY

,

KeySelector.Purpose.ENCRYPT

, or

KeySelector.Purpose.DECRYPT

)
**Parameters:** method

- the algorithm method that this key is to be used for.
Only keys that are compatible with the algorithm and meet the
constraints of the specified algorithm should be returned.
**Parameters:** context

- an

XMLCryptoContext

that may contain
useful information for finding an appropriate key. If this key
selector supports resolving

RetrievalMethod

types, the
context's

baseURI

and

dereferencer

parameters (if specified) should be used by the selector to
resolve and dereference the URI.
**Returns:** the result of the key selector
**Throws:** KeySelectorException

- if an exceptional condition occurs while
attempting to find a key. Note that an inability to find a key is not
considered an exception (

null

should be
returned in that case). However, an error condition (ex: network
communications failure) that prevented the

KeySelector

from finding a potential key should be considered an exception.
**Throws:** ClassCastException

- if the data type of

method

is not supported by this key selector

- singletonKeySelector

```java
public static
KeySelector
singletonKeySelector​(
Key
key)
```

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

**Parameters:** key

- the sole key to be stored in the key selector
**Returns:** a key selector that always selects the specified key
**Throws:** NullPointerException

- if

key

is

null

Constructor Detail

- KeySelector

```java
protected KeySelector()
```

Default no-args constructor; intended for invocation by subclasses only.

---

#### Constructor Detail

KeySelector

```java
protected KeySelector()
```

Default no-args constructor; intended for invocation by subclasses only.

---

#### KeySelector

protected KeySelector()

Default no-args constructor; intended for invocation by subclasses only.

Method Detail

- select

```java
public abstract
KeySelectorResult
select​(
KeyInfo
keyInfo,

KeySelector.Purpose
purpose,

AlgorithmMethod
method,

XMLCryptoContext
context)
throws
KeySelectorException
```

Attempts to find a key that satisfies the specified constraints.

**Parameters:** keyInfo

- a

KeyInfo

(may be

null

)
**Parameters:** purpose

- the key's purpose (

KeySelector.Purpose.SIGN

,

KeySelector.Purpose.VERIFY

,

KeySelector.Purpose.ENCRYPT

, or

KeySelector.Purpose.DECRYPT

)
**Parameters:** method

- the algorithm method that this key is to be used for.
Only keys that are compatible with the algorithm and meet the
constraints of the specified algorithm should be returned.
**Parameters:** context

- an

XMLCryptoContext

that may contain
useful information for finding an appropriate key. If this key
selector supports resolving

RetrievalMethod

types, the
context's

baseURI

and

dereferencer

parameters (if specified) should be used by the selector to
resolve and dereference the URI.
**Returns:** the result of the key selector
**Throws:** KeySelectorException

- if an exceptional condition occurs while
attempting to find a key. Note that an inability to find a key is not
considered an exception (

null

should be
returned in that case). However, an error condition (ex: network
communications failure) that prevented the

KeySelector

from finding a potential key should be considered an exception.
**Throws:** ClassCastException

- if the data type of

method

is not supported by this key selector

- singletonKeySelector

```java
public static
KeySelector
singletonKeySelector​(
Key
key)
```

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

**Parameters:** key

- the sole key to be stored in the key selector
**Returns:** a key selector that always selects the specified key
**Throws:** NullPointerException

- if

key

is

null

---

#### Method Detail

select

```java
public abstract
KeySelectorResult
select​(
KeyInfo
keyInfo,

KeySelector.Purpose
purpose,

AlgorithmMethod
method,

XMLCryptoContext
context)
throws
KeySelectorException
```

Attempts to find a key that satisfies the specified constraints.

**Parameters:** keyInfo

- a

KeyInfo

(may be

null

)
**Parameters:** purpose

- the key's purpose (

KeySelector.Purpose.SIGN

,

KeySelector.Purpose.VERIFY

,

KeySelector.Purpose.ENCRYPT

, or

KeySelector.Purpose.DECRYPT

)
**Parameters:** method

- the algorithm method that this key is to be used for.
Only keys that are compatible with the algorithm and meet the
constraints of the specified algorithm should be returned.
**Parameters:** context

- an

XMLCryptoContext

that may contain
useful information for finding an appropriate key. If this key
selector supports resolving

RetrievalMethod

types, the
context's

baseURI

and

dereferencer

parameters (if specified) should be used by the selector to
resolve and dereference the URI.
**Returns:** the result of the key selector
**Throws:** KeySelectorException

- if an exceptional condition occurs while
attempting to find a key. Note that an inability to find a key is not
considered an exception (

null

should be
returned in that case). However, an error condition (ex: network
communications failure) that prevented the

KeySelector

from finding a potential key should be considered an exception.
**Throws:** ClassCastException

- if the data type of

method

is not supported by this key selector

---

#### select

public abstract

KeySelectorResult

select​(

KeyInfo

keyInfo,

KeySelector.Purpose

purpose,

AlgorithmMethod

method,

XMLCryptoContext

context)
throws

KeySelectorException

Attempts to find a key that satisfies the specified constraints.

singletonKeySelector

```java
public static
KeySelector
singletonKeySelector​(
Key
key)
```

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

**Parameters:** key

- the sole key to be stored in the key selector
**Returns:** a key selector that always selects the specified key
**Throws:** NullPointerException

- if

key

is

null

---

#### singletonKeySelector

public static

KeySelector

singletonKeySelector​(

Key

key)

Returns a

KeySelector

that always selects the specified
key, regardless of the

KeyInfo

passed to it.

---

