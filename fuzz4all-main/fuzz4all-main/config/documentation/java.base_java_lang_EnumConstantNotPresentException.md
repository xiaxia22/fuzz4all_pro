# Class EnumConstantNotPresentException

**Source:** `java.base\java\lang\EnumConstantNotPresentException.html`

### Class Description

```java
public class
EnumConstantNotPresentException

extends
RuntimeException
```

Thrown when an application tries to access an enum constant by name
and the enum type contains no constant with the specified name.
This exception can be thrown by the

API used to read annotations
reflectively

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public EnumConstantNotPresentException​(
Class
<? extends
Enum
> enumType,

String
constantName)

Constructs an

EnumConstantNotPresentException

for the
specified constant.

**Parameters:**
- enumType

- the type of the missing enum constant
- constantName

- the name of the missing enum constant

---

### Method Details

#### public
Class
<? extends
Enum
> enumType()

Returns the type of the missing enum constant.

**Returns:**
- the type of the missing enum constant

---

#### public
String
constantName()

Returns the name of the missing enum constant.

**Returns:**
- the name of the missing enum constant

---

### Additional Sections

#### Class EnumConstantNotPresentException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.EnumConstantNotPresentException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.EnumConstantNotPresentException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.EnumConstantNotPresentException

java.lang.RuntimeException

- java.lang.EnumConstantNotPresentException

java.lang.EnumConstantNotPresentException

**All Implemented Interfaces:** Serializable

```java
public class
EnumConstantNotPresentException

extends
RuntimeException
```

Thrown when an application tries to access an enum constant by name
and the enum type contains no constant with the specified name.
This exception can be thrown by the

API used to read annotations
reflectively

.

**Since:** 1.5
**See Also:** AnnotatedElement

,

Serialized Form

public class

EnumConstantNotPresentException

extends

RuntimeException

Thrown when an application tries to access an enum constant by name
and the enum type contains no constant with the specified name.
This exception can be thrown by the

API used to read annotations
reflectively

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EnumConstantNotPresentException

​(

Class

<? extends

Enum

> enumType,

String

constantName)

Constructs an

EnumConstantNotPresentException

for the
specified constant.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

constantName

()

Returns the name of the missing enum constant.

Class

<? extends

Enum

>

enumType

()

Returns the type of the missing enum constant.

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

,

toString

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

EnumConstantNotPresentException

​(

Class

<? extends

Enum

> enumType,

String

constantName)

Constructs an

EnumConstantNotPresentException

for the
specified constant.

---

#### Constructor Summary

Constructs an

EnumConstantNotPresentException

for the
specified constant.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

constantName

()

Returns the name of the missing enum constant.

Class

<? extends

Enum

>

enumType

()

Returns the type of the missing enum constant.

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

,

toString

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

Returns the name of the missing enum constant.

Returns the type of the missing enum constant.

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

,

toString

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

- EnumConstantNotPresentException

```java
public EnumConstantNotPresentException​(
Class
<? extends
Enum
> enumType,

String
constantName)
```

Constructs an

EnumConstantNotPresentException

for the
specified constant.

**Parameters:** enumType

- the type of the missing enum constant
**Parameters:** constantName

- the name of the missing enum constant

============ METHOD DETAIL ==========

- Method Detail

- enumType

```java
public
Class
<? extends
Enum
> enumType()
```

Returns the type of the missing enum constant.

**Returns:** the type of the missing enum constant

- constantName

```java
public
String
constantName()
```

Returns the name of the missing enum constant.

**Returns:** the name of the missing enum constant

Constructor Detail

- EnumConstantNotPresentException

```java
public EnumConstantNotPresentException​(
Class
<? extends
Enum
> enumType,

String
constantName)
```

Constructs an

EnumConstantNotPresentException

for the
specified constant.

**Parameters:** enumType

- the type of the missing enum constant
**Parameters:** constantName

- the name of the missing enum constant

---

#### Constructor Detail

EnumConstantNotPresentException

```java
public EnumConstantNotPresentException​(
Class
<? extends
Enum
> enumType,

String
constantName)
```

Constructs an

EnumConstantNotPresentException

for the
specified constant.

**Parameters:** enumType

- the type of the missing enum constant
**Parameters:** constantName

- the name of the missing enum constant

---

#### EnumConstantNotPresentException

public EnumConstantNotPresentException​(

Class

<? extends

Enum

> enumType,

String

constantName)

Constructs an

EnumConstantNotPresentException

for the
specified constant.

Method Detail

- enumType

```java
public
Class
<? extends
Enum
> enumType()
```

Returns the type of the missing enum constant.

**Returns:** the type of the missing enum constant

- constantName

```java
public
String
constantName()
```

Returns the name of the missing enum constant.

**Returns:** the name of the missing enum constant

---

#### Method Detail

enumType

```java
public
Class
<? extends
Enum
> enumType()
```

Returns the type of the missing enum constant.

**Returns:** the type of the missing enum constant

---

#### enumType

public

Class

<? extends

Enum

> enumType()

Returns the type of the missing enum constant.

constantName

```java
public
String
constantName()
```

Returns the name of the missing enum constant.

**Returns:** the name of the missing enum constant

---

#### constantName

public

String

constantName()

Returns the name of the missing enum constant.

---

