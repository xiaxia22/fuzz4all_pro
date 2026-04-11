# Class XMLStreamException

**Source:** `java.xml\javax\xml\stream\XMLStreamException.html`

### Class Description

```java
public class
XMLStreamException

extends
Exception
```

The base exception for unexpected processing errors. This Exception
class is used to report well-formedness errors as well as unexpected
processing conditions.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Throwable
nested

*No description found.*

---

#### protected
Location
location

*No description found.*

---

### Constructor Details

#### public XMLStreamException()

Default constructor

---

#### public XMLStreamException​(
String
msg)

Construct an exception with the assocated message.

**Parameters:**
- msg

- the message to report

---

#### public XMLStreamException​(
Throwable
th)

Construct an exception with the assocated exception

**Parameters:**
- th

- a nested exception

---

#### public XMLStreamException​(
String
msg,

Throwable
th)

Construct an exception with the assocated message and exception

**Parameters:**
- th

- a nested exception
- msg

- the message to report

---

#### public XMLStreamException​(
String
msg,

Location
location,

Throwable
th)

Construct an exception with the assocated message, exception and location.

**Parameters:**
- th

- a nested exception
- msg

- the message to report
- location

- the location of the error

---

#### public XMLStreamException​(
String
msg,

Location
location)

Construct an exception with the assocated message, exception and location.

**Parameters:**
- msg

- the message to report
- location

- the location of the error

---

### Method Details

#### public
Throwable
getNestedException()

Gets the nested exception.

**Returns:**
- Nested exception

---

#### public
Location
getLocation()

Gets the location of the exception

**Returns:**
- the location of the exception, may be null if none is available

---

### Additional Sections

#### Class XMLStreamException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.stream.XMLStreamException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.stream.XMLStreamException

java.lang.Exception

- javax.xml.stream.XMLStreamException

javax.xml.stream.XMLStreamException

**All Implemented Interfaces:** Serializable

```java
public class
XMLStreamException

extends
Exception
```

The base exception for unexpected processing errors. This Exception
class is used to report well-formedness errors as well as unexpected
processing conditions.

**Since:** 1.6
**See Also:** Serialized Form

public class

XMLStreamException

extends

Exception

The base exception for unexpected processing errors. This Exception
class is used to report well-formedness errors as well as unexpected
processing conditions.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Location

location

protected

Throwable

nested

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XMLStreamException

()

Default constructor

XMLStreamException

​(

String

msg)

Construct an exception with the assocated message.

XMLStreamException

​(

String

msg,

Throwable

th)

Construct an exception with the assocated message and exception

XMLStreamException

​(

String

msg,

Location

location)

Construct an exception with the assocated message, exception and location.

XMLStreamException

​(

String

msg,

Location

location,

Throwable

th)

Construct an exception with the assocated message, exception and location.

XMLStreamException

​(

Throwable

th)

Construct an exception with the assocated exception

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Location

getLocation

()

Gets the location of the exception

Throwable

getNestedException

()

Gets the nested exception.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Location

location

protected

Throwable

nested

---

#### Field Summary

Constructor Summary

Constructors

Constructor

Description

XMLStreamException

()

Default constructor

XMLStreamException

​(

String

msg)

Construct an exception with the assocated message.

XMLStreamException

​(

String

msg,

Throwable

th)

Construct an exception with the assocated message and exception

XMLStreamException

​(

String

msg,

Location

location)

Construct an exception with the assocated message, exception and location.

XMLStreamException

​(

String

msg,

Location

location,

Throwable

th)

Construct an exception with the assocated message, exception and location.

XMLStreamException

​(

Throwable

th)

Construct an exception with the assocated exception

---

#### Constructor Summary

Default constructor

Construct an exception with the assocated message.

Construct an exception with the assocated message and exception

Construct an exception with the assocated message, exception and location.

Construct an exception with the assocated exception

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Location

getLocation

()

Gets the location of the exception

Throwable

getNestedException

()

Gets the nested exception.

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

Gets the location of the exception

Gets the nested exception.

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

============ FIELD DETAIL ===========

- Field Detail

- nested

```java
protected
Throwable
nested
```

- location

```java
protected
Location
location
```

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- XMLStreamException

```java
public XMLStreamException()
```

Default constructor

- XMLStreamException

```java
public XMLStreamException​(
String
msg)
```

Construct an exception with the assocated message.

**Parameters:** msg

- the message to report

- XMLStreamException

```java
public XMLStreamException​(
Throwable
th)
```

Construct an exception with the assocated exception

**Parameters:** th

- a nested exception

- XMLStreamException

```java
public XMLStreamException​(
String
msg,

Throwable
th)
```

Construct an exception with the assocated message and exception

**Parameters:** th

- a nested exception
**Parameters:** msg

- the message to report

