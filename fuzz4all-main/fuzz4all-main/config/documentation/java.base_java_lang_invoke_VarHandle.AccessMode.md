# Enum VarHandle.AccessMode

**Source:** `java.base\java\lang\invoke\VarHandle.AccessMode.html`

### Class Description

```java
public static enum
VarHandle.AccessMode

extends
Enum
<
VarHandle.AccessMode
>
```

The set of access modes that specify how a variable, referenced by a
VarHandle, is accessed.

**All Implemented Interfaces:** Serializable

,

Comparable

<

VarHandle.AccessMode

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
VarHandle.AccessMode
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VarHandle.AccessMode c : VarHandle.AccessMode.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
VarHandle.AccessMode
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public
String
methodName()

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

**Returns:**
- the signature-polymorphic method name

**See Also:**
- valueFromMethodName(java.lang.String)

---

#### public static
VarHandle.AccessMode
valueFromMethodName​(
String
methodName)

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

**Parameters:**
- methodName

- the signature-polymorphic method name

**Returns:**
- the

AccessMode

value

**Throws:**
- IllegalArgumentException

- if there is no

AccessMode

value associated with method name (indicating the method
name does not correspond to a

VarHandle

signature-polymorphic method name).

**See Also:**
- methodName()

---

### Additional Sections

#### Enum VarHandle.AccessMode

java.lang.Object

- java.lang.Enum

<

VarHandle.AccessMode

>
- - java.lang.invoke.VarHandle.AccessMode

java.lang.Enum

<

VarHandle.AccessMode

>

- java.lang.invoke.VarHandle.AccessMode

java.lang.invoke.VarHandle.AccessMode

**All Implemented Interfaces:** Serializable

,

Comparable

<

VarHandle.AccessMode

>

**Enclosing class:** VarHandle

```java
public static enum
VarHandle.AccessMode

extends
Enum
<
VarHandle.AccessMode
>
```

The set of access modes that specify how a variable, referenced by a
VarHandle, is accessed.

public static enum

VarHandle.AccessMode

extends

Enum

<

VarHandle.AccessMode

>

The set of access modes that specify how a variable, referenced by a
VarHandle, is accessed.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

COMPARE_AND_EXCHANGE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchange

COMPARE_AND_EXCHANGE_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeAcquire

COMPARE_AND_EXCHANGE_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeRelease

COMPARE_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndSet

GET

The access mode whose access is specified by the corresponding
method

VarHandle.get

GET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAcquire

GET_AND_ADD

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAdd

GET_AND_ADD_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddAcquire

GET_AND_ADD_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddRelease

GET_AND_BITWISE_AND

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAnd

GET_AND_BITWISE_AND_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndAcquire

GET_AND_BITWISE_AND_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndRelease

GET_AND_BITWISE_OR

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOr

GET_AND_BITWISE_OR_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrAcquire

GET_AND_BITWISE_OR_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrRelease

GET_AND_BITWISE_XOR

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXor

GET_AND_BITWISE_XOR_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorAcquire

GET_AND_BITWISE_XOR_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorRelease

GET_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSet

GET_AND_SET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetAcquire

GET_AND_SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetRelease

GET_OPAQUE

The access mode whose access is specified by the corresponding
method

VarHandle.getOpaque

GET_VOLATILE

The access mode whose access is specified by the corresponding
method

VarHandle.getVolatile

SET

The access mode whose access is specified by the corresponding
method

VarHandle.set

SET_OPAQUE

The access mode whose access is specified by the corresponding
method

VarHandle.setOpaque

SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.setRelease

SET_VOLATILE

The access mode whose access is specified by the corresponding
method

VarHandle.setVolatile

WEAK_COMPARE_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSet

WEAK_COMPARE_AND_SET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetAcquire

WEAK_COMPARE_AND_SET_PLAIN

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetPlain

WEAK_COMPARE_AND_SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetRelease

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

methodName

()

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

static

VarHandle.AccessMode

valueFromMethodName

​(

String

methodName)

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

static

VarHandle.AccessMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

VarHandle.AccessMode

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

COMPARE_AND_EXCHANGE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchange

COMPARE_AND_EXCHANGE_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeAcquire

COMPARE_AND_EXCHANGE_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeRelease

COMPARE_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndSet

GET

The access mode whose access is specified by the corresponding
method

VarHandle.get

GET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAcquire

