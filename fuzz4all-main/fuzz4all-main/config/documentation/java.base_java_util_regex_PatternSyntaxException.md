# Class PatternSyntaxException

**Source:** `java.base\java\util\regex\PatternSyntaxException.html`

### Class Description

```java
public class
PatternSyntaxException

extends
IllegalArgumentException
```

Unchecked exception thrown to indicate a syntax error in a
regular-expression pattern.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PatternSyntaxException​(
String
desc,

String
regex,
int index)

Constructs a new instance of this class.

**Parameters:**
- desc

- A description of the error
- regex

- The erroneous pattern
- index

- The approximate index in the pattern of the error,
or

-1

if the index is not known

---

### Method Details

#### public int getIndex()

Retrieves the error index.

**Returns:**
- The approximate index in the pattern of the error,
or

-1

if the index is not known

---

#### public
String
getDescription()

Retrieves the description of the error.

**Returns:**
- The description of the error

---

#### public
String
getPattern()

Retrieves the erroneous regular-expression pattern.

**Returns:**
- The erroneous pattern

---

#### public
String
getMessage()

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- The full detail message

---

### Additional Sections

#### Class PatternSyntaxException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.util.regex.PatternSyntaxException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.util.regex.PatternSyntaxException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.util.regex.PatternSyntaxException

java.lang.RuntimeException

- java.lang.IllegalArgumentException
- - java.util.regex.PatternSyntaxException

java.lang.IllegalArgumentException

- java.util.regex.PatternSyntaxException

java.util.regex.PatternSyntaxException

**All Implemented Interfaces:** Serializable

```java
public class
PatternSyntaxException

extends
IllegalArgumentException
```

Unchecked exception thrown to indicate a syntax error in a
regular-expression pattern.

**Since:** 1.4
**See Also:** Serialized Form

public class

PatternSyntaxException

extends

IllegalArgumentException

Unchecked exception thrown to indicate a syntax error in a
regular-expression pattern.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PatternSyntaxException

​(

String

desc,

String

regex,
int index)

Constructs a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescription

()

Retrieves the description of the error.

int

getIndex

()

Retrieves the error index.

String

getMessage

()

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

String

getPattern

()

Retrieves the erroneous regular-expression pattern.

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

PatternSyntaxException

​(

String

desc,

String

regex,
int index)

Constructs a new instance of this class.

---

#### Constructor Summary

Constructs a new instance of this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescription

()

Retrieves the description of the error.

int

getIndex

()

Retrieves the error index.

String

getMessage

()

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

String

getPattern

()

Retrieves the erroneous regular-expression pattern.

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

Retrieves the description of the error.

Retrieves the error index.

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

Retrieves the erroneous regular-expression pattern.

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

- PatternSyntaxException

```java
public PatternSyntaxException​(
String
desc,

String
regex,
int index)
```

Constructs a new instance of this class.

**Parameters:** desc

- A description of the error
**Parameters:** regex

- The erroneous pattern
**Parameters:** index

- The approximate index in the pattern of the error,
or

-1

if the index is not known

============ METHOD DETAIL ==========

- Method Detail

- getIndex

```java
public int getIndex()
```

Retrieves the error index.

**Returns:** The approximate index in the pattern of the error,
or

-1

if the index is not known

- getDescription

```java
public
String
getDescription()
```

Retrieves the description of the error.

**Returns:** The description of the error

- getPattern

```java
public
String
getPattern()
```

Retrieves the erroneous regular-expression pattern.

**Returns:** The erroneous pattern

- getMessage

```java
public
String
getMessage()
```

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

**Overrides:** getMessage

in class

Throwable
**Returns:** The full detail message

Constructor Detail

- PatternSyntaxException

```java
public PatternSyntaxException​(
String
desc,

String
regex,
int index)
```

Constructs a new instance of this class.

**Parameters:** desc

- A description of the error
**Parameters:** regex

- The erroneous pattern
**Parameters:** index

- The approximate index in the pattern of the error,
or

-1

if the index is not known

---

#### Constructor Detail

PatternSyntaxException

```java
public PatternSyntaxException​(
String
desc,

String
regex,
int index)
```

Constructs a new instance of this class.

**Parameters:** desc

- A description of the error
**Parameters:** regex

- The erroneous pattern
**Parameters:** index

- The approximate index in the pattern of the error,
or

-1

if the index is not known

---

#### PatternSyntaxException

public PatternSyntaxException​(

String

desc,

String

regex,
int index)

Constructs a new instance of this class.

Method Detail

- getIndex

```java
public int getIndex()
```

Retrieves the error index.

**Returns:** The approximate index in the pattern of the error,
or

-1

if the index is not known

- getDescription

```java
public
String
getDescription()
```

Retrieves the description of the error.

**Returns:** The description of the error

- getPattern

```java
public
String
getPattern()
```

Retrieves the erroneous regular-expression pattern.

**Returns:** The erroneous pattern

- getMessage

```java
public
String
getMessage()
```

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

**Overrides:** getMessage

in class

Throwable
**Returns:** The full detail message

---

#### Method Detail

getIndex

```java
public int getIndex()
```

Retrieves the error index.

**Returns:** The approximate index in the pattern of the error,
or

-1

if the index is not known

---

#### getIndex

public int getIndex()

Retrieves the error index.

getDescription

```java
public
String
getDescription()
```

Retrieves the description of the error.

**Returns:** The description of the error

---

#### getDescription

public

String

getDescription()

Retrieves the description of the error.

getPattern

```java
public
String
getPattern()
```

Retrieves the erroneous regular-expression pattern.

**Returns:** The erroneous pattern

---

#### getPattern

public

String

getPattern()

Retrieves the erroneous regular-expression pattern.

getMessage

```java
public
String
getMessage()
```

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

**Overrides:** getMessage

in class

Throwable
**Returns:** The full detail message

---

#### getMessage

public

String

getMessage()

Returns a multi-line string containing the description of the syntax
error and its index, the erroneous regular-expression pattern, and a
visual indication of the error index within the pattern.

---

