# Class ErrorManager

**Source:** `java.logging\java\util\logging\ErrorManager.html`

### Class Description

```java
public class
ErrorManager

extends
Object
```

ErrorManager objects can be attached to Handlers to process
any error that occurs on a Handler during Logging.

When processing logging output, if a Handler encounters problems
then rather than throwing an Exception back to the issuer of
the logging call (who is unlikely to be interested) the Handler
should call its associated ErrorManager.

---

### Field Details

#### public static final int GENERIC_FAILURE

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

**See Also:**
- Constant Field Values

---

#### public static final int WRITE_FAILURE

WRITE_FAILURE is used when a write to an output stream fails.

**See Also:**
- Constant Field Values

---

#### public static final int FLUSH_FAILURE

FLUSH_FAILURE is used when a flush to an output stream fails.

**See Also:**
- Constant Field Values

---

#### public static final int CLOSE_FAILURE

CLOSE_FAILURE is used when a close of an output stream fails.

**See Also:**
- Constant Field Values

---

#### public static final int OPEN_FAILURE

OPEN_FAILURE is used when an open of an output stream fails.

**See Also:**
- Constant Field Values

---

#### public static final int FORMAT_FAILURE

FORMAT_FAILURE is used when formatting fails for any reason.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ErrorManager()

*No description found.*

---

### Method Details

#### public void error​(
String
msg,

Exception
ex,
int code)

The error method is called when a Handler failure occurs.

This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.

**Parameters:**
- msg

- a descriptive string (may be null)
- ex

- an exception (may be null)
- code

- an error code defined in ErrorManager

---

### Additional Sections

#### Class ErrorManager

java.lang.Object

- java.util.logging.ErrorManager

java.util.logging.ErrorManager

```java
public class
ErrorManager

extends
Object
```

ErrorManager objects can be attached to Handlers to process
any error that occurs on a Handler during Logging.

When processing logging output, if a Handler encounters problems
then rather than throwing an Exception back to the issuer of
the logging call (who is unlikely to be interested) the Handler
should call its associated ErrorManager.

public class

ErrorManager

extends

Object

ErrorManager objects can be attached to Handlers to process
any error that occurs on a Handler during Logging.

When processing logging output, if a Handler encounters problems
then rather than throwing an Exception back to the issuer of
the logging call (who is unlikely to be interested) the Handler
should call its associated ErrorManager.

When processing logging output, if a Handler encounters problems
then rather than throwing an Exception back to the issuer of
the logging call (who is unlikely to be interested) the Handler
should call its associated ErrorManager.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CLOSE_FAILURE

CLOSE_FAILURE is used when a close of an output stream fails.

static int

FLUSH_FAILURE

FLUSH_FAILURE is used when a flush to an output stream fails.

static int

FORMAT_FAILURE

FORMAT_FAILURE is used when formatting fails for any reason.

static int

GENERIC_FAILURE

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

static int

OPEN_FAILURE

OPEN_FAILURE is used when an open of an output stream fails.

static int

WRITE_FAILURE

WRITE_FAILURE is used when a write to an output stream fails.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ErrorManager

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

error

​(

String

msg,

Exception

ex,
int code)

The error method is called when a Handler failure occurs.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

CLOSE_FAILURE

CLOSE_FAILURE is used when a close of an output stream fails.

static int

FLUSH_FAILURE

FLUSH_FAILURE is used when a flush to an output stream fails.

static int

FORMAT_FAILURE

FORMAT_FAILURE is used when formatting fails for any reason.

static int

GENERIC_FAILURE

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

static int

OPEN_FAILURE

OPEN_FAILURE is used when an open of an output stream fails.

static int

WRITE_FAILURE

WRITE_FAILURE is used when a write to an output stream fails.

---

#### Field Summary

CLOSE_FAILURE is used when a close of an output stream fails.

FLUSH_FAILURE is used when a flush to an output stream fails.

FORMAT_FAILURE is used when formatting fails for any reason.

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

OPEN_FAILURE is used when an open of an output stream fails.

WRITE_FAILURE is used when a write to an output stream fails.

Constructor Summary

Constructors

Constructor

Description

ErrorManager

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

error

​(

String

msg,

Exception

ex,
int code)

The error method is called when a Handler failure occurs.

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

The error method is called when a Handler failure occurs.

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

============ FIELD DETAIL ===========

- Field Detail

- GENERIC_FAILURE

```java
public static final int GENERIC_FAILURE
```

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

**See Also:** Constant Field Values

- WRITE_FAILURE

```java
public static final int WRITE_FAILURE
```

WRITE_FAILURE is used when a write to an output stream fails.

**See Also:** Constant Field Values

- FLUSH_FAILURE

```java
public static final int FLUSH_FAILURE
```

FLUSH_FAILURE is used when a flush to an output stream fails.

**See Also:** Constant Field Values

- CLOSE_FAILURE

```java
public static final int CLOSE_FAILURE
```

