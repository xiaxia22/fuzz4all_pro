# Class HttpRetryException

**Source:** `java.base\java\net\HttpRetryException.html`

### Class Description

```java
public class
HttpRetryException

extends
IOException
```

Thrown to indicate that a HTTP request needs to be retried
but cannot be retried automatically, due to streaming mode
being enabled.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public HttpRetryException​(
String
detail,
int code)

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

**Parameters:**
- detail

- the detail message.
- code

- the HTTP response code from server.

---

#### public HttpRetryException​(
String
detail,
int code,

String
location)

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

**Parameters:**
- detail

- the detail message.
- code

- the HTTP response code from server.
- location

- the URL to be redirected to

---

### Method Details

#### public int responseCode()

Returns the http response code

**Returns:**
- The http response code.

---

#### public
String
getReason()

Returns a string explaining why the http request could
not be retried.

**Returns:**
- The reason string

---

#### public
String
getLocation()

Returns the value of the Location header field if the
error resulted from redirection.

**Returns:**
- The location string

---

### Additional Sections

#### Class HttpRetryException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.net.HttpRetryException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.net.HttpRetryException

java.lang.Exception

- java.io.IOException
- - java.net.HttpRetryException

java.io.IOException

- java.net.HttpRetryException

java.net.HttpRetryException

**All Implemented Interfaces:** Serializable

```java
public class
HttpRetryException

extends
IOException
```

Thrown to indicate that a HTTP request needs to be retried
but cannot be retried automatically, due to streaming mode
being enabled.

**Since:** 1.5
**See Also:** Serialized Form

public class

HttpRetryException

extends

IOException

Thrown to indicate that a HTTP request needs to be retried
but cannot be retried automatically, due to streaming mode
being enabled.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HttpRetryException

​(

String

detail,
int code)

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

HttpRetryException

​(

String

detail,
int code,

String

location)

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getLocation

()

Returns the value of the Location header field if the
error resulted from redirection.

String

getReason

()

Returns a string explaining why the http request could
not be retried.

int

responseCode

()

Returns the http response code

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

HttpRetryException

​(

String

detail,
int code)

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

HttpRetryException

​(

String

detail,
int code,

String

location)

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

---

#### Constructor Summary

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getLocation

()

Returns the value of the Location header field if the
error resulted from redirection.

String

getReason

()

Returns a string explaining why the http request could
not be retried.

int

responseCode

()

Returns the http response code

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

Returns the value of the Location header field if the
error resulted from redirection.

Returns a string explaining why the http request could
not be retried.

Returns the http response code

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

- HttpRetryException

```java
public HttpRetryException​(
String
detail,
int code)
```

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

**Parameters:** detail

- the detail message.
**Parameters:** code

- the HTTP response code from server.

- HttpRetryException

```java
public HttpRetryException​(
String
detail,
int code,

String
location)
```

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

**Parameters:** detail

- the detail message.
**Parameters:** code

- the HTTP response code from server.
**Parameters:** location

- the URL to be redirected to

============ METHOD DETAIL ==========

- Method Detail

- responseCode

```java
public int responseCode()
```

Returns the http response code

**Returns:** The http response code.

- getReason

```java
public
String
getReason()
```

Returns a string explaining why the http request could
not be retried.

**Returns:** The reason string

- getLocation

```java
public
String
getLocation()
```

Returns the value of the Location header field if the
error resulted from redirection.

**Returns:** The location string

Constructor Detail

- HttpRetryException

```java
public HttpRetryException​(
String
detail,
int code)
```

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

**Parameters:** detail

- the detail message.
**Parameters:** code

- the HTTP response code from server.

- HttpRetryException

```java
public HttpRetryException​(
String
detail,
int code,

String
location)
```

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

**Parameters:** detail

- the detail message.
**Parameters:** code

- the HTTP response code from server.
**Parameters:** location

- the URL to be redirected to

---

#### Constructor Detail

HttpRetryException

```java
public HttpRetryException​(
String
detail,
int code)
```

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

**Parameters:** detail

- the detail message.
**Parameters:** code

- the HTTP response code from server.

---

#### HttpRetryException

public HttpRetryException​(

String

detail,
int code)

Constructs a new

HttpRetryException

from the
specified response code and exception detail message

HttpRetryException

```java
public HttpRetryException​(
String
detail,
int code,

String
location)
```

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

**Parameters:** detail

- the detail message.
**Parameters:** code

- the HTTP response code from server.
**Parameters:** location

- the URL to be redirected to

---

#### HttpRetryException

public HttpRetryException​(

String

detail,
int code,

String

location)

Constructs a new

HttpRetryException

with detail message
responseCode and the contents of the Location response header field.

Method Detail

- responseCode

```java
public int responseCode()
```

Returns the http response code

**Returns:** The http response code.

- getReason

```java
public
String
getReason()
```

Returns a string explaining why the http request could
not be retried.

**Returns:** The reason string

- getLocation

```java
public
String
getLocation()
```

Returns the value of the Location header field if the
error resulted from redirection.

**Returns:** The location string

---

#### Method Detail

responseCode

```java
public int responseCode()
```

Returns the http response code

**Returns:** The http response code.

---

#### responseCode

public int responseCode()

Returns the http response code

getReason

```java
public
String
getReason()
```

Returns a string explaining why the http request could
not be retried.

**Returns:** The reason string

---

#### getReason

public

String

getReason()

Returns a string explaining why the http request could
not be retried.

getLocation

```java
public
String
getLocation()
```

Returns the value of the Location header field if the
error resulted from redirection.

**Returns:** The location string

---

#### getLocation

public

String

getLocation()

Returns the value of the Location header field if the
error resulted from redirection.

---

