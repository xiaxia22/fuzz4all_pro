# Class AssertionError

**Source:** `java.base\java\lang\AssertionError.html`

### Class Description

```java
public class
AssertionError

extends
Error
```

Thrown to indicate that an assertion has failed.

The seven one-argument public constructors provided by this
class ensure that the assertion error returned by the invocation:

```java
new AssertionError(
expression
)
```

has as its detail message the

string conversion

of

expression

(as defined in section 15.18.1.1 of

The Java™ Language Specification

),
regardless of the type of

expression

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AssertionError()

Constructs an AssertionError with no detail message.

---

#### public AssertionError​(
Object
detailMessage)

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

If the specified object is an instance of

Throwable

, it
becomes the

cause

of the newly constructed assertion error.

**Parameters:**
- detailMessage

- value to be used in constructing detail message

**See Also:**
- Throwable.getCause()

---

#### public AssertionError​(boolean detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:**
- detailMessage

- value to be used in constructing detail message

---

#### public AssertionError​(char detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:**
- detailMessage

- value to be used in constructing detail message

---

#### public AssertionError​(int detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:**
- detailMessage

- value to be used in constructing detail message

---

#### public AssertionError​(long detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:**
- detailMessage

- value to be used in constructing detail message

---

#### public AssertionError​(float detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:**
- detailMessage

- value to be used in constructing detail message

---

#### public AssertionError​(double detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:**
- detailMessage

- value to be used in constructing detail message

---

#### public AssertionError​(
String
message,

Throwable
cause)

Constructs a new

AssertionError

with the specified
detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:**
- message

- the detail message, may be

null
- cause

- the cause, may be

null

**Since:**
- 1.7

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AssertionError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - java.lang.AssertionError

java.lang.Throwable

- java.lang.Error
- - java.lang.AssertionError

java.lang.Error

- java.lang.AssertionError

java.lang.AssertionError

**All Implemented Interfaces:** Serializable

```java
public class
AssertionError

extends
Error
```

Thrown to indicate that an assertion has failed.

The seven one-argument public constructors provided by this
class ensure that the assertion error returned by the invocation:

```java
new AssertionError(
expression
)
```

has as its detail message the

string conversion

of

expression

(as defined in section 15.18.1.1 of

The Java™ Language Specification

),
regardless of the type of

expression

.

**Since:** 1.4
**See Also:** Serialized Form

public class

AssertionError

extends

Error

Thrown to indicate that an assertion has failed.

The seven one-argument public constructors provided by this
class ensure that the assertion error returned by the invocation:

```java
new AssertionError(
expression
)
```

has as its detail message the

string conversion

of

expression

(as defined in section 15.18.1.1 of

The Java™ Language Specification

),
regardless of the type of

expression

.

The seven one-argument public constructors provided by this
class ensure that the assertion error returned by the invocation:

```java
new AssertionError(
expression
)
```

has as its detail message the

string conversion

of

expression

(as defined in section 15.18.1.1 of

The Java™ Language Specification

),
regardless of the type of

expression

.

new AssertionError(

expression

)

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AssertionError

()

Constructs an AssertionError with no detail message.

AssertionError

​(boolean detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(char detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(double detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(float detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(int detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(long detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(

Object

detailMessage)

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(

String

message,

Throwable

cause)

Constructs a new

AssertionError

with the specified
detail message and cause.

========== METHOD SUMMARY ===========

- Method Summary

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

AssertionError

()

Constructs an AssertionError with no detail message.

AssertionError

​(boolean detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(char detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(double detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(float detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(int detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(long detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(

Object

detailMessage)

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

​(

String

message,

Throwable

cause)

Constructs a new

AssertionError

with the specified
detail message and cause.

---

#### Constructor Summary

Constructs an AssertionError with no detail message.

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

Constructs a new

AssertionError

with the specified
detail message and cause.

Method Summary

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

- AssertionError

```java
public AssertionError()
```

Constructs an AssertionError with no detail message.

- AssertionError

```java
public AssertionError​(
Object
detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

If the specified object is an instance of

Throwable

, it
becomes the

cause

of the newly constructed assertion error.

**Parameters:** detailMessage

- value to be used in constructing detail message
**See Also:** Throwable.getCause()

- AssertionError

```java
public AssertionError​(boolean detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(char detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(int detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(long detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(float detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(double detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(
String
message,

Throwable
cause)
```

Constructs a new

AssertionError

with the specified
detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:** message

- the detail message, may be

null
**Parameters:** cause

- the cause, may be

null
**Since:** 1.7

Constructor Detail

- AssertionError

```java
public AssertionError()
```

Constructs an AssertionError with no detail message.

- AssertionError

```java
public AssertionError​(
Object
detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

If the specified object is an instance of

Throwable

, it
becomes the

cause

of the newly constructed assertion error.

**Parameters:** detailMessage

- value to be used in constructing detail message
**See Also:** Throwable.getCause()

- AssertionError

```java
public AssertionError​(boolean detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(char detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(int detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(long detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(float detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(double detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

- AssertionError

```java
public AssertionError​(
String
message,

Throwable
cause)
```

Constructs a new

AssertionError

with the specified
detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:** message

- the detail message, may be

null
**Parameters:** cause

- the cause, may be

null
**Since:** 1.7

---

#### Constructor Detail

AssertionError

```java
public AssertionError()
```

Constructs an AssertionError with no detail message.

---

#### AssertionError

public AssertionError()

Constructs an AssertionError with no detail message.

AssertionError

```java
public AssertionError​(
Object
detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

If the specified object is an instance of

Throwable

, it
becomes the

cause

of the newly constructed assertion error.

**Parameters:** detailMessage

- value to be used in constructing detail message
**See Also:** Throwable.getCause()

---

#### AssertionError

public AssertionError​(

Object

detailMessage)

Constructs an AssertionError with its detail message derived
from the specified object, which is converted to a string as
defined in section 15.18.1.1 of

The Java™ Language Specification

.

If the specified object is an instance of

Throwable

, it
becomes the

cause

of the newly constructed assertion error.

If the specified object is an instance of

Throwable

, it
becomes the

cause

of the newly constructed assertion error.

AssertionError

```java
public AssertionError​(boolean detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

---

#### AssertionError

public AssertionError​(boolean detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

boolean

, which is converted to
a string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

```java
public AssertionError​(char detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

---

#### AssertionError

public AssertionError​(char detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

char

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

```java
public AssertionError​(int detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

---

#### AssertionError

public AssertionError​(int detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

int

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

```java
public AssertionError​(long detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

---

#### AssertionError

public AssertionError​(long detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

long

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

```java
public AssertionError​(float detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

---

#### AssertionError

public AssertionError​(float detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

float

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

```java
public AssertionError​(double detailMessage)
```

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

**Parameters:** detailMessage

- value to be used in constructing detail message

---

#### AssertionError

public AssertionError​(double detailMessage)

Constructs an AssertionError with its detail message derived
from the specified

double

, which is converted to a
string as defined in section 15.18.1.1 of

The Java™ Language Specification

.

AssertionError

```java
public AssertionError​(
String
message,

Throwable
cause)
```

Constructs a new

AssertionError

with the specified
detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

**Parameters:** message

- the detail message, may be

null
**Parameters:** cause

- the cause, may be

null
**Since:** 1.7

---

#### AssertionError

public AssertionError​(

String

message,

Throwable

cause)

Constructs a new

AssertionError

with the specified
detail message and cause.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

Note that the detail message associated with

cause

is

not

automatically incorporated in
this error's detail message.

---

