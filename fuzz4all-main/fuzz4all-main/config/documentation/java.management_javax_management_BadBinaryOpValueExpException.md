# Class BadBinaryOpValueExpException

**Source:** `java.management\javax\management\BadBinaryOpValueExpException.html`

### Class Description

```java
public class
BadBinaryOpValueExpException

extends
Exception
```

Thrown when an invalid expression is passed to a method for
constructing a query. This exception is used internally by JMX
during the evaluation of a query. User code does not usually see
it.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public BadBinaryOpValueExpException​(
ValueExp
exp)

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

**Parameters:**
- exp

- the expression whose value was inappropriate.

---

### Method Details

#### public
ValueExp
getExp()

Returns the

ValueExp

that originated the exception.

**Returns:**
- the problematic

ValueExp

.

---

#### public
String
toString()

Returns the string representing the object.

**Overrides:**
- toString

in class

Throwable

**Returns:**
- a string representation of this throwable.

---

### Additional Sections

#### Class BadBinaryOpValueExpException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.management.BadBinaryOpValueExpException

java.lang.Throwable

- java.lang.Exception
- - javax.management.BadBinaryOpValueExpException

java.lang.Exception

- javax.management.BadBinaryOpValueExpException

javax.management.BadBinaryOpValueExpException

**All Implemented Interfaces:** Serializable

```java
public class
BadBinaryOpValueExpException

extends
Exception
```

Thrown when an invalid expression is passed to a method for
constructing a query. This exception is used internally by JMX
during the evaluation of a query. User code does not usually see
it.

**Since:** 1.5
**See Also:** Serialized Form

public class

BadBinaryOpValueExpException

extends

Exception

Thrown when an invalid expression is passed to a method for
constructing a query. This exception is used internally by JMX
during the evaluation of a query. User code does not usually see
it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BadBinaryOpValueExpException

​(

ValueExp

exp)

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ValueExp

getExp

()

Returns the

ValueExp

that originated the exception.

String

toString

()

Returns the string representing the object.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Constructor Summary

Constructors

Constructor

Description

BadBinaryOpValueExpException

​(

ValueExp

exp)

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

---

#### Constructor Summary

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ValueExp

getExp

()

Returns the

ValueExp

that originated the exception.

String

toString

()

Returns the string representing the object.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Returns the

ValueExp

that originated the exception.

Returns the string representing the object.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

---

#### Methods declared in class java.lang. Throwable

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

- BadBinaryOpValueExpException

```java
public BadBinaryOpValueExpException​(
ValueExp
exp)
```

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

**Parameters:** exp

- the expression whose value was inappropriate.

============ METHOD DETAIL ==========

- Method Detail

- getExp

```java
public
ValueExp
getExp()
```

Returns the

ValueExp

that originated the exception.

**Returns:** the problematic

ValueExp

.

- toString

```java
public
String
toString()
```

Returns the string representing the object.

**Overrides:** toString

in class

Throwable
**Returns:** a string representation of this throwable.

Constructor Detail

- BadBinaryOpValueExpException

```java
public BadBinaryOpValueExpException​(
ValueExp
exp)
```

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

**Parameters:** exp

- the expression whose value was inappropriate.

---

#### Constructor Detail

BadBinaryOpValueExpException

```java
public BadBinaryOpValueExpException​(
ValueExp
exp)
```

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

**Parameters:** exp

- the expression whose value was inappropriate.

---

#### BadBinaryOpValueExpException

public BadBinaryOpValueExpException​(

ValueExp

exp)

Constructs a

BadBinaryOpValueExpException

with the specified

ValueExp

.

Method Detail

- getExp

```java
public
ValueExp
getExp()
```

Returns the

ValueExp

that originated the exception.

**Returns:** the problematic

ValueExp

.

- toString

```java
public
String
toString()
```

Returns the string representing the object.

**Overrides:** toString

in class

Throwable
**Returns:** a string representation of this throwable.

---

#### Method Detail

getExp

```java
public
ValueExp
getExp()
```

Returns the

ValueExp

that originated the exception.

**Returns:** the problematic

ValueExp

.

---

#### getExp

public

ValueExp

getExp()

Returns the

ValueExp

that originated the exception.

toString

```java
public
String
toString()
```

Returns the string representing the object.

**Overrides:** toString

in class

Throwable
**Returns:** a string representation of this throwable.

---

#### toString

public

String

toString()

Returns the string representing the object.

---