GET_AND_ADD

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAdd

GET_AND_ADD_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddAcquire

GET_AND_ADD_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddRelease

GET_AND_BITWISE_AND

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAnd

GET_AND_BITWISE_AND_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndAcquire

GET_AND_BITWISE_AND_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndRelease

GET_AND_BITWISE_OR

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOr

GET_AND_BITWISE_OR_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrAcquire

GET_AND_BITWISE_OR_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrRelease

GET_AND_BITWISE_XOR

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXor

GET_AND_BITWISE_XOR_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorAcquire

GET_AND_BITWISE_XOR_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorRelease

GET_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSet

GET_AND_SET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetAcquire

GET_AND_SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetRelease

GET_OPAQUE

The access mode whose access is specified by the corresponding
method

VarHandle.getOpaque

GET_VOLATILE

The access mode whose access is specified by the corresponding
method

VarHandle.getVolatile

SET

The access mode whose access is specified by the corresponding
method

VarHandle.set

SET_OPAQUE

The access mode whose access is specified by the corresponding
method

VarHandle.setOpaque

SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.setRelease

SET_VOLATILE

The access mode whose access is specified by the corresponding
method

VarHandle.setVolatile

WEAK_COMPARE_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSet

WEAK_COMPARE_AND_SET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetAcquire

WEAK_COMPARE_AND_SET_PLAIN

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetPlain

WEAK_COMPARE_AND_SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetRelease

---

#### Enum Constant Summary

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchange

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeRelease

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndSet

The access mode whose access is specified by the corresponding
method

VarHandle.get

The access mode whose access is specified by the corresponding
method

VarHandle.getAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAdd

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddRelease

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAnd

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndRelease

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOr

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrRelease

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXor

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorRelease

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSet

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetRelease

The access mode whose access is specified by the corresponding
method

VarHandle.getOpaque

The access mode whose access is specified by the corresponding
method

VarHandle.getVolatile

The access mode whose access is specified by the corresponding
method

VarHandle.set

The access mode whose access is specified by the corresponding
method

VarHandle.setOpaque

The access mode whose access is specified by the corresponding
method

VarHandle.setRelease

The access mode whose access is specified by the corresponding
method

VarHandle.setVolatile

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSet

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetAcquire

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetPlain

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetRelease

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

methodName

()

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

static

VarHandle.AccessMode

valueFromMethodName

​(

String

methodName)

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

static

VarHandle.AccessMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

VarHandle.AccessMode

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- GET

```java
public static final
VarHandle.AccessMode
GET
```

The access mode whose access is specified by the corresponding
method

VarHandle.get

- SET

```java
public static final
VarHandle.AccessMode
SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.set

- GET_VOLATILE

```java
public static final
VarHandle.AccessMode
GET_VOLATILE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getVolatile

- SET_VOLATILE

```java
public static final
VarHandle.AccessMode
SET_VOLATILE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setVolatile

- GET_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAcquire

- SET_RELEASE

```java
public static final
VarHandle.AccessMode
SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setRelease

- GET_OPAQUE

```java
public static final
VarHandle.AccessMode
GET_OPAQUE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getOpaque

- SET_OPAQUE

```java
public static final
VarHandle.AccessMode
SET_OPAQUE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setOpaque

- COMPARE_AND_SET

```java
public static final
VarHandle.AccessMode
COMPARE_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndSet

- COMPARE_AND_EXCHANGE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchange

- COMPARE_AND_EXCHANGE_ACQUIRE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeAcquire

- COMPARE_AND_EXCHANGE_RELEASE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeRelease

- WEAK_COMPARE_AND_SET_PLAIN

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_PLAIN
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetPlain

- WEAK_COMPARE_AND_SET

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSet

- WEAK_COMPARE_AND_SET_ACQUIRE

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetAcquire

- WEAK_COMPARE_AND_SET_RELEASE

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetRelease

- GET_AND_SET

```java
public static final
VarHandle.AccessMode
GET_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSet

- GET_AND_SET_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_SET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetAcquire

- GET_AND_SET_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetRelease

- GET_AND_ADD

