# Class IllegalConnectorArgumentsException

**Source:** `jdk.jdi\com\sun\jdi\connect\IllegalConnectorArgumentsException.html`

### Class Description

```java
public class
IllegalConnectorArgumentsException

extends
Exception
```

Thrown to indicate an invalid argument or
inconsistent passed to a

Connector

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IllegalConnectorArgumentsException​(
String
s,

String
name)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

**Parameters:**
- s

- the detailed message.
- name

- the name of the invalid or inconsistent argument.

---

#### public IllegalConnectorArgumentsException​(
String
s,

List
<
String
> names)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

**Parameters:**
- s

- the detailed message.
- names

- a

List

containing the names of the
invalid or inconsistent argument.

---

### Method Details

#### public
List
<
String
> argumentNames()

Return a

List

containing the names of the
invalid or inconsistent arguments.

**Returns:**
- a

List

of argument names.

---

### Additional Sections

#### Class IllegalConnectorArgumentsException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - com.sun.jdi.connect.IllegalConnectorArgumentsException

java.lang.Throwable

- java.lang.Exception
- - com.sun.jdi.connect.IllegalConnectorArgumentsException

java.lang.Exception

- com.sun.jdi.connect.IllegalConnectorArgumentsException

com.sun.jdi.connect.IllegalConnectorArgumentsException

**All Implemented Interfaces:** Serializable

```java
public class
IllegalConnectorArgumentsException

extends
Exception
```

Thrown to indicate an invalid argument or
inconsistent passed to a

Connector

.

**Since:** 1.3
**See Also:** Serialized Form

public class

IllegalConnectorArgumentsException

extends

Exception

Thrown to indicate an invalid argument or
inconsistent passed to a

Connector

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IllegalConnectorArgumentsException

​(

String

s,

String

name)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

IllegalConnectorArgumentsException

​(

String

s,

List

<

String

> names)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

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

String

>

argumentNames

()

Return a

List

containing the names of the
invalid or inconsistent arguments.

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

IllegalConnectorArgumentsException

​(

String

s,

String

name)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

IllegalConnectorArgumentsException

​(

String

s,

List

<

String

> names)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

---

#### Constructor Summary

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

String

>

argumentNames

()

Return a

List

containing the names of the
invalid or inconsistent arguments.

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

Return a

List

containing the names of the
invalid or inconsistent arguments.

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

- IllegalConnectorArgumentsException

```java
public IllegalConnectorArgumentsException​(
String
s,

String
name)
```

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

**Parameters:** s

- the detailed message.
**Parameters:** name

- the name of the invalid or inconsistent argument.

- IllegalConnectorArgumentsException

```java
public IllegalConnectorArgumentsException​(
String
s,

List
<
String
> names)
```

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

**Parameters:** s

- the detailed message.
**Parameters:** names

- a

List

containing the names of the
invalid or inconsistent argument.

============ METHOD DETAIL ==========

- Method Detail

- argumentNames

```java
public
List
<
String
> argumentNames()
```

Return a

List

containing the names of the
invalid or inconsistent arguments.

**Returns:** a

List

of argument names.

Constructor Detail

- IllegalConnectorArgumentsException

```java
public IllegalConnectorArgumentsException​(
String
s,

String
name)
```

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

**Parameters:** s

- the detailed message.
**Parameters:** name

- the name of the invalid or inconsistent argument.

- IllegalConnectorArgumentsException

```java
public IllegalConnectorArgumentsException​(
String
s,

List
<
String
> names)
```

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

**Parameters:** s

- the detailed message.
**Parameters:** names

- a

List

containing the names of the
invalid or inconsistent argument.

---

#### Constructor Detail

IllegalConnectorArgumentsException

```java
public IllegalConnectorArgumentsException​(
String
s,

String
name)
```

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

**Parameters:** s

- the detailed message.
**Parameters:** name

- the name of the invalid or inconsistent argument.

---

#### IllegalConnectorArgumentsException

public IllegalConnectorArgumentsException​(

String

s,

String

name)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and the name of the argument
which is invalid or inconsistent.

IllegalConnectorArgumentsException

```java
public IllegalConnectorArgumentsException​(
String
s,

List
<
String
> names)
```

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

**Parameters:** s

- the detailed message.
**Parameters:** names

- a

List

containing the names of the
invalid or inconsistent argument.

---

#### IllegalConnectorArgumentsException

public IllegalConnectorArgumentsException​(

String

s,

List

<

String

> names)

Construct an

IllegalConnectorArgumentsException

with the specified detail message and a

List

of
names of arguments which are invalid or inconsistent.

Method Detail

- argumentNames

```java
public
List
<
String
> argumentNames()
```

Return a

List

containing the names of the
invalid or inconsistent arguments.

**Returns:** a

List

of argument names.

---

#### Method Detail

argumentNames

```java
public
List
<
String
> argumentNames()
```

Return a

List

containing the names of the
invalid or inconsistent arguments.

**Returns:** a

List

of argument names.

---

#### argumentNames

public

List

<

String

> argumentNames()

Return a

List

containing the names of the
invalid or inconsistent arguments.

---

