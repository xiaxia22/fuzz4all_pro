# Class ThreadDeath

**Source:** `java.base\java\lang\ThreadDeath.html`

### Class Description

```java
public class
ThreadDeath

extends
Error
```

An instance of

ThreadDeath

is thrown in the victim thread
when the (deprecated)

Thread.stop()

method is invoked.

An application should catch instances of this class only if it
must clean up after being terminated asynchronously. If

ThreadDeath

is caught by a method, it is important that it
be rethrown so that the thread actually dies.

The

top-level error
handler

does not print out a message if

ThreadDeath

is
never caught.

The class

ThreadDeath

is specifically a subclass of

Error

rather than

Exception

, even though it is a
"normal occurrence", because many applications catch all
occurrences of

Exception

and then discard the exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ThreadDeath()

*No description found.*

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ThreadDeath

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - java.lang.ThreadDeath

java.lang.Throwable

- java.lang.Error
- - java.lang.ThreadDeath

java.lang.Error

- java.lang.ThreadDeath

java.lang.ThreadDeath

**All Implemented Interfaces:** Serializable

```java
public class
ThreadDeath

extends
Error
```

An instance of

ThreadDeath

is thrown in the victim thread
when the (deprecated)

Thread.stop()

method is invoked.

An application should catch instances of this class only if it
must clean up after being terminated asynchronously. If

ThreadDeath

is caught by a method, it is important that it
be rethrown so that the thread actually dies.

The

top-level error
handler

does not print out a message if

ThreadDeath

is
never caught.

The class

ThreadDeath

is specifically a subclass of

Error

rather than

Exception

, even though it is a
"normal occurrence", because many applications catch all
occurrences of

Exception

and then discard the exception.

**Since:** 1.0
**See Also:** Serialized Form

public class

ThreadDeath

extends

Error

An instance of

ThreadDeath

is thrown in the victim thread
when the (deprecated)

Thread.stop()

method is invoked.

An application should catch instances of this class only if it
must clean up after being terminated asynchronously. If

ThreadDeath

is caught by a method, it is important that it
be rethrown so that the thread actually dies.

The

top-level error
handler

does not print out a message if

ThreadDeath

is
never caught.

The class

ThreadDeath

is specifically a subclass of

Error

rather than

Exception

, even though it is a
"normal occurrence", because many applications catch all
occurrences of

Exception

and then discard the exception.

An application should catch instances of this class only if it
must clean up after being terminated asynchronously. If

ThreadDeath

is caught by a method, it is important that it
be rethrown so that the thread actually dies.

The

top-level error
handler

does not print out a message if

ThreadDeath

is
never caught.

The class

ThreadDeath

is specifically a subclass of

Error

rather than

Exception

, even though it is a
"normal occurrence", because many applications catch all
occurrences of

Exception

and then discard the exception.

The

top-level error
handler

does not print out a message if

ThreadDeath

is
never caught.

The class

ThreadDeath

is specifically a subclass of

Error

rather than

Exception

, even though it is a
"normal occurrence", because many applications catch all
occurrences of

Exception

and then discard the exception.

The class

ThreadDeath

is specifically a subclass of

Error

rather than

Exception

, even though it is a
"normal occurrence", because many applications catch all
occurrences of

Exception

and then discard the exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ThreadDeath

()

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

ThreadDeath

()

---

#### Constructor Summary

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

- ThreadDeath

```java
public ThreadDeath()
```

Constructor Detail

- ThreadDeath

```java
public ThreadDeath()
```

---

#### Constructor Detail

ThreadDeath

```java
public ThreadDeath()
```

---

#### ThreadDeath

public ThreadDeath()

---