```java
public static final
VarHandle.AccessMode
GET_AND_ADD
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAdd

- GET_AND_ADD_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_ADD_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddAcquire

- GET_AND_ADD_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_ADD_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddRelease

- GET_AND_BITWISE_OR

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOr

- GET_AND_BITWISE_OR_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrRelease

- GET_AND_BITWISE_OR_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrAcquire

- GET_AND_BITWISE_AND

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAnd

- GET_AND_BITWISE_AND_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndRelease

- GET_AND_BITWISE_AND_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndAcquire

- GET_AND_BITWISE_XOR

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXor

- GET_AND_BITWISE_XOR_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorRelease

- GET_AND_BITWISE_XOR_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorAcquire

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
VarHandle.AccessMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VarHandle.AccessMode c : VarHandle.AccessMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
VarHandle.AccessMode
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- methodName

```java
public
String
methodName()
```

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

**Returns:** the signature-polymorphic method name
**See Also:** valueFromMethodName(java.lang.String)

- valueFromMethodName

```java
public static
VarHandle.AccessMode
valueFromMethodName​(
String
methodName)
```

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

**Parameters:** methodName

- the signature-polymorphic method name
**Returns:** the

AccessMode

value
**Throws:** IllegalArgumentException

- if there is no

AccessMode

value associated with method name (indicating the method
name does not correspond to a

VarHandle

signature-polymorphic method name).
**See Also:** methodName()

Enum Constant Detail

- GET

```java
public static final
VarHandle.AccessMode
GET
```

The access mode whose access is specified by the corresponding
method

VarHandle.get

- SET

```java
public static final
VarHandle.AccessMode
SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.set

- GET_VOLATILE

```java
public static final
VarHandle.AccessMode
GET_VOLATILE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getVolatile

- SET_VOLATILE

```java
public static final
VarHandle.AccessMode
SET_VOLATILE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setVolatile

- GET_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAcquire

- SET_RELEASE

```java
public static final
VarHandle.AccessMode
SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setRelease

- GET_OPAQUE

```java
public static final
VarHandle.AccessMode
GET_OPAQUE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getOpaque

- SET_OPAQUE

```java
public static final
VarHandle.AccessMode
SET_OPAQUE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setOpaque

- COMPARE_AND_SET

```java
public static final
VarHandle.AccessMode
COMPARE_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndSet

- COMPARE_AND_EXCHANGE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchange

- COMPARE_AND_EXCHANGE_ACQUIRE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeAcquire

- COMPARE_AND_EXCHANGE_RELEASE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeRelease

- WEAK_COMPARE_AND_SET_PLAIN

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_PLAIN
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetPlain

- WEAK_COMPARE_AND_SET

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSet

- WEAK_COMPARE_AND_SET_ACQUIRE

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetAcquire

- WEAK_COMPARE_AND_SET_RELEASE

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetRelease

- GET_AND_SET

```java
public static final
VarHandle.AccessMode
GET_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSet

- GET_AND_SET_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_SET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetAcquire

- GET_AND_SET_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetRelease

- GET_AND_ADD

```java
public static final
VarHandle.AccessMode
GET_AND_ADD
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAdd

- GET_AND_ADD_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_ADD_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddAcquire

- GET_AND_ADD_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_ADD_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddRelease

- GET_AND_BITWISE_OR

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOr

- GET_AND_BITWISE_OR_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrRelease

- GET_AND_BITWISE_OR_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrAcquire

- GET_AND_BITWISE_AND

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAnd

- GET_AND_BITWISE_AND_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndRelease

- GET_AND_BITWISE_AND_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndAcquire

- GET_AND_BITWISE_XOR

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXor

- GET_AND_BITWISE_XOR_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorRelease

- GET_AND_BITWISE_XOR_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorAcquire

---

#### Enum Constant Detail

GET

```java
public static final
VarHandle.AccessMode
GET
```

The access mode whose access is specified by the corresponding
method

VarHandle.get

---

#### GET

public static final

VarHandle.AccessMode

GET

The access mode whose access is specified by the corresponding
method

VarHandle.get

SET

```java
public static final
VarHandle.AccessMode
SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.set

---

#### SET

public static final

VarHandle.AccessMode

SET

The access mode whose access is specified by the corresponding
method

VarHandle.set

GET_VOLATILE

```java
public static final
VarHandle.AccessMode
GET_VOLATILE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getVolatile

---

#### GET_VOLATILE

public static final

VarHandle.AccessMode

GET_VOLATILE

The access mode whose access is specified by the corresponding
method

VarHandle.getVolatile

SET_VOLATILE