- XMLStreamException

```java
public XMLStreamException​(
String
msg,

Location
location,

Throwable
th)
```

Construct an exception with the assocated message, exception and location.

**Parameters:** th

- a nested exception
**Parameters:** msg

- the message to report
**Parameters:** location

- the location of the error

- XMLStreamException

```java
public XMLStreamException​(
String
msg,

Location
location)
```

Construct an exception with the assocated message, exception and location.

**Parameters:** msg

- the message to report
**Parameters:** location

- the location of the error

============ METHOD DETAIL ==========

- Method Detail

- getNestedException

```java
public
Throwable
getNestedException()
```

Gets the nested exception.

**Returns:** Nested exception

- getLocation

```java
public
Location
getLocation()
```

Gets the location of the exception

**Returns:** the location of the exception, may be null if none is available

Field Detail

- nested

```java
protected
Throwable
nested
```

- location

```java
protected
Location
location
```

---

#### Field Detail

nested

```java
protected
Throwable
nested
```

---

#### nested

protected

Throwable

nested

location

```java
protected
Location
location
```

---

#### location

protected

Location

location

Constructor Detail

- XMLStreamException

```java
public XMLStreamException()
```

Default constructor

- XMLStreamException

```java
public XMLStreamException​(
String
msg)
```

Construct an exception with the assocated message.

**Parameters:** msg

- the message to report

- XMLStreamException

```java
public XMLStreamException​(
Throwable
th)
```

Construct an exception with the assocated exception

**Parameters:** th

- a nested exception

- XMLStreamException

```java
public XMLStreamException​(
String
msg,

Throwable
th)
```

Construct an exception with the assocated message and exception

**Parameters:** th

- a nested exception
**Parameters:** msg

- the message to report

- XMLStreamException

```java
public XMLStreamException​(
String
msg,

Location
location,

Throwable
th)
```

Construct an exception with the assocated message, exception and location.

**Parameters:** th

- a nested exception
**Parameters:** msg

- the message to report
**Parameters:** location

- the location of the error

- XMLStreamException

```java
public XMLStreamException​(
String
msg,

Location
location)
```

Construct an exception with the assocated message, exception and location.

**Parameters:** msg

- the message to report
**Parameters:** location

- the location of the error

---

#### Constructor Detail

XMLStreamException

```java
public XMLStreamException()
```

Default constructor

---

#### XMLStreamException

public XMLStreamException()

Default constructor

XMLStreamException

```java
public XMLStreamException​(
String
msg)
```

Construct an exception with the assocated message.

**Parameters:** msg

- the message to report

---

#### XMLStreamException

public XMLStreamException​(

String

msg)

Construct an exception with the assocated message.

XMLStreamException

```java
public XMLStreamException​(
Throwable
th)
```

Construct an exception with the assocated exception

**Parameters:** th

- a nested exception

---

#### XMLStreamException

public XMLStreamException​(

Throwable

th)

Construct an exception with the assocated exception

XMLStreamException

```java
public XMLStreamException​(
String
msg,

Throwable
th)
```

Construct an exception with the assocated message and exception

**Parameters:** th

- a nested exception
**Parameters:** msg

- the message to report

---

#### XMLStreamException

public XMLStreamException​(

String

msg,

Throwable

th)

Construct an exception with the assocated message and exception

XMLStreamException

```java
public XMLStreamException​(
String
msg,

Location
location,

Throwable
th)
```

Construct an exception with the assocated message, exception and location.

**Parameters:** th

- a nested exception
**Parameters:** msg

- the message to report
**Parameters:** location

- the location of the error

---

#### XMLStreamException

public XMLStreamException​(

String

msg,

Location

location,

Throwable

th)

Construct an exception with the assocated message, exception and location.

XMLStreamException

```java
public XMLStreamException​(
String
msg,

Location
location)
```

Construct an exception with the assocated message, exception and location.

**Parameters:** msg

- the message to report
**Parameters:** location

- the location of the error

---

#### XMLStreamException

public XMLStreamException​(

String

msg,

Location

location)

Construct an exception with the assocated message, exception and location.

Method Detail

- getNestedException

```java
public
Throwable
getNestedException()
```

Gets the nested exception.

**Returns:** Nested exception

- getLocation

```java
public
Location
getLocation()
```

Gets the location of the exception

**Returns:** the location of the exception, may be null if none is available

---

#### Method Detail

getNestedException

```java
public
Throwable
getNestedException()
```

Gets the nested exception.

**Returns:** Nested exception

---

#### getNestedException

public

Throwable

getNestedException()

Gets the nested exception.

getLocation

```java
public
Location
getLocation()
```

Gets the location of the exception

**Returns:** the location of the exception, may be null if none is available

---

#### getLocation

public

Location

getLocation()

Gets the location of the exception

---

