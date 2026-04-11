# Class UnmappableCharacterException

**Source:** `java.base\java\nio\charset\UnmappableCharacterException.html`

### Class Description

```java
public class
UnmappableCharacterException

extends
CharacterCodingException
```

Checked exception thrown when an input character (or byte) sequence
is valid but cannot be mapped to an output byte (or character)
sequence.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnmappableCharacterException​(int inputLength)

Constructs an

UnmappableCharacterException

with the
given length.

**Parameters:**
- inputLength

- the length of the input

---

### Method Details

#### public int getInputLength()

Returns the length of the input.

**Returns:**
- the length of the input

---

#### public
String
getMessage()

Returns the message.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- the message

---

### Additional Sections

#### Class UnmappableCharacterException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.charset.CharacterCodingException
- - java.nio.charset.UnmappableCharacterException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.charset.CharacterCodingException
- - java.nio.charset.UnmappableCharacterException

java.lang.Exception

- java.io.IOException
- - java.nio.charset.CharacterCodingException
- - java.nio.charset.UnmappableCharacterException

java.io.IOException

- java.nio.charset.CharacterCodingException
- - java.nio.charset.UnmappableCharacterException

java.nio.charset.CharacterCodingException

- java.nio.charset.UnmappableCharacterException

java.nio.charset.UnmappableCharacterException

**All Implemented Interfaces:** Serializable

```java
public class
UnmappableCharacterException

extends
CharacterCodingException
```

Checked exception thrown when an input character (or byte) sequence
is valid but cannot be mapped to an output byte (or character)
sequence.

**Since:** 1.4
**See Also:** Serialized Form

public class

UnmappableCharacterException

extends

CharacterCodingException

Checked exception thrown when an input character (or byte) sequence
is valid but cannot be mapped to an output byte (or character)
sequence.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnmappableCharacterException

​(int inputLength)

Constructs an

UnmappableCharacterException

with the
given length.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getInputLength

()

Returns the length of the input.

String

getMessage

()

Returns the message.

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

UnmappableCharacterException

​(int inputLength)

Constructs an

UnmappableCharacterException

with the
given length.

---

#### Constructor Summary

Constructs an

UnmappableCharacterException

with the
given length.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getInputLength

()

Returns the length of the input.

String

getMessage

()

Returns the message.

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

Returns the length of the input.

Returns the message.

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

- UnmappableCharacterException

```java
public UnmappableCharacterException​(int inputLength)
```

Constructs an

UnmappableCharacterException

with the
given length.

**Parameters:** inputLength

- the length of the input

============ METHOD DETAIL ==========

- Method Detail

- getInputLength

```java
public int getInputLength()
```

Returns the length of the input.

**Returns:** the length of the input

- getMessage

```java
public
String
getMessage()
```

Returns the message.

**Overrides:** getMessage

in class

Throwable
**Returns:** the message

Constructor Detail

- UnmappableCharacterException

```java
public UnmappableCharacterException​(int inputLength)
```

Constructs an

UnmappableCharacterException

with the
given length.

**Parameters:** inputLength

- the length of the input

---

#### Constructor Detail

UnmappableCharacterException

```java
public UnmappableCharacterException​(int inputLength)
```

Constructs an

UnmappableCharacterException

with the
given length.

**Parameters:** inputLength

- the length of the input

---

#### UnmappableCharacterException

public UnmappableCharacterException​(int inputLength)

Constructs an

UnmappableCharacterException

with the
given length.

Method Detail

- getInputLength

```java
public int getInputLength()
```

Returns the length of the input.

**Returns:** the length of the input

- getMessage

```java
public
String
getMessage()
```

Returns the message.

**Overrides:** getMessage

in class

Throwable
**Returns:** the message

---

#### Method Detail

getInputLength

```java
public int getInputLength()
```

Returns the length of the input.

**Returns:** the length of the input

---

#### getInputLength

public int getInputLength()

Returns the length of the input.

getMessage

```java
public
String
getMessage()
```

Returns the message.

**Overrides:** getMessage

in class

Throwable
**Returns:** the message

---

#### getMessage

public

String

getMessage()

Returns the message.

---

