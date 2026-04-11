# Class OptionalDataException

**Source:** `java.base\java\io\OptionalDataException.html`

### Class Description

```java
public class
OptionalDataException

extends
ObjectStreamException
```

Exception indicating the failure of an object read operation due to
unread primitive data, or the end of data belonging to a serialized
object in the stream. This exception may be thrown in two cases:

- An attempt was made to read an object when the next element in the
stream is primitive data. In this case, the OptionalDataException's
length field is set to the number of bytes of primitive data
immediately readable from the stream, and the eof field is set to
false.

An attempt was made to read past the end of data consumable by a
class-defined readObject or readExternal method. In this case, the
OptionalDataException's eof field is set to true, and the length field
is set to 0.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public int length

The number of bytes of primitive data available to be read
in the current buffer.

---

#### public boolean eof

True if there is no more data in the buffered part of the stream.

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class OptionalDataException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.OptionalDataException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.OptionalDataException

java.lang.Exception

- java.io.IOException
- - java.io.ObjectStreamException
- - java.io.OptionalDataException

java.io.IOException

- java.io.ObjectStreamException
- - java.io.OptionalDataException

java.io.ObjectStreamException

- java.io.OptionalDataException

java.io.OptionalDataException

**All Implemented Interfaces:** Serializable

```java
public class
OptionalDataException

extends
ObjectStreamException
```

Exception indicating the failure of an object read operation due to
unread primitive data, or the end of data belonging to a serialized
object in the stream. This exception may be thrown in two cases:

- An attempt was made to read an object when the next element in the
stream is primitive data. In this case, the OptionalDataException's
length field is set to the number of bytes of primitive data
immediately readable from the stream, and the eof field is set to
false.

An attempt was made to read past the end of data consumable by a
class-defined readObject or readExternal method. In this case, the
OptionalDataException's eof field is set to true, and the length field
is set to 0.

**Since:** 1.1
**See Also:** Serialized Form

public class

OptionalDataException

extends

ObjectStreamException

Exception indicating the failure of an object read operation due to
unread primitive data, or the end of data belonging to a serialized
object in the stream. This exception may be thrown in two cases:

- An attempt was made to read an object when the next element in the
stream is primitive data. In this case, the OptionalDataException's
length field is set to the number of bytes of primitive data
immediately readable from the stream, and the eof field is set to
false.

An attempt was made to read past the end of data consumable by a
class-defined readObject or readExternal method. In this case, the
OptionalDataException's eof field is set to true, and the length field
is set to 0.

An attempt was made to read an object when the next element in the
stream is primitive data. In this case, the OptionalDataException's
length field is set to the number of bytes of primitive data
immediately readable from the stream, and the eof field is set to
false.

An attempt was made to read past the end of data consumable by a
class-defined readObject or readExternal method. In this case, the
OptionalDataException's eof field is set to true, and the length field
is set to 0.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

boolean

eof

True if there is no more data in the buffered part of the stream.

int

length

The number of bytes of primitive data available to be read
in the current buffer.

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

Field Summary

Fields

Modifier and Type

Field

Description

boolean

eof

True if there is no more data in the buffered part of the stream.

int

length

The number of bytes of primitive data available to be read
in the current buffer.

---

#### Field Summary

True if there is no more data in the buffered part of the stream.

The number of bytes of primitive data available to be read
in the current buffer.

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

============ FIELD DETAIL ===========

- Field Detail

- length

```java
public int length
```

The number of bytes of primitive data available to be read
in the current buffer.

- eof

```java
public boolean eof
```

True if there is no more data in the buffered part of the stream.

Field Detail

- length

```java
public int length
```

The number of bytes of primitive data available to be read
in the current buffer.

- eof

```java
public boolean eof
```

True if there is no more data in the buffered part of the stream.

---

#### Field Detail

length

```java
public int length
```

The number of bytes of primitive data available to be read
in the current buffer.

---

#### length

public int length

The number of bytes of primitive data available to be read
in the current buffer.

eof

```java
public boolean eof
```

True if there is no more data in the buffered part of the stream.

---

#### eof

public boolean eof

True if there is no more data in the buffered part of the stream.

---