```java
public static final
VarHandle.AccessMode
SET_VOLATILE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setVolatile

---

#### SET_VOLATILE

public static final

VarHandle.AccessMode

SET_VOLATILE

The access mode whose access is specified by the corresponding
method

VarHandle.setVolatile

GET_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAcquire

---

#### GET_ACQUIRE

public static final

VarHandle.AccessMode

GET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAcquire

SET_RELEASE

```java
public static final
VarHandle.AccessMode
SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setRelease

---

#### SET_RELEASE

public static final

VarHandle.AccessMode

SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.setRelease

GET_OPAQUE

```java
public static final
VarHandle.AccessMode
GET_OPAQUE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getOpaque

---

#### GET_OPAQUE

public static final

VarHandle.AccessMode

GET_OPAQUE

The access mode whose access is specified by the corresponding
method

VarHandle.getOpaque

SET_OPAQUE

```java
public static final
VarHandle.AccessMode
SET_OPAQUE
```

The access mode whose access is specified by the corresponding
method

VarHandle.setOpaque

---

#### SET_OPAQUE

public static final

VarHandle.AccessMode

SET_OPAQUE

The access mode whose access is specified by the corresponding
method

VarHandle.setOpaque

COMPARE_AND_SET

```java
public static final
VarHandle.AccessMode
COMPARE_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndSet

---

#### COMPARE_AND_SET

public static final

VarHandle.AccessMode

COMPARE_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndSet

COMPARE_AND_EXCHANGE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchange

---

#### COMPARE_AND_EXCHANGE

public static final

VarHandle.AccessMode

COMPARE_AND_EXCHANGE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchange

COMPARE_AND_EXCHANGE_ACQUIRE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeAcquire

---

#### COMPARE_AND_EXCHANGE_ACQUIRE

public static final

VarHandle.AccessMode

COMPARE_AND_EXCHANGE_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeAcquire

COMPARE_AND_EXCHANGE_RELEASE

```java
public static final
VarHandle.AccessMode
COMPARE_AND_EXCHANGE_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeRelease

---

#### COMPARE_AND_EXCHANGE_RELEASE

public static final

VarHandle.AccessMode

COMPARE_AND_EXCHANGE_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.compareAndExchangeRelease

WEAK_COMPARE_AND_SET_PLAIN

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_PLAIN
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetPlain

---

#### WEAK_COMPARE_AND_SET_PLAIN

public static final

VarHandle.AccessMode

WEAK_COMPARE_AND_SET_PLAIN

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetPlain

WEAK_COMPARE_AND_SET

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSet

---

#### WEAK_COMPARE_AND_SET

public static final

VarHandle.AccessMode

WEAK_COMPARE_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSet

WEAK_COMPARE_AND_SET_ACQUIRE

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetAcquire

---

#### WEAK_COMPARE_AND_SET_ACQUIRE

public static final

VarHandle.AccessMode

WEAK_COMPARE_AND_SET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetAcquire

WEAK_COMPARE_AND_SET_RELEASE

```java
public static final
VarHandle.AccessMode
WEAK_COMPARE_AND_SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetRelease

---

#### WEAK_COMPARE_AND_SET_RELEASE

public static final

VarHandle.AccessMode

WEAK_COMPARE_AND_SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.weakCompareAndSetRelease

GET_AND_SET

```java
public static final
VarHandle.AccessMode
GET_AND_SET
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSet

---

#### GET_AND_SET

public static final

VarHandle.AccessMode

GET_AND_SET

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSet

GET_AND_SET_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_SET_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetAcquire

---

#### GET_AND_SET_ACQUIRE

public static final

VarHandle.AccessMode

GET_AND_SET_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetAcquire

GET_AND_SET_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_SET_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetRelease

---

#### GET_AND_SET_RELEASE

public static final

VarHandle.AccessMode

GET_AND_SET_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndSetRelease

GET_AND_ADD

```java
public static final
VarHandle.AccessMode
GET_AND_ADD
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAdd

---

#### GET_AND_ADD

public static final

VarHandle.AccessMode

GET_AND_ADD

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAdd

GET_AND_ADD_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_ADD_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddAcquire

---

#### GET_AND_ADD_ACQUIRE

public static final

VarHandle.AccessMode

GET_AND_ADD_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddAcquire

GET_AND_ADD_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_ADD_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddRelease

---

#### GET_AND_ADD_RELEASE

public static final

VarHandle.AccessMode

