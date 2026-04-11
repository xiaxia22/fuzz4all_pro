# Class TooManyListenersException

**Source:** `java.base\java\util\TooManyListenersException.html`

### Class Description

```java
public class
TooManyListenersException

extends
Exception
```

The

TooManyListenersException

Exception is used as part of
the Java Event model to annotate and implement a unicast special case of
a multicast Event Source.

The presence of a "throws TooManyListenersException" clause on any given
concrete implementation of the normally multicast "void addXyzEventListener"
event listener registration pattern is used to annotate that interface as
implementing a unicast Listener special case, that is, that one and only
one Listener may be registered on the particular event listener source
concurrently.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TooManyListenersException()

Constructs a TooManyListenersException with no detail message.
A detail message is a String that describes this particular exception.

---

#### public TooManyListenersException​(
String
s)

Constructs a TooManyListenersException with the specified detail message.
A detail message is a String that describes this particular exception.

**Parameters:**
- s

- the detail message

---

### Method Details

*No entries found.*

### Additional Sections

#### Class TooManyListenersException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.util.TooManyListenersException

java.lang.Throwable

- java.lang.Exception
- - java.util.TooManyListenersException

java.lang.Exception

- java.util.TooManyListenersException

java.util.TooManyListenersException

**All Implemented Interfaces:** Serializable

```java
public class
TooManyListenersException

extends
Exception
```

The

TooManyListenersException

Exception is used as part of
the Java Event model to annotate and implement a unicast special case of
a multicast Event Source.

The presence of a "throws TooManyListenersException" clause on any given
concrete implementation of the normally multicast "void addXyzEventListener"
event listener registration pattern is used to annotate that interface as
implementing a unicast Listener special case, that is, that one and only
one Listener may be registered on the particular event listener source
concurrently.

**Since:** 1.1
**See Also:** EventObject

,

EventListener

,

Serialized Form

public class

TooManyListenersException

extends

Exception

The

TooManyListenersException

Exception is used as part of
the Java Event model to annotate and implement a unicast special case of
a multicast Event Source.

The presence of a "throws TooManyListenersException" clause on any given
concrete implementation of the normally multicast "void addXyzEventListener"
event listener registration pattern is used to annotate that interface as
implementing a unicast Listener special case, that is, that one and only
one Listener may be registered on the particular event listener source
concurrently.

The

TooManyListenersException

Exception is used as part of
the Java Event model to annotate and implement a unicast special case of
a multicast Event Source.

The presence of a "throws TooManyListenersException" clause on any given
concrete implementation of the normally multicast "void addXyzEventListener"
event listener registration pattern is used to annotate that interface as
implementing a unicast Listener special case, that is, that one and only
one Listener may be registered on the particular event listener source
concurrently.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TooManyListenersException

()

Constructs a TooManyListenersException with no detail message.

TooManyListenersException

​(

String

s)

Constructs a TooManyListenersException with the specified detail message.

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

TooManyListenersException

()

Constructs a TooManyListenersException with no detail message.

TooManyListenersException

​(

String

s)

Constructs a TooManyListenersException with the specified detail message.

---

#### Constructor Summary

Constructs a TooManyListenersException with no detail message.

Constructs a TooManyListenersException with the specified detail message.

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

- TooManyListenersException

```java
public TooManyListenersException()
```

Constructs a TooManyListenersException with no detail message.
A detail message is a String that describes this particular exception.

- TooManyListenersException

```java
public TooManyListenersException​(
String
s)
```

Constructs a TooManyListenersException with the specified detail message.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message

Constructor Detail

- TooManyListenersException

```java
public TooManyListenersException()
```

Constructs a TooManyListenersException with no detail message.
A detail message is a String that describes this particular exception.

- TooManyListenersException

```java
public TooManyListenersException​(
String
s)
```

Constructs a TooManyListenersException with the specified detail message.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message

---

#### Constructor Detail

TooManyListenersException

```java
public TooManyListenersException()
```

Constructs a TooManyListenersException with no detail message.
A detail message is a String that describes this particular exception.

---

#### TooManyListenersException

public TooManyListenersException()

Constructs a TooManyListenersException with no detail message.
A detail message is a String that describes this particular exception.

TooManyListenersException

```java
public TooManyListenersException​(
String
s)
```

Constructs a TooManyListenersException with the specified detail message.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message

---

#### TooManyListenersException

public TooManyListenersException​(

String

s)

Constructs a TooManyListenersException with the specified detail message.
A detail message is a String that describes this particular exception.

---