CLOSE_FAILURE is used when a close of an output stream fails.

**See Also:** Constant Field Values

- OPEN_FAILURE

```java
public static final int OPEN_FAILURE
```

OPEN_FAILURE is used when an open of an output stream fails.

**See Also:** Constant Field Values

- FORMAT_FAILURE

```java
public static final int FORMAT_FAILURE
```

FORMAT_FAILURE is used when formatting fails for any reason.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ErrorManager

```java
public ErrorManager()
```

============ METHOD DETAIL ==========

- Method Detail

- error

```java
public void error​(
String
msg,

Exception
ex,
int code)
```

The error method is called when a Handler failure occurs.

This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.

**Parameters:** msg

- a descriptive string (may be null)
**Parameters:** ex

- an exception (may be null)
**Parameters:** code

- an error code defined in ErrorManager

Field Detail

- GENERIC_FAILURE

```java
public static final int GENERIC_FAILURE
```

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

**See Also:** Constant Field Values

- WRITE_FAILURE

```java
public static final int WRITE_FAILURE
```

WRITE_FAILURE is used when a write to an output stream fails.

**See Also:** Constant Field Values

- FLUSH_FAILURE

```java
public static final int FLUSH_FAILURE
```

FLUSH_FAILURE is used when a flush to an output stream fails.

**See Also:** Constant Field Values

- CLOSE_FAILURE

```java
public static final int CLOSE_FAILURE
```

CLOSE_FAILURE is used when a close of an output stream fails.

**See Also:** Constant Field Values

- OPEN_FAILURE

```java
public static final int OPEN_FAILURE
```

OPEN_FAILURE is used when an open of an output stream fails.

**See Also:** Constant Field Values

- FORMAT_FAILURE

```java
public static final int FORMAT_FAILURE
```

FORMAT_FAILURE is used when formatting fails for any reason.

**See Also:** Constant Field Values

---

#### Field Detail

GENERIC_FAILURE

```java
public static final int GENERIC_FAILURE
```

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

**See Also:** Constant Field Values

---

#### GENERIC_FAILURE

public static final int GENERIC_FAILURE

GENERIC_FAILURE is used for failure that don't fit
into one of the other categories.

WRITE_FAILURE

```java
public static final int WRITE_FAILURE
```

WRITE_FAILURE is used when a write to an output stream fails.

**See Also:** Constant Field Values

---

#### WRITE_FAILURE

public static final int WRITE_FAILURE

WRITE_FAILURE is used when a write to an output stream fails.

FLUSH_FAILURE

```java
public static final int FLUSH_FAILURE
```

FLUSH_FAILURE is used when a flush to an output stream fails.

**See Also:** Constant Field Values

---

#### FLUSH_FAILURE

public static final int FLUSH_FAILURE

FLUSH_FAILURE is used when a flush to an output stream fails.

CLOSE_FAILURE

```java
public static final int CLOSE_FAILURE
```

CLOSE_FAILURE is used when a close of an output stream fails.

**See Also:** Constant Field Values

---

#### CLOSE_FAILURE

public static final int CLOSE_FAILURE

CLOSE_FAILURE is used when a close of an output stream fails.

OPEN_FAILURE

```java
public static final int OPEN_FAILURE
```

OPEN_FAILURE is used when an open of an output stream fails.

**See Also:** Constant Field Values

---

#### OPEN_FAILURE

public static final int OPEN_FAILURE

OPEN_FAILURE is used when an open of an output stream fails.

FORMAT_FAILURE

```java
public static final int FORMAT_FAILURE
```

FORMAT_FAILURE is used when formatting fails for any reason.

**See Also:** Constant Field Values

---

#### FORMAT_FAILURE

public static final int FORMAT_FAILURE

FORMAT_FAILURE is used when formatting fails for any reason.

Constructor Detail

- ErrorManager

```java
public ErrorManager()
```

---

#### Constructor Detail

ErrorManager

```java
public ErrorManager()
```

---

#### ErrorManager

public ErrorManager()

Method Detail

- error

```java
public void error​(
String
msg,

Exception
ex,
int code)
```

The error method is called when a Handler failure occurs.

This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.

**Parameters:** msg

- a descriptive string (may be null)
**Parameters:** ex

- an exception (may be null)
**Parameters:** code

- an error code defined in ErrorManager

---

#### Method Detail

error

```java
public void error​(
String
msg,

Exception
ex,
int code)
```

The error method is called when a Handler failure occurs.

This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.

**Parameters:** msg

- a descriptive string (may be null)
**Parameters:** ex

- an exception (may be null)
**Parameters:** code

- an error code defined in ErrorManager

---

#### error

public void error​(

String

msg,

Exception

ex,
int code)

The error method is called when a Handler failure occurs.

This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.

This method may be overridden in subclasses. The default
behavior in this base class is that the first call is
reported to System.err, and subsequent calls are ignored.

---