GET_AND_ADD_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndAddRelease

GET_AND_BITWISE_OR

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOr

---

#### GET_AND_BITWISE_OR

public static final

VarHandle.AccessMode

GET_AND_BITWISE_OR

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOr

GET_AND_BITWISE_OR_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrRelease

---

#### GET_AND_BITWISE_OR_RELEASE

public static final

VarHandle.AccessMode

GET_AND_BITWISE_OR_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrRelease

GET_AND_BITWISE_OR_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_OR_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrAcquire

---

#### GET_AND_BITWISE_OR_ACQUIRE

public static final

VarHandle.AccessMode

GET_AND_BITWISE_OR_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseOrAcquire

GET_AND_BITWISE_AND

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAnd

---

#### GET_AND_BITWISE_AND

public static final

VarHandle.AccessMode

GET_AND_BITWISE_AND

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAnd

GET_AND_BITWISE_AND_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndRelease

---

#### GET_AND_BITWISE_AND_RELEASE

public static final

VarHandle.AccessMode

GET_AND_BITWISE_AND_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndRelease

GET_AND_BITWISE_AND_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_AND_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndAcquire

---

#### GET_AND_BITWISE_AND_ACQUIRE

public static final

VarHandle.AccessMode

GET_AND_BITWISE_AND_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseAndAcquire

GET_AND_BITWISE_XOR

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXor

---

#### GET_AND_BITWISE_XOR

public static final

VarHandle.AccessMode

GET_AND_BITWISE_XOR

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXor

GET_AND_BITWISE_XOR_RELEASE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR_RELEASE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorRelease

---

#### GET_AND_BITWISE_XOR_RELEASE

public static final

VarHandle.AccessMode

GET_AND_BITWISE_XOR_RELEASE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorRelease

GET_AND_BITWISE_XOR_ACQUIRE

```java
public static final
VarHandle.AccessMode
GET_AND_BITWISE_XOR_ACQUIRE
```

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorAcquire

---

#### GET_AND_BITWISE_XOR_ACQUIRE

public static final

VarHandle.AccessMode

GET_AND_BITWISE_XOR_ACQUIRE

The access mode whose access is specified by the corresponding
method

VarHandle.getAndBitwiseXorAcquire

Method Detail

- values

```java
public static
VarHandle.AccessMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VarHandle.AccessMode c : VarHandle.AccessMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
VarHandle.AccessMode
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- methodName

```java
public
String
methodName()
```

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

**Returns:** the signature-polymorphic method name
**See Also:** valueFromMethodName(java.lang.String)

- valueFromMethodName

```java
public static
VarHandle.AccessMode
valueFromMethodName​(
String
methodName)
```

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

**Parameters:** methodName

- the signature-polymorphic method name
**Returns:** the

AccessMode

value
**Throws:** IllegalArgumentException

- if there is no

AccessMode

value associated with method name (indicating the method
name does not correspond to a

VarHandle

signature-polymorphic method name).
**See Also:** methodName()

---

#### Method Detail

values

```java
public static
VarHandle.AccessMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VarHandle.AccessMode c : VarHandle.AccessMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

VarHandle.AccessMode

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VarHandle.AccessMode c : VarHandle.AccessMode.values())
System.out.println(c);
```

for (VarHandle.AccessMode c : VarHandle.AccessMode.values())
System.out.println(c);

valueOf

```java
public static
VarHandle.AccessMode
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

VarHandle.AccessMode

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

methodName

```java
public
String
methodName()
```

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

**Returns:** the signature-polymorphic method name
**See Also:** valueFromMethodName(java.lang.String)

---

#### methodName

public

String

methodName()

Returns the

VarHandle

signature-polymorphic method name
associated with this

AccessMode

value.

valueFromMethodName

```java
public static
VarHandle.AccessMode
valueFromMethodName​(
String
methodName)
```

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

**Parameters:** methodName

- the signature-polymorphic method name
**Returns:** the

AccessMode

value
**Throws:** IllegalArgumentException

- if there is no

AccessMode

value associated with method name (indicating the method
name does not correspond to a

VarHandle

signature-polymorphic method name).
**See Also:** methodName()

---

#### valueFromMethodName

public static

VarHandle.AccessMode

valueFromMethodName​(

String

methodName)

Returns the

AccessMode

value associated with the specified

VarHandle

signature-polymorphic method name.

---

